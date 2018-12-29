import psycopg2

# What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.
def questionOne():

    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    # slug looks like path so we need to join using those two it seems.
    cursor.execute('select count(path) as views, title from log join articles on log.path like (\'%\' || articles.slug) group by title order by views desc limit 10;')
    results = cursor.fetchall()
    db.close()
    # results contains a list of tuples. Format this for readability.
    topArticles = []
    for i in range(3):
        # printing the results based on example format
        print('"{}" -- {} views'.format(results[i][1], results[i][0]))
        # returning same results to a list in case that's what I'm supposed to do
        topArticles.append('"{}" -- {} views'.format(results[i][1], results[i][0]))

    return topArticles

# Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.
def questionTwo():
    pass

# On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)
def questionThree():
    pass

questionOne()

