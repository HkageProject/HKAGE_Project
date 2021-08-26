students = ['demo']
scores = [60]
what_to_do = ''
from os import system

def antierror():
  pass

def clear():
  system('clear')

def add_student():
  student_name = input('Enter the name of the student: ')
  passed = 0
  score = 0
  while passed == 0:
    try:
      score = input('Enter score of student: ')
      score = float(score)
      passed = 1
    except:
      print('Error, Please enter a nuermal value for score.')
      print()
  students.append(student_name)
  scores.append(score)
  print(students)

def changestudentinfo():
  passed = 0
  while passed == 0:
    try:
      student_name = input('Please enter the name of the student: ')
      studentname = students.index(student_name)
      passed = 1
      passed_2 = 0
      while passed_2 == 0:
        try:
          score = input('Please enter the score of student: ')
          score = float(score)
          passed_2 = 1
        except:
          print('Please enter a number for score!')
    except:
      print('Student does not exist')
  print('Changing student info...')
  print(studentname)
  scores[studentname] = score
  print('Success!')

def viewstudent(_name, score):
  print('     - Student Info - ')
  print('Name of student: ' + _name)
  print('Score: ' + str(score))
  print('-------------------')

def view_student():
  brea = 0
  passed = 0
  while passed == 0:
    clear()
    name = input('Enter student name (enter exit to exit): ')
    try:
      student = students.index(name)
      student_score = scores[student]
      viewstudent(name, student_score) 
      input('Press enter to continue')  
    except:
      print('Invaild student name, enter exit to exit.')
      print()
      input('Press enter to continue')
      if name == 'exit':
        passed = 1
    if brea == 1:
      break        
    antierror()
  antierror()

def fetch_student_info():
  length = len(students)
  i = 0
  while i < length:
    name = students[i]
    score = scores[i]
    viewstudent(name, score)
    print()
    i += 1
  if length == 0:
    print('No data. Add a student!')
  input('Press Enter to perceed')

def delete_all_info():
  e = input('Press enter to confirm deleting, enter e to exit:')
  if e == '':
    students.clear()
    scores.clear()
    
def processinputs():
  clear()
  if what_to_do == '1':
    add_student()
  elif what_to_do == '2':
    changestudentinfo()
  elif what_to_do == '3':
    view_student()
  elif what_to_do == '4':
    fetch_student_info()
  elif what_to_do == '5':
    delete_all_info()
  else:
    print('Invaild command, please look at the instructions')


while True:
  clear()
  print('    - Student Info System -')
  print('Press 1 to add a student')
  print('Press 2 to change student info')
  print('Press 3 to view the info of a student')
  print('Press 4 to get infos of all students')
  print('Press 5 to delete all student info')
  what_to_do = input('Enter your Option: ')
  processinputs()
