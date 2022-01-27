from flask import Flask, redirect, render_template, request, template_rendered
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
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
        return 'blog post ' + str(self.id)




@app.route('/')
def index():
    return render_template('index.html', newsList = newsList)

# working on it >>>>>>>>>>>>>>>>>>> 
@app.route('/localdbnews', methods = ['GET', 'POST'])
def myApp():
    
    if request.method == 'POST':
        title = request.form['title']
        author =request.form['author']
        content = request.form['content']
        blogPost = BlogPost(title=title, author=author, content=content) 
        db.session.add(blogPost)
        db.session.commit()
    
    locallist = BlogPost.query.all()  

    return render_template('localdbnews.html', localList = locallist)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    blogpost = BlogPost.query.filter_by(id=f'{id}').first()
    db.session.delete(blogpost)
    db.session.commit()
    return redirect('/localdbnews')    

@app.route('/update/<int:id>', methods = ['POST', 'GET'])
def update(id):
    blogpost = BlogPost.query.filter_by(id=f'{id}').first()
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']
        BlogPost.query.filter_by(id=f'{id}').first().update({'title': title, 'author': author, 'content': content},synchronize_session=False)
        db.session.commit()
        return redirect('/localdbnews')
    return render_template('updatepost.html', blogpost= blogpost)



@app.route('/getmethod', methods = ['POST', 'GET'])
def getmethod():

    if request.method == 'GET':
        title = request.args.get('title')
        return  f'<h1>{title}</h1>'


if __name__ == '__main__':
    app.run(debug=True)
