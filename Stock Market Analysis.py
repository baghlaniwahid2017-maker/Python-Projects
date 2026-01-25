# ==============================
# STOCK MARKET ANALYSIS PROJECT
# ==============================

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# 1. PARAMETERS
# ------------------------------
TICKER = "AAPL"
PERIOD = "2y"
SHORT_MA = 20
LONG_MA = 50
RSI_PERIOD = 14

# ------------------------------
# 2. DOWNLOAD DATA
# ------------------------------
df = yf.download(TICKER, period=PERIOD)
df.dropna(inplace=True)

# ------------------------------
# 3. RETURNS & VOLATILITY
# ------------------------------
df['Daily_Return'] = df['Close'].pct_change()
df['Cumulative_Return'] = (1 + df['Daily_Return']).cumprod()

annual_volatility = df['Daily_Return'].std() * np.sqrt(252)

# ------------------------------
# 4. MOVING AVERAGES
# ------------------------------
df['MA_Short'] = df['Close'].rolling(window=SHORT_MA).mean()
df['MA_Long'] = df['Close'].rolling(window=LONG_MA).mean()

# ------------------------------
# 5. RSI CALCULATION
# ------------------------------
delta = df['Close'].diff()
gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)

avg_gain = gain.rolling(RSI_PERIOD).mean()
avg_loss = loss.rolling(RSI_PERIOD).mean()

rs = avg_gain / avg_loss
df['RSI'] = 100 - (100 / (1 + rs))

# ------------------------------
# 6. BUY / SELL SIGNALS
# ------------------------------
df['Signal'] = 0
df.loc[df['MA_Short'] > df['MA_Long'], 'Signal'] = 1
df.loc[df['MA_Short'] < df['MA_Long'], 'Signal'] = -1

df['Position'] = df['Signal'].shift()

# ------------------------------
# 7. STRATEGY BACKTESTING
# ------------------------------
df['Strategy_Return'] = df['Position'] * df['Daily_Return']
df['Strategy_Cumulative'] = (1 + df['Strategy_Return']).cumprod()

# ------------------------------
# 8. PERFORMANCE METRICS
# ------------------------------
total_return = df['Strategy_Cumulative'].iloc[-1] - 1
sharpe_ratio = (df['Strategy_Return'].mean() / df['Strategy_Return'].std()) * np.sqrt(252)

print("====== PERFORMANCE SUMMARY ======")
print(f"Ticker: {TICKER}")
print(f"Annual Volatility: {annual_volatility:.2%}")
print(f"Total Strategy Return: {total_return:.2%}")
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")

# ------------------------------
# 9. VISUALIZATION
# ------------------------------
plt.figure(figsize=(14,10))

# Price & Moving Averages
plt.subplot(3,1,1)
plt.plot(df['Close'], label='Close Price')
plt.plot(df['MA_Short'], label='Short MA')
plt.plot(df['MA_Long'], label='Long MA')
plt.title(f"{TICKER} Price & Moving Averages")
plt.legend()

# RSI
plt.subplot(3,1,2)
plt.plot(df['RSI'], label='RSI', color='purple')
plt.axhline(70, linestyle='--')
plt.axhline(30, linestyle='--')
plt.title("Relative Strength Index (RSI)")
plt.legend()

# Strategy Performance
plt.subplot(3,1,3)
plt.plot(df['Cumulative_Return'], label='Buy & Hold')
plt.plot(df['Strategy_Cumulative'], label='Strategy')
plt.title("Cumulative Returns Comparison")
plt.legend()

plt.tight_layout()
plt.show()
