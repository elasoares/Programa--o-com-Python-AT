
def exibir_menu():
    print("--- MENU ---")
    print("1. Iniciar atendimento")
    print("2. Fechar caixa")
    print("3. Verificar estoque")
    print("0. Encerrar programa")

def obter_opcao_menu():
    while True:
        try:
            entrada = input("Escolha uma opção: ").strip()
            if entrada.isdigit():
                return int(entrada)
            else:
                print("Erro: insira um número válido.")
        except:
            print(f"Erro na escolha da opção. Insira um número válido.")





