import yfinance as yf 

# 获取股票数据
symbol = "600519.SS"
start_data = "2022-01-01"
end_data = "2023-01-01"

data =yf.download(symbol, start=start_data, end=end_data)
print(data.head())