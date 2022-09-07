from flask import Blueprint,redirect,flash,render_template,url_for,request
from application.models import Users,Reservation,Boats,ReservationSchema
from application.Admin.forms import AddBoatForm
from application import db
import os
import requests
import json
from sqlalchemy import text
from datetime import datetime
from flask_login import login_user, current_user, logout_user, login_required
admin  = Blueprint('admin', __name__,template_folder='templates',static_folder='../static')


@admin.route('/admin')
@login_required
def Index():
    if current_user.is_authenticated:
        if current_user.is_admin == 0:
            return redirect(url_for("main.Index"))
    api = requests.get("https://boat1-rental.herokuapp.com/apis/get_all_users")    
    data= api.text    
    parse = json.loads(data)
    return render_template('admin/index.html',users=parse["users"])


@admin.route('/admin/orders')
@login_required
def Orders():
    if current_user.is_authenticated:
        if current_user.is_admin == 0:
            return redirect(url_for("main.Index"))
    
    api = requests.get('https://boat1-rental.herokuapp.com/apis/get_all_orders')
    data= api
    parse =json.loads(data.text)
    
    print(parse)
    return render_template('admin/orders.html',orders=parse['orders'])

@admin.route('/admin/accept_order/<int:id>',methods=["GET","POST"])
@login_required
def AcceptOrder(id):
    if current_user.is_authenticated:
        if current_user.is_admin == 0:
            return redirect(url_for("main.Index"))

    order = Reservation.query.filter_by(reserve_id=id).first()
    order.status = 'accepted'
    db.session.commit()
    flash("Accepted Successfully")
    return redirect(url_for("admin.Orders"))



@admin.route('/admin/complete_order/<int:id>',methods=["GET","POST"])
@login_required
def CompleteOrder(id):
    if current_user.is_authenticated:
        if current_user.is_admin == 0:
            return redirect(url_for("main.Index"))

    order = Reservation.query.filter_by(reserve_id=id).first()
    order.status = 'completed'
    db.session.commit()
    flash("Completed Successfully")
    return redirect(url_for("admin.Orders"))


@admin.route('/admin/delete_order/<int:id>',methods=["GET","POST"])
@login_required
def DeleteOrder(id):
    if current_user.is_authenticated:
        if current_user.is_admin == 0:
            return redirect(url_for("main.Index"))

    order = Reservation.query.filter_by(reserve_id=id).first()
    db.session.delete(order)
    db.session.commit()
    flash("Deleted Successfully")
    return redirect(url_for("admin.Orders"))



@admin.route('/admin/boats',methods=['GET','POST'])
@login_required
def GetBoats():
    if current_user.is_authenticated:
        if current_user.is_admin == 0:
            return redirect(url_for("main.Index"))
    
    form = AddBoatForm()
    if request.method == 'POST':
        boat = Boats(boat_name=form.boat_name.data,year=form.year.data,model=form.model.data,boat_fuel=form.boat_fuel.data,model_group=form.group.data,price_per_day=form.price_per_day.data,boat_type=form.boat_type.data,gear=form.gear.data,performance_ps=form.performance_ps.data,doors=form.doors.data,seats=form.seats.data,color=form.color.data)
        db.session.add(boat)
        db.session.commit()
        flash("Boat Added Successfully")
        return redirect(url_for('admin.GetBoats'))

    api = requests.get("https://boat1-rental.herokuapp.com/apis/get_all_boats")
    data= api.text
    parse = json.loads(data)
    print(parse)
    return render_template('admin/boats.html',form=form,boats=parse['boats'])




@admin.route('/admin/delete_boat/<int:id>',methods=["GET","POST"])
@login_required
def DeleteBoat(id):
    if current_user.is_authenticated:
        if current_user.is_admin == 0:
            return redirect(url_for("main.Index"))

    boat = Boats.query.filter_by(boat_id=id).first()
    db.session.delete(boat)
    db.session.commit()
    flash("Deleted Successfully")
    return redirect(url_for("admin.GetBoats"))



@admin.route('/admin/delete_user/<int:id>',methods=["GET","POST"])
@login_required
def DeleteUser(id):
    if current_user.is_authenticated:
        if current_user.is_admin == 0:
            return redirect(url_for("main.Index"))

    user = Users.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    flash("Deleted Successfully")
    return redirect(url_for("admin.Index"))


@admin.route('/admin_logout',methods=["GET","POST"])
@login_required
def Logout():
    if current_user.is_authenticated:
        if current_user.is_admin == 0:
            return redirect(url_for("main.Index"))
    logout_user()
    return redirect(url_for("auth.Login"))