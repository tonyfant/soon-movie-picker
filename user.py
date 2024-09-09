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
            
    
    def get_preferred_genres(self):
        return sorted(self.genres_score.items(), key=lambda x: x[1], reverse=True)[:3]
                
        
