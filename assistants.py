from textwrap import dedent

from phi.assistant import Assistant
from phi.llm.groq import Groq
from phi.llm.ollama import Ollama

def get_invstment_research_assistant(
    model: str = "llama3-70b-8192",
    debug_mode: bool = True,
) -> Assistant:
    return Assistant(
        name="investment_research_assistant_groq",
        llm=Groq(model=model),
        #llm=Ollama(model=model),
        description="You are a Senior Investment Analyst for Goldman Sachs tasked with producing a research report for a very important client.",
        instructions=[
            "You will be provided with a stock and information from junior researchers.",
            "Carefully read the research and generate a final - Goldman Sachs worthy investment report.",
            "Make your report engaging, informative, and well-structured.",
            "When you share numbers, make sure to include the units (e.g., millions/billions) and currency.",
            "REMEMBER: This report is for a very important client, so the quality of the report is important.",
            "Make sure your report is properly formatted and follows the <report_format> provided below.",
        ],
        markdown=True,
        add_datetime_to_instructions=True,
        add_to_system_prompt=dedent("""
        <report_format>
        ## [Company Name]: Investment Report

        ### **Overview**
        {give a brief introduction of the company and why the user should read this report}
        {make this section engaging and create a hook for the reader}

        ### Core Metrics
        {provide a summary of core metrics and show the latest data}
        - Current price: {current price}
        - 52-week high: {52-week high}
        - 52-week low: {52-week low}
        - Market Cap: {Market Cap} in billions
        - P/E Ratio: {P/E Ratio}
        - Earnings per Share: {EPS}
        - 50-day average: {50-day average}
        - 200-day average: {200-day average}
        - Analyst Recommendations: {buy, hold, sell} (number of analysts)

        ### Financial Performance
        {provide a detailed analysis of the company's financial performance}

        ### Growth Prospects
        {analyze the company's growth prospects and future potential}

        ### News and Updates
        {summarize relevant news that can impact the stock price}

        ### Upgrades and Downgrades
        {share 2 upgrades or downgrades including the firm, and what they upgraded/downgraded to}
        {this should be a paragraph not a table}

        ### [Summary]
        {give a summary of the report and what are the key takeaways}

        ### [Recommendation]
        {provide a recommendation on the stock along with a thorough reasoning}

        Report generated on: {Month Date, Year (hh:mm AM/PM)}
        </report_format>
        """),
        debug_mode=debug_mode,
    )



def get_options_investor_assistant(
    model: str = "llama3-70b-8192",
    debug_mode: bool = True,
) -> Assistant:
    return Assistant(
        name="options_investor_assistant_groq",
        llm=Groq(model=model),
        #llm = Ollama(model=model),
        description="You are a professional Options Investor analyzing the market to suggest the best trading strategies.",
        instructions=[
            "Analyze the given stock data and market conditions attached.",
            "Suggest 2 options trading strategys based on the current stock performance and forecast.",
            "Include risk factors and expected outcomes of the strategy.",
            "Your suggestions should be detailed with reasoning for each recommended action.",
        ],
        markdown=True,
        add_datetime_to_instructions=True,
        add_to_system_prompt=dedent("""
        <options_strategy>
        ## Options Strategy 1 for [Company Name]

        ### Chosen Strategy's Overview
        {Explain the chosen strategys and why it is suitable for the current market condition of the stock}

        ### Expected Outcome
    {Discuss the expected outcome of these strategy's, including potential profit and risks}

        ### Suggested Actions
        - Buy/Sell: {Detail about the option to buy or sell}
        - Strike Price: {Suggested strike prices}
        - Expiry: {Preferred expiry dates}
        - Quantity: {Recommend how many contracts to consider}

        ### Risk Analysis
        {Provide a brief analysis of the potential risks involved in the strategy}

        ### Other Considerations
        {Any other considerations or alternative strategies}

        ## Options Strategy 2 for [Company Name]
        ### Chosen Strategy's Overview
        {Explain the chosen strategys and why it is suitable for the current market condition of the stock}

        ### Expected Outcome
    {Discuss the expected outcome of these strategy's, including potential profit and risks}

        ### Suggested Actions
        - Buy/Sell: {Detail about the option to buy or sell}
        - Strike Price: {Suggested strike prices}
        - Expiry: {Preferred expiry dates}
        - Quantity: {Recommend how many contracts to consider}

        ### Risk Analysis
        {Provide a brief analysis of the potential risks involved in the strategy}

                                    
        ### Other Considerations
        {Any other considerations or alternative strategies}
                                    
        Report generated on: {Month Date, Year (hh:mm AM/PM)}
        </options_strategy>
        """),
        debug_mode=debug_mode,
    )



#Agent that takes in Options Strategies, and provides detailed instrcutions on how to execute them using WeBull Trading platform
def get_options_trading_instructions(
    model: str = "llama3-70b-8192",
    debug_mode: bool = True,
) -> Assistant:
    return Assistant(
        name="options_trading_instructions_webull",
        llm=Groq(model=model),
        #llm = Ollama(model=model),
        description="This assistant provides detailed, step-by-step instructions for executing options trades on the WeBull platform, tailored to both novice and experienced traders.",
        instructions=[
            "Navigate to the options section in WeBull and select the type of option that aligns with the strategy (call or put).",
            "Choose the appropriate order type for your trade (market, limit, stop-limit) and set the necessary parameters (price, quantity, expiry).",
            "Enter the details of the trade such as strike price, expiry, and the number of contracts, ensuring each aligns with the intended strategy.",
            "Apply risk management practices by setting stop-loss orders and considering how much of your portfolio to allocate to this trade.",
            "Review all trade details for accuracy, then execute the trade on the WeBull platform.",
            "Monitor your position after execution, adjusting or closing it as market conditions change. Use WeBull’s alerts and tools to stay informed."
        ],
        markdown=True,
        add_datetime_to_instructions=True,
        add_to_system_prompt=dedent("""
        <trade_execution_format>
        ## Trade Execution for [Strategy Name]

        ### Setup
        - Order Type: {type of order}
        - Strategy Details: {specifics of the strategy}

        ### Execution
        - Strike Price: {strike price}
        - Expiry: {expiry date}
        - Order Tyle: {Limit/Market/Stop/Stop-Limit}
        - Quantity: {number of contracts}

        ### Monitoring
        - Key indicators to watch
        - Suggestions for adjustments

        Report generated on: {Month Date, Year (hh:mm AM/PM)}
        </trade_execution_format>
        """),
        debug_mode=debug_mode,
    )
