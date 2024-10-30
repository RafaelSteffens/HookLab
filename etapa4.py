import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar dados JSON
df = pd.read_json('dados_compras.json')

# Identificar a quantidade total de compras realizadas
total_compras = df.shape[0]
print(f"Total de compras realizadas: {total_compras}\n")

# Calcular a média, o valor mínimo e máximo gasto por compra
media_gasto = df['Valor'].mean()
minimo_gasto = df['Valor'].min()
maximo_gasto = df['Valor'].max()

print(f"Média gasta por compra: {media_gasto:.2f}")
print(f"Valor mínimo gasto por compra: {minimo_gasto:.2f}")
print(f"Valor máximo gasto por compra: {maximo_gasto:.2f}\n")

# Determinar o produto mais caro e o mais barato
produto_mais_caro = df.loc[df['Valor'].idxmax()]['Nome do Item']
produto_mais_barato = df.loc[df['Valor'].idxmin()]['Nome do Item']

print(f"Produto mais caro: {produto_mais_caro}")
print(f"Produto mais barato: {produto_mais_barato}\n")

# Analisar a distribuição de gênero entre os consumidores
distribuicao_genero = df['Sexo'].value_counts()
print("Distribuição de gênero entre os consumidores:")
print(distribuicao_genero, "\n")

# Calcular o valor total gasto em compras por gênero
gasto_por_genero = df.groupby('Sexo')['Valor'].sum()
print("Valor total gasto em compras por gênero:")
print(gasto_por_genero, "\n")

# Visualizar a distribuição de gênero
plt.figure(figsize=(10, 5))
sns.countplot(x='Sexo', data=df)
plt.title('Distribuição de Gênero dos Consumidores')
plt.xlabel('Gênero')
plt.ylabel('Contagem')
plt.show()

# Visualizar gasto total por gênero
plt.figure(figsize=(10, 5))
gasto_por_genero.plot(kind='bar')
plt.title('Valor Total Gasto em Compras por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Valor Total Gasto')
plt.xticks(rotation=0)
plt.show()

# Histograma do valor gasto por compra
plt.figure(figsize=(10, 5))
sns.histplot(df['Valor'], bins=20, kde=True)
plt.title('Histograma do Valor Gasto por Compra')
plt.xlabel('Valor Gasto')
plt.ylabel('Frequência')
plt.show()
