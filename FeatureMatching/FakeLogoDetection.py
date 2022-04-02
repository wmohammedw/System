from PIL import Image  # fs
from PyQt5.QtCore import *  # fs "I don't think this is the library that we will use for GUI /Basheer"
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
        kp, des = orb.detectAndCompute(img, None) # Here it should be between 2 images (you only extraxted kp & des for 1) /Basheer
        return img, kp, des
        '''
            here you will write a code to load an image from the database (Folder).
            Also, you will fine the descriptors and keypoints for the laded image and return them.

            you can add as many parameters as you want.
        '''

    def compute_matches(self, des_frame, des_image1, des_image2, k_value = 2, n_coef = 0.68, choice = True):  # basheer
        '''
            Comment on 31-March-22 !
            *Solved 2-April-22*
            Good work. However, the code below is applicable only for real time detection. So, i need to
            add if statement for comparing two images. you can see the video here 
            (https://www.youtube.com/watch?v=Fe-KWKPk9Zc) for brute force algorithm (if the code below
            is applicable for comparing two images just write a comment below)
            *Solved 2-April-22*

            *Sloved 1-April-22*
            IMPORTANT NOTE:
            Plese use the variables that initialize it in the constructor. Also, do not forget self.
            further, you can make the k, and 0.68 as parameters in this method. Therefour, i can 
            optimaize it later. For now, put k=2, 0.68 as defulat value for the parameters.
            *Sloved 1-April-22*

        '''
        # If the user chose (Open Camera) choice will be True otherwise it will set to False
        if (choice):
        # Function for Computing Matches between the train and query descriptors
            if(len(des_frame) != 0 and len(des_image1) != 0):
                matches = self.flann.knnMatch(np.asarray(
                    des_image1, np.float32), np.asarray(des_frame, np.float32), k=k_value)
                good = []
                for m, n in matches:
                    if m.distance <n_coef*n.distance:
                        good.append([m])
                        return good
                    else:
                        return None
            else:
                # There are no descriptor
                pass
        else:
            # Image-to-Image matching using Brute-Force
            bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
            matches = bf.match(des_image1, des_image2)
            matches = sorted(matches, key = lambda x:x.distance)
            
            return matches
        
        # Drawing Matches
        # matching_result = cv2.drawMatches(img1, kp1, img2, kp2, matches[:50], None, flags=2) /for image-to-image
        # cv2.drawMatchesKnn(input_image,input_keypoints,frame,output_keypoints,matches,None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)/ real-time

    
    def input_image(self):  # fsfs
        '''
            Comment on 31-March-22 !
            *Solved on 4/1/2022
            1- delete global filepath
            2- use OpenCV to read images (we need to use one library for reading images to 
            prevent the conflicts)
            3- add the path variable as parameter in this method

        '''

        '''
            here you will write a code to let the user upload an image from his/her computer.
        '''
        # Here is the Temporary code until GUI is ready, you must enter the file path by yourself.
        
        filepath = input("Enter file path:\n")

        image = cv2.imread(filepath) #Pass the path to cv2

        #print(image.shape) 
        cv2.imshow("Image", image)

        cv2.waitKey(0) 

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
