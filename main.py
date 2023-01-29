from flask import Flask, render_template, request, url_for
from operator import itemgetter
from PIL import Image
from werkzeug.utils import secure_filename
import os
UPLOAD_FOLDERS = '/static'
ALLOWED_EXTENSIONS = {'jpg', 'png'}

def convert_in_color(path):
    img = Image.open(path)
    max_colors = 1000000
    list_colors = img.getcolors(max_colors)
    list_colors.sort(key=itemgetter(0), reverse=True)
    return list_colors

def image(path):
    img = Image.open(path)
    return img


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDERS


@app.route('/', methods=['GET', "POST"])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        try:
            if filename.split('.')[1] in ALLOWED_EXTENSIONS:
                file.save(os.path.join(app.config['UPLOAD_FOLDER']))
                return render_template('index.html', colors=convert_in_color(request.files['file']), image='static/test.png')
            else:
                return render_template('index.html')
        except:
            return render_template('index.html')
app.run(debug=True)