from flask import Blueprint,redirect,flash,render_template,url_for,request
from application.models import Users,Reservation,ReservationSchema,Boats
from application.Main.forms import BookBoatForm
from application import db
import os
import json
import requests

from sqlalchemy import text
from datetime import datetime
from flask_login import login_user, current_user, logout_user, login_required
main  = Blueprint('main', __name__,template_folder='templates',static_folder='../static')


@main.route('/')

def Index():
    if current_user.is_authenticated:
        if current_user.is_admin == 1:
            return redirect(url_for("admin.Index"))
    
    
    
    boats = requests.get('http://localhost:5000/apis/get_all_boats')
    data= boats.text
    parse = json.loads(data)
    
    return render_template('main/boats.html',boats=parse['boats'])



    
    
    
    



@main.route('/your_booked_order',methods=['GET','POST'])
@login_required
def GetYourBookedOrders():
    if current_user.is_authenticated:
        if current_user.is_admin == 1:
            return redirect(url_for("admin.Index"))
    
   
    api = requests.get("http://localhost:5000/apis/get_your_booked_orders?user_id="+str(current_user.id))
    data = api.text
    parse = json.loads(data)
    return render_template('main/index.html',orders=parse['orders'])



@main.route('/book_boat/<int:boat_id>',methods=['GET','POST'])
@login_required
def BookBoat(boat_id):
    if current_user.is_authenticated:
        if current_user.is_admin == 1:
            return redirect(url_for("admin.Index"))
    
    form = BookBoatForm()
    if request.method == 'POST' and form.validate():
        
        order = Reservation(client_id=current_user.id,boat_id=boat_id,reserve_date=form.ReserveDate.data,pickup_date=form.PickupDate.data,return_date=form.ReturnDate.data,reason=form.Reason.data,status='pending')
        db.session.add(order)
        db.session.commit()
        flash("You Have Booked a Car Successfully")
        return redirect(url_for("main.GetBoats"))
    boat = Boats.query.filter_by(boat_id=boat_id).first()
    return render_template('main/book_boat.html',form=form,boat_id=boat_id,boat=boat)


@main.route('/main/close_reservation/<int:id>',methods=["GET","POST"])
@login_required
def DeleteReservation(id):
    if current_user.is_authenticated:
        if current_user.is_admin == 1:
            return redirect(url_for("admin.Index"))

    order = Reservation.query.filter_by(reserve_id=id).first()
    db.session.delete(order)
    db.session.commit()
    flash("Reservation closed Successfully")
    return redirect(url_for("main.Index"))



@main.route('/main/edit_reservation/<int:id>',methods=["GET","POST"])
@login_required
def EditReservation(id):
    if current_user.is_authenticated:
        if current_user.is_admin == 1:
            return redirect(url_for("admin.Index"))
    reservation = Reservation.query.filter_by(reserve_id=id).first()
    form = BookBoatForm()

    if request.method == "POST":
        reservation.reserve_date = form.ReserveDate.data

        reservation.pickup_date = form.PickupDate.data
        reservation.return_date = form.ReturnDate.data
        reservation.reason = form.Reason.data
        db.session.commit()
        flash("Updated Successfully")
        return redirect(url_for("main.Index"))
    else:
        
        form.ReserveDate.data = reservation.reserve_date
        form.PickupDate.data = reservation.pickup_date
        form.ReturnDate.data = reservation.return_date
        form.Reason.data = reservation.reason
        return render_template("main/edit_reservation.html",form=form,id=id)




@main.route('/logout',methods=["GET","POST"])
@login_required
def Logout():
    if current_user.is_authenticated:
        if current_user.is_admin == 1:
            return redirect(url_for("admin.Index"))
    logout_user()
    return redirect(url_for("auth.Login"))