import json, hashlib
from qlks.models import User, UserRole


def read_data(path='data/room_type.json'):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def read_rooms(rType_id=None, kw=None, from_price=None, to_price=None):
    rooms = read_data(path='data/rooms.json')

    if rType_id:
        rType_id = int(rType_id)
        rooms = [r for r in rooms \
                    if r['room_type_id'] == rType_id]

    if kw:
        rooms = [r for r in rooms \
                    if r['name'].find(kw) >= 0]

    if from_price and to_price:
        from_price = float(from_price)
        to_price = float(to_price)
        rooms = [r for r in rooms \
                    if to_price >= r['price'] >= from_price]

    return rooms


def get_room_by_id(room_id):
    rooms = read_data(path='data/rooms.json')
    for r in rooms:
        if r["id"] == room_id:
            return r


def check_login(username, password, role=UserRole.ADMIN):
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())

    user = User.query.filter(User.username == username,
                             User.password == password,
                             User.user_role == role).first()

    return user

def get_user_by_id(user_id):
    return User.query.get(user_id)