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