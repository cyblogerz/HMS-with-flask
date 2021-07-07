from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Patient():
    def __init__(self,name,address,pno,sex,age):
        self.name=name
        self.address = address
        self.pno = pno
        self.sex = sex
        self.age = age

class reg(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    name =db.Column(db.String(80),nullable=False)
    address = db.Column(db.String(200),nullable=False)
    pno =db.Column(db.String(15),nullable=False)
    sex = db.Column(db.String(10),nullable =False)
    date = db.Column(db.DateTime, default= datetime.utcnow)
    age =db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return f"{self.sno} - {self.name}"


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/patreg',methods=["GET","POST"])
def patreg():
    if request.method == "POST":
        name= f"{request.form['firstname']} {request.form['lastname']}"
        age= request.form["age"]
        address = f"{request.form['address']},{request.form['address2']}"
        pno = request.form["pno"]
        sex = request.form["sex"]
        patient=reg(name=name,address =address,pno=pno,sex=sex,age=age)
        db.session.add(patient)
        db.session.commit()
    return render_template('patreg.html')

@app.route('/patlist')
def patlist():
   patlist = reg.query.all()
   return render_template('patlist.html',patlist=patlist)

if __name__ == "__main__":
    app.run(debug=True)