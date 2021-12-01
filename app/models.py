from app import db


class User(db.Model):
    """
    Adding id(primary key)
    ensures that email set is unique
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(40),  nullable=False)
    lastname = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return '<User: {}>'.format(self.email)



