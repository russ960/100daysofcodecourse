from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        #Method 1. 
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            #Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary
        
        #Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")

## HTTP GET - Read Record
@app.route("/random")
def get_cafe():
    random_cafe = choice(Cafe.query.all())
    print(random_cafe.id)
    return jsonify (cafe = {
        "id":random_cafe.id,
        "name":random_cafe.name,
        "map_url":random_cafe.map_url,
        "img_url":random_cafe.img_url,
        "location":random_cafe.location,
        "has_sockets":random_cafe.has_sockets,
        "has_toilet":random_cafe.has_toilet,
        "has_wifi":random_cafe.has_wifi,
        "can_take_calls":random_cafe.can_take_calls,
        "seats":random_cafe.seats,
        "coffee_price":random_cafe.coffee_price
        }
    )

@app.route("/all")
def get_all_cafe():
    all_cafe = Cafe.query.all()
    # my implementation below and her implementation kept.
    # cafes = {}
    # for cafe_item in all_cafe:
    #     cafes[cafe_item.id] = {
    #         "name":cafe_item.name,
    #         "map_url":cafe_item.map_url,
    #         "img_url":cafe_item.img_url,
    #         "location":cafe_item.location,
    #         "has_sockets":cafe_item.has_sockets,
    #         "has_toilet":cafe_item.has_toilet,
    #         "has_wifi":cafe_item.has_wifi,
    #         "can_take_calls":cafe_item.can_take_calls,
    #         "seats":cafe_item.seats,
    #         "coffee_price":cafe_item.coffee_price
    #         }
    # return jsonify(cafes)
    return jsonify(cafes=[cafe_item.to_dict() for cafe_item in all_cafe])

@app.route("/search")
def get_cafe_by_location():
    search_location = request.args.get('loc')
    print(search_location)
    all_cafes_by_location = Cafe.query.filter_by(location=search_location).all()

    if Cafe.query.filter_by(location=search_location).count() > 0:
        return jsonify(cafes=[cafe_item.to_dict() for cafe_item in all_cafes_by_location])
    else:
        return jsonify (error = {
        "Not Found":"Sorry, we don't have a cafe at that location."
        })


## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.form["name"],
        map_url=request.form["map_url"],
        img_url=request.form["img_url"],
        location=request.form["location"],
        has_sockets=bool(request.form["has_sockets"]),
        has_toilet=bool(request.form["has_toilet"]),
        has_wifi=bool(request.form["has_wifi"]),
        can_take_calls=bool(request.form["can_take_calls"])
    )
    try:
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify (response = {
            "success":"Successfully added the new cafe."
            })
    except Exception as e:
        print(e)
        return jsonify (error = {
            "Not Found":"Sorry, failed to add."
            })
## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<id>", methods=["PATCH"])
def update_price(id):
    new_price = request.args.get('new_price')
    cafe_details = Cafe.query.filter_by(id=id).first()
    if cafe_details:
        cafe_details.coffee_price = new_price
        db.session.commit()
        return jsonify (response = {
            "success":"Successfully updated the price."
            })
    else:
        return jsonify (error = {
            "Not Found": "Sorry a cafe with that id was not found in the database."
            }), 404


## HTTP DELETE - Delete Record
@app.route("/report-closed/<id>", methods=["DELETE"])
def delete_cafe(id):
    del_api_key = "TopSecretAPIKey"
    api_key = request.args.get('api-key')
    if api_key ==  del_api_key:
        cafe_details = Cafe.query.filter_by(id=id).first()
        if cafe_details:
            Cafe.query.filter_by(id=id).delete()
            db.session.commit()
            return jsonify (response = {
                "success":"Successfully removed cafe."
                }), 200
        else:
            return jsonify (error = {
                "Not Found": "Sorry a cafe with that id was not found in the database."
                }), 404
    else:
        return jsonify (error = {
                "error": "Sorry, that's not allowed. Make sure you have the correct api_key."
                }), 403

if __name__ == '__main__':
    app.run(debug=True)
