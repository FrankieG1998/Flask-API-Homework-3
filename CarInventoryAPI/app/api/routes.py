from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Car, car_schema, cars_schema

#api = Blueprint('api',__name__, url_prefix='/api')
api = Blueprint('api',__name__, url_prefix='/api')

#test API
@api.route('/getdata')
def getdata():
    return {'test': 'test1'}

#Add Cars
@api.route('/cars', methods = ['POST'])
@token_required
def create_car(current_user_token):
    car_make = request.json['car_make']
    car_model = request.json['car_model']
    year = request.json['year']
    color = request.json['color']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    car = Car(car_make, car_model, year, color, user_token = user_token )

    db.session.add(car)
    db.session.commit()

    response = car_schema.dump(car)
    return jsonify(response)



#Get List of Cars
@api.route('/cars', methods = ['GET'])
@token_required
def get_car(current_user_token):
    a_user = current_user_token.token
    cars = Car.query.filter_by(user_token = a_user).all()
    response = cars_schema.dump(cars)
    return jsonify(response)

#get details of sepcific car
@api.route('/cars/<id>', methods = ['GET'])
@token_required
def get_single_car(current_user_token, id):    # Currently showing cars of other users as well 
    car = Car.query.get(id)
    response = car_schema.dump(car)
    return jsonify(response)


#Update Car details
@api.route('/cars/<id>', methods = ['POST','PUT'])
@token_required
def update_car(current_user_token,id):
    car = Car.query.get(id) 
    car.car_make = request.json['car_make']
    car.car_model = request.json['car_model']
    car.year = request.json['year']
    car.color = request.json['color']
    car.user_token = current_user_token.token

    db.session.commit()
    response = car_schema.dump(car)
    return jsonify(response)


# Delete Specific Car
@api.route('/cars/<id>', methods = ['DELETE'])
@token_required
def delete_car(current_user_token, id):
    car = Car.query.get(id)
    db.session.delete(car)
    db.session.commit()
    response = car_schema.dump(car)
    return jsonify(response)