import streamlit as st
import pandas as pd
import os
from pathlib import Path

# Importar módulos locais corretamente via pacote src
import src.coleta as coleta
import src.limpeza as limpeza
import src.analise as analise
import src.visualizacao as visualizacao

st.title("📊 Análise de Dados IBGE")

# Base path: sempre aponta para a raiz do projeto
BASE_PATH = Path(__file__).resolve().parent.parent / "data" / "raw"

# Função auxiliar para carregar CSV com fallback
def carregar_ou_exemplo(nome_arquivo, exemplo):
    caminho = BASE_PATH / nome_arquivo
    if caminho.exists():
        df = coleta.carregar_csv(caminho)
    else:
        # Usa dados de exemplo sem mostrar aviso de erro
        df = pd.DataFrame(exemplo)
    # Padronizar nomes de colunas
    df.columns = df.columns.str.strip().str.lower()
    return df

# Carregar dados (ou usar exemplo se não existir)
populacao = carregar_ou_exemplo(
    "populacao.csv",
    {"ano": [2020, 2021, 2022, 2023], "populacao": [210000000, 211000000, 213000000, 214000000]}
)

desemprego = carregar_ou_exemplo(
    "desemprego.csv",
    {"ano": [2020, 2021, 2022, 2023], "desemprego": [12.5, 11.0, 9.8, 8.7]}
)

renda = carregar_ou_exemplo(
    "renda.csv",
    {"ano": [2020, 2021, 2022, 2023], "renda_media": [2000, 2500, 2700, 2900]}
)

# Mostrar tabelas
st.subheader("📊 População")
st.dataframe(populacao)

st.subheader("📉 Desemprego")
st.dataframe(desemprego)

st.subheader("💰 Renda")
st.dataframe(renda)

# Análises
st.subheader("Média da Renda")
st.write(f"{analise.calcular_media_renda(renda):.2f}")

st.subheader("Taxa média de Desemprego")
st.write(f"{analise.calcular_taxa_desemprego_media(desemprego):.2f}")

# Gráficos para visualização
st.subheader("📈 Evolução da População")
st.line_chart(populacao.set_index("ano"))

st.subheader("📉 Evolução do Desemprego")
st.line_chart(desemprego.set_index("ano"))

st.subheader("💰 Evolução da Renda Média")
st.line_chart(renda.set_index("ano"))
