from enum import verify
import os
import warnings
import logging

import pandas as pd


from crewai import Agent, Process, Task, Crew
from crew.agents.manager_agents import ManagerAgents
from crew.agents.research_agents import ResearchAgents
from crew.tasks.analysis_tasks import AnalysisTasks
from crew.tasks.research_tasks import ResearchTasks

from crew.utils import get_openai_api_key, get_serper_api_key
from crewai_tools import (
  FileReadTool,
  ScrapeWebsiteTool,
  MDXSearchTool,
  SerperDevTool,
  PDFSearchTool
)
from IPython.display import Markdown, display

from crew.agents.analysis_agents import AnalysisAgents
from crew.tasks.analysis_tasks import AnalysisTasks

warnings.filterwarnings('ignore')

openai_api_key = get_openai_api_key()
os.environ["OPENAI_MODEL_NAME"] = 'gpt-4o-mini'
os.environ["SERPER_API_KEY"] = get_serper_api_key()

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

class BtcCrew:
  
  def __init__(self):
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    self.logger = logging.getLogger(__name__)
    warnings.filterwarnings('ignore')
    
    os.environ["OPENAI_MODEL_NAME"] = 'gpt-4o-mini'
    os.environ["SERPER_API_KEY"] = get_serper_api_key()

    self.openai_api_key = get_openai_api_key()    
    
    self.price_researcher = ResearchAgents().price_researcher()
    self.volatility_researcher = ResearchAgents().volatility_researcher()
    self.price_analyst = AnalysisAgents().price_analyst()
    self.volatility_analyst = AnalysisAgents().volatility_analyst()
    self.market_maker_strategy_analyst = AnalysisAgents().market_maker_strategy_analyst()
    self.trader_manager = ManagerAgents().trader_manager()    
    
    self.research_tasks = ResearchTasks()
    
    self.research_btc_price = ResearchTasks().research_btc_price(self.price_researcher)
    self.analyse_volatility = AnalysisTasks().analyse_volatility([self.research_btc_price,], self.volatility_analyst)
    self.calculate_stop_loss = AnalysisTasks().calculate_stop_loss([self.analyse_volatility,], self.market_maker_strategy_analyst)
    self.verify_ballance_and_leverage = AnalysisTasks().verify_ballance_and_leverage([self.calculate_stop_loss,], self.market_maker_strategy_analyst)
    self.mount_maket_maker_strategy = AnalysisTasks().mount_maket_maker_strategy([self.verify_ballance_and_leverage,], self.market_maker_strategy_analyst)
    
  
  def run(self):
    self.logger.info("Running the Bitcoin Crew")
    crew = Crew(
      name="Bitcoin Crew",
      tasks=[self.research_btc_price, 
             self.analyse_volatility, 
             self.calculate_stop_loss, 
             self.verify_ballance_and_leverage, 
             self.mount_maket_maker_strategy
             ],
      agents=[self.price_researcher, 
              self.volatility_researcher, 
              self.price_analyst, 
              self.volatility_analyst, 
              self.market_maker_strategy_analyst
              ],
      process=Process.hierarchical,
      verbose=True,
      manager_agent=self.trader_manager,
      memory=True
    )
    
    inputs = {}
    
    result = crew.kickoff(inputs)
    

    costs = 0.150 * (crew.usage_metrics.prompt_tokens + crew.usage_metrics.completion_tokens) / 1_000_000
    print(f"Total costs: ${costs:.4f}")

    # Convert UsageMetrics instance to a DataFrame
    df_usage_metrics = pd.DataFrame([crew.usage_metrics.dict()])
    