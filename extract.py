import requests
from dotenv import load_dotenv
import os

load_dotenv()

def extract_data():
    list_genres = []
    list_movies = []
    list_movies_with_details = []

    base_url = "https://api.themoviedb.org/3"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.getenv('TOKEN')}"
    }

    def get_genres():
        try:
            response = requests.get(f"{base_url}/genre/movie/list", params={"language": "en-US"}, headers=headers)
            response.raise_for_status()
            data = response.json()
            
            list_genres.extend(data['genres'])
        except requests.exceptions.RequestException as e:
            print(f"Erro de conexão ao obter lista de gêneros dos filmes: {e}")
            return None
    
    get_genres()

    def get_popular_movies(page):
        try:
            print(f"Coletando a página {page}")
            response = requests.get(f"{base_url}/movie/popular", params={"language": "en-US", "page": page}, headers=headers)
            response.raise_for_status()

            data = response.json()
            list_movies = data.get('results', [])

            return list_movies
        except requests.exceptions.RequestException as e:
            print(f"Erro de conexão ao obter filmes populares: {e}")
            return []

    def get_movies():
        for page in range(1, 6):  # Faz 5 chamadas para obter 100 filmes (20 filmes por chamada)
            movies = get_popular_movies(page)
            list_movies_with_details.extend(movies)
        # Lógica para coletar todos os filmes disponíveis no endpoint
        # page = 1
        # while True:
        #     movies = popular_movies(page)
        #     if not movies:
        #         break
        #     list_movies_with_details.extend(movies)
        #     page += 1

    get_movies()


    def get_details_movie(id):
        try:
            response = requests.get(f"{base_url}/movie/{id}", params={"language": "en-US"}, headers=headers)
            response.raise_for_status()
            data = response.json()

            return data
        except requests.exceptions.RequestException as e:
            print(f"Erro de conexão ao obter detalhes do filme {id}: {e}")
            return None

    for movie in list_movies:
        movie_id = movie['id']
        details = get_details_movie(movie_id)
        if details:
            list_movies_with_details.append(details)

    for movie in list_movies_with_details:
        genre_ids = movie['genre_ids']
        genres = [genre['name'] for genre in list_genres if genre['id'] in genre_ids]
        movie['genres'] = genres

    return list_movies_with_details
