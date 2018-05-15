import webbrowser


class Movie():
    """store movie attributes as follows:
       title: stores the title of the movie.
       storyline: stores the basic info about the movie.
       poster_image_url: stores the URL of the movie poster.
       trailer_youtube_url: stores the URL of the movie trailer.
    """

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube,):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

        def show_trailer(self):
            """plays the trailer of the movie when clicked on."""
            webbrowser.open(self.trailer_youtube_url)
