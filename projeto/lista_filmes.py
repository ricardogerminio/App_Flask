import urllib.request
import json

api_key = "8f2bbcc07a85a14d8443404dade0e335"

def resultado_filmes(tipo):
    if tipo == "populares":
        url = f"https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key={api_key}"
    elif tipo == "animacao":
        url = f"https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key={api_key}"
    elif tipo == "2010":
        url = f"https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key={api_key}"
    else:
        url = ""
    
    resposta = urllib.request.urlopen(url)
    dados = resposta.read()
    dados_json = json.loads(dados)
    return dados_json['results']

#print(dados_json['results'])