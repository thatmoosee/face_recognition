import cv2
import face_recognition
#import serial need this to communicate with the arduino i'd reccomend to look at a tutorial or documentation on how to use it and set it up as you need special variables
import time
known_face_encodings = []
known_face_names = []

//change the following code
known_person1_image = face_recognition.load_image_file("max.jpg")
known_person2_image = face_recognition.load_image_file("sam.jpg")
known_person3_image = face_recognition.load_image_file("clayton.jpg")
known_person4_image = face_recognition.load_image_file("kade.jpg")



known_person1_encoding = face_recognition.face_encodings(known_person1_image)[0]
known_person2_encoding = face_recognition.face_encodings(known_person2_image)[0]
known_person3_encoding = face_recognition.face_encodings(known_person3_image)[0]
known_person4_encoding = face_recognition.face_encodings(known_person4_image)[0]

known_face_encodings.append(known_person1_encoding)
known_face_encodings.append(known_person2_encoding)
known_face_encodings.append(known_person3_encoding)
known_face_encodings.append(known_person4_encoding)

known_face_names.append("Max")
known_face_names.append("Sam")
known_face_names.append("Clayton")
known_face_names.append("Kade") 

video_capture = cv2.VideoCapture(0)
#connecting to the arduino
#arduinoData=serial.Serial('com3',115200)
time.sleep(1)
while True:
    ret, frame = video_capture.read()
   

    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unkown"

        if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
            
        cv2.rectangle(frame,(left, top), (right,bottom), (0,0,255) ,2)
        cv2.putText(frame, name, (left,top - 10), cv2.FONT_HERSHEY_SIMPLEX, .9, (0,0,255), 2)
        #data = name +'\r'
        #arduinoData.write(data.encode()) sends data to arduino

    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): # press q in the window to exit
         break
    
video_capture.release()

cv2.destroyAllWindows

