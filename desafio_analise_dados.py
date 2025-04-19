import pandas as pd
import numpy as np

dados = {
    "Região": ["Norte", "Norte", "Sul", "Sul", "Norte"],
    "Mês": ["Jan", "Fev", "Jan", "Fev", "Mar"],
    "Vendas": [1500, np.nan, 2200, 1800, 2000],
    "Despesas": [300, 250, np.nan, 400, 350]
}

df = pd.DataFrame(dados)

df.to_excel("vendas.xlsx", index=False)

df = pd.read_excel("vendas.xlsx")
print("Dados carregados:\n", df)

df["Vendas"].fillna(df["Vendas"].median(), inplace=True)

df["Despesas"].fillna(df["Despesas"].mean(), inplace=True)


agrupado = df.groupby(["Região", "Mês"]).agg({"Vendas": "sum", "Despesas": "mean"})
print("\nDados agrupados:\n", agrupado)

combinado = np.hstack([df["Vendas"].values.reshape(-1, 1), df["Despesas"].values.reshape(-1, 1)])
print("\nColunas combinadas:\n", combinado)

sumario = df.describe()
print("\nSumário estatístico:\n", sumario)
