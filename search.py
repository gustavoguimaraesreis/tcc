import datetime 

def search(text, username, since, until, retweet, replies):
    global filename
    
    query = text

    if username!='':
        query +=f"from:{username}"

    if until == ' ':
        until = datetime.datetime.strftime(datetime.date.today(), '%Y-%m-%d')
        query +=f"until:{until}"
    
    if since == ' ':
        since = datetime.datetime.strftime(datetime,datetime.strptime(until, '%Y-%m-%d') -
                                           datetime.time.delta(days=7), '%Y-%m-%d')
        query =+f"since:{since}"
    
    if retweet == 's':
        query +=f"exclude:retweets"
    
    if replies == 's':
        query +=f"exclude:replies"

    if username != '' and text !='':
        filename =f"{since}_{until}_{username}_{text}.csv"
    
    elif username !='':
       filename =f"{since}_{until}_{username}.csv"
    
    else:
        filename =f"{since}_{until}_{text}.csv"

    print(filename)
    print(query)

    return query
