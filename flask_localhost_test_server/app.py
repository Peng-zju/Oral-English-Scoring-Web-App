import mysql.connector
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

mysql_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='WinterProject',
    database="winter_proj_db"
)
cursor = mysql_db.cursor()

app = Flask(__name__)

CORS(app, supports_credentials=True)


@app.route('/admin')
def admin():
    return render_template('index.html')


@app.route('/get_new_info/<region_id>/<bank_id>/<current_ver>', methods=['GET'])
def get_new_questions(region_id, bank_id, current_ver):
    cursor.execute(
        'SELECT qid, left(requirement, 20), left(body, 90), comment, image FROM Question WHERE rid = %s AND type_id = %s AND version > %s;',
        (region_id, bank_id, current_ver))
    data = cursor.fetchall()
    list = []
    for row in data:
        object = {'qid': row[0], 'requirement': row[1], 'body': row[2], 'comment': row[3], 'image': row[4]}
        list.append(object)
    return jsonify(list)


@app.route('/get_version/<region_id>/<bank_id>', methods=['GET'])
def get_current_ver(region_id, bank_id):
    cursor.execute('SELECT latest_ver FROM QuestionBank WHERE rid = %s AND type_id = %s;', (region_id, bank_id))
    result = cursor.fetchone()[0]
    return str(result)


@app.route('/admin/get_all_questions', methods=['GET'])
def get_all_questions():
    cursor.execute('SELECT qid, region_name, type_name, requirement, body, comment, image, version FROM Question Q, QuestionBank QB, Region R WHERE Q.rid = R.rid AND Q.type_id = QB.type_id AND QB.rid = R.rid;')
    data = cursor.fetchall()
    list = []
    for row in data:
        object = {'qid': row[0], 'region_name': row[1], 'type_name': row[2], 'requirement': row[3], 'body': row[4], 'comment': row[5], 'image': row[6], 'version': row[7]}
        list.append(object)
    return jsonify(list)


@app.route('/admin/get_all_regions', methods=['GET'])
def get_all_regions():
    cursor.execute('SELECT * FROM Region;')
    data = cursor.fetchall()
    list = []
    for row in data:
        object = {'rid': row[0], 'region_name': row[1]}
        list.append(object)
    return jsonify(list)


@app.route('/admin/get_all_regions_details', methods=['GET'])
def get_all_regions_details():
    cursor.execute(
        'SELECT R.rid, R.region_name, COUNT(*) AS bank_count FROM Region R, QuestionBank QB WHERE R.rid = QB.rid GROUP BY R.rid;')
    data = cursor.fetchall()
    list = []
    for row in data:
        object = {'rid': row[0], 'region_name': row[1], 'bank_count': row[2]}
        list.append(object)
    return jsonify(list)


@app.route('/admin/post_question_bank', methods=['POST'])
def post_question_bank():
    cursor.execute("INSERT INTO QuestionBank VALUES (%s, %s, '2000-1-1 00:00:00', %s)",
                   (request.json['rid'], request.json['type_id'], request.json['type_name']))
    mysql_db.commit()
    return ""


@app.route('/admin/post_question', methods=['POST'])
def post_question():
    cursor.execute('INSERT INTO Question VALUES(%s, %s, NULL, %s, %s, %s, NULL, NOW());', (request.json['rid'], request.json['type_id'], request.json['requirement'], request.json['body'], request.json['comment']))
    mysql_db.commit()
    return ""


@app.route('/admin/post_region', methods=['POST'])
def post_region():
    cursor.execute('INSERT INTO Region VALUES(%s, %s);', (request.json['rid'], request.json['region_name']))
    mysql_db.commit()
    return ""


@app.route('/admin/get_types/<rid>', methods=['GET'])
def get_types(rid):
    cursor.execute('SELECT * FROM QuestionBank WHERE rid = %s;', (rid,))
    data = cursor.fetchall()
    list = []
    for row in data:
        object = {'rid': row[0], 'type_id': row[1], 'latest_ver': row[2], 'type_name': row[3]}
        list.append(object)
    return jsonify(list)


@app.route('/admin/delete_questions', methods=['POST'])
def delete_questions():
    command = 'DELETE FROM Question WHERE qid IN (%s);' % (str(request.get_data(), encoding="utf-8"))
    cursor.execute(command)
    mysql_db.commit()
    return ""


@app.route('/admin/edit_question', methods=['POST'])
def edit_questions():
    cursor.execute('DELETE FROM Question WHERE qid = %s;', (request.json['qid'],))
    mysql_db.commit()
    cursor.execute('SELECT rid FROM Region WHERE region_name = %s;', (request.json['region_name'],))
    rid = cursor.fetchone()
    cursor.execute('INSERT INTO Question VALUES(%s, %s, NULL, %s, %s, %s, NULL, NOW());', (rid, request.json['type_id'], request.json['requirement'], request.json['body'], request.json['comment']))
    mysql_db.commit()
    return ""


@app.route('/admin/login', methods=['POST'])
def login():
    if request.json['account'] == 'winter' and request.json['password'] == '5815':
        return 200


if __name__ == '__main__':
    app.run()
