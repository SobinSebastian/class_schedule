from flask import *
from database import *

import demjson
import uuid


api=Blueprint('api',__name__)

@api.route('/login',methods=['get','post'])
def login():
	data={}
	
	username = request.args['username']
	password = request.args['password']
	q="SELECT * from login where username='%s' and password='%s'" % (username,password)
	res = select(q)
	if res :
		data['status']  = 'success'
		data['data'] = res
		data['method']='login'
	else:
		data['status']	= 'failed'
		data['method']='login'
	return  demjson.encode(data)


@api.route('/User_view_department',methods=['get','post'])
def User_view_department():
	data={}
	data['method']='User_view_department'
 
	login_id=request.args['login_id']
 
	q="SELECT * FROM `departments` INNER JOIN `courses` USING(`department_id`) INNER JOIN `students` USING(`course_id`) WHERE `login_id`='%s'"%(login_id)
	print(q)
	res=select(q)
	if res:
		data['status']='success'
		data['data']=res
	else:
		data['status']='failed'
	return demjson.encode(data)

@api.route('/User_view_Subjects',methods=['get','post'])
def User_view_Subjects():
	data={}
	data['method']='User_view_Subjects'
	course_ids=request.args['course_ids']
 
	q="SELECT * FROM `subjects` WHERE `course_id`='%s'"%(course_ids)
	res=select(q)
	if res:
		data['status']='success'
		data['data']=res
	else:
		data['status']='failed'
	return demjson.encode(data)




@api.route('/User_view_time_table',methods=['get','post'])
def User_view_time_table():
	data = {}

	subject_ids=request.args['subject_ids']
	
	q="SELECT * FROM `schedule` INNER JOIN `teachers` USING (`teacher_id`) WHERE `schedule`.`subject_id`='%s'  ORDER BY `schedule_id` DESC"%(subject_ids)
	print(q)
	result=select(q)
	if result:
		data['status'] = 'success'
		data['data'] = result
		
	else:
		data['status'] = 'failed'
	data['method'] = 'User_view_time_table'
	return demjson.encode(data)



@api.route('/User_view_post',methods=['get','post'])
def User_view_post():
	data={}

	subject_ids=request.args['subject_ids']
	
	q="SELECT * FROM `post_notes`  INNER JOIN `subjects` USING(`subject_id`) WHERE `subject_id`='%s'"%(subject_ids)
	res = select(q)
	if res :
		data['status']  = 'success'
		data['data'] = res
	else:
		data['status']	= 'failed'
	data['method']='User_view_post'
	return  demjson.encode(data)


@api.route('/User_post_doubt',methods=['get','post'])
def User_post_doubt():

    data = {}

    complaints=request.args['complaints']
    subject_id=request.args['subject_id']
    loginid=request.args['loginid']


    qr="INSERT INTO `doubts` VALUES(NULL,(SELECT `student_id`FROM `students` WHERE `login_id`='%s'),'%s','%s','Pending')"%(loginid,subject_id,complaints)
    print(qr)
    id=insert(qr)
    if id>0:
        data['status'] = 'success'  
    else:
        data['status'] = 'failed'
    data['method']='User_post_doubt'
    return demjson.encode(data)

@api.route('/User_view_post_doubt',methods=['get','post'])
def User_view_post_doubt():
	data={}

	subject_id=request.args['subject_id']
	loginid=request.args['loginid']
	
	q="SELECT * FROM `doubts` WHERE `student_id`=(SELECT `student_id` FROM `students` WHERE `login_id`='%s') AND `subject_id`='%s'"%(loginid,subject_id)
	res = select(q)
	if res :
		data['status']  = 'success'
		data['data'] = res
	else:
		data['status']	= 'failed'
	data['method']='User_view_post_doubt'
	return  demjson.encode(data)




@api.route('/User_view_calendar',methods=['get','post'])
def User_view_calendar():
	data={}
	
 
	q="SELECT * FROM `calender`"
	res=select(q)
	if res:
		data['status'] = 'success'
		data['data'] = res
	else:
		data['status'] = 'failed'
		data['method']='User_view_calendar'
	return demjson.encode(data)