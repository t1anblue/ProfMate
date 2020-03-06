import cv2
import requests
import json
import detect
import FaceSet
from picamera import PiCamera
import Camera
import time
import datetime
import database

class mainDisplayControl:
    
    def __init__ (self, lec_code, lec_time):
        self.lec_code = lec_code
        self.lec_time = lec_time

    def init_display(self): #read the lec code from server
    
        print("Welcome!\n")
        print("Hello from ProfMate\n")
        Lec_Name = self.lec_code
        print("Next Lec: " + Lec_Name + "\n")
        return

    def take_picture_display(self, camera):

        Camera.take_picture(camera) #take picture by camera module
        print('\nTaking Picture...\n')
        return

    def detect_face_dispaly(self):

        print('\nDetecting Faces...\n')
        face_tokens = detect.detect_face('/home/pi/Desktop/ProfMate/pic.jpg') #use api to check the picture
        
        print('\nFinished\n')
        num = len(face_tokens)
        print('\nFaces find: ' + str(num) + '\n')

        return face_tokens

    def show_result_display(self, num_show):

        print('Lec Code: ' + self.lec_code + '\n')
        print('Num showup: ' + str(num_show) + '\n')
        return

    def goodbye_display(self):

        print('\nLec ' + self.lec_code + ' is finished\n')
        print('\nGood Job Prof!\n')
        return

def face_match_single(face_tokens, outer_id):

    print('\nSearch Facese...\n')
    match_result_set = []
    num = len(face_tokens)

    for i in range(num):

        single_face = FaceSet.Search_Face(face_tokens[i], outer_id)
        match_result_set.append(single_face)

    print('Search Finished...')
    return match_result_set

def upload_results(match_result_set):

    num = len(match_result_set)
    for i in range (num):

        if(match_result_set[i][1] > 80):
            
            date = time.strftime("%Y-%m-%d", time.localtime())
            time = time.strftime("%H:%M:%S", time.localtime())
            student_id = match_result_set[i][0]                       
 #           database.insert_pool(student_id, date, time) #upload to database send student ID
    return

def get_attendance_count():

    #return count from db
  #  database.update_percentage()    
    return 


def attendance_controller(camera):

    outer_id = '12345678helloAi'
    #camera = PiCamera()
    print('The class is start!')
    
    #getLecCode()
    #getLecTime()
    lec_code = '4IO6' #get from database  send time to check current code
    lec_time = '9:30'
    task = mainDisplayControl(lec_code, lec_time)
    face_tokens_set = []
    task.init_display()
    time.sleep(3)
    for i in range (5): #take 5 pictures at the beginning of the class
        task.take_picture_display(camera)
        face_tokens_set.append(task.detect_face_dispaly())
        time.sleep(10)

    for j in range (5):
        match_result_set = face_match_single(face_tokens_set[j], outer_id)
        upload_results(match_result_set) #need data from database
        time.sleep(2)

    num_count = get_attendance_count()
    task.show_result_display(num_count)
    
    return



#######################################################################################
    
class studentControl:

    def __init__ (self, first_name, last_name, student_id, student_courses, outer_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = int(student_id)    
        self.student_courses = int(student_courses)
        self.outer_id = outer_id

    def addStudent(self, face_token):

        #UI input
        #Read Student information from .txt file
        
        #database part
        database.regist(self.student_id,self.last_name,self.first_name,self.student_courses)
        #Face++ part
        FaceSet.Set_Student_ID(face_token, self.student_id);
        FaceSet.Add_Face(self.outer_id, face_token);

        return

    def checkExist(self):

        #database part
        #database.check(student_id, first_name, last_name)


        return



def registration_controller():

    error = 0;
    outer_id = '12345678helloAi'
    f = open("/home/pi/Desktop/ProfMate/student_info.txt", mode='r')
    info = f.readlines()
    picture_addr = info[0].strip()
    first_name = info[1].strip()
    last_name = info[2].strip()
    student_id = int(info[3].strip())

    print(first_name)
    print(last_name)
    
    #if multiple, consider for loop
    student_courses = 101
    
    face_tokens = detect.detect_face(picture_addr)
    
    if(len(face_tokens) > 1):
        print("Invalid Picture: Multiple Face Detected")
        #terminate
        error = 1
        return error
    
    
    face_token = face_tokens[0]
    
    newStudent = studentControl(first_name, last_name, student_id, student_courses, outer_id)
    
    newStudent.addStudent(face_token) #Add Student to both Face++ and DB
    return
    

    

    
#######################################################################################

'''class profControl:

    def __init__ (self, first_name, last_name, prof_courses, outer_id):
        self.first_name = first_name
        self.last_name = last_name  
        self.prof_courses = prof_courses
        self.outer_id = outer_id
        
        
    def check_lec_attendance(course_id):
    
    
    
    def check_student_attendance(student_id):
    
    
    
def professor_controller():'''
