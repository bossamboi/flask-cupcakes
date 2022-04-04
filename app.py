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

    return (jsonify(cupcakes=serialized), 200)

@app.get('/api/cupcakes/<int:cupcake_id>')
def get_single_cupcake(cupcake_id):
    """Gets a single cupcake"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return (jsonify(cupcake=serialized), 200)

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