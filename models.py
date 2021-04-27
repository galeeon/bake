from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000), unique=False, nullable=False)
    body = db.Column(db.Text, unique=False, nullable=True)
    photo = db.Column(db.Text, unique=False, nullable=True)

    def __repr__(self):
        return f"Article({self.id}, {self.title}, {self.body})"
