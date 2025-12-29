import os
import pandas as pd
import src.dashboard as dashboard

def test_carregar_ou_exemplo_fallback():
    # força uso do exemplo porque o arquivo não existe
    exemplo = {"ano": [2020], "populacao": [210000000]}
    df = dashboard.carregar_ou_exemplo("nao_existe.csv", exemplo)

    # verifica se os dados de exemplo foram carregados corretamente
    assert "ano" in df.columns
    assert "populacao" in df.columns
    assert df.iloc[0]["ano"] == 2020
    assert df.iloc[0]["populacao"] == 210000000

def test_carregar_ou_exemplo_com_arquivo(tmp_path):
    # cria um CSV temporário
    arquivo = tmp_path / "populacao.csv"
    pd.DataFrame({"ano": [2020], "populacao": [210000000]}).to_csv(arquivo, index=False)

    # força o BASE_PATH a apontar para tmp_path
    dashboard.BASE_PATH = tmp_path
    df = dashboard.carregar_ou_exemplo("populacao.csv", {"ano": [], "populacao": []})

    # verifica se os dados foram carregados do arquivo
    assert df.iloc[0]["ano"] == 2020
    assert df.iloc[0]["populacao"] == 210000000
