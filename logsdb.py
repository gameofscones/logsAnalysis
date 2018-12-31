import psycopg2
from collections import OrderedDict

# What are the most popular three articles of all time?
# Which articles have been accessed the most?
# Present this information as a sorted list
# with the most popular article at the top.


def questionOne():

    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    # slug looks like path so we need to join using those two it seems.
    cursor.execute('''select count(path) as views,
                        title from log join articles on
                        log.path like (\'%\' || articles.slug)
                        group by title order by views desc limit 10;''')
    results = cursor.fetchall()
    db.close()
    # results contains a list of tuples. Format this for readability.
    topArticles = []
    for i in range(3):
        article = results[i][1]
        views = results[i][0]
        # printing the results based on example format
        print('"{}" -- {} views'.format(article, views))
        # returning same results to a list in case that's what's needed
        topArticles.append('"{}" -- {} views'.format(article, views))

    return topArticles

# Who are the most popular article authors of all time?
# That is, when you sum up all of the articles each author has written,
# which authors get the most page views?
# Present this as a sorted list with the most popular author at the top.


def questionTwo():
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute('''select name, count(*) as views
                    from articles join authors on articles.author = authors.id
                    join log on log.path like ('%' || articles.slug) group by
                    name, title order by views desc limit 10;''')
    results = cursor.fetchall()
    db.close()
    topAuthors = {}
    # iterate over the list of results,
    # if the object at index 0 in each tuple is not in the top authors list
    # add the key and value. If the name is in the top authors list,
    # then add the value of the name to the one that is in the top authors list
    for i in results:
        if i[0] in topAuthors:
            # if the name is already in the top authors,
            # simply add the value to the current value
            topAuthors[i[0]] += i[1]
        else:
            # if the name is not in top authors, add everything.
            topAuthors[i[0]] = i[1]

    # Sort the dictionary
    sortedDictionary = OrderedDict(
        sorted(topAuthors.items(), key=lambda t: t[1])[::-1])
    sortedDictList = list(sortedDictionary.items())

    def showTopAuthors():
        for i in range(4):
            name = sortedDictList[i][0]
            totalViews = sortedDictList[i][1]
            print("{} -- {} views".format(name, totalViews))

    showTopAuthors()
    return sortedDictList

# On which days did more than 1% of requests lead to errors?
# The log table includes a column status that indicates the
# HTTP status code that the news site sent to the user's browser.


def questionThree():
    # divide the number of errored requests (Status 404), by the total number of requests then multiply it by 100 to get the percentage. WHERE this value is > 1%,display the date, and the percentage.
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute('''''')
    results = cursor.fetchall()
    db.close()
    pass


# questionOne()
# questionTwo()
