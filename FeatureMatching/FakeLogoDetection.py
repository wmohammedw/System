from PIL import Image  # fs
from PyQt5.QtCore import *  # fs
import os  # fs
import cv2  # omran
import numpy as np  # Basheer


class FakeLogoDetection:

    '''
        this is not the final version. we may add new methods if we need it. 
    '''

    def __init__(self):

        # Preparing the FLANN Based matcher
        self.index_params = dict(algorithm=1, trees=3)
        self.search_params = dict(checks=100)
        self.flann = cv2.FlannBasedMatcher(
            self.index_params, self.search_params)

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
        '''
            Comment on 31-March-22 !

            Good work. However, the code below is applicable only for real time detection. So, i need to add 
            if statement and write similar code with small modification for comparing between
            two images. (initialize the variable in init method) see the following video 
            (https://www.youtube.com/watch?v=Fe-KWKPk9Zc)

            the second thing, return the image itself with the kp and des.

            the third thing, i think you can read the image in RGB insted of Grayscale

        '''

        img = cv2.imread(path)
        orb = cv2.ORB_create()
        kp, des = orb.detectAndCompute(img, None)
        return img, kp, des
        '''
            here you will write a code to load an image from the database (Folder).
            Also, you will fine the descriptors and keypoints for the laded image and return them.

            you can add as many parameters as you want.
        '''

    def compute_matches(self, descriptors_output, descriptors_input, k_value = 2, n_coef = 0.68):  # basheer
        '''
            Comment on 31-March-22 !

            Good work. However, the code below is applicable only for real time detection. So, i need to
            add if statement for comparing two images. you can see the video here 
            (https://www.youtube.com/watch?v=Fe-KWKPk9Zc) for brute force algorithm (if the code below
            is applicable for comparing two images just write a comment below)


            *Sloved 1-April-22*
            IMPORTANT NOTE:
            Plese use the variables that initialize it in the constructor. Also, do not forget self.
            further, you can make the k, and 0.68 as parameters in this method. Therefour, i can 
            optimaize it later. For now, put k=2, 0.68 as defulat value for the parameters.
            *Sloved 1-April-22*

        '''

        # Function for Computing Matches between the train and query descriptors
        if(len(descriptors_output) != 0 and len(descriptors_input) != 0):
            matches = self.flann.knnMatch(np.asarray(
                descriptors_input, np.float32), np.asarray(descriptors_output, np.float32), k=k_value)
            good = []
            for m, n in matches:
                if m.distance <n_coef*n.distance:
                    good.append([m])
                    return good
                else:
                    return None

    def input_image(self):  # fsfs
        '''
            Comment on 31-March-22 !

            1- delete global filepath
            2- use OpenCV to read images (we need to use one library for reading images to 
            prevent the conflicts)
            3- add the path variable as parameter in this method

        '''

        '''
            here you will write a code to let the user upload an image from his/her computer.
        '''
        # Here is the Temporary code until GUI is ready, you must enter the file path by yourself.
        global filepath
        # The path must be seperated by "/"
        filepath = input("Enter file path")

        print("the file is:\n", filepath)

        im = Image.open(filepath)
        im.show()  # It will show you the image in Microsoft Photos "Or the deafult Image Viewer in your device"

        # The below code is not ready 100%, it will be modified once the GUI is uploaded.

        # def getfile(self):
        #filepath = QFileDialog.getOpenFileName(self, 'Open file', '',"Image files (*.jpg)")
        # self.le.setPixmap(QPixmap(filepath))

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

    def show_text(self, img, match_percent):  # omran
        '''
            Comment on 31-March-22 !

            plese add the configration for the text like, color, location of the text, and ect. Also,
            make the threshold (0.85) as parameter in the method. 

            the second thing, check if the below code is applicable in real-time and when comparing 
            two images.
        '''
        THRESHOLD = 0.85
        org = (50, 75)
        fontScale = 2
        c = (0,0,255)
        thickness = 4
        font = cv2.FONT_ITALIC
        
        if(match_percent >= THRESHOLD):
            new_img = cv2.putText(img=img, text='Real', org=org, color=c, fontFace=font, fontScale=fontScale,thickness=thickness)
        else:
            new_img = cv2.putText(img=img, text='Real', org=org, color=c, fontFace=font, fontScale=fontScale,thickness=thickness)
        
        return new_img
