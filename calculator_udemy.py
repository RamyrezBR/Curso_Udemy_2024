#   Notas sobre organização de código, clean code e f-strings

# Calculadora com While


while True:
    print('-_'*18)
    print(f'Calculadora com While')
    print(f"{'v1.0':>36}")
    print('-_'*18)
    opt_quit=input('\nQuer Sair? [s]im: ').lower().startswith('s')
    
    if opt_quit is True:
        break
    
    while True:
        print('-_'*18)
        print(f'Calculadora com While')
        print(f"{'v1.0':>36}")
        print('-_'*18)
        n1=input('\nDigite um numero: ')
        n2=input('Digite outro número: ')
        if n1.isdigit() and n2.isdigit():
            oper=str(input('Digite a operação (+-*/): '))
            if any(sinal in oper for sinal in '+-*/'):
                result=eval(f'{n1}{oper}{n2}')
                print(f'\n{n1:^5}{oper:^5}{n2:^5} = {result:^5}')
                break
            else:
                print('Erro')
                break

        else:
            print('não é num')
            break
    
    
        
   

   
    

