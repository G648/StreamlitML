import pandas as pd
from sklearn import model_selection, preprocessing, pipeline, linear_model, metrics
import os

#primeira etapa: carregamento dos dados
#vamos utilizar o pandas pra isso

def carregar_dados(caminho_arquivo="historicoAcademico.csv"):
    """
    Carrega os dados de um arquivo CSV.
    """
    try:
        if os.path.exists(caminho_arquivo):
            # Correção 1: Usando pd.read_csv
            df = pd.read_csv(caminho_arquivo, encoding="latin1", delimiter=',')
            
            print("Arquivo carregado com sucesso!")
            
            return df
        else:
            print(f"Erro: Arquivo não encontrado em '{caminho_arquivo}'")
            return None
            
    # Correção 4: Capturando a exceção específica
    except Exception as e:
        print(f"Erro inesperado ao carregar o arquivo: {e}")
        return None

# --- Chamando a função e armazenando o resultado ---
dados = carregar_dados()
