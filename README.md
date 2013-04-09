UC Berkeley Enrollment Information: Scraper and API
==================================================

Tools for scraping enrollment information from the UC Berkeley [Online Schedule
of Classes](http://schedule.berkeley.edu) and providing an API for accessing
this data once stored.

## Requirements

* Python 2.7.x
* pip
* virtualenv

The contents of `requirements.txt`:

    Flask==0.9
    Flask-RESTful==0.1.7
    Jinja2==2.6
    Werkzeug==0.8.3
    argparse==1.2.1
    beautifulsoup4==4.1.3
    pycrypto==2.6
    requests==1.2.0
    wsgiref==0.1.2

## Usage

Initialize the SQLite3 database as `enrollment.db` using the schema in
`enrollment.sql`:

    sqlite3 enrollment.db < enrollment.sql

Running `python getInfo.py` will get the information for the Fall 2013 courses
and store them in the database `enrollment.db`. `python api.py` will start
Flask and provide access to an API for the data.