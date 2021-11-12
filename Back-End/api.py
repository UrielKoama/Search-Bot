from flask import Flask
from flask_restful import Api, Resource, abort, reqparse

app = Flask(__name__)
api = Api(app)

supported_search_endpoints = ['movie', 'music', 'sports']

def abort_if_search_doesnt_exist(search_type):
    if search_type not in supported_search_endpoints:
        abort(404, message="The {} search endpoint is not currently supported.".format(search_type))

class Search(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('keywords', required=True, help='Keywords to query twitter for', action='append')
        super(Search, self).__init__()

    def get(self, search_type):
        abort_if_search_doesnt_exist(search_type)
        args = self.reqparse.parse_args(strict=True)
        keywords = args['keywords'] # will need to send this to the keyword validation logic
        return {search_type: keywords}


api.add_resource(Search, '/search/<string:search_type>')

if __name__ == '__main__':
    app.run(debug=True)
