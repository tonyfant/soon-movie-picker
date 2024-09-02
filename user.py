import api_util

class User():
    def __init__(self,username: str,nationality:str,subscriptions:list = []):
        self.username = username
        if len(nationality)==2:  
            self.nationality = nationality
        else:
            print('User not created, nationaity not valid')
            return 
        self.subscriptions = subscriptions
        genres = api_util.get_genres()
        self.genres_score = dict()
        for genre in genres.values():
            self.genres_score[genre] = 0
    
        
    def update_preferences(self,genres_liked: list,genres_disliked:list,like: bool):
        if like:
            for genre in genres_liked:
                self.genres_score[genre]+=1
        else:  
            for genre in genres_disliked:
                self.genres_score[genre]-=1
                
    def print_preferences(self):
        for genre in self.genres_score.keys():
            print(f"Genre: {genre}, score: {self.genres_score[genre]}")
                
# test_user= User('ericucca',['netflix'])

# genres_liked=[28,99]
# genres_disliked = [36,14]

# test_user.update_genres_preference(genres_liked,genres_disliked,True)


# test_user.update_genres_preference(genres_liked,genres_disliked,False)