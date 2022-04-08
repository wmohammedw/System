
from FeatureMatching.FakeLogoDetection import FakeLogosDetection
from DenseMotionEstimation.ObjectMovmentPrediction import ObjectMovmentDetection

if __name__ == '__main__':
    # --------------------------- Festure matching --------------------------------------------------
    fake_logo_detection = FakeLogosDetection()
# image to image matching
    img_kp1, img_kp2 = fake_logo_detection.load_image(img1_path=r'D:\IAU\5 - year\Second semester\Computer vision\System\FeatureMatching\Dataset\starbox-real.jpg',
                                                      img2_path=r'D:\IAU\5 - year\Second semester\Computer vision\System\FeatureMatching\fake logos\star.jpg')

    matching = fake_logo_detection.compute_matches(
        des_image1=img_kp1[2], des_image2=img_kp2[2])
    fake_logo_detection.image_to_image_matching(
        img_kp1[0], img_kp1[1], img_kp2[0], img_kp2[1], matching)
# real time matching
    # input_image, input_keypoints, input_descriptors = fake_logo_detection.load_image(
    #     img1_path=r'D:\IAU\5 - year\Second semester\Computer vision\System\FeatureMatching\Dataset\starbox-real.jpg')
    # fake_logo_detection.real_time_matching(
    #     input_image, input_keypoints, input_descriptors)

    # --------------------------- Dense motion --------------------------------------------------

    # denseMotion = ObjectMovmentDetection()
    # denseMotion.video_motion_estimation(
    #     video_file_path=r'DenseMotionEstimation\Teens Involved in Car Crash That Was Like a Movie Scene.mp4')

    # denseMotion.real_time()

    # --------------------------- Facial recognition --------------------------------------------------
