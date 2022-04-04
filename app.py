from flask import Flask, request, json, jsonify
from models import Cupcake, db, connect_db, DEFAULT_IMG

"""Flask app for Cupcakes"""

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'MYPASSWORRD'

connect_db(app)
db.create_all()

@app.get('/api/cupcakes')
def get_cupcakes():
    """Get all cupcakes"""

    cupcakes = Cupcake.query.all()
    serialized = [cupcake.serialize() for cupcake in cupcakes]

    # don't need to specify status code if expecting status 200
    return jsonify(cupcakes=serialized)

@app.get('/api/cupcakes/<int:cupcake_id>')
def get_single_cupcake(cupcake_id):
    """Gets a single cupcake"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)

@app.post('/api/cupcakes')
def create_cupcake():
    """Creates a cupcake"""

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json["image"] or None

    cupcake = Cupcake(flavor = flavor,
                        size = size,
                        rating = rating,
                        image = image)

    db.session.add(cupcake)
    db.session.commit()

    serialized = cupcake.serialize()

    return (jsonify(cupcake=serialized), 201)


@app.route('/api/cupcakes/<int:cupcake_id>', methods=['PATCH'])
def update_cupcake_field(cupcake_id):
    """Updates provided fields for a cupcake"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    # req = request.get_json()
    # print('req type=',type(req))

    # for k, v in req.items():
    #     print("k=",k)
    #     print("v=",v)
    #     cupcake.flavor = v


    flavor = request.json["flavor"] or cupcake.flavor
    size = request.json["size"] or cupcake.size
    rating = request.json["rating"] or cupcake.rating
    image = request.json["image"] or cupcake.image

    cupcake.flavor = flavor
    cupcake.size = size
    cupcake.rating = rating
    cupcake.image = image

    db.session.add(cupcake)
    db.session.commit()

    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)



@app.route('/api/cupcakes/<int:cupcake_id>', methods=['DELETE'])
def delete_cupcake(cupcake_id):
    """Deletes a cupcake"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)


    db.session.delete(cupcake)
    db.session.commit()
    return jsonify({"deleted" : cupcake_id})