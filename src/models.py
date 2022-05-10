
import uuid

from src import db

class Cars(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    auto = db.Column(db.String(120),nullable=False)
    plate = db.Column(db.String(8),unique=True,nullable=False)
    color= db.Column(db.String(20),nullable=False)

    def __init__(self,auto,plate,color):
        self.auto = auto
        self.plate = plate
        self.color=color
        self.uuid= str(uuid.uuid4())

    def __repr_(self):
        return f'Cars({self.uuid}, {self.auto}, {self.plate}, {self.color})'

    def to_dict(self):
        return {
            'id':self.id,
            'auto':self.auto,
            'plate':self.plate,
            'color':self.color
        }



