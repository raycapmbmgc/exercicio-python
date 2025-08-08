
numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

pessoas = [
    {"nome": "tony"},
    {"nome": "thor"},
    {"nome": "peter"}
]

natureza = ["rio", "floresta", "leão", "montanha", "oceano", "estrela", "vento", "cachoeira", "lua", "girassol"]
tecnologia = ["algoritmo", "API", "blockchain", "código", "software", "nuvem", "hardware", "interface", "pixel", "servidor"]

# 1. Percorrer lista
def percorrer_lista(lista):
    print("Todos os números da lista:")
    for i in lista:
        print(i)

# 2. Maior número
def numeros_maiores(lista):
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior

# 3. Segundo maior número
def segundo_maior_numero(lista):
    maior = numeros_maiores(lista)
    segundo_maior = None
    for numero in lista:
        if numero != maior:
            if segundo_maior is None or numero > segundo_maior:
                segundo_maior = numero
    return segundo_maior

# 4. Números pares
def numeros_pares(lista):
   return [numero for numero in lista if numero % 2 == 0]

# 5. Números ímpares
def numeros_impares(lista):
    return [numero for numero in lista if numero % 2 != 0]

# 6. Buscar número
def buscar_numero(numero, lista):
    return numero in lista

# 7. Extraindo nomes
def extraindo_nomes(pessoas):
    print("Pessoas da Marvel:")
    for i in pessoas:
        print(i["nome"])

# 8. Somar lista
def somar_lista(lista):
    return sum(lista)

# 9. Contar ocorrências
def contar_ocorrencias(lista, valor):
    return lista.count(valor)

# 10. Remover duplicatas
def remover_duplicatas(lista):
    return list(set(lista))

# 11. Verificar se lista está vazia
def verificar_lista_vazia(lista):
    return len(lista) == 0

# 12. Juntar duas listas
def juntar_listas(lista1, lista2):
    return lista1 + lista2

# 13. Menor número
def menor_numero(lista):
    return min(lista)

# 14. Calcular média
def calcular_media(lista):
    return sum(lista) / len(lista) if lista else 0

# 15. Inverter lista
def inverter_lista(lista):
    return lista[::-1]

# Chamadas das funções
percorrer_lista(numeros)
print("O maior número é:", numeros_maiores(numeros))
print("O segundo maior número é:", segundo_maior_numero(numeros))
print("Números pares:", numeros_pares(numeros))
print("Números ímpares:", numeros_impares(numeros))
print("Número 42 está na lista?", buscar_numero(42, numeros))
print("Número 18 está na lista?", buscar_numero(18, numeros))
extraindo_nomes(pessoas)
print("Soma dos números:", somar_lista(numeros))
print("Ocorrências do número 13:", contar_ocorrencias(numeros, 13))
print("Lista sem duplicatas:", remover_duplicatas(numeros))
print("A lista está vazia?", verificar_lista_vazia(numeros))
print("Lista combinada (natureza + tecnologia):", juntar_listas(natureza, tecnologia))
print("Menor número:", menor_numero(numeros))
print("Média dos números:", calcular_media(numeros))
print("Lista invertida:", inverter_lista(numeros))
