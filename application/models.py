
from application import db,login_manager,ma
from flask_login import UserMixin


@login_manager.user_loader
def load_user(id):
        
    return Users.query.get(int(id))


class Users(db.Model,UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100),nullable=False)
    firstname = db.Column(db.String(100),nullable=False)
    lastname = db.Column(db.String(100),nullable=False)
    password= db.Column(db.String(200),nullable=False)
    gender= db.Column(db.String(100),nullable=False)
    age= db.Column(db.String(100),nullable=False)
    street= db.Column(db.String(300),nullable=False)
    state= db.Column(db.String(300),nullable=False)
    plz= db.Column(db.String(300),nullable=False)

    

    is_admin = db.Column(db.Integer,nullable=True)

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id","email","plz","firstname","lastname","gender","password","age","is_admin","street","state")

class Boats(db.Model):
    boat_id = db.Column(db.Integer(), primary_key=True)
    boat_name = db.Column(db.String(300))
    model = db.Column(db.String(300))
    model_group = db.Column(db.String(300))
    price_per_day = db.Column(db.String(300))


    boat_type = db.Column(db.String(300))
    gear = db.Column(db.String(300))
    boat_fuel = db.Column(db.String(300))
    performance_ps = db.Column(db.String(300))
    doors = db.Column(db.String(300))
    seats = db.Column(db.String(300))
    year = db.Column(db.String(300))
    color = db.Column(db.String(300))

    


class BoatsSchema(ma.Schema):
    class Meta:
        fields = ("boat_id",'boat_name','model_group','model','group','price_per_day','category','boat_type','gear','boat_fuel','performance_ps','doors','seats','year','color')


class Reservation(db.Model):
    reserve_id = db.Column(db.Integer(), primary_key=True)
    client_id = db.Column(db.ForeignKey('users.id',
                                             ondelete='CASCADE'))
    boat_id = db.Column(db.ForeignKey('boats.boat_id',
                                             ondelete='CASCADE'))
    reserve_date = db.Column(db.Date(),nullable=True)
    pickup_date = db.Column(db.Date(),nullable=True)
    return_date = db.Column(db.Date(),nullable=True)
    reason = db.Column(db.String(1000),nullable=True)
    status = db.Column(db.String(100),nullable=True)

class ReservationSchema(ma.Schema):
    class Meta:
        fields = ("reserve_id",'client_id','boat_id','reserve_date','pickup_date','return_date','reason','status','id','firstname','lastname','car_name','car_id')
