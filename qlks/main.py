from flask import render_template, request, redirect
from qlks import app, utils, login
from qlks.admin import *
from flask_login import login_user


@app.route("/")
def index():
    room_type = utils.read_data()
    return render_template('index1.html',
                           room_type=room_type)


@app.route("/rooms")
def room_list():
    rType_id = request.args.get('room_type_id')
    kw = request.args.get('kw')
    from_price = request.args.get('from_price')
    to_price = request.args.get('to_price')
    rooms = utils.read_rooms(rType_id=rType_id,
                                   kw=kw,
                                   from_price=from_price,
                                   to_price=to_price)

    return render_template('room-list.html',
                           #Xem lai cho nay
                           room=rooms)

@app.route("/rooms/<int:room_id>")
def room_detail(room_id):
    room = utils.get_room_by_id(room_id=room_id)

    return render_template('room_detail.html',
                           room=room)

@app.route('/login', methods=['post'])
def login_usr():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password', '')

        user = utils.check_login(username=username,
                                 password=password)
        if user:
            login_user(user=user)

    return redirect('/admin')

@login.user_loader
def get_user(user_id):
    return utils.get_user_by_id(user_id=user_id)

if __name__ == '__main__':
    app.run(debug=True)