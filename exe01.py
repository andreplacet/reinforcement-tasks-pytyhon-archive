# Exercicio 01

import re

ips_validos = []
ips_invalidos = []


def verificar_ip(ip):
    ip_regex = re.compile(r'\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b')

    if ip_regex.search(ip):
        return True
    return False


def abrir_arquivo(arquivo):
    lista = []
    with open(arquivo, 'r') as file:
        f = file.readlines()
        for item in f:
            lista.append(item.rstrip())
    file.close()
    return lista


def escrever_arquivo(lista, lista2):
    with open('lista_ips.txt', 'w') as f:
        f.writelines('[IPS VALIDOS}\n')
        for item in lista:
            f.write(f'{item}\n')
        f.writelines('[IPS INVALIDOS]\n')
        for i in lista2:
            f.writelines(f'{i}\n')


arquivo = abrir_arquivo('ips.txt')

for item in arquivo:
    valida = verificar_ip(item)
    if valida:
        ips_validos.append(item)
    else:
        ips_invalidos.append(item)

escrever_arquivo(ips_validos, ips_invalidos)

