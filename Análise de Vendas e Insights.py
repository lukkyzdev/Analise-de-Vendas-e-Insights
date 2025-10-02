import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

conexao = sqlite3.connect('dados_vendas.db')
cursor = conexao.cursor()

cursor.execute('DROP TABLE IF EXISTS vendas1')

cursor.execute('''
CREATE TABLE vendas1 (
id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
data_venda DATE,
produto TEXT,
categoria TEXT,
valor_venda REAL
)
''')

cursor.execute('''
INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda) VALUES
('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
('2023-01-05', 'Produto B', 'Roupas', 350.00),
('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
('2023-03-15', 'Produto D', 'Livros', 200.00),
('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
('2023-04-02', 'Produto F', 'Roupas', 400.00),
('2023-05-05', 'Produto G', 'Livros', 150.00),
('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
('2023-07-20', 'Produto I', 'Roupas', 600.00),
('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
('2023-09-30', 'Produto K', 'Livros', 300.00),
('2023-10-05', 'Produto L', 'Roupas', 450.00),
('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
('2023-12-20', 'Produto N', 'Livros', 250.00);
''')

conexao.commit()

df_vendas = pd.read_sql_query("SELECT * FROM vendas1", conexao)

print(df_vendas.head())

# Informações gerais
print(df_vendas.info())

# Estatísticas descritivas
print(df_vendas.describe())

# Total de vendas por categoria
totais_categoria = df_vendas.groupby("categoria")["valor_venda"].sum()
print(totais_categoria)

# Total de vendas por mês
df_vendas["data_venda"] = pd.to_datetime(df_vendas["data_venda"])
df_vendas["mes"] = df_vendas["data_venda"].dt.month
totais_mes = df_vendas.groupby("mes")["valor_venda"].sum()
print(totais_mes)

# Produto mais vendido
top_produto = df_vendas.groupby("produto")["valor_venda"].sum().sort_values(ascending=False).head(5)
print(top_produto)

# Vendas por categoria
totais_categoria.plot(kind="bar", title="Total de Vendas por Categoria")
plt.ylabel("Valor de Vendas")
plt.show()

# Vendas por mês (linha)
totais_mes.plot(kind="line", marker="o", title="Vendas por Mês")
plt.ylabel("Valor de Vendas")
plt.show()

# Boxplot por categoria
sns.boxplot(data=df_vendas, x="categoria", y="valor_venda")
plt.title("Distribuição de Vendas por Categoria")
plt.show()
