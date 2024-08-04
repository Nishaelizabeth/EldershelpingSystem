from flask import *
from database import *
import uuid
admin=Blueprint('admin',__name__)
 

@admin.route('/adminhome',methods=['get','post'])
def adminhome():
	if not session.get('Login_id') is None:
		return render_template('adminhome.html')

	else:
		return redirect(url_for('public.login'))










@admin.route('/admin_view_complaints',methods=['get','post'])
def admin_view_complaints():
	data={}
	if not session.get('Login_id') is None:
		q="SELECT * FROM user INNER JOIN complaints USING(User_id)"
		res=select(q)
		data['complaints']=res
		if 'action' in request.args:
			action=request.args['action']
			id=request.args['id']
			if action=="update":
				q="select * from complaints inner join user using(User_id) where Complaint_id='%s' "%(id)
				res=select(q)
				data['updater']=res
		if 'update' in request.form:
			reply=request.form['reply']
			q="update complaintS set Reply='%s' where Complaint_id='%s'"%(reply,id)
			update(q)
			return redirect(url_for('admin.admin_view_complaints'))
		return render_template('admin_view_complaints.html',data=data)


	else:
		return redirect(url_for('public.login'))



@admin.route('/admin_view_ecomplaints',methods=['get','post'])
def admin_view_ecomplaints():
	data={}
	if not session.get('Login_id') is None:
		q="SELECT * FROM request INNER JOIN ecomplaints USING(Request_id)  inner join user USING (User_id)  inner join wdetails using(Wdetails_id)"
		res=select(q)
		data['complaints']=res
		if 'action' in request.args:
			action=request.args['action']
			id=request.args['id']
			if action=="update":
				q="select * from ecomplaints inner join request using(Request_id) inner join user USING (User_id) where Ecomplaint_id='%s' "%(id)
				res=select(q)
				data['updater']=res
		if 'update' in request.form:
			reply=request.form['reply']
			q="update ecomplaints set Reply='%s' where Ecomplaint_id='%s'"%(reply,id)
			update(q)
			return redirect(url_for('admin.admin_view_ecomplaints'))
		return render_template('admin_view_ecomplaints.html',data=data)


	else:
		return redirect(url_for('public.login'))



@admin.route('/view_caregiver',methods=['get','post'])
def view_caregiver():
	data={}
	if not session.get('Login_id') is None:
		id=request.args['id']
		q="SELECT * FROM `caregiver` inner join login using(Login_id) where Caregiver_id='%s'"%(id) 
		res=select(q)
		print(res)
		data['hos']=res

		if 'action' in request.args:
			action=request.args['action']
			id=request.args['id']
		else:
			action=None

		if action=="accept":
			q="update login set Usertype='caregiver' where Login_id='%s'"%(id)
			update(q)
			return redirect(url_for('admin.view_caregiver',id=id))

		if action=="reject":
			q="update login set Usertype='rejected' where Login_id='%s'"%(id)
			update(q)
			return redirect(url_for('admin.view_caregiver',id=id))
		return render_template("view_caregiver.html",data=data)
	else:
		return redirect(url_for('public.login'))




@admin.route('/admin_view_caregiver',methods=['get','post'])
def admin_view_caregiver():
	data={}
	if not session.get('Login_id') is None:

		q="SELECT * FROM `caregiver` inner join login using(Login_id)"
		res=select(q)
		print(res)
		data['hos']=res

		if 'action' in request.args:
			action=request.args['action']
			id=request.args['id']
		else:
			action=None

		if action=="accept":
			q="update login set Usertype='caregiver' where Login_id='%s'"%(id)
			update(q)
			return redirect(url_for('admin.admin_view_caregiver'))

		if action=="reject":
			q="update login set Usertype='rejected' where Login_id='%s'"%(id)
			update(q)
			return redirect(url_for('admin.admin_view_caregiver'))
		return render_template("admin_view_caregiver.html",data=data)
	else:
		return redirect(url_for('public.login'))


@admin.route('/admin_view_users',methods=['get','post'])
def admin_view_users():
	data={}
	if not session.get('Login_id') is None:

		q="SELECT * FROM `user` inner join login using(Login_id)"
		res=select(q)
		print(res)
		data['doct']=res

		if 'action' in request.args:
			action=request.args['action']
			id=request.args['id']
		else:
			action=None

		if action=="accept":
			q="update login set usertype='doctor' where login_id='%s'"%(id)
			update(q)
			return redirect(url_for('admin.admin_view_users'))

		if action=="reject":
			q="update login set usertype='reject' where login_id='%s'"%(id)
			update(q)
			return redirect(url_for('admin.admin_view_users'))
		return render_template("admin_view_users.html",data=data)
	else:
		return redirect(url_for('public.login'))






