from flask import Flask, render_template, request,jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder="static")

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:250768ak@localhost/trainingtest'
app.config.from_object('config.Development')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Person, AdditionPerson

##  first_table user_id, name, middle_name, bornDate, gender
# user_id, education, comment, citizenship
education_val = {
    '1': 'Secondary Education',
    "2": 'The highest incomplete education',
    "3": 'Higher education'
}


@app.route('/',)
def index():

    return render_template("picture.html")


@app.route('/add-form',methods=['POST','GET'])
def add_form():
    gender = 'gender'
    citizen = 'citizen'
    if request.method == 'POST':
        data = request.get_json()
        if gender in data.keys():
            gender = data['gender']
        if data['education'] in education_val:
            data['education'] = education_val.get(str(data['education']))
        else:
            data['education'] = "Dont have education"
        if citizen in data.keys():
            citizen = True
        else:
            citizen = False
        bio = Person(name=data['userName'], middle_name=data['userSurname'], born_date=data['dateBorn'], gender=gender)
        db.session.add(bio)
        db.session.commit()
        additional_info = AdditionPerson(education=data['education'], comment=data['comment'], citizen=citizen, id=bio.user_id)
        db.session.add(additional_info)
        db.session.commit()

    return jsonify('success')
