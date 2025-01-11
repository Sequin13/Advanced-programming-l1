import csv


class Links:
    def __init__(self, movie_id, imdb_id, tmdb_id):
        self.movie_id = movie_id
        self.imdb_id = imdb_id
        self.tmdb_id = tmdb_id

    def __dict__(self):
        return {
            "movie_id": self.movie_id,
            "imdb_id": self.imdb_id,
            "tmdb_id": self.tmdb_id
        }


def get_links_from_db():
    links = []
    with (open('database/movies.csv', mode='r', encoding='utf-8')
          as links_file):
        read_links_csv = csv.DictReader(links_file, delimiter=',')
        for row in read_links_csv:
            link = Links(row['movieId'], row['imdbId'], row['tmdbId'])
            links.append(link)
    return links
