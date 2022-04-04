
from FeatureMatching.FakeLogoDetection import FakeLogosDetection

if __name__ == '__main__':
    fake_logo_detection = FakeLogosDetection()

    # img_kp1, img_kp2 = fake_logo_detection.load_image(img1_path=r'D:\IAU\5 - year\Second semester\Computer vision\System\FeatureMatching\Dataset\starbox-real.jpg',
    #                                                   img2_path=r'D:\IAU\5 - year\Second semester\Computer vision\System\FeatureMatching\fake logos\starbox-fake.jpg')

    # matching = fake_logo_detection.compute_matches(
    #     des_image1=img_kp1[2], des_image2=img_kp2[2], real_time=False)

    # print(matching)

    # fake_logo_detection.image_to_image_matching(
    #     img_kp1[0], img_kp1[1], img_kp2[0], img_kp2[1], matching, 20)

    input_image, input_keypoints, input_descriptors = fake_logo_detection.load_image(
        img1_path=r'D:\IAU\5 - year\Second semester\Computer vision\System\FeatureMatching\Dataset\bag.jpeg')
    fake_logo_detection.real_time_matching(
        input_image, input_keypoints, input_descriptors, MIN_MATCHES=20)
