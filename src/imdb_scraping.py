import requests
from bs4 import BeautifulSoup
import pandas as pd
import yaml
from pymongo import MongoClient

# The IMDb URL for the movie's reviews page
url = 'https://www.imdb.com/title/tt0111161/reviews'

# Function to scrape reviews
def scrape_imdb_reviews(url, num_reviews=1999):
    reviews = []
    page_num = 1

    while len(reviews) < num_reviews:
        response = requests.get(f"{url}?start={page_num * 10}")
        soup = BeautifulSoup(response.text, 'html.parser')
        review_containers = soup.find_all("div", class_="text show-more__control")

        if not review_containers:
            break

        for review in review_containers:
            text = review.get_text(strip=True)
            reviews.append(text)

        page_num += 1

    return reviews[:num_reviews]

# Scrape 400 reviews
reviews = scrape_imdb_reviews(url, num_reviews=400)

# Create a DataFrame
df = pd.DataFrame({'Reviews': reviews})

# Print the DataFrame
print(df)

# Load MongoDB configuration from config.yml
with open('../config.yml', 'r') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

# Create a MongoDB client
mongodb_client = MongoClient(host=config['mongodb']['host'], port=config['mongodb']['port'])
db = mongodb_client[config['mongodb']['database']]
collection = db[config['mongodb']['collection']]

# Insert the movie reviews into MongoDB
for review in reviews:
    post = {
        'text': review
    }
    collection.insert_one(post)

# Close the MongoDB client
mongodb_client.close()
