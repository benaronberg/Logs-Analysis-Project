# Logs-Analysis-Project

This project provides the user with a simple reporting tool for analysing traffic to a newspaper site.  A limited set of queries are provided to the user in a small python based web page using DB-API to query a PostgreSQL database.  Currently, those queries are:
* The top three most popular articles of all time on the site
* A listing of the authors sorted from most article views to least
* Days on which more than 1% of requests led to errors

## Getting Started

Just run the newsdata_site.py file with python3 and open up a web browser to localhost on port 8000.

### Prerequisites

The code requires pyscopg2 and Flask.  It was written with Python v3.6.7, but earlier version of python3 will likely work.  

PostgreSQL is required to run the Logs Analysis code.  Download can be found here(https://www.postgresql.org/download/) and install instructions here(https://www.postgresql.org/docs/9.3/tutorial-install.html)

Alternatively, you can use Vagrant(https://www.vagrantup.com/docs/installation/) and VirtualBox to set up the environment using the Udacity provided Vagrantfile found here(https://github.com/udacity/fullstack-nanodegree-vm/blob/master/vagrant/Vagrantfile)

You must also have the "news" database set up locally.  The SQL file can be found here (https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).  To install on Linux, cd into the directory containing newsdata.sql and run the following command:

```
psql -d news -f newsdata.sql
```

This will create the necessary tables and populate them with data.

### Installing

These instructions assume you have already set up the news database as described in the Prerequisites(#Prerequisites) section.

1. Run the python file newsdata_site.py to get the server up.

```
python3 newsdata_site.py
```

2. Connect to localhost:8000 in a web browser.  Select from the three queries available.  Query results will be displayed below the selection buttons. 

## Acknowledgements

* udacity.com for providing the database and guidance on writing this code
