from app.schemas.user import UserCreate, UserUpdate

users_db = {}
current_user_id = 1


def get_all_users():
    return list(users_db.values())


def get_user_by_id(user_id: int):
    return users_db.get(user_id)


def create_user(user: UserCreate):
    global current_user_id

    new_user = {
        "id": current_user_id,
        "name": user.name,
        "email": user.email,
        "age": user.age
    }

    users_db[current_user_id] = new_user
    current_user_id += 1

    return new_user


def update_user(user_id: int, user: UserUpdate):
    if user_id not in users_db:
        return None

    users_db[user_id] = {
        "id": user_id,
        "name": user.name,
        "email": user.email,
        "age": user.age
    }

    return users_db[user_id]


def delete_user(user_id: int):
    if user_id not in users_db:
        return None

    return users_db.pop(user_id)