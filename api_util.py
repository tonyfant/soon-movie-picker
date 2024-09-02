import requests


api_key = '27d711165befe0f09626632f49285e2d'


def get_movie_by_id(id): ##completata
    url = f'https://api.themoviedb.org/3/movie/{id}?api_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data: {response.status_code}")



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


def get_movie_providers_by_nationality(movie_id,nationality):
    """
    Questa funzione prende un ID di un film e restituisce i provider
    di streaming dove il film è disponibile.
    """
    url = f'https://api.themoviedb.org/3/movie/{movie_id}/watch/providers?api_key={api_key}'
    response = requests.get(url)
    providers = response.json().get('results', {})
    if providers[nationality]['flatrate']:
        return providers[nationality]['flatrate']
    else:
        print('Movie not available by subscriptions')
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



def recommend_movie(user,movies_visited):
    popular_movies = get_popular_movies()
    
    if not popular_movies:
        print("No popular movies found.")
        return None
    
    best_score = float('-inf')
    best_movie = None
    
    for movie in popular_movies:
        if movie['id'] in movies_visited:
            continue
        movie_genres = [genre for genre in movie['genre_ids']]
        score = sum(user.genres_score.get(genre, 0) for genre in movie_genres)
        
        if score > best_score:
            best_score = score
            best_movie = movie
    from movie import Movie
    if best_movie:
        return Movie(best_movie['id'])
    else:
        print("No suitable movie found.")
        return None