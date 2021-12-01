from flask import Flask
from flask_restful import Api, Resource, abort, reqparse
import search_twitter

app = Flask(__name__)
api = Api(app)

supported_search_endpoints = ['movie', 'music', 'sports']

def abort_if_search_doesnt_exist(search_type):
    if search_type not in supported_search_endpoints:
        abort(404, message="The {} search endpoint is not currently supported.".format(search_type))

def parse_args(args):
    query_params_dict = dict()

    if 'keywords' in args:
        query_params_dict['keywords'] = args['keywords']

    if 'verified' in args:
        query_params_dict['verified'] = True

    if 'username' in args:
        query_params_dict['username'] = args['username']

    if 'retweet' in args:
        query_params_dict['retweet'] = True

    return query_params_dict


class Search(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('keywords', required=True, help='Keywords to query twitter for', action='append')
        self.reqparse.add_argument('username', help='Twitter user that you want to filter tweets from')
        self.reqparse.add_argument('verified', help='Defines if you want to view tweets from only verified users')
        self.reqparse.add_argument('retweet', help='Defines if you want to view original tweets and retweets or just original tweets')

        super(Search, self).__init__()

    def get(self, search_type):
        abort_if_search_doesnt_exist(search_type)
        args = self.reqparse.parse_args(strict=True)

        # TODO: Need to send keywords to the keyword validation logic
        query_params_dict = parse_args(args)
        return {search_type: search_twitter.perform_search(query_params_dict)}


api.add_resource(Search, '/search/<string:search_type>')

if __name__ == '__main__':
    app.run(debug=True)
