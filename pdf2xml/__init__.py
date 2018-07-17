from flask import Flask

app = Flask(__name__)

import pdf2xml.views
if __name__ == "__main__":
    app.run()
