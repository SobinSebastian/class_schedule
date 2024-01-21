from flask import *
from database import *
import uuid
admin=Blueprint('admin',__name__)
 

@admin.route('/adminhome',methods=['get','post'])
def adminhome():
	return render_template('adminhome.html')



@admin.route('/admin_manage_dept',methods=['get','post'])
def admin_manage_dept():
	data={}
	if 'submit' in request.form:
		dept=request.form['dept']
		des=request.form['des']
		q="select * from departments where department_name='%s'"%(dept)
		res=select(q)
		if res:
			flash('THIS DEPARTMENT IS ALREADY ADDED')
			return redirect(url_for('admin.admin_manage_dept'))
		else:
			q="insert into departments values(NULL,'%s','%s')"%(dept,des)
			lid=insert(q)
			flash('ADDED SUCCESSULLY')
			return redirect(url_for('admin.admin_manage_dept'))

	q="select * from departments"
	res=select(q)
	if res:
		data['dept']=res
		print(res)

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:

		action=None
	if action=='delete':
		q="delete from departments where department_id='%s'"%(id)
		delete(q)
		flash('DELETED SUCCESSULLY')
		return redirect(url_for('admin.admin_manage_dept'))
	if action=='update':
		q="select * from departments where department_id='%s'"%(id)
		data['updater']=select(q)
	if 'update' in request.form:
		dept=request.form['dept']
		des=request.form['des']
		q="update departments set department_name='%s',department_description='%s' where department_id='%s'"%(dept,des,id)
		update(q)
		flash('UPDATED SUCCESSULLY')
		return redirect(url_for('admin.admin_manage_dept'))
	return render_template('admin_manage_dept.html',data=data)



@admin.route('/admin_manage_course',methods=['get','post'])
def admin_manage_course():
	data={}
	did=request.args['did']
	data['did']=did
	dept=request.args['dept']
	data['dept']=dept
	
	if 'submit' in request.form:
		c=request.form['c']
		d=request.form['d']
		des=request.form['des']
		q="select * from courses where course_name='%s' and department_id='%s'"%(c,did)
		res=select(q)
		if res:
			flash("ALREADY ADDED THIS COURSE")
			return redirect(url_for('admin.admin_manage_course',did=did,dept=dept))
		else:
			q="insert into courses values(NULL,'%s','%s','%s','%s')"%(did,c,d,des)
			lid=insert(q)
			flash('ADDED SUCCESSULLY')
			return redirect(url_for('admin.admin_manage_course',did=did,dept=dept))

	q="select * from courses where department_id='%s'"%(did)
	res=select(q)
	if res:
		data['courses']=res
		print(res)

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:

		action=None
	if action=='delete':
		q="delete from courses where course_id='%s'"%(id)
		delete(q)
		flash('DELETED SUCCESSULLY')
		return redirect(url_for('admin.admin_manage_course',did=did,dept=dept))
	if action=='update':
		q="select * from courses where course_id='%s'"%(id)
		data['updater']=select(q)
	if 'update' in request.form:
		c=request.form['c']
		d=request.form['d']
		des=request.form['des']
		q="update courses set course_name='%s',duration='%s',description='%s' where course_id='%s'"%(c,d,des,id)
		update(q)
		flash('UPDATED SUCCESSULLY')
		return redirect(url_for('admin.admin_manage_course',did=did,dept=dept))
	return render_template('admin_manage_course.html',data=data)


@admin.route('/admin_manage_subject',methods=['get','post'])
def admin_manage_subject():
	data={}
	cid=request.args['cid']
	data['cid']=cid
	cname=request.args['cname']
	data['cname']=cname
	
	if 'submit' in request.form:
		s=request.form['s']
		th=request.form['th']
		des=request.form['des']
		
		q="insert into subjects values(NULL,'%s','%s','%s','%s')"%(cid,s,th,des)
		lid=insert(q)
		flash('ADDED SUCCESSULLY')
		return redirect(url_for('admin.admin_manage_subject',cid=cid,cname=cname))

	q="select * from subjects where course_id='%s'"%(cid)
	res=select(q)
	if res:
		data['subjects']=res
		print(res)

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:

		action=None
	if action=='delete':
		q="delete from subjects where subject_id='%s'"%(id)
		delete(q)
		flash('DELETED SUCCESSULLY')
		return redirect(url_for('admin.admin_manage_subject',cid=cid,cname=cname))
	if action=='update':
		q="select * from subjects where subject_id='%s'"%(id)
		data['updater']=select(q)
	if 'update' in request.form:
		s=request.form['s']
		th=request.form['th']
		des=request.form['des']
		q="update subjects set subject_name='%s',total_hours='%s',subject_description='%s' where subject_id='%s'"%(s,th,des,id)
		update(q)
		flash('UPDATED SUCCESSULLY')
		return redirect(url_for('admin.admin_manage_subject',cid=cid,cname=cname))
	return render_template('admin_manage_subject.html',data=data)




@admin.route('/admin_manage_aca_calender',methods=['get','post'])
def admin_manage_aca_calender():
	data={}
	
	if 'submit' in request.form:
		date=request.form['date']
		title=request.form['title']
		des=request.form['des']
	
		q="insert into calender values(NULL,'%s','%s','%s')"%(date,title,des)
		lid=insert(q)
		flash('ADDED SUCCESSULLY')
		return redirect(url_for('admin.admin_manage_aca_calender'))

	q="select * from calender"
	res=select(q)
	if res:
		data['calender']=res
		print(res)

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:

		action=None
	if action=='delete':
		q="delete from calender where calender_id='%s'"%(id)
		delete(q)
		return redirect(url_for('admin.admin_manage_aca_calender'))
	if action=='update':
		q="select * from calender where calender_id='%s'"%(id)
		data['updater']=select(q)
	if 'update' in request.form:
		date=request.form['date']
		title=request.form['title']
		des=request.form['des']
		q="update calender set date='%s',title='%s',description='%s' where calender_id='%s'"%(date,title,des,id)
		update(q)
		return redirect(url_for('admin.admin_manage_aca_calender'))
	return render_template('admin_manage_aca_calender.html',data=data)



@admin.route('/admin_manage_teachers',methods=['get','post'])
def admin_manage_teachers():
	data={}
	q="select * from departments inner join courses using(department_id) inner join subjects using(course_id)"
	print(q)
	res=select(q)
	data['details']=res	
	print(res)
	return render_template('admin_manage_teachers.html',data=data)



@admin.route('/admin_manage_teachersub',methods=['get','post'])
def admin_manage_teachersub():
	data={}
	dept=request.args['dept']
	data['dept']=dept
	subject_id=request.args['subject_id']
	data['subject_id']=subject_id
	subname=request.args['subname']
	data['subname']=subname


	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		phone=request.form['phone']
		email=request.form['email']
		qua=request.form['qua']
		uname=request.form['uname']
		password=request.form['password']
		q="select * from login where username='%s'"%(uname)
		res=select(q)
		if res:
			flash("USERNAME ALREADY TAKEN BY ANOTHER USER")
			return redirect(url_for('admin.admin_manage_teachersub',dept=dept,subject_id=subject_id,subname=subname))
		else:

			q="insert into login values(NULL,'%s','%s','teacher')"%(uname,password)
			lid=insert(q)
			q="insert into teachers values(NULL,'%s','%s','%s','%s','%s','%s','%s','%s')"%(lid,dept,subject_id,fname,lname,phone,email,qua)
			print(q)
			insert(q)
			flash('REGISTRATION SUCCESS')
			return redirect(url_for('admin.admin_manage_teachersub',dept=dept,subject_id=subject_id,subname=subname))
	q="select * from teachers where subject_id='%s'"%(subject_id)
	res=select(q)
	if res:
		data['teacher']=res
		print(res)
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=='delete':
		q="delete from teachers where teacher_id='%s'"%(id)
		delete(q)
		flash('DELETED SUCCESSULLY')
		return redirect(url_for('admin.admin_manage_teachersub',dept=dept,subject_id=subject_id,subname=subname))
	if action=='update':
		q="select * from teachers where teacher_id='%s'"%(id)
		data['updater']=select(q)
	if 'update' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		phone=request.form['phone']
		email=request.form['email']
		qua=request.form['qua']
		
		q="update teachers set first_name='%s',last_name='%s',phone='%s',email='%s',qualification='%s' where teacher_id='%s'"%(fname,lname,phone,email,qua,id)
		update(q)
		flash('UPDATED SUCCESSULLY')
		return redirect(url_for('admin.admin_manage_teachersub',dept=dept,subject_id=subject_id,subname=subname))
	return render_template('admin_manage_teachersub.html',data=data)




@admin.route('/admin_manage_students',methods=['get','post'])
def admin_manage_students():
	data={}
	q="select * from courses "
	res=select(q)
	data['courses']=res
	if 'submit' in request.form:
		course_id=request.form['course_id']
		fname=request.form['fname']
		lname=request.form['lname']
		hname=request.form['hname']
		place=request.form['place']
		pin=request.form['pin']
		ph=request.form['phone']
		email=request.form['email']
		gen=request.form['gen']	
		dob=request.form['date']
		uname=request.form['uname']
		password=request.form['password']
		q="select * from login where username='%s'"%(uname)
		res=select(q)
		if res:
			flash("USERNAME ALREADY TAKEN BY ANOTHER USER")
			return redirect(url_for('admin.admin_manage_students'))
		else:
			q="insert into login values(NULL,'%s','%s','student')"%(uname,password)
			lid=insert(q)
			q="insert into students values(NULL,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(lid,course_id,fname,lname,hname,place,pin,ph,email,gen,dob)
			print(q)
			insert(q)
			flash('REGISTRATION SUCCESSULL')
			return redirect(url_for('admin.admin_manage_students'))
	q="select * from students inner join courses using(course_id) inner join login using(login_id)"
	res=select(q)
	if res:
		data['student']=res
		print(res)
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=='delete':
		q="delete from students where login_id='%s'"%(id)
		delete(q)
		flash('DELETED SUCCESSULLY')
		return redirect(url_for('admin.admin_manage_students'))
	if action=='update':
		q="select * from students where login_id='%s'"%(id)
		data['updater']=select(q)
	if 'update' in request.form:
		course_id=request.form['course_id']
		fname=request.form['fname']
		lname=request.form['lname']
		hname=request.form['hname']
		place=request.form['place']
		pin=request.form['pin']
		ph=request.form['phone']
		email=request.form['email']
		gen=request.form['gen']	
		dob=request.form['date']
		q="update students set first_name='%s',last_name='%s',house_name='%s',place='%s',pincode='%s',phone='%s',email='%s',dob='%s',gender='%s',dob='%s' where login_id='%s'"%(course_id,fname,lname,hname,place,pin,ph,email,gen,dob,id)
		update(q)
		flash('UPDATED SUCCESSULLY')
		return redirect(url_for('admin.admin_manage_students'))
	return render_template('admin_manage_students.html',data=data)




@admin.route('/admin_generate_shedule',methods=['get','post'])
def admin_generate_shedule():

	data={}
	q="select * from departments inner join courses using(department_id)"
	print(q)
	res=select(q)
	data['details']=res	
	print(res)
	
	return render_template('admin_generate_shedule.html',data=data)



@admin.route('/admin_generate_shedulesub',methods=['get','post'])
def admin_generate_shedulesub():
	data={}
	cid=request.args['cid']
	cname=request.args['cname']
	data['cid']=cid
	data['cname']=cname
	q="select * from subjects where course_id='%s'"%(cid)
	res=select(q)
	data['subjects']=res
	q="select * from teachers"
	res=select(q)
	data['t']=res

	if 'submit' in request.form:
		subject_id=request.form['subject_id']
		data['subject_id']=subject_id
		q="select * from teachers where subject_id='%s'"%(subject_id)
		res=select(q)
		data['teacher']=select(q)

	if 'add' in request.form:
		teacher_id=request.form['teacher_id']
		date=request.form['date']
		stime=request.form['stime']
		etime=request.form['etime']
		subject_id=request.form['subject_id']
		# q="select * from schedule where and date='%s' and starting_hour BETWEEN '%s' AND '%s' and course_id in(select subject_id from subjects where course_id='%s')("%(subject_id,date,stime,etime,cid)
		# print(q)
		
		q="SELECT * FROM SCHEDULE WHERE DATE='%s' AND ((starting_hour BETWEEN '%s' AND '%s') OR (starting_hour='%s') OR (ending_hour BETWEEN '%s' AND '%s')) AND subject_id IN(SELECT subject_id FROM subjects WHERE course_id='%s')"%(date,stime,etime,stime,stime,etime,cid)
		print(q)
		res=select(q)
		print(res)
		if res:
			flash('ALREADY SECHEDULED IN THIS PERIOD')
			return redirect(url_for('admin.admin_generate_shedulesub',cid=cid,cname=cname))
		else:
			print("^^^^^^^^^^^^")
			q="insert into schedule values(NULL,'%s','%s','%s','%s','%s','pending','pending')"%(subject_id,date,stime,etime,teacher_id)
			lid=insert(q)
			return redirect(url_for('admin.admin_generate_shedulesub',cid=cid,cname=cname))

	q="SELECT * FROM `schedule` INNER JOIN subjects USING(subject_id) INNER JOIN teachers USING(teacher_id)  WHERE `schedule`.subject_id IN(SELECT subject_id FROM subjects WHERE course_id='%s')"%(cid)
	print(q)
	res=select(q)
	if res:
		data['shedule']=res
		print(res)
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=='delete':
		q="delete from schedule where schedule_id='%s'"%(id)
		delete(q)
		return redirect(url_for('admin.admin_generate_shedulesub',cid=cid,cname=cname))
	# if action=='update':
	# 	q="select * from category where category_id='%s'"%(id)
	# 	data['updater']=select(q)
	# if 'update' in request.form:
	# 	cat=request.form['cat']
	# 	q="update category set category='%s' where category_id='%s'"%(cat,id)
	# 	update(q)
	# 	return redirect(url_for('admin.admin_generate_shedulesub'))
	return render_template('admin_generate_shedulesub.html',data=data)



@admin.route('/admin_view_user',methods=['get','post'])
def admin_view_user():
	data={}
	q="select * from customer"
	res=select(q)
	data['users']=res
	print(res)
	return render_template('admin_view_user.html',data=data)



@admin.route('/admin_view_shedule',methods=['get','post'])
def admin_view_shedule():
	data={}
	cid=request.args['cid']
	cname=request.args['cname']
	data['cid']=cid
	data['cname']=cname
	q="select * from subjects where course_id='%s'"%(cid)
	res=select(q)
	data['subjects']=res
	q="select * from teachers"
	res=select(q)
	data['t']=res


	q="SELECT * FROM `schedule` INNER JOIN subjects USING(subject_id) INNER JOIN teachers USING(teacher_id)  WHERE `schedule`.subject_id IN(SELECT subject_id FROM subjects WHERE course_id='%s')"%(cid)
	print(q)
	res=select(q)
	if res:
		data['shedule']=res
		print(res)
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=='cp':
		q="select * from classupdates where schedule_id='%s'"%(id)
		res=select(q)
		data['updater']=res
		

	return render_template('admin_view_shedule.html',data=data)



# @admin.route('/admin_view_user',methods=['get','post'])
# def admin_view_user():
# 	data={}
# 	q="select * from customer"
# 	res=select(q)
# 	data['users']=res
# 	print(res)
# 	return render_template('admin_view_user.html',data=data)



# @admin.route('/admin_view_bookings',methods=['get','post'])
# def admin_view_bookings():
# 	data={}
# 	q="SELECT *,`order_details`.`quantity` AS oquantity FROM `order_details` INNER JOIN order_master USING(omaster_id)INNER JOIN users USING(user_id) INNER JOIN products USING(product_id) WHERE `order_master`.`status`='ordered'"
# 	res=select(q)
# 	print(res)
# 	data['orders']=res
# 	return render_template("admin_view_bookings.html",data=data)

# @admin.route('/admin_manage_branches',methods=['get','post'])
# def admin_manage_branches():
# 	data={}
# 	if 'submit' in request.form:
# 		bname=request.form['bname']
# 		lat=request.form['lat']
# 		lon=request.form['lon']
# 		ph=request.form['phone']
# 		email=request.form['email']
# 		uname=request.form['uname']
# 		password=request.form['password']
# 		q="select * from login where username='%s' and password='%s'"%(uname,password)
# 		res=select(q)
# 		if res:
# 			flash('THIS USER NAME AND PASSWORD ALREADY TAKEN BY ANOTHER USER')
# 			return redirect(url_for('admin.admin_manage_branches'))
# 		else:
# 			q="insert into login values('%s','%s','branch')"%(uname,password)
# 			lid=insert(q)
# 			q="select * from branches order by branch_id desc limit 1"
# 			res=select(q)
# 			if res:
# 				prebid=res[0]['branch_id'].split("__")
# 				print(prebid)
# 				bid=int(prebid[1])+1
# 				bid="B__"+str(bid)
# 				print(bid)
# 			else:
# 				bid="B__1"
# 			q="insert into branches values('%s','%s','%s','%s','%s','%s','%s')"%(bid,uname,bname,lat,lon,ph,email,)
# 			insert(q)
# 			return redirect(url_for('admin.admin_manage_branches'))
# 	q="select * from branches"
# 	res=select(q)
# 	if res:
# 		data['branch']=res
# 		print(res)
# 	if 'action' in request.args:
# 		action=request.args['action']
# 		id=request.args['id']
# 	else:
# 		action=None
# 	if action=='delete':
# 		q="delete from branches where branch_id='%s'"%(id)
# 		delete(q)
# 		return redirect(url_for('admin.admin_manage_branches'))
# 	if action=='update':
# 		q="select * from branches where branch_id='%s'"%(id)
# 		data['updater']=select(q)
# 	if 'update' in request.form:
# 		bname=request.form['bname']
# 		lat=request.form['lat']
# 		lon=request.form['lon']
# 		ph=request.form['phone']
# 		email=request.form['email']
# 		q="update branches set branch_name='%s',latitude='%s',longitude='%s',phone='%s',email='%s' where branch_id='%s'"%(bname,lat,lon,ph,email,id)
# 		update(q)
# 		return redirect(url_for('admin.admin_manage_branches'))
# 	return render_template('admin_manage_branches.html',data=data)



# @admin.route('/admin_view_feedback',methods=['get','post'])
# def admin_view_feedback():
# 	data={}
# 	q="SELECT * FROM feedback INNER JOIN branches using(branch_id) inner join admins using(admin_id)"
# 	res=select(q)
# 	data['feedbacks']=res
# 	print(res)
# 	if 'action' in request.args:
# 		action=request.args['action']
# 		id=request.args['id']
# 		if action=="update":
# 			q="select * from feedback inner join admins using(admin_id) where feedback_id='%s' "%(id)
# 			res=select(q)
# 			data['updater']=res
# 	if 'update' in request.form:
# 		reply=request.form['reply']
# 		q="update feedback set reply='%s' where feedback_id='%s'"%(reply,id)
# 		update(q)
# 		return redirect(url_for('admin.admin_view_feedback'))
# 	return render_template('admin_view_feedback.html',data=data)


# @admin.route('/admin_review_andrate',methods=['get','post'])
# def admin_review_andrate():
# 	data={}
# 	q="select * from review_rating inner join branches using(branch_id) inner join customers using(customer_id)"
# 	res=select(q)
# 	print(res)
# 	data['rating']=res
# 	print(res)
# 	# q="select * from feedback inner join branches using(branch_id) where admin_id='%s'"%(cid)	
# 	# res=select(q)
# 	# data['fb']=res
# 	# print(res)
# 	return render_template('admin_review_andrate.html',data=data)


# @admin.route('/admin_view_complaints',methods=['get','post'])
# def admin_view_complaints():
# 	data={}
# 	q="SELECT * FROM user INNER JOIN complaint USING(user_id)"
# 	res=select(q)
# 	data['complaints']=res
# 	if 'action' in request.args:
# 		action=request.args['action']
# 		id=request.args['id']
# 		if action=="update":
# 			q="select * from complaint inner join user using(user_id) where complaint_id='%s' "%(id)
# 			res=select(q)
# 			data['updater']=res
# 	if 'update' in request.form:
# 		reply=request.form['reply']
# 		q="update complaint set reply='%s' where complaint_id='%s'"%(reply,id)
# 		update(q)
# 		return redirect(url_for('admin.admin_view_complaints'))
# 	return render_template('admin_view_complaints.html',data=data)

