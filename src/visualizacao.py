import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

st.title("Análise IBGE - População por Estado e Município")

# Lista de localidades (Brasil, estados e municípios)
localidades = {
    "Brasil": "N1[all]",
    "Rio de Janeiro": "N3[33]",
    "São Paulo": "N3[35]",
    "Minas Gerais": "N3[31]",
    "Bahia": "N3[29]",
    "São João de Meriti (RJ)": "N6[3305109]",
    "Belo Horizonte (MG)": "N6[3106200]",
    "Salvador (BA)": "N6[2927408]"
}

# Filtro interativo
localidade_escolhida = st.selectbox("Escolha a localidade:", list(localidades.keys()))

# Montar URL da API IBGE (tabela 6579 = população estimada)
url = f"https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/all/variaveis/9324?localidades={localidades[localidade_escolhida]}"
response = requests.get(url)
data = response.json()

# Transformar em DataFrame
anos = []
populacao = []
for item in data[0]['resultados'][0]['series'][0]['serie'].items():
    ano, valor = item
    anos.append(int(ano))
    populacao.append(int(valor))

df = pd.DataFrame({"Ano": anos, "População (milhões)": [v/1_000_000 for v in populacao]})

# Mostrar tabela
st.subheader(f"Tabela de população - {localidade_escolhida}")
st.dataframe(df)

# Calcular média
media = df["População (milhões)"].mean()

# Mostrar média em card
st.metric(label=f"Média da população em {localidade_escolhida}", value=f"{media:.2f} milhões")

# Mostrar média como texto explicativo
st.markdown(f"**A média da população em {localidade_escolhida} no período analisado foi de {media:.2f} milhões.**")

# Gráfico com cores vivas e linha da média
fig, ax = plt.subplots(figsize=(8,5))
ax.plot(df["Ano"], df["População (milhões)"], marker="o", color="dodgerblue", linewidth=2.5, label="População")
ax.axhline(y=media, color="crimson", linestyle="--", linewidth=2, label=f"Média ({media:.2f} milhões)")
ax.set_facecolor("#f9f9f9")
ax.set_title(f"População de {localidade_escolhida} segundo IBGE", fontsize=14, fontweight="bold")
ax.set_xlabel("Ano")
ax.set_ylabel("População (milhões)")
ax.grid(True, linestyle=":", alpha=0.7)
ax.legend()

st.subheader("Gráfico de população com média")
st.pyplot(fig)
