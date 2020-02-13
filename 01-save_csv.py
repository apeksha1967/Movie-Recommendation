# import required libraries
import pandas as pd

# read csv
# rename columns
movies = pd.read_csv('ml-1m/movies.dat', sep = '::', header = None)
movies.columns = ['movieid','name','genre']

ratings = pd.read_csv('ml-1m/ratings.dat', sep = '::', header = None)
ratings.columns = ['userid','movieid','rating','time']

# drop columns
# sort df by movieid to take avg of rating
ratings = ratings.drop(['userid','time'], axis =1)
ratings.sort_values(by=['movieid'], inplace=True)

m_ids = []
rates = []
for i in range(len(ratings['movieid'])):
    sigma = ratings[ratings['movieid'] == i].mean()
    m_id = round(sigma[0])
    rate = round(sigma[1])
    m_ids.append(m_id)
    rates.append(rate)
# print(m_ids, rates)

# create new dataframe
# dropna for row 0
ratings = {
    "movieid":m_ids,
    "rating":rates
}
ratings = pd.DataFrame(ratings)
ratings = ratings.dropna()

# merge dataframes on movieid
movies = movies.merge(ratings, on = 'movieid')

# saving as csv
movies.to_csv('movies_ratings.csv')
