from tokenizer import Tokenizer
import unittest


class TestTokenizer(unittest.TestCase):

    def test_get_tokens(self):

        test_english = Tokenizer(language="en")
        self.assertEqual(test_english.get_tokens("Mr. one two three"),
        ["Mr.", 
        "one",
        "two",
        "three"])

        test_french = Tokenizer(language="fr")
        self.assertEqual(test_french.get_tokens("""Demain, dès l’aube, à l’heure où blanchit la campagne"""),
         ["Demain",
         "dès",
         "l’",
         "aube",
         "à",
         "l’",
         "heure",
         "où",
         "blanchit",
         "la",
         "campagne"])

        test_german = Tokenizer(language="de")
        self.assertEqual(test_german.get_tokens("""Astern – schwälende Tage, alte Beschwörung, Bann, die Götter halten die Waage eine zögernde Stunde an."""), 
                                                [
    "Astern",
    "schwälende",
    "Tage",
    "alte",
    "Beschwörung",
    "Bann",
    "die",
    "Götter",
    "halten",
    "die",
    "Waage",
    "eine",
    "zögernde",
    "Stunde",
    "an"
  ])

        test_spanish = Tokenizer(language="es")
        self.assertEqual(test_spanish.get_tokens("""No duerme nadie por el cielo. Nadie, nadie. No duerme nadie. """), 
        [
    "No",
    "duerme",
    "nadie",
    "por",
    "el",
    "cielo",
    "Nadie",
    "nadie",
    "No",
    "duerme",
    "nadie"
  ])

        test_portuguese = Tokenizer(language="pt")
        self.assertTrue(test_portuguese.get_tokens("""Bailando no ar, gemia inquieto vaga-lume:"""),
        [
    "Bailando",
    "no",
    "ar",
    "gemia",
    "inquieto",
    "vaga-lume"
  ])
    

    def test_do(self):

        # test cases for autodetection of language

        test = Tokenizer(detect_language=True)

        self.assertEqual(test.do("one two three"),{
  "lang": "en",
  "tokens": [
    "one",
    "two",
    "three"
  ]
})
        self.assertEqual(test.do("un deux trois"),{
  "lang": "fr",
  "tokens": [
    "un",
    "deux",
    "trois"
  ]
})
        self.assertEqual(test.do("eins zwei drei"), {
  "lang": "de",
  "tokens": [
    "eins",
    "zwei",
    "drei"
  ]
})
        self.assertEqual(test.do("uno dos tres"),{
  "lang": "es",
  "tokens": [
    "uno",
    "dos",
    "tres"
  ]
})
        self.assertEqual(test.do("um dois três"),{
  "lang": "pt",
  "tokens": [
    "um",
    "dois",
    "três"
  ]
})

        # test case for not supported language

        self.assertEqual(test.do("yksi kaksi kolme"), {
  "error": "detected language is not supported"
})

if __name__ == '__main__':
    unittest.main()