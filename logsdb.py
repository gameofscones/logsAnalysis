#!/usr/bin/env python3
"""Print top articles, authors, and days with most failed page requests."""
import psycopg2
from datetime import datetime
from collections import OrderedDict


def printArticleRankings():
    """Print top three articles.

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

    print('''1. What are the three most popular articles of all time?
            \n-------------------------------------------------''')
    for views, article in results:
        print('"{}" -- {} views'.format(article, views))


def printAuthorRankings():
    """Print the most popular article authors of all time.

    When you sum up all of the articles each author has written,
    which authors get the most page views?
    Present this as a sorted list with the most popular author at the top.
    """
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute('''select name, count(*) as views
                    from articles join authors on articles.author = authors.id
                    join log on log.path = '/article/' || articles.slug group
                    by name order by views desc;''')
    results = cursor.fetchall()
    db.close()

    print('''\n2. Who are the most popular authors of all time?
                \n-------------------------------------------------''')
    for name, views in results:
        print("{} -- {} views".format(name, views))


def printErrorReport():
    """Print the days where more than 1% of reqests return an error.

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

    print('''\n3. On which days did more than 1% of requests lead to errors?
                \n-------------------------------------------------''')
    for date, percent in results:
        print('{} -- {}% errors'.format(date, percent))


if __name__ == "__main__":

    printArticleRankings()
    printAuthorRankings()
    printErrorReport()
