from flask import (
    request,
    render_template,
    send_from_directory,
    url_for,
    jsonify
)
from werkzeug import secure_filename
import os
import io
from pdf2xml import app
from pdfminer.lc_pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.lc_converter import LegalXMLConverter
from pdfminer.lc_layout import LAParams
from pdfminer.lc_pdfpage import PDFPage
from pdfminer.lc_image import ImageWriter


basedir = os.path.abspath(os.path.dirname(__file__))

from logging import Formatter, FileHandler
handler = FileHandler(os.path.join(basedir, 'log.txt'), encoding='utf8')
handler.setFormatter(
    Formatter("[%(asctime)s] %(levelname)-8s %(message)s", "%Y-%m-%d %H:%M:%S")
)
app.logger.addHandler(handler)


app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'js_static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     'static/js', filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    elif endpoint == 'css_static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     'static/css', filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


@app.route('/css/<path:filename>')
def css_static(filename):
    return send_from_directory(app.root_path + '/static/css/', filename)


@app.route('/js/<path:filename>')
def js_static(filename):
    return send_from_directory(app.root_path + '/static/js/', filename)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/uploadajax', methods=['POST'])
def upldfile():
    if request.method == 'POST':
        files = request.files['file']
        if files and allowed_file(files.filename):
            
            rsrcmgr = PDFResourceManager()
            retstr = io.BytesIO()
            codec = 'utf-8'
            laparams = LAParams()
            device = LegalXMLConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            password = ""
            maxpages = 0
            caching = True
            pagenos = set()
            for page in PDFPage.get_pages(files, pagenos, maxpages=maxpages,
                                  password=password,
                                  caching=caching,
                                  check_extractable=True):
                page.rotate = (page.rotate+0) % 360
                interpreter.process_page(page)

            device.close()
            text = retstr.getvalue()
            retstr.close()
            return jsonify(text=text)


if __name__ == '__main__':
    app.run(debug=False)
