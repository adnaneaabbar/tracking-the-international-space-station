# Automated Trading Bot

Building a trading bot that can take trading strategies using **technical analysis** and execute them in an automated fashion using the **TD Ameritrade API**.

This bot will mimic 4 common scenarios :

*  Maintaining a portfolio of multiple instruments. The **Portfolio** object will be able to calculate common risk metrics related to a portfolio and give real-time feedback as you trade.

*  Define an order that can be used to trade a financial instrument. With the **Trade** object, you can define simple or even complex orders using Python. These orders will also help similify common scenarios like defining both a take profit and stop loss at the same time.

*  A real-time data table that includes both historical and real-time prices as they change. The **StockFrame** will make the process of storing your data easy and quick. Additionally, it will be setup so that way you can easily select your financial data as it comes in and do further analysis if needed.

*  Define and calculate indicators using both historical and real-time prices. The **Indicator** object will help you easily define the input of your indicators, calculate them, and then update their values as new prices come.

---

# Inspiration

This project was the fruit of an inspiration from the previously finished [stock-trading-system](https://github.com/adnaneaabbar/stock-trading-system) project. I like to to look at it as the continuity of my **data science/finance and trading** orientation.

---

# Recommendation

I would like to recommend following this youtube channel : [Sigma Coding](https://www.youtube.com/channel/UCBsTB02yO0QGwtlfiv5m25Q) for the insightful information it contains about trading bots and many other technologies.
