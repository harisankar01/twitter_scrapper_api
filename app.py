import utils.http_session
import utils.transport
import utils.session
from dotenv import load_dotenv
from flask import Flask, jsonify, request
import tweepy as tw
from os import getenv

load_dotenv()
app = Flask(__name__)
# ENV vars
key = getenv("API_KEY")
key_secret = getenv("API_SECRET")
access_token = getenv("ACCESS_TOKEN")
access_secret = getenv("TOKEN_SECRET")
auth = tw.OAuthHandler(key, key_secret, "oob")
auth.set_access_token(access_token, access_secret)
api = tw.API(auth)

global points

# Test route


@app.route('/', methods=["GET"])
def index():
    return jsonify("Welcome to twitter scrapper")

# Get tweets from twitter


@app.route('/tweets', methods=["GET"])
def get_tweets():
    args = request.args
    domain = args.get("domain", default="", type=str)
    tweets = list(tw.Cursor(
        api.search_tweets, "{0} in India ".format(domain), result_type='recent', tweet_mode='extended', count=50).items(50))
    Tweet_outpt = []
    for i in tweets:
        text = ""
        try:
            text = i._json['retweeted_status']['full_text'] if i.full_text.startswith(
                "RT @") else i.full_text
        except AttributeError:
            text = i.full_text
        place = ""
        if i.place:
            place = i.place.full_name
# Result json structure
        json_output = {
            "Department": domain,
            "tweet": text,
            "tweet_associated_place": place,
            "tweeter_location": i.user.location,
            "Time_of_tweet": i.created_at,
            "User name": i.user.name,
        }
        Tweet_outpt.append(json_output)
    return jsonify(Tweet_outpt)
