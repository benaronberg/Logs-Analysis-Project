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
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select articles.title, count(log.id) as views from articles, log where log.path like '%' || articles.slug || '%' group by log.path, articles.title order by views desc limit 3;")
    r = c.fetchall()
    db.close()
    result = "".join(RESULT % (title, views) for title, views in r)
    return render_template('HTML_WRAP.html', result=result)


@app.route('/authors_by_popularity', methods=['GET'])
def authors_by_popularity():
    """Return all article authors and the number of page views articles written by each auther have recieved, sorted from most views to least views"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select authors.name, count(log.id) as views from authors, articles, log where log.path like '%' || articles.slug || '%' and articles.author = authors.id group by authors.id order by views desc;")
    r = c.fetchall()
    db.close()
    result = "".join(RESULT % (name, views) for name, views in r)
    return render_template('HTML_WRAP.html', result=result)


@app.route('/peak_error_days', methods=['GET'])
def peak_error_days():
    """Return days on which more than 1% of requests led%to errors"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select date(time), cast(100 * cast(sum(case when status not like '%200%' then 1 else 0 end) as decimal(7,2)) / cast(count(id) as decimal(7,2)) as decimal(7,2)) as percent_errors from log group by date(time) having cast(sum(case when status not like '%200%' then 1 else 0 end) as decimal(7,2)) / cast(count(id) as decimal(7,2)) >= 0.01;")
    r = c.fetchall()
    db.close()
    result = "".join(RESULT % (time, percent_errors) for time, percent_errors in r)
    return render_template('HTML_WRAP.html', result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
