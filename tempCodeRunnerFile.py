from user import User 
import api_util

user1 = User("ericucca",['netfix'])
user2 = User("tony",['netflix','prime video'])


available_providers = api_util.get_providers()