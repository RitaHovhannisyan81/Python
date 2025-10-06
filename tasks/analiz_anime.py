

import pandas as pd
anime = pd.read_csv("anime.csv")
ratings = pd.read_csv("rating.csv")

print("Anime datasets: ")
print(anime.head()) #տպում է առաջին 5 տողերը

print("\nRatings dataset: ")
print(ratings.head())

#Հիմնական տեղեկություն
print(anime.info()) # Սյունակների տեսակը և բացակայող արժեքների ստուգում
print(anime.describe())# Թվային տվյալների արագ վիճակագրություն

