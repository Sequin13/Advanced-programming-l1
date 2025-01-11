import csv


class Tags:
    def __init__(self, user_id, movie_id, tag, timestamp):
        self.user_id = user_id
        self.movie_id = movie_id
        self.tag = tag
        self.timestamp = timestamp

    def __dict__(self):
        return {
            "user_id": self.user_id,
            "movie_id": self.movie_id,
            "tag": self.tag,
            "timestamp": self.timestamp
        }


def get_tags_from_db():
    tags = []
    with (open('database/tags.csv', mode='r', encoding='utf-8')
          as tags_file):
        read_tag_csv = csv.DictReader(tags_file, delimiter=',')
        for row in read_tag_csv:
            tag = Tags(row['userId'], row['movieId'],
                       row['tag'], row['timestamp'])
            tags.append(tag)
    return tags
