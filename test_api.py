from flask import Blueprint, jsonify, request, abort
from config import json_template

api_test = Blueprint('api_test', 'api_test', url_prefix='/api/v1')

@api_test.route('test', methods=['GET'])
def tests():
    user_id = request.args.get('user', type=int)

    if user_id is None:
        abort(404)

    response = json_template

    obj = Connector()

    #Bunch of DB I can't share 

    if db_connect['STATUS'] == 'SUCESS':
        conn = db_connect['conn']

        try:
            result = conn.execute(some_sql)

            test = []

            for row in result:
                test.append(dict(row))

                response['sql'] = test

                except Exception as e:
                    print(str(e.args[0]))
            else:
                print('failed to connect to db')

    return jsonify(response)
            