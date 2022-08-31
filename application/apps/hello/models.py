from application import db
from application.utils.models import BaseModel


class Author(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), unique=True)
    # back_populates定义双向关系
    # back_populates参数的值需要设为关系另一侧的关系属性名
    articles = db.relationship("Article", back_populates='author')

    def __repr__(self):
        return "<Author id:%r, name:%r>" % (self.id, self.name)


class Article(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), index=True)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    author = db.relationship('Author', back_populates='articles')

    def __repr__(self):
        return "<Article id:%r, title:%r, author_id:%r>" % \
               (self.id, self.title, self.author_id)
