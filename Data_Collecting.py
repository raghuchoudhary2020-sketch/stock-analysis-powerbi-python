import yfinance as yf
import pandas as pd 

tickers = ["RELIANCE.NS", "TCS.NS", "INFY.NS"]
start_date = "2023-01-01"
end_date = "2025-01-01"


data = yf.download(tickers, start=start_date, end=end_date, auto_adjust=True)["Close"]

final_df = pd.DataFrame()

for ticker in tickers:
    df = pd.DataFrame(data[ticker])
    df.reset_index(inplace=True)
    df.rename(columns={ticker: "Price"}, inplace=True)
    df["Ticker"] = ticker

    
    df["Daily_Return"] = df["Price"].pct_change()

    
    df["MA_20"] = df["Price"].rolling(window=20).mean()
    df["MA_50"] = df["Price"].rolling(window=50).mean()

   
    df["Volatility"] = df["Daily_Return"].rolling(window=20).std()

   
    final_df = pd.concat([final_df, df])


final_df.to_csv("stock_market_data.csv", index=False)

print("Data collection complete! File saved as stock_market_data.csv")