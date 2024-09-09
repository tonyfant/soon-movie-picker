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
    from movie import Movie
    subscription_len = len(user.subscriptions)
    subscription_url = ''
    for i in range(subscription_len):
        subscription_url += f'{user.subscriptions[i]}%7C'
    if sum(user.genres_score.values())!=0:
        url = f"https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=false&page={random.randint(0,3)}&sort_by=popularity.desc&watch_region=IT&with_genres={user.get_preferred_genres()[0][0]}%7C{user.get_preferred_genres()[1][0]}%7C{user.get_preferred_genres()[2][0]}&with_watch_providers={subscription_url}"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyN2Q3MTExNjViZWZlMGYwOTYyNjYzMmY0OTI4NWUyZCIsIm5iZiI6MTcyNTQ4MzA5NC40ODk5NjksInN1YiI6IjY2YzlmZmUyYjRhOWE5ZTVmNDk0YWFhMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.tOq-sJa_2ogrks5_USvMBXBUaaGZo2RT-PUR45r9VqE"
        }

        response = requests.get(url, headers=headers)
        if response.status_code!=200:
            movies = get_popular_movies()
            return Movie(movies[random.randint(0,19)]['id'])
        else:
            data = response.json()
            movie = Movie(data['results'][random.randint(0,len(data['results'])-1)]['id'])
            return movie
    else:
        movies = get_popular_movies()
        return Movie(movies[random.randint(0,19)]['id'])



def get_movie_poster_url(movie_id):
    movie_data = get_movie_by_id(movie_id)
    if movie_data and 'poster_path' in movie_data:
        poster_path = movie_data['poster_path']
        base_url = 'https://image.tmdb.org/t/p/original'
        return f'{base_url}{poster_path}'
    else:
        print(f"Failed to fetch poster for movie ID {movie_id}")
        return None  
