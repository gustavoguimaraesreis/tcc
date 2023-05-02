import snscrape.modules.twitter as sntwitter
import pandas as pd
import query_builder as qb

tweets_list = []

text = input('Consulta a ser realizada: ')
since = input('Data de início das buscas: ') #formato YYYY-MM-DD
until = input(('Data de encerramento das buscas: '))
count = int(input('Quantos tweets voce deseja buscar: '))


file_name = f"{text}_{since}_{until}.csv"

query = qb.query_builder(text, since, until)


#Data format: YYYY-MM-DD
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    if i>= count:
        break
    tweets_list.append([tweet.date, tweet.id, tweet.rawContent, tweet.user.username, tweet.url])
    
tweets_df = pd.DataFrame(tweets_list, columns=['DateTime', 'TweetId', 'TweetContent', 
                                               'Username', 'URL'])


tweets_df['Month'] = tweets_df['DateTime'].dt.month
tweets_df['MonthName'] = tweets_df['DateTime'].dt.month_name() 
tweets_df['MonthDay'] = tweets_df['DateTime'].dt.day 
tweets_df['DayName'] = tweets_df['DateTime'].dt.day_name() 
tweets_df['Week'] = tweets_df['DateTime'].dt.isocalendar().week 

tweets_df['Date'] = [d.date() for d in tweets_df['DateTime']] 
tweets_df['Time'] = [d.time() for d in tweets_df['DateTime']] 

tweets_df.drop('DateTime',axis=1,inplace=True) 

tweets_df.to_csv(f"{file_name}",index=False)

# result = tweets_df.to_json(path_or_buf= file_name, orient='records', force_ascii=False, lines=True)

# tweets_df['Date'] = [d.date() for d in tweets_df['DateTime']]
# tweets_df['Time'] = [d.time() for d in tweets_df['DateTime']]

# tweets_df.drop('DateTime', axis=1, inplace=True)
# tweets_df.info()
# print(tweets_df)

# result = tweets_df.to_json(path_or_buf='resultado.json', orient='records', lines=True, indent=4)

# file_name = input("Qual o nom do arquivo que deseja salvar os resultados? ") # exemplo: resultado.json