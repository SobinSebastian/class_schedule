from flask import *
from database import *
import uuid
teacher=Blueprint('teacher',__name__)
 

@teacher.route('/teacherhome',methods=['get','post'])
def teacherhome():
	tname=session['tname']
	tid=session['tid']

	return render_template('teacherhome.html',tname=tname)


@teacher.route('/teacher_view_tt',methods=['get','post'])
def teacher_view_tt():
	data={}
	tid=session['tid']
	q="select subject_id from teachers where teacher_id='%s'"%(tid)
	res=select(q)
	subject_id=res[0]['subject_id']

	q="SELECT * FROM `schedule` INNER JOIN subjects USING(subject_id)  WHERE  teacher_id='%s'"%(tid)
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

	if action=='a':
		q="update schedule set teacher_availability_status='available' where schedule_id='%s'"%(id)
		update(q)
		return redirect(url_for('teacher.teacher_view_tt'))
	if action=='na':
		q="update schedule set teacher_availability_status='notavailable' where schedule_id='%s'"%(id)
		update(q)
		return redirect(url_for('teacher.teacher_view_tt'))

	if action=='c':
		q="update schedule set schedule_status='conducted' where schedule_id='%s'"%(id)
		update(q)
		return redirect(url_for('teacher.teacher_view_tt'))

	if action=='cp':
		q="select * from classupdates where schedule_id='%s'"%(id)
		res=select(q)
		data['updater']=res
		data['upload']='hai'

	if 'submit' in request.form:
		portion=request.form['portion']	
		q="insert into classupdates values(NULL,'%s','%s','%s','%s')"%(id,tid,subject_id,portion)
		insert(q)
		return redirect(url_for('teacher.teacher_view_tt',action='cp',id=id))
		
	return render_template('teacher_view_tt.html',data=data)


@teacher.route('/teacher_view_oteacher',methods=['get','post'])
def teacher_view_oteacher():

	data={}
	tid=session['tid']
	q="select department_id from teachers where teacher_id='%s'"%(tid)
	res=select(q)
	department_id=res[0]['department_id']
	q="SELECT * FROM `schedule` INNER JOIN subjects USING(subject_id) INNER JOIN teachers USING(teacher_id)  WHERE  department_id='%s' and teacher_id!='%s' order by date desc"%(department_id,tid)
	print(q)
	res=select(q)
	if res:
		data['oteacher']=res
		print(res)

	return render_template('teacher_view_oteacher.html',data=data)




@teacher.route('/teacher_post',methods=['get','post'])
def teacher_post():

	data={}
	subject_id=request.args['subject_id']
	data['shid']=subject_id
	tid=session['tid']

	if 'submit' in request.form:		
		file=request.files['file']
		path='static/'+str(uuid.uuid4())+file.filename
		file.save(path)
		q="insert into post_notes values(NULL,'%s','%s','%s')"%(subject_id,tid,path)
		insert(q)
		return redirect(url_for('teacher.teacher_post',subject_id=subject_id))
	q="select * from post_notes where subject_id='%s'"%(subject_id)
	res=select(q)
	if res:
		data['notes']=res
		print(res)
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=='delete':
		q="delete from post_notes where note_id='%s'"%(id)
		delete(q)
		return redirect(url_for('teacher.teacher_post',subject_id=subject_id))
	# if action=='update':
	# 	q="select * from class where class_id='%s'"%(id)
	# 	data['updater']=select(q)
	# if 'update' in request.form:
	# 	clz=request.form['clz']
	# 	vid=request.files['vid']
	# 	path='static/'+str(uuid.uuid4())+vid.filename
	# 	vid.save(path)
	# 	q="update class set class='%s',video='%s' where class_id='%s'"%(clz,path,id)
	# 	print(q)
	# 	update(q)
	# 	return redirect(url_for('admin.teacher_post'))

	return render_template('teacher_post.html',data=data)


@teacher.route('/teacher_view_doubts',methods=['get','post'])
def teacher_view_doubts():
	data={}
	shid=request.args['shid']
	data['shid']=shid
	tid=session['tid']
	q="SELECT * FROM doubts INNER JOIN students USING(student_id) where subject_id='%s'"%(shid)
	res=select(q)
	data['doubt']=res
	print(res)
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		if action=="update":
			q="select * from  doubts INNER JOIN students USING(student_id) where doubt_id='%s'"%(id)
			res=select(q)
			data['updater']=res
	if 'update' in request.form:
		ans=request.form['ans']
		q="update doubts set answer='%s' where doubt_id='%s'"%(ans,id)
		update(q)
		return redirect(url_for('teacher.teacher_view_doubts',shid=shid))
	return render_template('teacher_view_doubts.html',data=data)


@teacher.route('/teacher_view_students',methods=['get','post'])
def teacher_view_students():
	data={}
	tid=session['tid']
	q="select course_id,course_name from teachers inner join subjects using(subject_id) inner join courses using(course_id) where teacher_id='%s'"%(tid)
	print(q)
	res=select(q)
	course_id=res[0]['course_id']
	data['course_name']=res[0]['course_name']
	q="select * from students where course_id='%s'"%(course_id)
	res=select(q)
	data['students']=res
	print(res)
	
	return render_template('teacher_view_students.html',data=data)