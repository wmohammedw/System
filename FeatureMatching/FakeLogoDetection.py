import os


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

    def load_image(self):  # omran
        '''
            here you will write a code to load an image from the database (Folder).
            Also, you will fine the descriptors and keypoints for the laded image and return them.

            you can add as many parameters as you want.
        '''
        pass

    def compute_matches(self):  # basheer
        '''
            here you will use either knn or brute force to compute the matching between images.
        '''
        pass

    def input_image(self):  # fsfs
        '''
            here you will write a code to let the user upload an image from his/her computer.
        '''
        #global picPath
        #picPath = askopenfilename()
        #picPath = os.path.abspath(filename)
        # 
        # #PicNamePath must be replaced with the entrybox GUI component
        # picNamePath.insert(1.0, picPath)

        ####Temp Code until GUI is Ready.
        picPath = input("Enter Picture Path")
        picPath = os.path.abspath(picPath)

        #picNamePath.insert(1.0, picPath)


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

    def show_text(self):  # omran
        '''

        '''
        pass
