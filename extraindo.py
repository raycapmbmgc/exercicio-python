pessoas = [
    {"nome": "tony"},
    {"nome": "thor"},
    {"nome": "peter"}
]

def extraindo_nomes(pessoas):
    print("Pessoas da Marvel:")
    for i in pessoas:
        print(i["nome"])

extraindo_nomes(pessoas)