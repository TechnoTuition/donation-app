import razorpay
import json
from flask_sqlalchemy import SQLAlchemy

from flask import Flask, render_template, request,redirect,url_for

app = Flask(__name__,static_folder = "static", static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer,nullable=False)
    

    def __repr__(self):
        return '<User %r>' % self.username
        


razorpay_client = razorpay.Client(auth=("rzp_test_cbFCyT1bTI7swV", "eOBbeZgjD9OAzfLKEKo4cUdH"))


@app.route('/')
def app_create():
    return render_template('index.html')


@app.route('/pay', methods=['POST'])
def app_charge():
    if request.method == "POST":
        amount = request.form["amount"]
        print(amount)
        data = { "amount": int(amount)*100, "currency": "INR", "receipt": "order_rcptid_11" }
        payment = razorpay_client.order.create(data=data) 
        user = User(amount=amount)
        db.session.add(user)
        db.session.commit()
    return render_template("app.html",payment=payment)
        
    

@app.route('/success')
def success_p():
    return 
if __name__ == '__main__':
    app.run(debug=True)
