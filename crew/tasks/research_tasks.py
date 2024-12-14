from crewai import Task
from datetime import datetime, timedelta

class ResearchTasks:
    
    def research_btc_price(self, agent):
        return Task(
            description=(
                "Conduct a comprehensive price analysis of Bitcoin including:\n"
                "1. Current price across major exchanges (Binance, Coinbase, Kraken)\n"
                "2. 24h price change and volume\n"
                "3. Key price levels (support/resistance)\n"
                "4. Order book depth analysis\n"
                "5. Recent price action patterns\n\n"
                "Use reliable data sources like Google, CoinGecko API, TradingView, and exchange APIs.\n"
                "Identify any significant price movements and their potential causes."
            ),
            expected_output=(
                "Detailed JSON report containing:\n"
                "- Current price data (timestamp, price, exchange)\n"
                "- 24h statistics (high, low, volume, change)\n"
                "- Technical levels (support, resistance)\n"
                "- Order book summary\n"
                "- Pattern analysis\n"
                "- Market sentiment indicators"
            ),
            output_file="btc_price_analysis.json",
            agent=agent
        )
    
    def research_market_volatility(self, agent):
        return Task(
            description=(
                "Analyze Bitcoin's current volatility metrics including:\n"
                "1. Historical Volatility (1h, 24h, 7d)\n"
                "2. Implied Volatility from options markets\n"
                "3. Volatility Index (VIX) correlation\n"
                "4. Volume-weighted volatility\n"
                "5. Volatility regime analysis\n\n"
                "Focus on identifying potential volatility breakouts and risk levels.\n"
                "Compare current volatility with historical patterns."
            ),
            expected_output=(
                "Comprehensive JSON report containing:\n"
                "- Volatility metrics across timeframes\n"
                "- Options market implied volatility\n"
                "- Volatility regime classification\n"
                "- Risk metrics (VaR, Expected Shortfall)\n"
                "- Volume analysis\n"
                "- Volatility forecast"
            ),
            output_file="btc_volatility_analysis.json",
            agent=agent
        )
    
    def research_market_sentiment(self, agent):
        return Task(
            description=(
                "Analyze current market sentiment through multiple indicators:\n"
                "1. Social media sentiment (Twitter, Reddit)\n"
                "2. Fear & Greed Index\n"
                "3. Exchange inflow/outflow\n"
                "4. Futures market sentiment\n"
                "5. Institutional interest indicators\n\n"
                "Consider news impact and overall market narrative.\n"
                "Look for sentiment divergences from price action."
            ),
            expected_output=(
                "Detailed JSON report containing:\n"
                "- Social sentiment metrics\n"
                "- Market indicators\n"
                "- On-chain metrics\n"
                "- News sentiment analysis\n"
                "- Institutional flows\n"
                "- Overall market sentiment score"
            ),
            output_file="btc_sentiment_analysis.json",
            agent=agent
        )
    
    def research_market_making_opportunities(self, agent):
        return Task(
            description=(
                "Analyze market making opportunities with $150 USD capital:\n"
                "1. Spread analysis across exchanges\n"
                "2. Volume distribution patterns\n"
                "3. Optimal leverage calculations\n"
                "4. Risk parameters for different timeframes\n"
                "5. Liquidity analysis\n\n"
                "Focus on identifying profitable spreads while maintaining risk management.\n"
                "Consider fees, slippage, and minimum order sizes."
            ),
            expected_output=(
                "Strategic JSON report containing:\n"
                "- Spread opportunities by exchange\n"
                "- Optimal position sizes\n"
                "- Leverage recommendations\n"
                "- Risk management parameters\n"
                "- Expected profit calculations\n"
                "- Implementation strategy"
            ),
            output_file="market_making_strategy.json",
            agent=agent
        )
    
    def research_correlation_analysis(self, agent):
        return Task(
            description=(
                "Analyze Bitcoin's correlations with various markets:\n"
                "1. Traditional markets (S&P 500, Gold, DXY)\n"
                "2. Other cryptocurrencies\n"
                "3. Macro events impact\n"
                "4. Sector-specific correlations\n"
                "5. Geographic market correlations\n\n"
                "Focus on identifying leading indicators and correlation changes.\n"
                "Consider multiple timeframes for correlation strength."
            ),
            expected_output=(
                "Detailed JSON report containing:\n"
                "- Correlation coefficients\n"
                "- Temporal correlation analysis\n"
                "- Leading indicator identification\n"
                "- Market dependency metrics\n"
                "- Correlation change alerts\n"
                "- Trading implications"
            ),
            output_file="btc_correlation_analysis.json",
            agent=agent
        )