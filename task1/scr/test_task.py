import unittest

from calculate_statistics import (
    calc_average_sentence_length, 
    calc_average_word_length, 
    count_non_declarative, 
    count_sentences, 
    calc_topK_repeated_Ngrams
    )

class TestCountSentences(unittest.TestCase):

    def test1(self):
        expected_value = 1
        returned_value = count_sentences("Hello, World.")
        self.assertEqual(returned_value, expected_value)

    def test2(self):
        expected_value = 1
        returned_value = count_sentences("Hello, World!")
        self.assertEqual(returned_value, expected_value)

    def test3(self):
        expected_value = 1
        returned_value = count_sentences("Where are you from?")
        self.assertEqual(returned_value, expected_value)
    
    def test4(self):
        expected_value = 1
        returned_value = count_sentences("I\'m sorry...")
        self.assertEqual(returned_value, expected_value)

    def test5(self):
        expected_value = 1
        returned_value = count_sentences("Hello, Mr. Darcy.")
        self.assertEqual(returned_value, expected_value)

    def test6(self):
        expected_value = 1
        returned_value = count_sentences("Hello, Dr. Darcy!?")
        self.assertEqual(returned_value, expected_value)

    def test7(self):
        expected_value = 1
        returned_value = count_sentences("Hello, Mr.Darcy. ")
        self.assertEqual(returned_value, expected_value)

    def test8(self):
        expected_value = 1
        returned_value = count_sentences("Hello, Mr. Bennet...")
        self.assertEqual(returned_value, expected_value)

    def test9(self):
        expected_value = 5
        returned_value = count_sentences("I\'d never given much thought to how I would \
        die — though I\'d had reason enough in the last few months — but even if I had, \
        I would not have imagined it like this. I stared without breathing across the long \
        room, into the dark eyes of the hunter, and he looked pleasantly back at me. Surely \
        it was a good way to die, in the place of someone else, someone I loved. Noble, even. \
        That ought to count for something.")
        self.assertEqual(returned_value, expected_value)
    
    def test10(self):
        expected_value = 0
        returned_value = count_sentences("")
        self.assertEqual(returned_value, expected_value)

    def test11(self):
        expected_value = 1
        returned_value = count_sentences('He said: "Hello. How are you?"')
        self.assertEqual(returned_value, expected_value)

class TestAmountOfNonDeclarative(unittest.TestCase):

    def test1(self):
        expected_value = 1
        returned_value = count_non_declarative("Thanks a lot!")
        self.assertEqual(returned_value, expected_value)

    def test2(self):
        expected_value = 1
        returned_value = count_non_declarative("Wow! It was amazing.")
        self.assertEqual(returned_value, expected_value)

    def test3(self):
        expected_value = 0
        returned_value = count_non_declarative("")
        self.assertEqual(returned_value, expected_value)

    def test4(self):
        expected_value = 0
        returned_value = count_non_declarative("Hi.")
        self.assertEqual(returned_value, expected_value)

    def test5(self):
        expected_value = 1
        returned_value = count_non_declarative("Yo!!!!")
        self.assertEqual(expected_value, returned_value)

class TestAverageLengthOfWords(unittest.TestCase):

    def test1(self):
        expected_value = 9.5
        returned_value = calc_average_word_length("Interesting sentence.")
        self.assertEqual(returned_value, expected_value)

    def test2(self):
        expected_value = 28 / 6
        returned_value = calc_average_word_length("That ought to count for something.")
        self.assertEqual(returned_value, expected_value)

    def test3(self):
        expected_value = 0
        returned_value = calc_average_word_length("")
        self.assertEqual(returned_value, expected_value)

    def test4(self):
        expected_value = 5
        returned_value = calc_average_word_length("Hello!!!")
        self.assertEqual(returned_value, expected_value)

    def test5(self):
        expected_value = 1
        returned_value = calc_average_word_length("L.")
        self.assertEqual(returned_value, expected_value)

    def test5(self):
        expected_value = 0
        returned_value = calc_average_word_length("1.")
        self.assertEqual(returned_value, expected_value)

class TestAverageLengthOfSentence(unittest.TestCase):

    def test1(self):
        expected_value = 7.5
        returned_value = calc_average_sentence_length("Wow! It was amazing.")
        self.assertEqual(expected_value, returned_value)

    def test2(self):
        expected_value = 5
        returned_value = calc_average_sentence_length("Hello!!!")
        self.assertEqual(expected_value, returned_value)

    def test3(self):
        expected_value = 0
        returned_value = calc_average_sentence_length("")
        self.assertEqual(expected_value, returned_value)

    def test4(self):
        expected_value = 0
        returned_value = calc_average_sentence_length("1.")
        self.assertEqual(expected_value, returned_value)

    def test5(self):
        expected_value = 0
        returned_value = calc_average_sentence_length(" ")
        self.assertEqual(expected_value, returned_value)

class TestNGrams(unittest.TestCase):
    def test1(self):
        expected_value = [("hel", 1), ("ell", 1), ("llo", 1), ("lo,", 1), ("o, ", 1),
                          (", w", 1)]
        returned_value = calc_topK_repeated_Ngrams("Hello, World!", 6, 3)
        self.assertEqual(expected_value, returned_value)

    def test2(self):
        expected_value = []
        returned_value = calc_topK_repeated_Ngrams("", 50, 50)
        self.assertEqual(expected_value, returned_value)
    
    def test3(self):
        expected_value = [("h", 1)]
        returned_value = calc_topK_repeated_Ngrams("H", 1, 1)
        self.assertEqual(expected_value, returned_value)

if __name__ == "__main__":
    unittest.main()