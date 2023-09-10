from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"

Game = namedtuple('Game', 'title link')



def get_games():
    parsed_feed = feedparser.parse(FEED_URL)
    games = []
    for entry in parsed_feed.entries:
        game = Game(entry.title, entry.link)
        games.append(game)
    return games
    
    
print(get_games())