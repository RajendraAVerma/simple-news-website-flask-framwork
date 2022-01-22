from distutils.log import debug
from flask import Flask, render_template

from services.api import Api

apiClass = Api()

newsList = apiClass.newsList

app = Flask(__name__,template_folder='templete')


@app.route('/')
def index():
    return render_template('index.html', newsList = newsList)


if __name__ == '__main__':
    app.run(debug=True)
