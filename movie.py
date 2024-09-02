import api_util

class Movie():
    def __init__(self,id):
        self.id = id
        data = api_util.get_movie_by_id(id)
        self.title = data['title']
        self.year = data['release_date']
        self.overview = data['overview']
        self.subscriptions_needed = api_util.get_movie_providers_by_nationality(id,"IT")
        
    def print_info(self):
        
        print(f'''
              Title: {self.title},
              Release date: {self.year}
              Description: {self.overview}
              ''')
        
        
# movie1 = Movie(5075)

# movie1.print_info()