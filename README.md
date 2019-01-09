# Logs Analysis

This project sets up a mock PostgreSQL database using newsdata.sql. The script, logsdb.py, uses the psycopg2 library to query the database and produce reports the following information:
* The three most popular articles of all time
* The most popular article authors of all time
* Days with a spike in http request errors

## Requirements

* Vagrant (https://www.vagrantup.com/)
* Virtualbox (https://www.virtualbox.org/wiki/Downloads)
* newsdata.sql (https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
* Python 3
* psycopg2

## Usage
1. Clone the git repository into your desired location
2. From the repo folder, run vagrant up, and vagrant ssh, then cd into /vagrant
3. Unzip newsdata.sql, and place it into the cloned repository in the same directory as logsdb.py
4. Load the data by running the command `psql -d news -f newsdata.sql`
5. Run logsdb.py


## Config

To omit the results for a specific question, scroll to the bottom of logsdb.py and comment out the functions that you do not want displayed. The default configuration is:

```
printArticleRankings()
printAuthorRankings()
printErrorReport()
```
