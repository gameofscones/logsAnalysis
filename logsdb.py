#!/usr/bin/env python3
import psycopg2
from datetime import datetime
from collections import OrderedDict



def printArticleRankings():
    """
    What are the most popular three articles of all time?
    Which articles have been accessed the most?
    Present this information as a sorted list
    with the most popular article at the top.
    """

    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    # slug looks like path so we need to join using those two it seems.
    cursor.execute('''select count(path) as views,
                        title from log join articles on
                        log.path = '/article/' || articles.slug
                        group by title order by views desc limit 3;''')
    results = cursor.fetchall()
    db.close()
    # results contains a list of tuples. Format this for readability.
    topArticles = []
    # for i in range(3):
    #     article = results[i][1]
    #     views = results[i][0]
    #     # printing the results based on example format
    #     print('"{}" -- {} views'.format(article, views))
    #     # returning same results to a list in case that's what's needed
    #     topArticles.append('"{}" -- {} views'.format(article, views))
    for views, article in results:
        print('"{}" -- {} views'.format(article, views))

    return topArticles




def printAuthorRankings():
    """
        Who are the most popular article authors of all time?
        That is, when you sum up all of the articles each author has written,
        which authors get the most page views?
        Present this as a sorted list with the most popular author at the top.
    """
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute('''select name, count(*) as views
                    from articles join authors on articles.author = authors.id
                    join log on log.path = '/article/' || articles.slug group by
                    name order by views desc;''')
    results = cursor.fetchall()
    db.close()

    for name, views in results:
        print("{} -- {} views".format(name, views))


def printErrorReport():
    """
        On which days did more than 1% of requests lead to errors?
        The log table includes a column status that indicates the
        HTTP status code that the news site sent to the user's browser.
    """
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute('''select to_char(time, 'Mon DD, YYYY'), 
                      cast(cast(num as float)/total * 100 as decimal(10,2)) as 
                      error_percent from (select time::date, count(*) as total, 
                      count(*) filter (where status like'4%') as num from 
                      log group by time::date order by time) log where 
                      cast(num as float)/total * 100 > 1; ''')
    results = cursor.fetchall()
    db.close()

    for date,percent in results:
        print('{} -- {}% errors'.format(date,percent))




printArticleRankings()
printAuthorRankings()
printErrorReport()
