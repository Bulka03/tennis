from flask import Flask, render_template

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/ilya')
def ilya():
    return render_template('ilya.html')

@app.route('/company')
def company():
    return render_template('company.html')

@app.route('/workers')
def workers():
    return render_template('workers.html')

if __name__ == '__main__':
    app.run(debug=True)