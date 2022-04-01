from PyQt5.QtCore import * #fs
import os #fs
import cv2 #omran + fs

class FakeLogoDetection:

    '''
        this is not the final version. we may add new methods if we need it. 
    '''

    def __init__(self):
        '''
            You need to initilize the variables here before use them in the below methods.
            follow the OOP concepts.

            for example in load_image method:
                if you want to resize the image
                you will define the variable here
                img_size = 250

                and use it inside load_image method.
        '''
        pass

    def load_image(self, path):  # omran
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        orb = cv2.ORB_create()
        kp, des = orb.detectAndCompute(img, None)
        return kp, des
        '''
            here you will write a code to load an image from the database (Folder).
            Also, you will fine the descriptors and keypoints for the laded image and return them.

            you can add as many parameters as you want.
        '''

    def compute_matches(self):  # basheer
        '''
            here you will use either knn or brute force to compute the matching between images.
        '''
        pass

    def input_image(self)#, inputImage):  # fsfs
        '''
            here you will write a code to let the user upload an image from his/her computer.
        '''
        
        filepath = input("Enter file path:\n") #can be seperated by "\" or "/"

        image = cv2.imread(filepath) #Pass the path to cv2

        #print(image.shape) 
        cv2.imshow("Image", image)

        cv2.waitKey(0) 


        #The below code is not ready 100%, it will be modified once the GUI is uploaded.
        

        #def getfile(self):
            #filepath = QFileDialog.getOpenFileName(self, 'Open file', '',"Image files (*.jpg)")
            #self.le.setPixmap(QPixmap(filepath))


    def real_time_matching(self):  # mhm
        '''
            here you need to write a code to open the camera and start matching the image that we 
            have in the database and start matching.
        '''
        pass

    def image_to_image_matching(self):  # mhm
        '''
            in the previous method, we apply it in real time. Now, we need to compare or matching 
            between two images only.
        '''
        pass

    def show_text(self,img,match_percent):  # omran
        if(match_percent >= 0.85):
            cv2.putText(img, 'Real')
        else:
            cv2.putText(img, 'Fake')
        pass
