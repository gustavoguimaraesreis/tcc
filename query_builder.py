import datetime 

def query_builder(text, since, until):

    query = text

    if since == ' ':
        since = datetime.datetime.strftime(datetime,
                                           datetime.strptime(until, '%Y-%m-%d') -
                                           datetime.time.delta(days=7), 
                                           '%Y-%m-%d')
    query += f" since:{since}"

    if until == ' ':
        until = datetime.datetime.strftime(datetime.date.today(), 
                                           '%Y-%m-%d')
    query += f" until:{until}"
    
    return query
