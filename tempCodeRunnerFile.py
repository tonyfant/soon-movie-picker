from user import User 
import api_util
from movie import Movie

# available_providers = api_util.get_providers()

user = User("ericucca","IT",[8,9,10,11,12,337])

movies_visited = []
genres = api_util.get_genres()



def display_menu():
    print('''
          Film Matching System
          1) Like
          2) Dislike
          3) It's my film
          ''')

def check_subscriptions(user:User,movie:Movie):
    for subscription in movie.subscriptions_needed:
        print(f'richiesta{subscription}, in possesso: {user.subscriptions}')
        if subscription in user.subscriptions:
            return True
    return False
        

print("Let's start,")

choose = 0
movie = api_util.recommend_movie(user)
print('assegnato')
while choose != 3:
    if check_subscriptions(user,movie):
        print('compatibile')
        movie.print_info()
        display_menu()
        choose = int(input('Option selected: '))
        if choose == 1:
            user.update_preferences(api_util.get_movie_genres(movie.id),[],True)
        elif choose ==2:
            user.update_preferences([],api_util.get_movie_genres(movie.id),False)
        elif choose ==3:
            print('Movie chosen')
            break
        else:
            print('Choose not valid')
        user.print_preferences()
        movie = api_util.recommend_movie(user)
        print('assegnato')
    else:
        print('non compatibile')
        movie = api_util.recommend_movie(user)
        print('assegnato')
