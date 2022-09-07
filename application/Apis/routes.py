from flask import Blueprint,redirect,flash,render_template,url_for,request,jsonify
from application.models import Users,Reservation,ReservationSchema,Boats,BoatsSchema,UserSchema

from application import db
import os
from sqlalchemy import text
from datetime import datetime
from flask_login import login_user, current_user, logout_user, login_required
apis  = Blueprint('apis', __name__,template_folder='templates',static_folder='../static',url_prefix="/apis")


@apis.route('/get_reservations')
@login_required
def Index():
    id = request.args.get('id')
    orders_query = text("SELECT * FROM reservation  LEFT JOIN boats on boats.boat_id=reservation.boat_id where client_id="+str(id))
    order_execute = db.engine.execute(orders_query)
    reservation_schema = ReservationSchema(many=True)
    orders = reservation_schema.dump(order_execute)
    return jsonify({
        "reservations":orders
    })


@apis.route('/get_all_boats',methods=['GET'])
def GetBoats():
    
    boats_query = Boats.query.all()
    boats_schema = BoatsSchema(many=True)
    boats = boats_schema.dump(boats_query)
    return jsonify({
        "boats":boats
    })

@apis.route('/get_all_orders')
def AllOrders():
    orders_query = text("SELECT * FROM reservation LEFT JOIN users on users.id=client_id LEFT JOIN boats on boats.boat_id=reservation.boat_id")
    order_execute = db.engine.execute(orders_query)
    orders_schema = ReservationSchema(many=True)

    orders = orders_schema.dump(order_execute)
    return jsonify({
        "orders":orders
    })


        

@apis.route('/get_all_users')
def GetAllUsers():
    user_query = Users.query.filter_by(is_admin=0).all()
    users_schema = UserSchema(many=True)
    users = users_schema.dump(user_query)

    return jsonify({
        "users":users
    })



@apis.route("/get_your_booked_orders")
def GetYourBookedOrders():
    user_id = request.args.get("user_id")
    orders_query = text("SELECT * FROM reservation  LEFT JOIN boats on boats.boat_id=reservation.boat_id where client_id="+str(user_id))
    order_execute = db.engine.execute(orders_query)
    reservation_schema = ReservationSchema(many=True)
    orders = reservation_schema.dump(order_execute)

    return jsonify({
        "orders":orders
    })
