import requests
import os

# Grab the bearer token for the authentication
bearer_token = os.environ.get("BEARER_TOKEN")

search_url = "https://api.twitter.com/2/tweets/search/recent"

def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    print(r.headers)
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response)
    if response.status_code != 200:
        raise Exception(response.status_code)
    return response.json()

def build_query_string(params):
    query_string = '('

    for keyword_index in range(len(params['keywords'])):
        if keyword_index == len(params['keywords']) - 1:
            query_string += params['keywords'][keyword_index]
        else:
            query_string += f"{params['keywords'][keyword_index]} "

    if 'username' in params:
        query_string += f" from:{params['username']}"

    query_string += ')'

    if 'verified' in params:
        query_string += ' is:verified'

    if 'retweet' in params:
        query_string += ' is:retweet'
    else:
        query_string += ' -is:retweet'

    query_string += ' lang:en'

    # TODO: Need to confirm how to get the URL to view the tweet
    return {'query': query_string,
            'tweet.fields': 'text',
            'user.fields': 'username',
            'expansions': 'author_id'}

def parse_json(json_response):
    return {'username': json_response['includes']['users'][0]['name'],
            'text': json_response['data'][0]['text']}


# Params will contain all parameters the user input and it will be sent over as a dictionary of lists
def perform_search(params):
    json_response = connect_to_endpoint(search_url, build_query_string(params))
    return parse_json(json_response)
