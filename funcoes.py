filmes = [
    {"titulo": "Inception", "diretor": "Christopher Nolan", "ano": 2010, "genero": "Sci-Fi"},
    {"titulo": "The Matrix", "diretor": "Lana Wachowski", "ano": 1999, "genero": "Action"},
    {"titulo": "Parasite", "diretor": "Bong Joon-ho", "ano": 2019, "genero": "Thriller"},
    {"titulo": "Interstellar", "diretor": "Christopher Nolan", "ano": 2014, "genero": "Sci-Fi"},
]

def listar_filmes():
    print("todos os filmes")
    for i in filmes:
        print(i)
    

def lista_titulos_por_ano():
    print("todos os anos")
    for i in filmes:
        print(i["ano"])  
   
listar_filmes()
lista_titulos_por_ano()