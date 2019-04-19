# Logs-Analysis-Project

This project provides the user with a simple reporting tool for analysing traffic to a newspaper site.  A limited set of queries are provided to the user in a small python based web page using DB-API to query a PostgreSQL database.

## Getting Started

Just run the newsdata_site.py file with python3 and open up a web browser to localhost on port 8000.

## Prerequisites

The code requires pyscopg2 and Flask.  It was written with Python v3.6.7, but hearlier version of python3 will likely work.  You must also have the "news" database set up locally.

##  Installing

These instructions assume you have already set up the news database.

1. Run the python file newsdata_site.py to get the server up.

```
python3 newsdata_site.py
```

2. Connect to localhost:8000 in a web browser.  Select from the three queries available.  Query results will be displayed below the selection buttons. 


