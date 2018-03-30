
import pandas as pd
import os
import time
from datetime import datetime

# u_cols = ['user_id','age','sex','occupation','zip_code']
# user = pd.read_csv(
#     'http://files.grouplens.org/datasets/movielens/ml-100k/u.user',
#     sep = '|',names = u_cols )
# print user.head()

r_cols = ['user_id', 'movie_id', 'rating','unix_timestamp']
rating = pd.read_csv(
    'http://files.grouplens.org/datasets/movielens/ml-100k/u.data', sep = '\t', names=r_cols)
# print rating.head()

# m_cols = ['movie_id', 'title', 'release_date','video_release_date', 'imdb_url']
# movies = pd.read_csv(
#     'http://files.grouplens.org/datasets/movielens/ml-100k/u.item',
#     sep = '|',names = m_cols, usecols=[0,1,2,3,4])
# print movies.head()


# old = user[user.age > 25]
# selected_user = user[(user.sex == 'F')&(user.occupation == 'programmer')]
# print selected_user.dtypes
# print selected_user.describe()

# print rating.head()
# grouped_data = rating['movie_id'].groupby(rating['user_id'])
# print grouped_data.head()
# count_per_user = grouped_data.count()
# print count_per_user.head()

grouped_data = rating['rating'].groupby(rating['user_id'])
# grouped_data = rating.groupby('movie_id')
print grouped_data.count()
average_rating = grouped_data.mean()
print average_rating
# print average_rating.head()
print average_rating.max()
# good_movie_ids = average_rating[(average_rating == average_rating.max())].index