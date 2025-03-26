import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Configurações iniciais do Streamlit
st.set_page_config(page_title="Dashboard: Preços de Casas em São Paulo", layout="wide")
st.title("Dashboard Interativo: Preços de Casas em São Paulo")
st.markdown("""
Este dashboard explora o dataset **House Prices - São Paulo** e demonstra uma análise exploratória interativa, além de construir um modelo preditivo de regressão para estimar os preços das casas.
""")

# Função para carregar os dados
@st.cache_data
def load_data():
    df = pd.read_csv('housing_sp_city.csv', encoding='latin1')
    return df

# Carrega os dados
data = load_data()
st.sidebar.header("Configurações e Filtros")
st.sidebar.write("Dataset com", data.shape[0], "registros")

# Exibe o dataset se o usuário desejar
if st.sidebar.checkbox("Mostrar dados brutos"):
    st.subheader("Dados Brutos")
    st.dataframe(data)

# --- Análise Exploratória ---
st.header("1. Análise Exploratória dos Dados")

# Histograma do Preço
st.subheader("Distribuição dos Preços das Casas")
fig1 = px.histogram(data, x="preco_venda", nbins=30, title="Distribuição dos Preços das Casas")
st.plotly_chart(fig1, use_container_width=True)

# Mapa de Correlação
st.subheader("Mapa de Correlação")
numeric_cols = data.select_dtypes(include=[np.number])

# Remover colunas que contêm valores constantes
numeric_cols = numeric_cols.loc[:, (numeric_cols != numeric_cols.iloc[0]).any()]

# Calcular a matriz de correlação
corr_matrix = numeric_cols.corr()

# Plotar o mapa de calor da correlação
fig2, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
st.pyplot(fig2)

# --- Modelagem Preditiva ---
st.header("2. Modelagem Preditiva")

st.markdown("""
Utilizaremos um modelo de **Random Forest** para prever o preço das casas com base em algumas variáveis selecionadas.
""")

# Selecionar features e variável alvo
features = ["area_util", "quartos", "banheiros", "vagas_garagem"]
X = data[features]
y = data['preco_venda']

# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar o modelo de Random Forest
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Treinar o modelo
model.fit(X_train, y_train)

# Fazer previsões
y_pred = model.predict(X_test)

# Avaliar o modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
st.subheader("Desempenho do Modelo de Random Forest")
st.write(f"**MSE:** {mse:.2f}")
st.write(f"**R²:** {r2:.2f}")

# Plotar previsões vs. valores reais
st.subheader("Previsões vs. Valores Reais")
fig3 = px.scatter(x=y_test, y=y_pred, labels={'x': 'Valores Reais', 'y': 'Previsões'}, title="Previsões vs. Valores Reais")
st.plotly_chart(fig3, use_container_width=True)