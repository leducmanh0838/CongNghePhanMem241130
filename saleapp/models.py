from encodings.utf_7 import encode
from idlelib.iomenu import encoding

from sqlalchemy import Column, Integer, String, Text, Boolean, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
from unicodedata import category
from enum import Enum as UserEnum
from saleapp import db, app
from flask_login import UserMixin

class UserRole(UserEnum):
    USER = 1
    ADMIN = 2


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)


class Category(BaseModel):
    __tablename__ = 'category'

    name = Column(String(50), nullable=False)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class User(BaseModel, UserMixin):
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    avatar = Column(String(100), nullable=False)
    active = Column(Boolean, default=True)
    user_role = Column(Enum(UserRole), default=UserRole.USER)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = Column(String(50), nullable=False)
    description = Column(Text)
    price = Column(Float, default=0)
    image = Column(String(100))
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        import hashlib
        password = str(hashlib.md5('123456'.encode('utf-8')).digest())

        u = User(name='Manh', username='admin', password=password,
                 avatar = 'https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg',
                 user_role=UserRole.ADMIN)
        db.session.add(u)
        db.session.commit()

        # c1 = Category(name='Điện thoại')
        # c2 = Category(name='Laptop')
        # c3 = Category(name='Máy tính bàn')
        #
        # db.session.add_all([c1, c2, c3])
        # db.session.commit()

        # p1 = Product(name='iPhone 14', description='12GB',
        #              image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg',
        #              category_id=c1.id)  # Sử dụng ID của c1
        # p2 = Product(name='iPhone 15', description='12GB',
        #              image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg',
        #              category_id=c1.id)
        # p3 = Product(name='iPhone 16', description='12GB',
        #              image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg',
        #              category_id=c1.id)
        # p4 = Product(name='iPhone 17', description='12GB',
        #              image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg',
        #              category_id=c1.id)
        # p5 = Product(name='iPhone 18', description='12GB',
        #              image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg',
        #              category_id=c1.id)
        #
        # db.session.add_all([p1, p2, p3, p4, p5])
        # db.session.commit()