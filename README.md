# PDF File to text

## Dependencies
- Python2

## Install
Set up and activate a Python2.7 virtual environment. Then,
```
$ pip install -e .
``` 
Additionally, install [lc_pdfminer](https://github.com/gawati/pdf-to-xml) 

## Run
```
$ export FLASK_APP=pdf2xml
$ flask run --port=5000
```

To turn on development features, set the env variable before running.
```
$ export FLASK_ENV=development
```

## Build & Distribution
Version is maintained in `tagit/setup.py`.  
`python setup.py sdist` will create a development package with “.dev” and the current date appended.  
`python setup.py release sdist` will create a release package with only the version.  
To learn more about the deploy process referenced, read [this](http://flask.pocoo.org/docs/1.0/patterns/distribute/)

## Deploy
Activate the Python2 virtual environment.

1. Install gunicorn
```
$ pip install gunicorn
```

2. Set the log paths in `gunicorn.conf`

3. Configure apache (apache.conf)
```
<Location "/path/to/pdf2xml-service">
    ProxyPass "http://127.0.0.1:5000/"
    ProxyPassReverse "http://127.0.0.1:5000/"
</Location>
```

4. Run gunicorn
```
$ gunicorn -c gunicorn.conf -b 0.0.0.5000 pdf2xml:app
```

Check the app in the browser, http://your-ip-here/path/to/flaskapp  