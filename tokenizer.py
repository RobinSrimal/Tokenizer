from languages import get_nlp
from google_trans_new import google_translator  

class Tokenizer:

    """
    Tokenizer for the languages English, French, German, Spanish and Portuguese.

    1. removes punktuation if it is not a vital part of a word.

    2. the user can either 

        2.1. provide the language by setting language to 

            "en" for English,
            "fr" for French,
            "de" for German,
            "es" for Spanish,
            "pt" for Portuguese

            By default it is set to None.

        2.2. or set detect_language to True to enable autodetecting 
            of the language. If the detected language is not among the 
            supported ones an error message is returned. 

            By default detect_language is set to False. 

    3. The "do" method returns - given correct input - a dictionary of the form 
    {"lang": "detected or provided language,
    "tokens": "created tokens in the form of a list"} 

    """


    def __init__(self, language = None, detect_language = False):

        self.language = language
        self.detect_language = detect_language

    def get_tokens(self, language, text):

        nlp = get_nlp(language)
        tokenizer = nlp.Defaults.create_tokenizer(nlp)
        tokens = tokenizer(text)
        # clean punctuation 
        tokens = [token for token in tokens if not token.is_punct]

            return tokens

    def do(self, text):

        if self.detect_language:

            detector = google_translator()  
            language = detector.detect(text)

            if language in ["en","fr","de","es","pt"]:

                tokens = self.get_tokens(language, text)
        
                return {"lang": language, "tokens": tokens}

            else: 
                return {"error": "detected language is not supported"}

        if self.language:

            if self.language in ["en","fr","de","es","pt"]:

                tokens = self.get_tokens(self.language, text)

                return {"lang": language, "tokens": tokens}

            else: 
                return {"error": "provided language is not supported"}

