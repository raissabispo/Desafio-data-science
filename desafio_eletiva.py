import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# grupos
grupo_a = np.array([3, 5, 7, 9, 11])
grupo_b = np.array([2, 4, 6, 8, 10])

#média, moda e mediana
media_a = np.mean(grupo_a)
mediana_a = np.median(grupo_a)
desvio_a = np.std(grupo_a)

media_b = np.mean(grupo_b)
mediana_b = np.median(grupo_b)
desvio_b = np.std(grupo_b)

print("Grupo A - Média: ", media_a, ", Mediana: ", mediana_a, ", Desvio Padrão: ", desvio_a)
print("Grupo B - Média: ", media_b, ", Mediana: ", mediana_b, ", Desvio Padrão: ", desvio_b)

shapiro_a = stats.shapiro(grupo_a)
shapiro_b = stats.shapiro(grupo_b)

print("\nTeste de normalidade (Shapiro-Wilk) para o Grupo A: ", shapiro_a)
print("Teste de normalidade (Shapiro-Wilk) para o Grupo B: ", shapiro_b)

if shapiro_a.pvalue > 0.05 and shapiro_b.pvalue > 0.05:
    correlacao, _ = stats.pearsonr(grupo_a, grupo_b)
    print("\nCorrelação de Pearson: ", correlacao)
else:
    correlacao, _ = stats.spearmanr(grupo_a, grupo_b)
    print("\nCorrelação de Spearman: ", correlacao)

plt.scatter(grupo_a, grupo_b, color='blue')
plt.title('Gráfico de Dispersão entre Grupo A e Grupo B')
plt.xlabel('Grupo A')
plt.ylabel('Grupo B')
plt.grid(True)
plt.show()
