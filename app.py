from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from matplotlib.pyplot import title
from services.api import Api

apiClass = Api()

newsList = apiClass.newsList

app = Flask(__name__,template_folder='templete')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'blog post' + str(self.id)




@app.route('/')
def index():
    return render_template('index.html', newsList = newsList)

# # working on it >>>>>>>>>>>>>>>>>>> 
# @app.route('/localdbnews')
# def myApp():
#     db.session.add(BlogPost(title='this is post 1 >', content="this is content of 1", author =" rajendra a verma"))

#     locallist = BlogPost.query.all()
#     print(">>>>>>>>>>>>>>>>>>>>>>>>>>>", locallist)
#     return render_template('localdbnews.html', localList = locallist)

if __name__ == '__main__':
    app.run(debug=True)
