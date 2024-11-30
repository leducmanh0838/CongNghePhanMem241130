import hashlib
import json
from saleapp import app, db
from saleapp.models import Category, Product, User


def load_categories():
    return Category.query.all()


def load_products(cate_id=None, kw=None):
    query = Product.query

    if cate_id:
        query = query.filter(Product.category_id.__eq__(cate_id))

    if kw:
        query = query.filter(Product.name.contains(kw))
    return query.all()


def get_product_by_id(product_id):
    return Product.query.get(product_id)


def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).digest())

    return User.query.filter(User.username.__eq__(username.strip()),
                             User.password.__eq__(password)).first()


def get_user_by_id(user_id):
    return User.query.get(user_id)


def register(name, username, password, avatar):
    u = User(name=name, username=username,
             password=str(hashlib.md5(password.strip().encode('utf-8')).digest()),
             avatar=avatar)
    db.session.add(u)
    db.session.commit()