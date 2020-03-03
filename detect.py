
import cv2
import requests
import json

def detect_face(file_address):

    face_tokens = []
 
    url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
    files = {'image_file':open(file_address, 'rb')}
    payload = {'api_key': '3k5330OLIwDpiJJO3Npb1uqN-KQFPMnq',
               'api_secret': '_IAulzB2KhoT3d77wotVQc2MwOD_lm5i',
               'return_landmark': 0,
               'return_attributes':'gender,age,glass'}
     
    r = requests.post(url,files=files,data=payload)
    data=json.loads(r.text)
    print (r.text)

    face_count = data['face_num']

    for i in range(face_count):
        width = data['faces'][i]['face_rectangle']['width']
        top = data['faces'][i]['face_rectangle']['top']
        height = data['faces'][i]['face_rectangle']['height']
        left = data['faces'][i]['face_rectangle']['left']
        face_tokens.append(data['faces'][i]['face_token'])
        img = cv2.imread(file_address)
        vis = img.copy()
        cropImg = vis[top:top+height,left:left+width]
        imageName = "faceFind%d"%i
        cv2.imwrite('/home/pi/Desktop/Face/'+imageName+'.png', cropImg)

    return face_tokens    
    
cv2.waitKey (0)
