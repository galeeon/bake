from typing import List
from flask import Flask, render_template
from models import db, Article
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite'
app.config['SECRET_KEY'] = 'AWWWWW'
app.config['SIMPLEMDE_JS_IIFE'] = True
app.config['SIMPLEMDE_USE_CDN'] = True
db.app = app
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def homepage():
    articles: List[Article] = Article.query.all()
    return render_template('index.html',
                           title='Главная страница',
                           articles=articles)

# Подробный просмотр статьи
@app.route('/articles/<int:article_id>')
def get_article(article_id):
    articles: Article = Article.query.filter_by(id=article_id).first()
    return render_template('article.html', title=articles.title, articles=articles)


@app.route('/about')
def about():
    return render_template('about.html',
                           title='О нас')

if __name__ == '__main__':
    app.run()
