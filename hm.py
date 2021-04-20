from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return "this website developed by Mr. Ritik Bhardwaj"


if __name__ == '__main__':
    app.run(debug=True)
