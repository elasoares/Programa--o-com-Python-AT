from leitura_arquivo import *
from menu import *
from opcoes_menu import *


def main():
    arquivo = obter_caminho_arq()
    produtos = ler_arquivo(arquivo)
    clientes_atendidos = []  
    cliente_id = 1  

    while True:
        exibir_menu()
        opcao = obter_opcao_menu()

        match opcao:
            case 1:
                iniciar_atendimento(produtos, clientes_atendidos, cliente_id)
            case 2:
                fechar_caixa(clientes_atendidos, arquivo, produtos)
            case 3:
                verificar_estoque(produtos)
            case 0:
                print("Programa encerrado.")
                break
            case _:
                print("Erro: opção inválida. Tente novamente.")                
main()
