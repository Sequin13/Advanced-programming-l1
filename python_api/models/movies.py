import csv


class Movie:
    def __init__(self, movie_id, title, genres):
        self.movie_id = movie_id
        self.title = title
        self.genres = genres

    def __dict__(self):
        return {
            "movie_id": self.movie_id,
            "title": self.title,
            "genres": self.genres
        }


def get_movies_from_db():
    movies = []
    with open('database/movies.csv', mode='r', encoding='utf-8') as movies_file:
        read_movies_csv = csv.DictReader(movies_file, delimiter=',')
        for row in read_movies_csv:
            movie = Movie(row['movieId'], row['title'], row['genres'])
            movies.append(movie)
    return movies
