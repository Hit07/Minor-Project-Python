import json

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from random import choice

app = Flask(__name__)

API_KEY = 'Cafe@123'
# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route('/random', methods=['GET'])
def random_cafe():
    cafe = db.session.execute(db.select(Cafe))
    cafes = choice(cafe.scalars().all())
    return jsonify(cafes=[
        {
            "name": cafes.name,
            "map_url": cafes.map_url,
            "img_url": cafes.img_url,
            "location": cafes.location,
            'amenities': {
                "seats": cafes.seats,
                "has_toilet": cafes.has_toilet,
                "has_wifi": cafes.has_wifi,
                "has_sockets": cafes.has_sockets,
                "can_take_calls": cafes.can_take_calls,
                "coffee_price": cafes.coffee_price
            }
        }
    ])


@app.route('/all', methods=['GET'])
def all_cafes():
    cafe = db.session.execute(db.select(Cafe)).scalars().all()
    all_cafes = []
    for cafes in cafe:
        all_cafes.append({
            "name": cafes.name,
            "map_url": cafes.map_url,
            "img_url": cafes.img_url,
            "location": cafes.location,
            'amenities': {
                "seats": cafes.seats,
                "has_toilet": cafes.has_toilet,
                "has_wifi": cafes.has_wifi,
                "has_sockets": cafes.has_sockets,
                "can_take_calls": cafes.can_take_calls,
                "coffee_price": cafes.coffee_price
            }
        })
    return jsonify(all_cafes)


@app.route('/search', methods=['GET'])
def search():
    loc = request.args.get('loc')
    cafe = db.session.execute(db.select(Cafe).filter(Cafe.location == loc)).scalars().all()
    if not cafe:
        return jsonify({"error": {"Not Found": "Sorry, we don't have a cafe at that location."}}, 400)
    all_cafes = []
    for cafes in cafe:
        all_cafes.append({
            "name": cafes.name,
            "map_url": cafes.map_url,
            "img_url": cafes.img_url,
            "location": cafes.location,
            'amenities': {
                "seats": cafes.seats,
                "has_toilet": cafes.has_toilet,
                "has_wifi": cafes.has_wifi,
                "has_sockets": cafes.has_sockets,
                "can_take_calls": cafes.can_take_calls,
                "coffee_price": cafes.coffee_price
            }
        })
    return jsonify(all_cafes)


# HTTP POST - Create Record
@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get('name'),
        map_url=request.form.get('map_url'),
        img_url=request.form.get('img_url'),
        location=request.form.get('location'),
        seats=request.form.get('seats'),
        has_toilet=bool(request.form.get('has_toilet')),
        has_wifi=bool(request.form.get('has_wifi')),
        has_sockets=bool(request.form.get('has_sockets')),
        can_take_calls=bool(request.form.get('can_take_calls')),
        coffee_price=request.form.get('coffee_price')
    )
    try:
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify({"success": "Cafe added successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@app.route('/add-cafe', methods=['POST','GET'])
def add_json_cafe():
    if request.is_json:
        try:
            data = request.get_json()

            new_cafe = Cafe(
                name=data['name'],
                map_url=data['map_url'],
                img_url=data['img_url'],
                location=data['location'],
                seats=data['seats'],
                has_toilet=bool(data['has_toilet']),
                has_wifi=bool(data['has_wifi']),
                has_sockets=bool(data['has_sockets']),
                can_take_calls=bool(data['can_take_calls']),
                coffee_price=data['coffee_price']
            )

            db.session.add(new_cafe)
            db.session.commit()
            return jsonify({"success": "Cafe added successfully"}), 201
        except KeyError as e:
            return jsonify({"error": f"Missing required field: {str(e)}"}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Request must be JSON"}), 400


# HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:cafe_id>', methods=['GET','PATCH'])
def update_price(cafe_id):
    new_price = request.form.get('new_price')
    cafe = db.get_or_404(Cafe, cafe_id)
    print(new_price)
    cafe.coffee_price = new_price
    if cafe:
        db.session.commit()
        return jsonify({"success": "Coffee price updated successfully"})
    else:
        db.session.rollback()
        return jsonify({"error": {
            "Not Found": "Sorry a cafe with that id was not found in the database."}
        })


# HTTP DELETE - Delete Record
@app.route('/report-closed/<int:cafe_id>', methods=['DELETE'])
def delete_cafe(cafe_id):
    api_key = request.form.get('api_key')
    cafe = db.get_or_404(Cafe,cafe_id)
    if cafe:
        if api_key != API_KEY:
            return jsonify({'error':'Sorry not authorized, not valid api key'})
        else:
            cafe_data = {
                "id": cafe.id,
                "name": cafe.name,
                "map_url": cafe.map_url,
                "img_url": cafe.img_url,
                "location": cafe.location,
                "seats": cafe.seats,
                "has_toilet": cafe.has_toilet,
                "has_wifi": cafe.has_wifi,
                "has_sockets": cafe.has_sockets,
                "can_take_calls": cafe.can_take_calls,
                "coffee_price": cafe.coffee_price
            }
            with open('closed_cafe.txt', 'a') as closed_cafe:
                closed_cafe.write(json.dumps(cafe_data) + '\n')
            db.session.delete(cafe)
            db.session.commit()
            return jsonify({'Success':'Cafe is removed successfully'})
    return jsonify({"error": 'Cafe with the "id" not found!'})


if __name__ == '__main__':
    app.run(debug=True)
