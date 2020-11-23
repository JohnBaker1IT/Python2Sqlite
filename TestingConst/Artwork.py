from Artist import Artist

class Artwork:
    # TODO: Define constructor with parameters to initialize instance attributes
    #       (title, year_created, artist)
    title = 'None'
    year_created = 0
    artist = Artist.name
        
    def __init__(self, title='None', year_created = 0, artist = Artist.name):
        self.title = 'None'
        self.year_created = 0
        self.artist = Artist.name
        
        
        self.title = title
        self.year_created = year_created
        self.artist = artist

    def print_info(self):
        self.artist.print_info()
        print('Title: %s, %d' % (self.title, self.year_created))