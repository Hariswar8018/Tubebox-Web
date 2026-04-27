from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

videos = []  # temporary storage

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['video']
        title = request.form['title']
        desc = request.form['description']

        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            videos.append({
                'title': title,
                'description': desc,
                'file': file.filename
            })

        return redirect(url_for('videos_page'))

    return render_template('upload.html')

@app.route('/videos')
def videos_page():
    return render_template('videos.html', videos=videos)

@app.route('/telegram')
def telegram():
    return render_template('telegram.html')

@app.route('/contact')
def contact():
    return render_template('contactus.html')

@app.route('/privacy-policy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms-and-condition')
def terms():
    return render_template('terms.html')

@app.route('/why-choose-us')
def why():
    return render_template('why.html')

@app.route('/app')
def download():
    return redirect("https://play.google.com/store/apps/details?id=com.tube.box.entertainment.app&hl=en_IN")

@app.route('/login', methods=['POST','GET'])
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

