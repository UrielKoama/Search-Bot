import requests
import os
import json

# Grab the bearer token for the authentication
bearer_token = os.environ.get("BEARER_TOEKN")

search_url = "https://api.twitter.com/2/tweets/search/recent"


def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    if response.status_code != 200:
        raise Exception(response.status_code, response.txt)
    return response.json()

def build_query_string(params):
    query_string = '('

    for keyword in params['keywords']:
        pass

    # TODO: Need to confirm which of these fields are necessary and how to get the URL to view the tweet
    return {'query': query_string,
            'tweet.fields': 'id,author_id,text,source',
            'user.fields': 'username,url,verified',
            'expansions': 'author_id'}

# Params will contain all parameters the user input and it will be sent over as a dictionary of lists
def perform_search(params):
    json_response = connect_to_endpoint(search_url, build_query_string(params))
    # TODO: Add in logic to parse JSON response
    print(json.dumps(json_response, indent=4, sort_keys=True))
