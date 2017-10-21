import praw
import csv
import pycountry
from geotext import GeoText
from collections import Counter


r = praw.Reddit(client_id='',
                client_secret='',
                password='',
                user_agent='',
                username='')

countries = []
subreddit = r.subreddit('earthporn')



with open('earthporn_top_posts_with_country.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(('Country', 'Score', 'ID', 'Title'))

    for submission in subreddit.top(limit=1000):
        location = "N/A"
        title = submission.title.encode('UTF-8')
        score = submission.score
        postid = submission.id

        places = GeoText(title)

        for key, value in places.country_mentions.items():
            if key != "":
                countries.append(key)
                location = key
        writer.writerow((location, str(score), postid, title))


countryList = Counter(countries).keys()
valueList = Counter(countries).values()
for i in xrange(1, len(countryList)):
    print str(pycountry.countries.get(alpha_2=countryList[i]).name) + ", " + str(valueList[i])

    # You can now access all of the places found by the Extractor
