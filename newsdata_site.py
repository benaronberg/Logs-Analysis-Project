#!/usr/bin/env python3
import psycopg2
from flask import Flask, render_template, Markup

DBNAME = "news"
app = Flask(__name__)

# HTML template for an individual comment
RESULT = '''\
    <div>%s -- %s</div>
'''


@app.route('/', methods=['GET'])
def main():
    '''Main page of the forum.'''
    return render_template('HTML_WRAP.html')


@app.route('/top_3', methods=['GET'])
def top_3():
    """Return the most popular three articles of all time in the database"""
    query = '''SELECT articles.title, count(log.id) as views
                    FROM articles, log
                    WHERE log.path like '%' || articles.slug || '%'
                    GROUP BY log.path, articles.title
                    ORDER BY views desc limit 3;
            '''
    r = execute_query(query)
    result = "".join(RESULT % (title, views) for title, views in r)
    return render_template('HTML_WRAP.html', result=result)


@app.route('/authors_by_popularity', methods=['GET'])
def authors_by_popularity():
    """Return all article authors and the number of page views articles written
        by each auther have recieved, sorted from most views to least views"""
    query = '''SELECT authors.name, count(log.id) as views
                    FROM authors, articles, log
                    WHERE log.path like '/article/' || articles.slug
                    AND articles.author = authors.id
                    GROUP BY authors.id
                    ORDER BY views desc;
            '''
    r = execute_query(query)
    result = "".join(RESULT % (name, views) for name, views in r)
    return render_template('HTML_WRAP.html', result=result)


@app.route('/peak_error_days', methods=['GET'])
def peak_error_days():
    """Return days on which more than 1% of requests led%to errors"""
    query = '''SELECT date(time),
                    cast(100 * cast(sum(
                    case when status not like '%200%' then 1 else 0 end)
                    as decimal(7,2)) /
                    cast(count(id) as decimal(7,2)) as decimal(7,2))
                    as percent_errors
                    FROM log
                    GROUP BY date(time)
                    having cast(sum(case when
                    status not like '%200%' then 1 else 0 end)
                    as decimal(7,2)) / cast(count(id) as decimal(7,2)) >= 0.01;
            '''

    r = execute_query(query)
    r = '''RESULT % (time, percent_errors) for time, percent_errors in r'''
    result = "".join(result_join)
    return render_template('HTML_WRAP.html', result=result)


def execute_query(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    r = c.fetchall()
    db.close()
    return r


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
