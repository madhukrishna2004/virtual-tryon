from flask import Flask, render_template

app = Flask(__name__)

# Landing page
@app.route('/')
def index():
    return render_template('index.html')

# Try-On page
@app.route('/try')
def try_on():
    return render_template('try.html')

if __name__ == '__main__':
    app.run(debug=True)
