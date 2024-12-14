import json


def read_json(file):
    with open(file, 'r') as file:
        return json.load(file)


def list2dict(profs):
    res = dict()
    for prof in profs:
        if prof['user_id']:
            res[prof['user_id']] = prof
    return res


def save_file(text, file_path):
    with open(file_path, 'w') as file:
        file.write(text)


sql, insert = '', 'INSERT INTO COMMON_MEMBER (username, password, name, email, department_id, year_id, role, created_at, updated_at)\nVALUES '
user_file, profile_file, result_file = 'json/auth_user.json', 'json/accounts_profile.json', 'sql/accounts_user.sql'
users, profiles = read_json(user_file), read_json(profile_file)
profiles = list2dict(profiles)

for user in users:
    pk = user['id']
    if pk in profiles:
        profile = profiles[pk]
        username, password, email = user['username'], user['password'], user['email']
        is_active, is_staff = user['is_active'], user['is_staff']
        name, department_id, year_id = profile['name'], profile['department_id'], profile['year_id']
        sql += f"{insert}('{username}', '{password}', '{name}', '{email}', {department_id}, {year_id}, 'ROLE_USER', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);\n"
save_file(sql, result_file)
