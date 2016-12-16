class Movie():
    """This class provides a way to store movie information."""

    def __init__(self, movie_title, poster_image, trailer_youtube):
        """This function(class constructor) takes as input arguments that
        will be assigned to the instances of the class Movie.
        """
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
