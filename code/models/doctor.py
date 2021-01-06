from db import db


class DoctorModel(db.Model):
    __tablename__ = "Doctors"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)
    gender = db.Column(db.String(80))
    address = db.Column(db.String(80))
    mobile = db.Column(db.String(80))
    age = db.Column(db.Integer)

    def __init__(
        self,
        username: str,
        password: str,
        first_name: str,
        last_name: str,
        email: str,
        gender: str,
        mobile: str,
        address: str,
        age: int,
    ):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.mobile = mobile
        self.address = address
        self.age = age

    def json(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "gender": self.gender,
            "mobile": self.mobile,
            "address": self.address,
            "age": self.age,
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username: str):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id: int):
        return cls.query.filter_by(id=_id).first()
