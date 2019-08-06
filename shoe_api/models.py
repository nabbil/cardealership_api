from shoe_api import app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# init Database
db = SQLAlchemy(app)

# init MArshmallow
ma = Marshmallow(app)

# Create Product Model


class Salesperson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(250))

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


# Create Product Schema

class SalespersonSchema(ma.Schema):
    class Meta:  # YOU HAVE TO USE THIS META
        fields = ('id', 'first_name', 'last_name')

# Init the Schema


salesperson_schema = SalespersonSchema(strict=True)
salespersons_schema = SalespersonSchema(many=True, strict=True)
