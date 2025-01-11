import csv


class Ratings:
    def __init__(self, user_id, movie_id, rating, timestamp):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating
        self.timestamp = timestamp

    def __dict__(self):
        return {
            "user_id": self.user_id,
            "movie_id": self.movie_id,
            "rating": self.rating,
            "timestamp": self.timestamp
        }


def get_ratings_from_db():
    ratings = []
    with (open('database/ratings.csv', mode='r', encoding='utf-8')
          as ratings_file):
        read_ratings_csv = csv.DictReader(ratings_file, delimiter=',')
        for row in read_ratings_csv:
            rating = Ratings(row['userId'], row['movieId'],
                             row['rating'], row['timestamp'])
            ratings.append(rating)
    return ratings
