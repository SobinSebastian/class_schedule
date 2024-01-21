from flask import *
from database import *
public=Blueprint('public',__name__)

@public.route('/',methods=['get','post'])
def home():

	
	return render_template('home.html')

@public.route('/login',methods=['get','post'])
def login():
	if 'submit' in request.form:
		uname=request.form['uname']
		password=request.form['password']
		q="select * from login where username='%s' and password='%s'"%(uname,password)
		res=select(q)
		if res:
			session['lid']=res[0]['login_id']
			
			if res[0]['usertype']=='admin':
				return redirect(url_for('admin.adminhome'))

			if res[0]['usertype']=='teacher':
				q="select * from teachers where login_id='%s'"%(session['lid'])
				res=select(q)
				print(res)
				session['tid']=res[0]['teacher_id']
				session['tname']=res[0]['first_name']
				return redirect(url_for('teacher.teacherhome'))

		

			if res[0]['usertype']=='pending':
				flash("YOUR REQUEST STATUS ON PENDING")
				return redirect(url_for('public.login'))
				
		else:
			flash("COMPLETE REGISTRATION BEFORE TRY TO LOGIN")
	return render_template('login.html')

# @public.route('/customerreg',methods=['get','post'])
# def customerreg():
# 	data={}
# 	if 'submit' in request.form:
# 		print("^^^^^^^^^^^^^^^^^^^^^^^^")
# 		fname=request.form['fname']
# 		lname=request.form['lname']
# 		place=request.form['place']
# 		ph=request.form['phone']
# 		email=request.form['email']
# 		uname=request.form['uname']
# 		password=request.form['password']
# 		q="select * from login where username='%s'"%(uname)
# 		res=select(q)
# 		if res:
# 			flash('THIS USER NAME ALREADY TAKEN BY ANOTHER USER')
# 			return redirect(url_for('public.customerreg'))
# 		else:
# 			q="insert into login values('%s','%s','customer')"%(uname,password)
# 			insert(q)
# 			q="insert into customer values(NULL,'%s','%s','%s','%s','%s','%s')"%(uname,fname,lname,place,ph,email)
# 			insert(q)
# 			return redirect(url_for('public.customerreg'))
# 	return render_template('customerreg.html',data=data)


# @public.route('/customerreg',methods=['get','post'])
# def customerreg():
# 	data={}
# 	if 'submit' in request.form:
# 		fname=request.form['fname']
# 		lname=request.form['lname']
# 		ph=request.form['phone']
# 		email=request.form['email']
# 		lat=request.form['lat']
# 		lon=request.form['lon']
# 		uname=request.form['uname']
# 		password=request.form['password']
# 		q="select * from login where username='%s' and password='%s'"%(uname,password)
# 		res=select(q)
# 		if res:
# 			flash('THIS USER NAME AND PASSWORD ALREADY TAKEN BY ANOTHER USER')
# 			return redirect(url_for('public.customerreg'))
# 		else:
# 			q="insert into login values('%s','%s','customer')"%(uname,password)
# 			lid=insert(q)
# 			q="select * from customers order by customer_id desc limit 1"
# 			res=select(q)
# 			if res:
# 				s="c__"
# 				precid=res[0]['customer_id'].split("__")
# 				print(precid)
# 				cid=int(precid[1])+1
# 				cid="c__"+str(cid)
# 				print(cid)
# 			else:
# 				cid="c__1"
# 			q="insert into customers values('%s','%s','%s','%s','%s','%s','%s','%s')"%(cid,uname,fname,lname,ph,email,lat,lon)
# 			insert(q)
# 			return redirect(url_for('public.customerreg'))
# 	return render_template('customerreg.html',data=data)
