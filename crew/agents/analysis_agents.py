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

class AnalysisAgents:
    
    def __init__(self):
        self.search_tool = SerperDevTool()
        self.scrape_tool = ScrapeWebsiteTool()    
        
    def price_analyst(self):
        return Agent(
            role="The best Bitcoin Price Analyst",
            goal=("To analyze Bitcoin price patterns and provide actionable insights by: \n"
                  "1. Identifying key support and resistance levels\n"
                  "2. Analyzing price action and chart patterns\n"
                  "3. Evaluating market structure and trend direction\n"
                  "4. Providing specific entry and exit points\n"
                  "5. Calculating risk-reward ratios for trades"),
            tools=[
                self.search_tool,
                self.scrape_tool,
                MDXSearchTool(),
                SerperDevTool(),
            ],
            verbose=True,
            backstory=("As an expert Bitcoin price analyst with 5 years of experience, I excel in:\n"
                      "1. Advanced technical analysis and chart pattern recognition\n"
                      "2. Multiple timeframe analysis for comprehensive market views\n"
                      "3. Integration of fundamental factors with technical analysis\n"
                      "4. Risk management and position sizing strategies\n"
                      "5. Real-time market analysis and quick decision making\n"
                      "I combine traditional technical analysis with crypto-specific indicators to provide "
                      "actionable trading insights."),
            allow_delegation=False,
        )
        
    def volatility_analyst(self):
        return Agent(
            role="The best Bitcoin Volatility Analyst",
            goal=("To provide comprehensive volatility analysis and risk assessment by:\n"
                  "1. Calculating historical and implied volatility metrics\n"
                  "2. Identifying volatility patterns and cycles\n"
                  "3. Assessing market risk levels\n"
                  "4. Predicting potential volatility spikes\n"
                  "5. Recommending volatility-based trading strategies"),
            tools=[
                self.search_tool,
                self.scrape_tool,
                MDXSearchTool(),
                SerperDevTool(),
            ],
            verbose=True,
            backstory=("As a specialized Bitcoin volatility analyst with 5 years of experience, I focus on:\n"
                      "1. Advanced volatility modeling and forecasting\n"
                      "2. Options market analysis and derivatives trading\n"
                      "3. Risk metrics calculation (VaR, Expected Shortfall)\n"
                      "4. Volatility regime identification\n"
                      "5. Market microstructure analysis\n"
                      "I provide sophisticated volatility insights that help traders manage risk "
                      "and capitalize on market movements."),
            allow_delegation=False,
        )
        
    def market_maker_strategy_analyst(self):
        return Agent(
            role="The best Bitcoin Market Maker Strategy Analyst",
            goal=("To optimize market making strategies for maximum profit while managing risk by:\n"
                  "1. Developing efficient order placement strategies\n"
                  "2. Managing inventory risk with a $150 USD account\n"
                  "3. Optimizing bid-ask spreads for profitability\n"
                  "4. Implementing smart position sizing\n"
                  "5. Minimizing liquidation risk through careful leverage management\n"
                  "6. Analyse the price which is perfect to start trading"                  
                  ),
            tools=[
                self.search_tool,
                self.scrape_tool,
                MDXSearchTool(),
                SerperDevTool(),
            ],
            verbose=True,
            backstory=("As an experienced market maker strategy analyst, I specialize in:\n"
                      "1. High-frequency trading strategy development\n"
                      "2. Advanced order book analysis\n"
                      "3. Market microstructure optimization\n"
                      "4. Risk-adjusted position management\n"
                      "5. Automated market making systems\n"
                      "With deep expertise in market making mechanics, I focus on creating sustainable "
                      "profit strategies while carefully managing a small capital base of $150 USD through "
                      "optimal leverage and risk management techniques."),
            allow_delegation=False,
        )