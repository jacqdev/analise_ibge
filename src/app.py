import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

st.title("Análise IBGE - Comparação de População com Filtro de Período")

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

# Filtros interativos
col1, col2 = st.columns(2)
localidade1 = col1.selectbox("Escolha a primeira localidade:", list(localidades.keys()), index=1)
localidade2 = col2.selectbox("Escolha a segunda localidade:", list(localidades.keys()), index=2)

def get_data(localidade):
    url = f"https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/all/variaveis/9324?localidades={localidades[localidade]}"
    response = requests.get(url)
    data = response.json()
    anos, populacao = [], []
    for item in data[0]['resultados'][0]['series'][0]['serie'].items():
        ano, valor = item
        anos.append(int(ano))
        populacao.append(int(valor))
    return pd.DataFrame({"Ano": anos, "População (milhões)": [v/1_000_000 for v in populacao]})

# Obter dados das duas localidades
df1 = get_data(localidade1)
df2 = get_data(localidade2)

# Filtro de período
anos_disponiveis = sorted(df1["Ano"].unique())
inicio, fim = st.select_slider(
    "Selecione o período:",
    options=anos_disponiveis,
    value=(anos_disponiveis[0], anos_disponiveis[-1])
)

df1_filtrado = df1[(df1["Ano"] >= inicio) & (df1["Ano"] <= fim)]
df2_filtrado = df2[(df2["Ano"] >= inicio) & (df2["Ano"] <= fim)]

# Calcular médias
media1 = df1_filtrado["População (milhões)"].mean()
media2 = df2_filtrado["População (milhões)"].mean()

# Mostrar métricas
st.metric(label=f"Média da população em {localidade1} ({inicio}-{fim})", value=f"{media1:.2f} milhões")
st.metric(label=f"Média da população em {localidade2} ({inicio}-{fim})", value=f"{media2:.2f} milhões")

# Gráfico comparativo
fig, ax = plt.subplots(figsize=(9,6))
ax.plot(df1_filtrado["Ano"], df1_filtrado["População (milhões)"], marker="o", color="dodgerblue", linewidth=2.5, label=f"{localidade1}")
ax.plot(df2_filtrado["Ano"], df2_filtrado["População (milhões)"], marker="s", color="darkorange", linewidth=2.5, label=f"{localidade2}")
ax.axhline(y=media1, color="blue", linestyle="--", linewidth=1.5, label=f"Média {localidade1} ({media1:.2f}M)")
ax.axhline(y=media2, color="orange", linestyle="--", linewidth=1.5, label=f"Média {localidade2} ({media2:.2f}M)")
ax.set_facecolor("#f9f9f9")
ax.set_title(f"Comparação de População: {localidade1} vs {localidade2} ({inicio}-{fim})", fontsize=14, fontweight="bold")
ax.set_xlabel("Ano")
ax.set_ylabel("População (milhões)")
ax.grid(True, linestyle=":", alpha=0.7)
ax.legend()

st.subheader("Gráfico comparativo de população")
st.pyplot(fig)