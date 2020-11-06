# Exercicio 2

def abrir_arquivo(file):
    lista = []
    with open(file, 'r') as f:
        data = f.readlines()
        for item in data:
            lista.append(item.strip().split())
    return lista


def conversor(lista):
    for item in range(len(lista)):
        tamanho_mbytes = float(lista[item][1]) / (1024 * 1024)
        lista[item][1] = f'{tamanho_mbytes:.2f}'


def espaco_total(lista):
    total = 0
    for item in range(len(lista)):
        total += float(lista[item][1])
    return total


def porcentagem_de_uso(lista, total):
    for item in range(len(lista)):
        percentual = (float(lista[item][1]) / total) * 100
        lista[item].append(f'{percentual:1f}')


dados = abrir_arquivo('usuarios.txt')
conversor(dados)
total = espaco_total(dados)
porcentagem_de_uso(dados, total)

with open('relatorio-usuarios.txt', 'w') as f:
    f.write(f'ACME Inc. {" " * 10}   {"Uso do espaço em disco pelos usúarios"}\n')
    f.write(f'{"-" * 60}\n')
    f.write(f'NR   Usuario       Espaço utilizado    % do uso\n')
    for _ in range(len(dados)):
        f.write(f'{_ + 1}    {dados[_][0]:<10}      {dados[_][1]:^11}         {dados[_][2]:^11}%\n')

    f.write(f'\nEspaço total ocupado: {total} MB\n')
    f.write(f'Espaço médio ocupado: {total / len(dados):2f} MB')
