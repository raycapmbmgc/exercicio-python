numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

pessoas = [
    {"nome": "tony"},
    {"nome": "thor"},
    {"nome": "peter"}
]

natureza = ["rio", "floresta", "leão", "montanha", "oceano", "estrela", "vento", "cachoeira", "lua", "girassol"]
tecnologia = ["algoritmo", "API", "blockchain", "código", "software", "nuvem", "hardware", "interface", "pixel", "servidor"]


def segundo_maior_numero(lista):
    maior = numeros_maiores(lista)
    segundo_maior = None
    for numero in lista:
        if numero != maior:
            if segundo_maior is None or numero > segundo_maior:
                segundo_maior = numero
    return segundo_maior

print("O segundo maior número é:", segundo_maior_numero(numeros))
