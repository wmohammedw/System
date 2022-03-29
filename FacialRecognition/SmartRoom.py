
class SmartDisck:

    '''
        this is not the final version. we may add new methods if we need it. 
    '''

    def __init__(self):
        '''
            You need to initilize the variables here before use them in the below methods.
            follow the OOP concepts.

            for example in model_training method:
                you will initilize the batch_size here:
                batch_size = 32

                and use it inside model_training method.
        '''
        pass

    def extract_faces(self):
        '''
            here you neet to write a function to extract the faces inide each image. you may use
            haar cascade or MTCNN (better) algorithms.

            you can add as many parameters you want.
        '''
        pass

    def data_augmentation(self):
        '''
            here you will apply the data augmentation on training set only.

            you can add as many parameters you want.
        '''
        pass

    def model_architecture(self):
        '''
            here you need to write the model (we will try CNN first with Transfer learning)
            architecture without compile and fit functions.

            you can add as many parameters you want.
        '''
        pass

    def model_training(self):
        '''
            here you will set the model configuration such as checkpoint, early stopping, optimizer, 
            compile, and fit methods.

            you can add as many parameters you want.
        '''
        pass

    def arduino(self):
        '''
            we will disscused later.
        '''
        pass

    def bounded_box(self):
        '''
            here you want to show the bounded box around the face.

            you can add as many parameters you want.
        '''
        pass
