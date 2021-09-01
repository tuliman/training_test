import contextlib
import time

from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder="static")

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:250768ak@localhost/trainingtest'
app.config.from_object('config.Development')

url_db = app.config['SQLALCHEMY_DATABASE_URI']
from models import AdditionPersonBase, PersonBase, Phone, db_session

##  first_table user_id, name, middle_name, bornDate, gender
# user_id, education, comment, citizenship
education_val = {
    '1': 'Secondary Education',
    "2": 'The highest incomplete education',
    "3": 'Higher education'
}


@app.route('/', )
def index():
    return render_template("picture.html")


@app.route('/add-form', methods=['POST', 'GET'])
def add_form():
    gender = 'gender'

    result = {}

    if request.method == 'POST':
        data = request.get_json()

        for num, obj in enumerate(data):
            values = {}
            d = (list({i.get('name'): i.get('value')} for i in obj))
            d = ([values.update(dic) for dic in d])

            result.update({num: values})

            for res in result.values():

                if gender in res.keys():
                    res['gender'] = res['gender']
                else:
                    res.update({gender: gender})
                if res['education'] in education_val:
                    res['education'] = education_val.get(str(res['education']))
                else:
                    res['education'] = "Dont have education"

                if 'citizen' not in res:
                    res.update({'citizen': False})
                if res['citizen'] == 'on':
                    res['citizen'] = True

                with db_session(url_db) as ses:
                    print(dir(ses))
                    ses.connection()
                    bio = PersonBase(name=res['userName'], middle_name=res['userSurname'], born_date=res['dateBorn'],
                                     gender=res['gender'])

                    ses.add(bio)
                    ses.commit()

                    addition_info = AdditionPersonBase(education=res['education'], comment=res['comment'],
                                                       citizen=res['citizen'],
                                                       id=bio.user_id)
                    ses.add(addition_info)
                    phone = Phone(phone=res['phone'], phone_id=bio.user_id)
                    ses.add(phone)
                    ses.commit()

    print(result)

    return jsonify('success')
