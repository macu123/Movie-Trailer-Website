import webbrowser

class Movie():
    def __init__(self, title, storyline, img_url, trailer_url, starring,
                 language, genre, release_date):
        self.title = title
        self.storyline = storyline
        self.img_url = img_url
        self.trailer_url = trailer_url
        self.starring = starring
        self.language = language
        self.genre = genre
        self.release_date = release_date

    def show_trailer(self):
        webbrowser.open(self.trailer_url)
