import webbrowser #module to access the browser

class Movie():
    """ This class defines the information to be stored about a movie"""
    
    def __init__(self,movie_title,storyline,poster_image,youtube_trailer):
        self.title=movie_title #instances of the class movie  
        self.storyline=storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=youtube_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)  #function to open a specific url in the browser 
        
        
