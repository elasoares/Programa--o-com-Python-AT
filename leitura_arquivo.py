import os
import pathlib
def obter_caminho_arq():
    arq = pathlib.Path(__file__).parent.resolve()
    diretorio = os.path.join(arq, "caixa")
    os.makedirs(diretorio, exist_ok=True)
    arq_csv = os.path.join(diretorio, "produtos.csv")
    return arq_csv

def ler_arquivo(arq_csv):
    produtos = []
    try:
        with open(arq_csv, "r") as arq:
            for linha in arq:
                linha = linha.strip("").split(",")
                id, nome, quantidade, preco = linha
                produtos.append([int(id), nome, int(quantidade), float(preco)])
    except :
        print(f"Erro ao ler o arquivo CSV.")
    return produtos