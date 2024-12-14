from crewai import Task

class AnalysisTasks:
    
    def analyse_volatility(self, tasks_context = None, agent = None):
        return Task(
            description=str(
                "Analyze the volatility of Bitcoin over the past 24 hours, focusing on price, volume, and market cap. "
                "Additionally, calculate the volatility index (VI) for Bitcoin over the past 14 hours. Use a 14-period smoothing Average True Range (ATR) indicator, "
                "considering intraday, daily, weekly, or monthly periods as applicable."
            ),
            expected_output=str(
                "Output the results as a JSON containing the volatility index for Bitcoin over the specified period."
            ),
            output_file="btc_volatility.json",
            context=tasks_context,
            agent=agent
        )
        
    def calculate_stop_loss(self, tasks_context = None, agent = None):
        return Task(
            description=str(
                "Determine the high and low stop-loss levels for the BTC price based on my position."
            ),
            expected_output=str(
                "JSON with the high and low values for the stop loss BTC price for my position."
            ),
            output_file="btc_stop_loss.json",
            context=tasks_context,
            agent=agent
        )
        
    def mount_maket_maker_strategy(self, tasks_context = None, agent = None):
        return Task(
            description=str(
                "Develop a market-making strategy for Bitcoin with the following features:"
                "Place competitive bid and ask orders."
                "Dynamically adjust spreads, order sizes, and intervals based on market conditions such as current price, volatility, and wallet balance."
                "Maintain a balanced inventory to minimize risk and ensure sufficient margin to continue trading while avoiding liquidation."
                "Leverage Management:"
                "Adjust leverage dynamically according to current price and volatility to minimize liquidation risk. Liquidations are not permitted."
                "Order and Strategy Parameters:"
                "Calculate the number of order pairs, leverage, and trading parameters based on current market data and wallet balance."
                "The strategy should consider wallet margin constraints and optimize for profitability within safe risk boundaries."
                "Required Output Parameters:"

                "current_price: The current price of Bitcoin."
                "volatility_index: A measure of Bitcoin's market volatility."
                "order_pairs: The number of bid-ask pairs to trade."
                "order_start_size: The initial size of each order (starting at 100)."
                "order_step_size: The incremental size for subsequent orders."
                "interval_percentage: The percentage interval between orders."
                "min_spread: The percentage minimum interval between bid and ask orders."
                "target_to_profit_limit: The target profit limit as a percentage of PnL."
                "target_to_profit_market: The target profit for market-based trades in percentage."
                "leverage: The leverage applied in the market-making strategy."
                "high_stop_loss: The upper stop-loss level for the strategy."
                "low_stop_loss: The lower stop-loss level for the strategy."
                "Ensure the strategy:"

                "Maximizes profitability while maintaining strict risk control."
                "Adapts dynamically to changing market conditions."
                "Provides robust output for transparent and effective trading decisions."
            ),
            expected_output=str(
                "JSON with the market making strategy for Bitcoin contracts trading. "
                
            ),
            output_file="market_making_strategy.json",
            context=tasks_context,
            agent=agent
            
        )
        
    def verify_ballance_and_leverage(self, tasks_context = None, agent = None):
        return Task(
            description=str(
                "Validate the balance and leverage metrics of the market-making strategy, ensuring accuracy and alignment with risk management guidelines. Identify discrepancies or potential issues and provide actionable feedback to optimize the strategy."
            ),
            expected_output=str(
                "JSON with the market making strategy for Bitcoin contracts trading. "
                "Adjust the Leverage based on the current price and volatility, to avoid liquidation. "
                "No liquidation are allowed. The number or orders, the leverage, are calculated based on the current price,"
                " volatility, and wallet balance. We need to have margin to continue trading with the balance of the wallet wich is USD 150. "
                "The market making strategy is based on the current price, volatility, and wallet balance. "
            ),
            context=tasks_context,
            agent=agent
        )
        
    