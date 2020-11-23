# TODO: Import Artist from Artist.py and Artwork from Artwork.py

from Artist import Artist
from Artwork import Artwork


if __name__ == "__main__":
#     user_artist_name = input()
#     user_birth_year = int(input())
#     user_death_year = int(input())
#     user_title = input()
#     user_year_created = int(input())
    
    user_artist_name = 'Brice Marden'
    user_birth_year = 1881
    user_death_year = 1973
    user_title = 'Three Musicians'
    user_year_created = 1921  
    
    user_artist_name = 'Pablo Picasso'
    user_birth_year = 1881
    user_death_year = 1973
    user_title = 'Three Musicians'
    user_year_created = 1921                       
                        

    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)

    new_artwork = Artwork(user_title, user_year_created, user_artist)
  
    new_artwork.print_info()