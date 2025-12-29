import pandas as pd
import src.visualizacao as vis

def test_grafico_linha():
    dados = pd.DataFrame({
        "ano": [2020, 2021, 2022],
        "renda_media": [2000, 2500, 3000]
    })
    fig = vis.grafico_linha(dados, "ano", "renda_media", "Evolução da Renda")
    assert fig is not None  # garante que o gráfico foi criado
