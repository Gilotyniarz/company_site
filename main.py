from flask import Flask, render_template, request, url_for, redirect, session



app = Flask(__name__)


@app.route('/')
def base():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)

