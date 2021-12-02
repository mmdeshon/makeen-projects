def update_dict(user_dict, user_tuple):
    user_dict[user_tuple[0]] = user_tuple[1]
    return user_dict


person = {"name": "Andy"}
print(update_dict(person, ('age', 20)))
