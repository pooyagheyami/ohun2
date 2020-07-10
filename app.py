# In the name of God

from flask import Flask, render_template, redirect, request
import os


# configure app
app = Flask(__name__)

@app.route("/")
def index():
    title = 'SolMusic | HTML Template'
    return render_template("index.html", mytitle=title )


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)