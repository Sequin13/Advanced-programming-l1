from flask import jsonify, Flask
from flask_restful import Resource, Api

from python_api.models.links import get_links_from_db
from python_api.models.movies import get_movies_from_db
from python_api.models.ratings import get_ratings_from_db
from python_api.models.tags import get_tags_from_db

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class MoviesEndpoint(Resource):
    def get(self):
        movies = get_movies_from_db()
        return jsonify([movie.__dict__() for movie in movies])


class RatingsEndpoint(Resource):
    def get(self):
        ratings = get_ratings_from_db()
        return jsonify([rating.__dict__() for rating in ratings])


class TagsEndpoint(Resource):
    def get(self):
        tags = get_tags_from_db()
        return jsonify([tag.__dict__() for tag in tags])


class LinksEndpoint(Resource):
    def get(self):
        links = get_links_from_db()
        return jsonify([link.__dict__() for link in links])


api.add_resource(MoviesEndpoint, '/movies')
api.add_resource(RatingsEndpoint, '/ratings')
api.add_resource(TagsEndpoint, '/tags')
api.add_resource(LinksEndpoint, '/tags')
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
