import cv2

                             
class HumanDetector:
    def __init__(self):
        self.net = cv2.dnn.readNetFromCaffe('faceDetector/deploy.prototxt.txt',
                               'faceDetector/res10_300x300_ssd_iter_140000.caffemodel')
        self.prob_threshold = 0.965
        print('Human detector ready')


    def detect(self, img_path):
        img = cv2.imread(img_path)
        (h, w) = img.shape[:2]
        # blobFromImage function is used for mean substraction and scaling
        # mean values for the ImageNet training set are R=103.93, G=116.77, and B=123.68 
        blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0, 
                                 (300, 300), (104.0, 117.0, 123.0))
        self.net.setInput(blob)
        detections = self.net.forward()
        for i in range(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > self.prob_threshold:
                return True
        return False