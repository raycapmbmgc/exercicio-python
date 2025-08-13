numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
pessoas = [
    {"nome": "tony"},
    {"nome": "thor"},
    {"nome": "peter"}
]

natureza = ["rio", "floresta", "leão", "montanha", "oceano", "estrela", "vento", "cachoeira", "lua", "girassol"]
tecnologia = ["algoritmo", "API", "blockchain", "código", "software", "nuvem", "hardware", "interface", "pixel", "servidor"]

def numeros_impares(lista):
    return [numero for numero in lista if numero % 2 != 0]

print("Números ímpares:", numeros_impares(numeros))