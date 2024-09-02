from user import User 
import api_util
from movie import Movie

# available_providers = api_util.get_providers()

user = User("ericucca","IT",[8])
user2 = User("tony",'IT',[9,8])
movies_visited = []

def display_menu():
    print('''
          Film Matching System
          1) Like
          2) Dislike
          3) It's my film
          ''')
movie_compatible=False

print("Let's start,")
while not movie_compatible : 
    movie = api_util.recommend_movie(user,movies_visited)
    for sub_1 in movie.subscriptions_needed:
        for sub_2 in user.subscriptions:
            if sub_1==sub_2:
                print(f"You got this subscription, id: {sub_2}")
                movies_visited.append(movie.id)
                movie_compatible=True
    movies_visited.append(movie.id)


    

movie.print_info()
display_menu()
choose = input('Option selected: ')
while choose != 3:
    if choose == 1:
        user.uppdate_preferences(api_util.get_movie_genres(movie.id),[],True)
    elif choose ==2:
        user.uppdate_preferences([],api_util.get_movie_genres(movie.id),False)
    elif choose ==3:
        print('Movie chosen')
        break
    else:
        print('Choose not valid')


