import snscrape.modules.twitter as sntwitter
import pandas as pd
import query_builder as qb

tweets_list = []

text = input('Consulta a ser realizada: ')
since = input('Data de início das buscas: ') #formato YYYY-MM-DD
until = input(('Data de encerramento das buscas: '))
count = int(input('Quantos tweets voce deseja buscar: '))


file_name = f"tweets/facebook/teste/{text}_{since}_{until}.json"

query = qb.query_builder(text, since, until)


#Data format: YYYY-MM-DD
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    if i>= count:
        break
    # tweet.date = tweet.date.strftime("%m/%d/%Y, %H:%M:%S")
    tweet.date = tweet.date.strftime("%d/%m/%Y")
    tweets_list.append([tweet.date, tweet.id, tweet.rawContent, tweet.user.username, tweet.url])
    
tweets_df = pd.DataFrame(tweets_list, columns=['Date', 'TweetId', 'TweetContent', 
                                               'Username', 'URL'])

result = tweets_df.to_json(path_or_buf= file_name, orient='records', force_ascii=False, lines=True)

# tweets_df['Date'] = [d.date() for d in tweets_df['DateTime']]
# tweets_df['Time'] = [d.time() for d in tweets_df['DateTime']]

# tweets_df.drop('DateTime', axis=1, inplace=True)
# tweets_df.info()
# print(tweets_df)

# result = tweets_df.to_json(path_or_buf='resultado.json', orient='records', lines=True, indent=4)

# file_name = input("Qual o nom do arquivo que deseja salvar os resultados? ") # exemplo: resultado.json