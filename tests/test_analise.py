import pandas as pd
import pytest
from src import analise

def test_media_renda():
    dados = pd.DataFrame({"ano": [2020, 2021], "renda_media": [2000, 2500]})
    resultado = analise.calcular_media_renda(dados)
    assert resultado == 2250

def test_taxa_media_desemprego():
    dados = pd.DataFrame({"ano": [2020, 2021], "desemprego": [10, 12]})
    resultado = analise.calcular_taxa_desemprego_media(dados)
    assert resultado == 11

def test_media_renda_coluna_inexistente():
    dados = pd.DataFrame({"ano": [2020], "renda": [2000]})  # falta 'renda_media'
    with pytest.raises(KeyError):
        analise.calcular_media_renda(dados)

def test_taxa_desemprego_coluna_inexistente():
    dados = pd.DataFrame({"ano": [2020], "taxa": [10]})  # falta 'desemprego'
    with pytest.raises(KeyError):
        analise.calcular_taxa_desemprego_media(dados)
