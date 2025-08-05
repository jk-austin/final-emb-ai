from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        #test for output 'joy'
        result_joy = emotion_detector('I am glad this happened')
        self.assertEqual(result_joy['dominant emotion'], 'joy')
        #test for output 'anger'
        result_anger = emotion_detector('I am really mad about this')
        self.assertEqual(result_anger['dominant emotion'], 'anger')
        #test for output 'disgust'
        result_disgust = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_disgust['dominant emotion'], 'disgust')
        #test for output 'sadness'
        result_sadness = emotion_detector('I am so sad about this')
        self.assertEqual(result_sadness['dominant emotion'], 'sadness')
        #test for output 'fear'
        result_fear = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_fear['dominant emotion'], 'fear')

if __name__ == '__main__': unittest.main()
