import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Definir os símbolos das ações
symbols = ['PETR4.SA', 'VALE3.SA', 'ITUB4.SA', 'BBDC4.SA', 'ABEV3.SA', 'B3SA3.SA']

# Definir o período de análise
start_date = '2020-01-01'
end_date = '2020-12-31'

# Obter os dados do Yahoo Finance
data = pd.DataFrame()
for symbol in symbols:
    data[symbol] = yf.download(tickers=symbol, start=start_date, end=end_date,interval='1d')['Adj Close']

columns = {'PETR4', 'VALE3', 'ITUB4', 'BBDC4', 'ABEV3', 'B3SA3'}
data.columns = columns

# Calcular os retornos
returns = data.pct_change().dropna()

# Plotar os retornos
returns.plot(figsize=(12,8))
plt.title('Retornos das ações')
plt.xlabel('Data')
plt.ylabel('Retorno')
plt.legend()
#plt.show()

# Criar o modelo de regressão
model = smf.ols(formula='PETR4 ~ VALE3', data=returns)

results = model.fit()

print(results.summary())