'''Exercício - Sistema de perguntas e respostas'''

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2',
        'Opções': [1,2,3,4,5],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5',
        'Opções': ['25','55','10','51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2',
        'Opções': ['4','5','2','1'],
        'Resposta': '5',
    },
]

pontos=0
for j in range(3):
    
    list_aux=perguntas[j].get('Opções')
    print(f'\n{perguntas[j].get("Pergunta")}\n')
    for i in range(len(list_aux)):
        print(f'{i}) {list_aux[i]}')
    p1=input('\nEscolha uma opção:')
    if p1.isdigit():
        p1=int(p1)
        if int(list_aux[p1])==int(perguntas[j].get('Resposta')):
            print('\nAcertou!!')
            pontos+=1
    else:
        print('\nErrou!!')
print(f'\nSua pontuação: {pontos} pts')
