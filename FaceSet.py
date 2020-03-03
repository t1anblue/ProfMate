
#Face Set create

import cv2
import requests
import json
from detect import detect_face
from Camera import take_picture
 
def Create_FaceSet():

    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/create'

    payload = {'api_key': '3k5330OLIwDpiJJO3Npb1uqN-KQFPMnq',
               'api_secret': '_IAulzB2KhoT3d77wotVQc2MwOD_lm5i',
               'display_name': 'class4IO6',
               'outer_id':'12345678helloAi'}

    r = requests.post(url,data=payload)
    data = json.loads(r.text)
    print(r.text)

    outer_id = data['outer_id']
    return outer_id

def Set_Student_ID(face_token, user_id):

    url = 'https://api-cn.faceplusplus.com/facepp/v3/face/setuserid'
    payload = {'api_key': '3k5330OLIwDpiJJO3Npb1uqN-KQFPMnq',
               'api_secret': '_IAulzB2KhoT3d77wotVQc2MwOD_lm5i',
               'face_token': face_token,
               'user_id':user_id}

    r = requests.post(url,data=payload)
    data = json.loads(r.text)
    print(r.text)

    student_id_check = data['user_id']

    if(student_id_check == user_id):

        print("Set successful")
    else:
        print("Set Fail")

    return


def Add_Face(outer_id, face_token):

    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/addface'

    payload = {'api_key': '3k5330OLIwDpiJJO3Npb1uqN-KQFPMnq',
                'api_secret': '_IAulzB2KhoT3d77wotVQc2MwOD_lm5i',
                'outer_id':outer_id,
                'face_tokens': face_token}
    r = requests.post(url,data=payload)
    data = json.loads(r.text)
    print(r.text)

    return

def Search_Face(face_token, outer_id):

    url = 'https://api-cn.faceplusplus.com/facepp/v3/search'
    #files = {'image_file':open(file_address, 'rb')}
    payload = {'api_key': '3k5330OLIwDpiJJO3Npb1uqN-KQFPMnq',
               'api_secret': '_IAulzB2KhoT3d77wotVQc2MwOD_lm5i',
               'face_token': face_token,
               'outer_id': outer_id}
    
    r = requests.post(url ,data=payload)
    data=json.loads(r.text)
    print (r.text)

    confidence = data['results'][0]['confidence']
    student_id = data['results'][0]['user_id']

    return [student_id, confidence]


    
                   

    

    

    

