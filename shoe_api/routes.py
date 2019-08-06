from shoe_api import app
from shoe_api.models import db, salesperson_schema, salespersons_schema, Salesperson
from flask import request, jsonify

# Create Product
@app.route('/salesperson', methods=['POST'])
def add_product():
    first_name = request.json['first_name']
    last_name = request.json['last_name']

    new_person = Salesperson(first_name, last_name)

    db.session.add(new_person)
    db.session.commit()

# Now we will desplay Json formatted data using poostman
    return salesperson_schema.jsonify(new_person)

# Get Single Product
@app.route('/salesperson/<id>', methods=["GET"])
def get_person(id):
    person = Salesperson.query.get(id)
    return salesperson_schema.jsonify(person)

# Create an Update
@app.route('/salesperson/<id>', methods=["PUT"])
def update_person(id):
    person = Salesperson.query.get(id)
# Say what we want to update
    first_name = request.json['first_name']
    last_name = request.json['last_name']

    person.first_name = first_name
    person.last_name = last_name

    db.session.commit()

    return salesperson_schema.jsonify(person)


# Delete Product
@app.route('/salesperson/<id>', methods=["DELETE"])
def delete_person(id):
    person = Salesperson().query.get(id)
    db.session.delete(person)
    db.session.commit()

    return salesperson_schema.jsonify(person)

# Get All Products
@app.route('/salesperson', methods=["GET"])
def get_all_persons():
    all_persons = Salesperson.query.all()
    result = salespersons_schema.dump(all_persons)
    # data is avalible on result because when product schema is dumped it will give you anythong avalbile on that rout if htere is anything avalibe on that rout, if you just put result and not rresult.data you would just get an object.
    return jsonify(result.data)
