import csv
from tabulate import tabulate
from datetime import datetime



def caixa(produtos):
    print()
    print("Produtos disponíveis:")
    headers = ["ID", "Produto", "Quantidade", "Preço"]
    print(tabulate(produtos, headers=headers, tablefmt="grid"))

def iniciar_atendimento(produtos, clientes_atendidos, cliente_id):
    while True:
        itens_comprados = []
        valor_total = 0  

        caixa(produtos)
        try:
            while True:
                id_produto = int(input("Digite o ID do produto ou 0 para finalizar: "))
                if id_produto == 0:  
                    break

                produto = next((p for p in produtos if p[0] == id_produto), None)
                if not produto:
                    print("Erro: produto não cadastrado.")
                    continue

                quantidade = int(input(f"Digite a quantidade de '{produto[1]}' que deseja comprar: "))
                if quantidade > produto[2]:
                    print("Erro: Produto não disponível no estoque.")
                    continue

                preco_total = quantidade * produto[3]
                itens_comprados.append([produto[0], produto[1], quantidade, produto[3], preco_total])
                valor_total += preco_total  

                produto[2] -= quantidade  
        except ValueError:
            print("Erro: entrada inválida. Digite um número válido.")

        if itens_comprados:
            gerar_nota_fiscal(cliente_id, itens_comprados, valor_total)
            clientes_atendidos.append((cliente_id, valor_total))  

        cliente_id += 1  
        continuar_atendimento = input("Iniciar atendimento para o próximo cliente? (s/n): ").lower()
        if continuar_atendimento != "s": 
            break

    return cliente_id


def gerar_nota_fiscal(cliente_id, itens_comprados, valor_total):
    print()
    print(f"Cliente {cliente_id}")
    print(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print()
    headers = ["ID", "Produto", "Quant.", "Preço", "Total"]
    print(tabulate(itens_comprados, headers=headers, tablefmt="grid"))
    print()
    total_itens = len(itens_comprados)  

    print(f"Itens: {total_itens}")
    print(f"Total : {valor_total:.2f}")
    print()



def salvar_produtos(arquivo, produtos):
    try:
        with open(arquivo, "w", newline="") as arq:
            escritor = csv.writer(arq)
            escritor.writerows(produtos)
    except:
        print(f"Erro ao salvar produtos.")

def fechar_caixa(clientes_atendidos, arquivo, produtos):
    print("Fechamento do Caixa")
    print(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print()
    headers = ["Cliente", "Total"]
    total_vendas = sum(cliente[1] for cliente in clientes_atendidos)
    print(tabulate( clientes_atendidos, headers=headers, tablefmt="grid"))
    print(f"Total de vendas: {total_vendas:.2f}")
    print()
    
    salvar_produtos(arquivo, produtos)
    print("Produtos atualizados e salvos com sucesso!")

def verificar_estoque(produtos):
    print()
    print("Produtos sem estoque: ")
    for produto in produtos:
        if(produto[2] == 0):
            print("Produto", produto[0])
    print()
    

