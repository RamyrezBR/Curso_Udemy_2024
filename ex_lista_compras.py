# Exercício que consiste em criar uma aplicação onde será criada uma lista de compras na qual o usuário será capaz de inserir, apagar e listar os itens, bem como deverá haver tratamento de erros para evitar erros de execução.

list_buy=[]

while True:

    print(f'''
        {'-_'*30}
          [i]nserir [a]pagar [l]istar [s]air:               v1.0
        {'-_'*30} 
          ''')
    opc=str(input("-> "))
   
    try:
        if opc=="i":
            item=str(input("\nNome do produto a ser add: "))
            if item in list_buy:
                print(f'\nJá existe {item} na lista! ')
            else:
                list_buy.append(item)
                print("\nItem adc com sucesso!")
        elif opc=="a":
            if len(list_buy)>0:
                item=str(input("\nNome do produto a ser del: "))
                list_buy.remove(item)
                print("\nItem apagado com sucesso!")
            else:
                print("\nA lista está vazia!")    
        elif opc=="l":
            if len(list_buy)>0:
                print('\nLista:')
                for i,j in enumerate(list_buy):
                    print(f'{i} {j}')
            else:
                print("\nA lista está vazia!")
            
        elif opc=="s":
            print("\nSaindo...")
            break
        else:
            print("\nValor inserido é inválido!")
        
    except Exception:
        print("\nProduto não encontrado!")
