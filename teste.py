import pandas as pd
import numpy as np
import snscrape.modules.twitter as sntwitter
import datetime
import query_builder as sh
from tqdm.notebook import tqdm_notebook


text = input('Consulta a ser realizada: ')

username = input('Nome de usuário espécifico para fazer a consulta: ')

since = input('Data de início das buscas: ')

until = input(('Data de encerramento das buscas: '))

count = int(input('Número máximo de resultados(ou -1 para retonar o máximo possível): '))

retweet = input('Excluir retweets?(s/n): ')

replies  = input('Excluir respostas?(s/n): ')

q = sh.search(text, username, since, until, retweet, replies)

# print(type(q))

tweets_list = []

tweet_enum= enumerate(sntwitter.TwitterSearchScraper(q).get_items())

for i, tweet in tweet_enum:
    print(i)
    print(tweet)
    tweets_list.append([tweet.date, tweet.id, tweet.rawContent,])

tweet_df = pd.DataFrame(tweets_list, columns=['DateTime', 'TweetID', 'Text'])

tweet_df.info()

print(tweet_df)
# print(type(sntwitter.TwitterSearchScraper(q).get_items()))


# for i,tweet in enumerate(tqdm_notebook(sntwitter.TwitterSearchScraper(q).get_items())):
#     print(i)
#     if i >= count:
#         print(i)
#         break
#     tweets_list.append([tweet.date, tweet.id, tweet.rawDescription])
    # print(tweets_list[i])



# if count == -1:
#     for i,tweet in enumerate(tqdm_notebook(sntwitter.TwitterSearchScraper(q).get_items())): 
#         tweets_list.append([tweet.date, tweet.id, tweet.rawContent, tweet.user.username,tweet.lang])
# else:
#     with tqdm_notebook(total=count) as pbar:
#         for i,tweet in enumerate(sntwitter.TwitterSearchScraper(q).get_items()):
#             if i>=count:
#                 break
#             tweets_list.append([tweet.date, tweet.id, tweet.rawContent, tweet.user.username,tweet.lang])
#             pbar.update(1) 
# if count == -1:
#     for i, tweet in enumerate(tqdm_notebook(sntwitter.TwitterSearchScraper(
#         (q).get_items()))):
#         tweets_list.append([tweet.Date, tweet.id, tweet.rawContent, tweet.user.username, tweet.lang])
# else:
#     with tqdm_notebook(total=count) as pbar:
#         for i, tweet in enumerate(tqdm_notebook(sntwitter.TwitterSearchScraper(
#         (q).get_items()))):
#             if i >= count: 
#                 break

#             tweets_list.append([tweet.Date, tweet.id, tweet.rawContent, tweet.user.username, tweet.lang])
#             pbar.update(1)


# if count == -1:
#     for i, tweet in enumerate(sntwitter.TwitterSearchScraper(
#         (q).get_items())):
#         tweets_list.append([tweet.Date, tweet.id, tweet.rawContent, tweet.user.username, tweet.lang])
# else:
#     for i, tweet in enumerate(sntwitter.TwitterSearchScraper(
#         (q).get_items())):
#             if i >= count: 
#                 break

#             tweets_list.append([tweet.Date, tweet.id, tweet.rawContent, tweet.user.username, tweet.lang])





