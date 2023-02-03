![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)  ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![Twitter](https://img.shields.io/badge/Twitter-%231DA1F2.svg?style=for-the-badge&logo=Twitter&logoColor=white)
## Tweet Scrapper

A API created using the **flask** framework which scrape tweets from twitter using the provided keywords.
The **tweepy** package provides many abstract methods to make http request to the twitter API to get the tweets from twitter API.

## Endpoints

- `/`: A `GET` request endpoint for checking if the backend is up and running. Return "Welcome to twitter scrapper" on the `GET` request
- `/tweets?domain=keyword`: A `GET` request endpoint wich is used to get the tweets from twitter based on the keyword provided as argumnet to the request.

## Local Development

- Sign up for a developer account in [Twitter developer platform](https://developer.twitter.com/en) website and get to your developer portal to get the API key and ACCESS TOKEN.
- Specify all the environment varibles in the `.env` file. The structure present in the `sample.env` file can be used to create the `.env` file.

- Clone the repository

```
git clone https://github.com/harisankar01/twitter_scrapper_api.git
cd twitter_scrapper_api
```

- Run the local server

```
python3 wsgi.py
```

Then go to the url `http://127.0.0.1:3000/tweets?domain=games` to get all the tweets regarding games from twitter.
A sample json response from the API is,

```
{
  "Department": "games",
  "Time_of_tweet": "Thu, 04 Aug 2022 17:19:28 GMT",
  "User name": "kishore kumar",
  "tweet": "Glad to be present at the closing ceremony of the 4th @ONGC_ #ParaGames in New Delhi today. #ParaAthletes from India’s oil &amp; gas PSUs showed exemplary skill and spirit at these games.These multi-talented ParaAthletes are assets to their organisations. @HardeepSPuri @PetroleumMin https://t.co/VQPxfBonlN",
  "tweet_associated_place": "",
  "tweeter_location": "New Delhi, India"
}
```

These tweets can be proceeced and integrated into many applications.
