from flask import *
from database import *
public=Blueprint('public',__name__)

@public.route('/',methods=['get','post'])
def home():
	session.clear()
	
	return render_template('home.html')

@public.route('/login',methods=['get','post'])
def login():
	session.clear()
	if 'submit' in request.form:
		uname=request.form['uname']
		password=request.form['password']
		q="select * from login where Username='%s' and Password='%s'"%(uname,password)
		res=select(q)

		if res:
			session['Login_id']=res[0]['Login_id']

			if res[0]['Usertype']=='admin':
				return redirect(url_for('admin.adminhome'))

			if res[0]['Usertype']=='caregiver':
				q="select * from caregiver where Login_id='%s'"%(session['Login_id'])
				res=select(q)
				print(res)
				session['Caregiver_id']=res[0]['Caregiver_id']
				session['Fname']=res[0]['Fname']
				return redirect(url_for('caregiver.caregiverhome'))
			
	
		else:
			flash("LOGIN FAILED")
	return render_template('login.html')



@public.route('/caregiver_reg',methods=['get','post'])
def caregiver_reg():
	data={}
	if 'submit' in request.form:
		print("^^^^^^^^^^^^^^^^^^^^^^^^")
		fn=request.form['fn']
		ln=request.form['ln']
		pl=request.form['pl']
		ph=request.form['phone']
		email=request.form['email']
		qualification=request.form['qualification']
		uname=request.form['uname']
		password=request.form['password']
		q="select * from login where username='%s'"%(uname)
		res=select(q)
		
		

		if res:
			flash('THIS USER NAME ALREADY TAKEN BY ANOTHER USER')
			return redirect(url_for('public.caregiver_reg'))
		else:
			q="insert into login values(NULL,'%s','%s','pending')"%(uname,password)
			lid=insert(q)
			q="insert into caregiver values(NULL,'%s','%s','%s','%s','%s','%s','%s')"%(lid,fn,ln,pl,ph,email,qualification)
			insert(q)
			return redirect(url_for('public.caregiver_reg'))
	return render_template('caregiver_reg.html',data=data)


