from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from src.models import Cars

class CarSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Cars 
        exclude = ['id']
        load_instance = True
