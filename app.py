from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

"""
Создать базу db необходимо руками в режиме terminal
    >python3
    >from app import db
    >db.create_all()
    >exit()
"""


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<{Article} {self.id}>'


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return "About page..."


@app.route('/create', methods=['GET', 'POST'])
def create_article():
    if request.method == 'POST':
        title = request.form['title']  # name='title'
        intro = request.form['intro']
        text = request.form['text']

        article = Article(title=title, intro=intro, text=text)
        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/posts')
        except:
            return f'Ошибка во время записи статьи в базу...'
    else:
        return render_template("create_article.html")


@app.route('/posts')
def posts():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template("posts.html", articles=articles)


@app.route('/posts/<int:id>')
def post_detail(id):
    article = Article.query.get(id)
    return render_template("post_detail.html", article=article)


if __name__ == "__main__":
    app.run(debug=True)
