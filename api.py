from flask import *
from database import*
import uuid

api=Blueprint('api',__name__)
@api.route('/login',methods=['get','post'])
def login():
	data={}
	username = request.form['username1']
	password = request.form['password']
	
	q="SELECT * FROM `login` WHERE `Username`='%s' AND `Password`='%s'"%(username,password)
	res = select(q)
	if res:
		login_id=res[0]['Login_id']
		return jsonify(status="true", lid=res[0]['Login_id'], type=res[0]["Usertype"])
	else:
		return jsonify(status="false")

@api.route('/register',methods=['get','post'])
def register():
	data={}
	fname=request.form['name']
	lname=request.form['lname']
	phone=request.form['phone']
	email=request.form['email']

	place=request.form['place']

	uname=request.form['username']
	passw=request.form['password']
	q="Insert into login values (null,'%s','%s','user')"%(uname,passw)
	ids=insert(q)
	print(q)
	q="INSERT INTO `user` VALUES(NULL,'%s','%s','%s','%s','%s','%s')"%(ids,fname,lname,place,phone,email)
	print(q) 
	res=insert(q)
	
	
	if res:
		return jsonify(status="true",data=res)
	else:
		return jsonify(status="false")
@api.route('/view_request',methods=['get','post'])
def view_request():
	data={}
	r="select * from wdetails inner join caregiver using(Caregiver_id)"
	res=select(r)
	if res:
		return jsonify(status="true",data=res)
	else:
		return jsonify(status="false")
@api.route('/send_request',methods=['get','post'])
def send_request():
	data={}
	request1=request.form['request']
	Wdetails_id=request.form['Wdetails_id']
	lid=request.form['lid']
	print("=================",lid)
	total_amount=request.form['total_amount']
	y="insert into request values(null,(select User_id from user where Login_id='%s'),'%s','%s',curdate(),curtime(),'%s','pending')"%(lid,Wdetails_id,request1,total_amount)
	res=insert(y)
	if res:
		return jsonify(status="true",data=res)
	else:
		return jsonify(status="false")
@api.route('/view_request_user',methods=['get','post'])
def view_request_user():
	data={}
	log_id=request.form['lid']

	q="SELECT * FROM request inner join wdetails using(Wdetails_id) inner join caregiver using(Caregiver_id) where `User_id`=(SELECT `User_id` FROM `user` WHERE `Login_id`='%s')"%(log_id)
	print(q)
	res=select(q)
	if res:
		return jsonify(status="true",data=res)
	else:
		return jsonify(status="false")
@api.route('/view_extra_work',methods=['get','post'])
def view_extra_work():
	data={}
	Request_id=request.form['Request_id']

	q="SELECT * FROM ework where Request_id='%s'"%(Request_id)
	print(q)
	res=select(q)
	if res:
		return jsonify(status="true",data=res)
	else:
		return jsonify(status="false")
@api.route('/confirm_amount',methods=['post'])
def confirm_amount():
	Request_id=request.form['Request_id']
	Extraamount=request.form['Extraamount']
	u="update request set Total=Total+'%s' where Request_id='%s'"%(Extraamount,Request_id)
	res=update(u)
	if res:
		return jsonify(status="true",data=res)
	else:
		return jsonify(status="false")
@api.route('/payment',methods=['post'])
def payment():
	Request_id=request.form['Request_id']
	Total=request.form['amount']
	u="insert into payment values(null,'%s','%s',curdate())"%(Request_id,Total)
	res=insert(u)
	u="update request set Status='paid' where Request_id='%s'"%(Request_id)
	res=update(u)
	if res:
		return jsonify(status="true",data=res)
	else:
		return jsonify(status="false")
@api.route('/send_info',methods=['get','post'])
def send_info():
	data={}
	request2=request.form['request']
	Request_id=request.form['Request_id']

	q="INSERT INTO `info` VALUES(NULL,'%s','%s')"%(Request_id,request2)
	res=insert(q)

	if res:
		return jsonify(status="true",data=res)
	else:
		return jsonify(status="false")
@api.route('/send_ecomplaint',methods=['get','post'])
def send_ecomplaint():
	data={}
	name=request.form['name']
	Request_id=request.form['Request_id']

	q="INSERT INTO `ecomplaints` VALUES(NULL,'%s','%s','pending',CURDATE())"%(Request_id,name)
	res=insert(q)

	if res:
		return jsonify(status="true",data=res)
	else:
		return jsonify(status="false")

@api.route('/view_ecomplaint',methods=['get','post'])
def view_ecomplaint():
	data={}
	Request_id=request.form['Request_id']

	q="SELECT * FROM `ecomplaints` WHERE Request_id='%s'"%(Request_id)
	print(q)
	res=select(q)
	if res:
		return jsonify(status="true",data=res)
	else:
		return jsonify(status="false")

@api.route('/send_complaint',methods=['get','post'])
def send_complaint():
	data={}
	feedback=request.form['name']
	log_id=request.form['lid']

	q="INSERT INTO `complaints` VALUES(NULL,(SELECT `User_id` FROM `user` WHERE `Login_id`='%s'),'%s','pending',CURDATE())"%(log_id,feedback)
	res=insert(q)

	if res:
		return jsonify(status="true",data=res)
	else:
		return jsonify(status="false")

@api.route('/view_complaint',methods=['get','post'])
def view_feedback():
	data={}
	log_id=request.form['lid']

	q="SELECT * FROM `complaints` WHERE `User_id`=(SELECT `User_id` FROM `user` WHERE `Login_id`='%s')"%(log_id)
	print(q)
	res=select(q)
	if res:
		return jsonify(status="true",data=res)
	else:
		return jsonify(status="false")
@api.route('/chat_tech',methods=['get','post'])
def chat_tech():

	data = {}
	lid=request.form['lid']
	caregiverId=request.form['caregiverId']
	# r="select * from chat "
	r="select * from chat where (Sender_id='%s' and Receiver_id=(select Login_id from caregiver where Caregiver_id='%s')) or (Receiver_id='%s' and Sender_id=(select Login_id from caregiver where Caregiver_id='%s'))"%(lid,caregiverId,lid,caregiverId)
	res=select(r)
	print("TTtttttttttttttttttt",res)
	if res:
		return jsonify(status="true",data=res)
	else:
		return jsonify(status="false")

@api.route('/send_message',methods=['get','post'])
def send_message():

	data = {}

	lid=request.form['lid']
	caregiverId=request.form['caregiverId']
	message=request.form['message']
	r="insert into chat values(null,'%s',(select Login_id from caregiver where Caregiver_id='%s'),'%s',curdate())"%(lid,caregiverId,message)
	res=insert(r)

	
	
	if res:
		return jsonify(status="true")
	else:
		return jsonify(status="false")
@api.route('/add_rate',methods=['get','post'])
def add_rate():

	data = {}

	rate=request.form['rate']
	Request_id=request.form['Request_id']
	review=request.form['review']
	r="insert into rating values(null,'%s','%s','%s',curdate())"%(Request_id,rate,review)
	
	res=insert(r)
	if res:
		return jsonify(status="true")
	else:
		return jsonify(status="false")
@api.route('/view_rate',methods=['get','post'])
def view_rate():

	data = {}


	Request_id=request.form['Request_id']
	
	r="select * from rating where Request_id='%s'"%(Request_id)
	
	res=select(r)
	if res:
		return jsonify(status="true",data=res)
	else:
		return jsonify(status="false")