from flask_restful import Resource, abort, reqparse
from app import api

supported_search_endpoints = ['movie', 'music', 'sports']

def abort_if_search_doesnt_exist(search_type):
    if search_type not in supported_search_endpoints:
        abort(404, message="The {} search endpoint is not currently supported.".format(search_type))

class Search(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('keywords', type=list, required=True, help='Keywords to query twitter for')
        super(Search, self).__init__()

    def put(self, search_type):
        abort_if_search_doesnt_exist(search_type)
        args = self.reqparse.parse_args(strict=True)
        keywords = args['keywords'] # will need to send this to the keyword validation logic
        return {search_type: keywords}


api.add_resource(Search, '/search/<string:search_type>')
