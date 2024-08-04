from flask import *
from database import *
import uuid
caregiver=Blueprint('caregiver',__name__)
 

@caregiver.route('/caregiverhome',methods=['get','post'])
def caregiverhome():
	if not session.get('Login_id') is None:

		hid=session['Caregiver_id']
		fname=session['Fname']
		return render_template('caregiver_home.html',fname=fname)

	else:
		return redirect(url_for('public.login'))







@caregiver.route('/cargiver_viewwork',methods=['get','post'])
def cargiver_viewwork():
	if not session.get('Login_id') is None:
		data={}
	
		q="select * from ework  inner join request using (Request_id)inner join wdetails using(Wdetails_id) inner join user using(User_id) where wdetails.Caregiver_id='%s'"%(session['Caregiver_id'])
		res=select(q)
		data['doct']=res
		return render_template('cargiver_viewwork.html',data=data)
	else:
		return redirect(url_for('public.login'))


	

@caregiver.route('/caregiver_view_ecomplaints',methods=['get','post'])
def caregiver_view_ecomplaints():
	data={}
	if not session.get('Login_id') is None:
		Request_id=request.args['id']
		q="SELECT * FROM request INNER JOIN ecomplaints USING(Request_id)  inner join user USING (User_id)  inner join wdetails using(wdetails_id)  where Request_id='%s'"%(Request_id)
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
			return redirect(url_for('caregiver.caregiver_viewrequest'))
		return render_template('caregiver_view_ecomplaints.html',data=data)


	else:
		return redirect(url_for('public.login'))






@caregiver.route('/cargiver_viewinfo',methods=['get','post'])
def cargiver_viewinfo():
	if not session.get('Login_id') is None:
		data={}
		id=request.args['id']
		q="select * from info inner join request USING (Request_id) where Request_id='%s'"%(id)
		res=select(q)
		data['app']=res
		print(q)
		
		return render_template('cargiver_viewinfo.html',data=data)
	else:
		return redirect(url_for('public.login'))




@caregiver.route('/caregiver_viewrequest',methods=['get','post'])
def caregiver_viewrequest():
	if not session.get('Login_id') is None:
		data={}
		
		q="select * from request inner join wdetails USING(Wdetails_id) inner join user using(User_id) where Caregiver_id='%s'"%(session['Caregiver_id'])
		res=select(q)
		print(q)
		data['app']=res

		if 'action' in request.args:
			action=request.args['action']
			id=request.args['id']
		else:
			action=None

		if action=="accept":
			q="update request set Status='Accepted' where Request_id='%s'"%(id)
			update(q)
			return redirect(url_for('caregiver.caregiver_viewrequest'))

		if action=="reject":
			q="update request set Status='reject' where Request_id='%s'"%(id)
			update(q)
			return redirect(url_for('caregiver.caregiver_viewrequest'))
		return render_template('caregiver_viewrequest.html',data=data)
	else:
		return redirect(url_for('public.login'))




@caregiver.route('/cargiver_Addwork',methods=['get','post'])
def cargiver_Addwork():
	if not session.get('Login_id') is None:
		data={}
		Caregiver_id=session['Caregiver_id']

		if "submit" in request.form:
			details=request.form['details']
			amount=request.form['amount']

			q="insert into wdetails values(null,'%s','%s','%s')"%(Caregiver_id,details,amount)
			insert(q)
			return redirect(url_for('caregiver.cargiver_Addwork'))
		
		return render_template('cargiver_Addwork.html',data=data)
	else:
		return redirect(url_for('public.login'))


@caregiver.route('/caregiver_view_rating',methods=['get','post'])
def caregiver_view_rating():
	if not session.get('Login_id') is None:
		data={}
		id=request.args['id']
		q="select * from rating inner join request USING (Request_id) where Request_id='%s'"%(id)
		res=select(q)
		data['app']=res
		print(q)
		
		return render_template('caregiver_view_rate.html',data=data)
	else:
		return redirect(url_for('public.login'))
@caregiver.route('/cargiver_extrawork',methods=['get','post'])
def cargiver_extrawork():
	if not session.get('Login_id') is None:
		data={}
		Request_id=request.args['id']

		if "submit" in request.form:
			details=request.form['details']
			amount=request.form['amount']

			q="insert into ework values(null,'%s','%s','%s','pending')"%(Request_id,details,amount)
			insert(q)
			return redirect(url_for('caregiver.caregiver_viewrequest'))
		
		return render_template('cargiver_extrawork.html',data=data)
	else:
		return redirect(url_for('public.login'))



@caregiver.route('/chat',methods=['get','post'])
def chat():
	data={}
	slid=request.args['slid']
	if 'submit' in request.form:
		message=request.form['message']
		h="insert into chat values(null,'%s',(select Login_id from user where User_id='%s'),'%s',curdate())"%(session['Login_id'],slid,message)
		insert(h)
		return redirect(url_for('caregiver.chat',slid=slid))
	gg="SELECT * FROM chat INNER JOIN login ON `login`.`Login_id`=`chat`.`Sender_id` where `Sender_id`='%s' AND `Receiver_id`=(select Login_id from user where User_id='%s') or (`Sender_id`=(select Login_id from user where User_id='%s') AND `Receiver_id`='%s' )"%(session['Login_id'],slid,slid,session['Login_id'])
	print(gg)
	data['view']=select(gg)
	return render_template('chat.html',data=data,slid=slid)


