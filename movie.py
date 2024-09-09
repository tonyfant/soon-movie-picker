import api_util

class Movie():
    def __init__(self,id):
        self.id = id
        data = api_util.get_movie_by_id(id)
        self.title = data['title']
        self.year = data['release_date']
        self.overview = data['overview']
        # self.subscriptions_needed = api_util.get_movie_providers_by_nationality(id)
        self.genres = api_util.get_movie_genres(id)
        self.picture_url = api_util.get_movie_poster_url(id)
        
    def print_info(self):
        
        print(f'''
              Title: {self.title},
              Release date: {self.year}
              Description: {self.overview}
              Genres: {self.genres}
              ''')             
            #   Subscriptions needed: {self.subscriptions_needed}

    def print_genres(self):
        genres_dict = {
                    28:"Action",
                    12:"Adventure",
                    16:"Animation",
                    35:"Comedy",
                    80:"Crime",
                    99:"Documentary",
                    18:"Drama",
                    10751:"Family",
                    14:"Fantasy",
                    36:"History",
                    27:"Horror",
                    10402:"Music",
                    9648:"Mystery",
                    10749:"Romance",
                    878:"Science Fiction",
                     10770:"TV Movie",
                    53:"Thriller",
                    10752:"War",
                    37:"Western"}
        genres_list=[]
        for genre in self.genres:
            this_genre=genres_dict[genre]
            genres_list.append(this_genre)
            
        return genres_list
    

# movie1 = Movie(5075)

# movie1.print_info()