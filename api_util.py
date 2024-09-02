import requests
import random

api_key = '27d711165befe0f09626632f49285e2d'


def get_movie_by_id(id): ##completata
    url = f'https://api.themoviedb.org/3/movie/{id}?api_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data: {response.status_code}")


def get_movie_casually():
    movie = None
    while not movie:
        url = f'https://api.themoviedb.org/3/movie/{random.randint(0,100000)}?api_key={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            movie = response.json()
    return movie


def get_genres(): ##completata
    url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}'
    response = requests.get(url)
    
    if response.status_code == 200:
        genres = response.json().get('genres', [])
        genre_dict = {genre['name']: genre['id'] for genre in genres}
        return genre_dict
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return {}
    
def get_movie_genres(movie_id): 
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        movie = response.json()
    else:
        print(f"Failed to fetch data: {response.status_code}")
    genres = []
    for genre in movie['genres']:
        genres.append(genre['id'])
    return genres


def get_providers():
    url = f'https://api.themoviedb.org/3/watch/providers/movie?api_key={api_key}'
    response = requests.get(url)
    providers = response.json()
    providers_dict = dict()
    for provider in providers['results']:
        providers_dict[provider['provider_id']] = provider['provider_name']
    return providers_dict


def get_movie_providers_by_nationality(movie_id, nationality="US"):
    print(movie_id)
    url = f'https://api.themoviedb.org/3/movie/{movie_id}/watch/providers?api_key={api_key}'
    response = requests.get(url)
    providers = response.json().get('results', {})

    # Verifica se la chiave 'nationality' esiste nel dizionario 'providers'
    if nationality in providers:
        if 'flatrate' in providers[nationality]:
            return [provider['provider_id'] for provider in providers[nationality]['flatrate']]
        else:
            print('Movie not available by subscriptions in your region')
            return []
    else:
        print(f'Movie not available in {nationality}')
        return []

    


def get_popular_movies():
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get('results', [])
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return []


def recommend_movie(user):
    from user import User
    from movie import Movie
    if sum(user.genres_score.values()) == 0:
        return Movie(get_movie_casually()['id'])
    score = 0
    while score<1:
        casual_movie = get_movie_casually()

        movie = Movie(casual_movie['id'])
        score = 0
        for genre in movie.genres:
            score+=user.genres_score[genre]
    return movie
        
    
    
    
    
    

# old function, works
# def recommend_movie(user,movies_visited):
#     popular_movies = get_popular_movies()
    
#     if not popular_movies:
#         print("No popular movies found.")
#         return None
    
#     best_score = float('-inf')
#     best_movie = None
    
#     for movie in popular_movies:
#         if movie['id'] in movies_visited:
#             continue
#         movie_genres = [genre for genre in movie['genre_ids']]
#         score = sum(user.genres_score.get(genre, 0) for genre in movie_genres)
        
#         if score > best_score:
#             best_score = score
#             best_movie = movie
#     from movie import Movie
#     if best_movie:
#         return Movie(best_movie['id'])
#     else:
#         print("No suitable movie found.")
#         return None