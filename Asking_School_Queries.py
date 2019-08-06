
print("HI")

while True:

	import mysql.connector
	import speech_recognition as sr    
	import time

	mydb = mysql.connector.connect(
  		host="127.0.0.1",
  		user="root",
  		passwd="pokemon2345",
  		database="school_py")

	mycursor = mydb.cursor()
	question_word = ''
	query =''

	while True:
		handled_query = ''
		action_word = ''
		ans_type = ''
		ans_table = ''
		prosQuery = ''

		#r = sr.Recognizer()                                                                                   
        #                     with sr.Microphone() as source:
        #                             print("Speak:")
        #                             audio = r.listen(source)  
		#try:
        #                             print("You said " + r.recognize_google(audio))
		#except sr.UnknownValueError:
    	#	        print("Could not understand audio")
		#except sr.RequestError as e:
    	#	        print("Could not request results; {0}".format(e))

		#query = r.recognize_google(audio)

		query = input("Query ......    ")

		if query == '/h' or query == '/help':
			print("Guildlines for writing a query : ")
			print("Start your sentence with a question word. The question wors are : ")
			print("			i) Who")
			print("			ii) How many")
			print("			iii) Which")
			print()
			continue

		handled_query = query.split(' ')

		new_query = []
		for x in handled_query:
			#print(x)
			if not(x == 'is' or x == 'and' or x == 'in' or x == 'the' or x == 'or' or x == 'of' or x == 'does' or x == 'are' or x == 'there' or x == 'all'):
				new_query.append(x)

		if new_query[0] == 'Which' or new_query[0] == 'In' or new_query[0] == 'which':
			question_word = 'In Which'
			action_word = new_query[2]
			#print(action_word)
			#print(question_word)
		elif new_query[0] == 'How' and new_query[1] == 'many':
			question_word = 'How many'
			#print(True)
			action_word = new_query[2]
			#print(action_word)
		elif new_query[0] == 'List':
			question_word = 'List'
			action_word = new_query[1]
		else:
			question_word = new_query[0]
			action_word= new_query[1]

		if question_word == 'Who':
			if action_word == 'teaches' or action_word == 'teacher':
				ans_table = 'teacher'
			elif action_word == 'studies':
				ans_table = 'student'
			elif action_word == 'class':
				#print(True)
				if new_query[2] == 'teacher':
					ans_table = 'section' #Class Teacher
					#print(True)
			elif action_word == 'Gardener' or action_word == 'Maid' or action_word == 'Watchman' or action_word == 'Head Support':
				ans_table = 'support_staff'
			#print(action_word)
			#print(ans_table)

			if question_word == 'Who' and ans_table == 'section':
				prosQuery2 = "SELECT s.grade_name, s.section_name, s.class_teacher_id FROM section s WHERE s.grade_name = '%s' AND s.section_name = '%s'" % (new_query[3], new_query[4])
				mycursor.execute(prosQuery2)
				myesult = mycursor.fetchall()
				x = myesult[0]
				prosQuery = "SELECT t.teacher_first_name, t.teacher_last_name, t.date_of_birth, t.teacher_id, t.teaching_subject, t.date_of_job_joining FROM teacher t WHERE t.teacher_id = '{}'".format(x[2])
			elif question_word == 'Who' and ans_table == 'teacher':
				x = new_query[-1]
				prosQuery= "SELECT t.teacher_first_name, t.teacher_last_name, t.date_of_birth, t.teacher_id, t.teaching_subject, t.date_of_job_joining FROM teacher t WHERE t.teaching_subject = '{}'".format(x)
			elif question_word == 'Who' and ans_table == 'student':
				z = len(new_query)
				if z == 4:
					x = new_query[-2]
					y = new_query[-1]
					prosQuery = "SELECT s.student_first_name, s.student_last_name, s.date_of_birth, s.admission_id, s.guardian, s.grade_name, s.section_name FROM student s WHERE s.grade_name = '{}' AND s.section_name = '{}'".format(x,y)
				elif z == 3 and len(new_query[-1]) == 1 and new_query[-1] != 'X' and new_query[-1] != 'I' and new_query[-1] != 'V':
					y = new_query[-1]
					prosQuery = "SELECT s.student_first_name, s.student_last_name, s.date_of_birth, s.admission_id, s.guardian, s.grade_name, s.section_name FROM student s WHERE s.section_name = '{}'".format(y)
				else:
					y = new_query[-1]
					prosQuery = "SELECT s.student_first_name, s.student_last_name, s.date_of_birth, s.admission_id, s.guardian, s.grade_name, s.section_name FROM student s WHERE s.grade_name = '{}'".format(y)
			elif ans_table == 'support_staff':
				prosQuery = "SELECT s.support_staff_first_name, s.support_staff_last_name, s.staff_id, s.date_of_birth, s.job, s.date_of_job_joining FROM support_staff s WHERE s.job = '{}'".format(action_word)
			elif action_word == 'boys' or action_word == 'girls':
				if action_word == 'boys':
					z = 'M'
				elif action_word == 'girls':
					z  = 'F'
				if len(new_query) == 4:
					x = new_query[-2]
					y = new_query[-1]
					prosQuery = "SELECT s.student_first_name, s.student_last_name, s.date_of_birth, s.admission_id, s.guardian, s.grade_name, s.section_name FROM student s WHERE s.grade_name = '{}' AND s.section_name = '{}' AND s.gender = '{}'".format(x,y,z)
				elif len(new_query) == 3 and len(new_query[-1]) ==1 and new_query[-1] != 'I'and new_query[-1] != 'V'and new_query[-1] != 'X':	
					x = new_query[-1]
					prosQuery = "SELECT s.student_first_name, s.student_last_name, s.date_of_birth, s.admission_id, s.guardian, s.grade_name, s.section_name FROM student s WHERE s.section_name = '{}' AND s.gender = '{}'".format(x,z)
				else:
					x = new_query[-1]
					prosQuery = "SELECT s.student_first_name, s.student_last_name, s.date_of_birth, s.admission_id, s.guardian, s.grade_name, s.section_name FROM student s WHERE s.grade_name = '{}' AND s.gender = '{}'".format(x,z)	
			mycursor.execute(prosQuery)
			try:
				myResult = mycursor.fetchall()
				print(myResult)
			except Exception:
				print("Invalid Query. Type /h or /help for more information")	

		elif question_word == 'In Which':
			if action_word == 'class':
				#print(True)
				prosQuery = "SELECT s.student_first_name, s.student_last_name, s.date_of_birth, s.admission_id, s.guardian, s.grade_name, s.section_name FROM student s WHERE s.student_first_name = '{}'".format(new_query[-2])
			mycursor.execute(prosQuery)
			myHalfResult = mycursor.fetchall()
			x = myHalfResult[0]
			myResult = []
			myResult.append(x[-2])
			myResult.append(x[-1])
			print(myResult)
			
		elif question_word == 'How many':
			#print(True)
			#print(action_word)
			if action_word == 'students':
				if len(new_query) == 5:
					#print('1st')
					x = new_query[-2]
					y = new_query[-1]
					prosQuery = "SELECT COUNT(s.admission_id) FROM student s WHERE s.grade_name = '{}' AND s.section_name = '{}'".format(x,y)
				elif len(new_query) == 4 and len(new_query[-1]) == 1 and new_query[-1] != 'V' and new_query[-1] != 'I' and new_query[-1] != 'X':
					x = new_query[-1]
					prosQuery = "SELECT COUNT(s.admission_id) FROM student s WHERE s.section_name = '{}'".format(x)
				else:
					x = new_query[-1]
					prosQuery = "SELECT COUNT(s.admission_id) FROM student s WHERE s.grade_name = '{}'".format(x)
			if action_word == 'teachers':
				#print(new_query[3])
				if new_query[3] == 'teaches' or new_query[3] == 'teach':
					#print(True)
					x = new_query[4]
					prosQuery= "SELECT COUNT(t.teacher_id) FROM teacher t WHERE t.teaching_subject = '{}'".format(x)
			try:
				mycursor.execute(prosQuery)
				myResult = mycursor.fetchall()
				print(myResult)
			except Exception:
				print('Invalid Query')

		elif question_word == 'List':
			if new_query[-1] != action_word:
				z = True
			else:
				z= False
			if action_word == 'students' and z == True:
				prosQuery = "SELECT * FROM student s"
				print(True)
			elif action_word == 'students' and z != True:
				print(True)
				prosQuery = "SELECT s.student_first_name, s.student_last_name FROM student s"
			if action_word == 'teachers' and z == True:
				prosQuery = "SELECT * FROM teacher t"
			elif action_word == 'teachers' and z != True:
				prosQuery = "SELECT s.teacher_first_name, s.teacher_last_name FROM teacher s"
			if action_word == 'support_staff' and z == True:
				prosQuery = "SELECT * FROM support_staff s"
			elif action_word == 'support_staff' and z != True:
				prosQuery = "SELECT s.support_staff_first_name, s.support_staff_last_name FROM support_staff s"
			if action_word == 'parents' and z == True:
				prosQuery = "SELECT * FROM parent p"
				#print('parents-')
			elif action_word == 'parents' and z != True:
				prosQuery = "SELECT p.parent_first_name, p.ward_admission_id FROM parent p"	
			try:
				mycursor.execute(prosQuery)
				myResult = mycursor.fetchall()
				print(myResult)
			except Exception:
				print("Invalid Query ")
