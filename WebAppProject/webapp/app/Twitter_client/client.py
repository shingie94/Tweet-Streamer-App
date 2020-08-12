import requests
from requests_oauthlib import OAuth1
import twitter_credentials

class Client():
    ##Authenticate Twitter api##
    def authenticate_twitter(self):
        url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
        auth = OAuth1(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET_KEY, twitter_credentials.ACCESS_TOKEN_KEY,
        twitter_credentials.ACCESS_TOKEN_SECRET)
        requests.get(url, auth=auth)
        return auth

    ##Client get response##
    def client_response(self, keyword):
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------")
        response = requests.get('https://api.twitter.com/1.1/search/tweets.json?q={keyword}&count=20&result_type=recent'.format(keyword = keyword), auth = self.authenticate_twitter())
        r = response.json()

        #Loop through responses
        tweet = 0
        while tweet < len(r['statuses']):
            print ("Date Created: {}".format(r['statuses'][tweet]['created_at']))
            print ("Tweet: {}".format(r['statuses'][tweet]['text']))
            print("----------------------------------------------------------------------------------------------------------------------------------------------------------")
            tweet+=1

if __name__ == '__main__':
    client = Client()
    query = input("What do you want search for? ")
    client.client_response(query)
