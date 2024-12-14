import os
import warnings

from crewai import Agent, Task, Crew
from crew.utils import get_openai_api_key, get_serper_api_key
from crewai_tools import (
  FileReadTool,
  ScrapeWebsiteTool,
  MDXSearchTool,
  SerperDevTool,
  PDFSearchTool
)
from IPython.display import Markdown, display

class ResearchAgents:
    def __init__(self):
        self.search_tool = SerperDevTool()
        self.scrape_tool = ScrapeWebsiteTool()

    def volatility_researcher(self):
        return Agent(
            role="The best Bitcoin Volatility Researcher",
            goal="To provide the best results on Bitcoin's volatility",
            verbose=True,
            backstory=("I am a Bitcoin volatility researcher. I have been researching Bitcoin's volatility for the past 5 years. "
                        "I have a deep understanding of the factors that affect Bitcoin's volatility, and I use this knowledge "
                        "to provide accurate and insightful analysis to my clients. Check https://www.cryptocompare.com/coins/btc/charts/USD?bc=VOLATILITY&p=1H"),
            allow_delegation=False,
        )      
        
    def price_researcher(self):
        return Agent(
            role="The best Bitcoin Price Researcher",
            goal=("To provide comprehensive and accurate analysis of Bitcoin's price movements by analyzing "
                  "market data, trading volumes, technical indicators, and relevant market news. "
                  "Focus on both short-term price movements and long-term trends."),
            verbose=True,
            tools=[
                self.search_tool,
                self.scrape_tool,
                MDXSearchTool(),
                SerperDevTool(),
            ],
            backstory=("As a veteran Bitcoin price researcher with 5 years of experience, I specialize in: \n"
                      "1. Technical analysis of Bitcoin price patterns and trends\n"
                      "2. Analysis of market indicators including volume, momentum, and volatility\n"
                      "3. Monitoring of key price levels and market structures\n"
                      "4. Integration of on-chain metrics with price analysis\n"
                      "5. Assessment of market sentiment and news impact on price\n"
                      "I provide data-driven insights by combining multiple data sources and analytical methods "
                      "to form comprehensive price analysis reports."),
            allow_delegation=False,
        )
        
