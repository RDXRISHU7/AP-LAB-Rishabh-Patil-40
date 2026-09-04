class Movie:
    def __init__(self, name, rating, ticket_price):
        self.name = name
        self.rating = rating
        self.ticket_price = ticket_price

        # Categorize movie based on rating
        if rating >= 8:
            self.category = "Hit"
        elif rating >= 5:
            self.category = "Average"
        else:
            self.category = "Flop"

    def display(self):
        print("Movie Name:", self.name)
        print("Rating:", self.rating)
        print("Ticket Price:", self.ticket_price)
        print("Category:", self.category)
        print("------------------------")


class Cinema:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def display_movies(self):
        print("===== Movie Collection =====")
        for movie in self.movies:
            movie.display()


# Creating Cinema object
cinema = Cinema()

# Adding movies
cinema.add_movie(Movie("Avengers", 9, 250))
cinema.add_movie(Movie("Dangal", 7, 200))
cinema.add_movie(Movie("Race 3", 3, 150))

# Display movie details
cinema.display_movies()
