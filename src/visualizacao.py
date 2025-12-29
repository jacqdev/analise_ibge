import matplotlib.pyplot as plt
import pandas as pd

def grafico_linha(dados: pd.DataFrame, coluna_x: str, coluna_y: str, titulo: str):
    """
    Cria um gráfico de linha simples e retorna a figura.
    """
    fig, ax = plt.subplots(figsize=(8,5))
    ax.plot(dados[coluna_x], dados[coluna_y], marker="o", linestyle="-", color="blue")
    ax.set_title(titulo)
    ax.set_xlabel(coluna_x)
    ax.set_ylabel(coluna_y)
    ax.grid(True)
    return fig
