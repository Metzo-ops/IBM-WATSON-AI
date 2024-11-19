from SentimentAnalysis import sentiment_analysis as sa
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        # Cas de test pour un sentiment positif
        result_1 = sa.sentiment_analyzer('I love working with Python')
        self.assertEqual(result_1['label'], 'SENT_POSITIVE')

        # Cas de test pour un sentiment négatif
        result_2 = sa.sentiment_analyzer('I hate working with Python')
        self.assertEqual(result_2['label'], 'SENT_NEGATIVE')

        # result_3 = sa.sentiment_analyzer('I hate working with Python')
        # self.assertEqual(result_3['label'], 'SENT_NEUTRAL')
    
unittest.main()