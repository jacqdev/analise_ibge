import pandas as pd
import pytest
import src.coleta as coleta

def test_carregar_csv(tmp_path):
    # cria um CSV temporário válido
    arquivo = tmp_path / "teste.csv"
    pd.DataFrame({"Ano": [2020], "Renda_media": [2000]}).to_csv(arquivo, index=False)

    # chama a função de coleta
    df = coleta.carregar_csv(arquivo)

    # verifica se as colunas foram padronizadas
    assert "ano" in df.columns
    assert "renda_media" in df.columns
    assert df.iloc[0]["ano"] == 2020
    assert df.iloc[0]["renda_media"] == 2000

def test_carregar_csv_arquivo_inexistente():
    # tenta carregar um arquivo que não existe
    with pytest.raises(FileNotFoundError):
        coleta.carregar_csv("arquivo_inexistente.csv")

def test_carregar_csv_erro_runtime(tmp_path):
    # cria um arquivo vazio para forçar erro de leitura
    arquivo = tmp_path / "invalido.csv"
    arquivo.write_text("")  # arquivo sem conteúdo

    # espera que a função levante RuntimeError
    with pytest.raises(RuntimeError):
        coleta.carregar_csv(arquivo)
