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
    {"lang": "detected or provided language",
    "tokens": "created tokens in the form of a list"} 

    """


    def __init__(self, language = None, detect_language = False):

        self.language = language
        self.detect_language = detect_language

    def get_nlp(self, language):

        """"
        this method returns the corresponding spacy language model when 
        provided with a language. To do so it also does the required 
        import. This is certainly not the standard approach. 
        But as this endpoint will be deployed to Heroku (space limitation)
        and only be invoked rarely it is the fastest approach.
        """

        if language == "en":

            from spacy.lang.en import English
            return English()

        elif language == "fr":

            from spacy.lang.fr import French
            return French()

        elif language == "de":

            from spacy.lang.de import German
            return German()

        elif language == "es":

            from spacy.lang.es import Spanish
            return Spanish()

        elif language == "pt":

            from spacy.lang.pt import Portuguese
            return Portuguese()

        else:

            return {"error": "invalid or not supported language entered"}


    def get_tokens(self, text):

        nlp = self.get_nlp(self.language)
        tokenizer = nlp.Defaults.create_tokenizer(nlp)
        tokens = tokenizer(text)
        # clean punctuation and transform tokens object to list
        tokens = [token.text for token in tokens if not token.is_punct]

        return tokens

    def do(self, text):

        if self.detect_language:

            detector = google_translator()  
            self.language = detector.detect(text)[0]

            if self.language in ["en","fr","de","es","pt"]:

                tokens = self.get_tokens(text)

                return {"lang": self.language, "tokens": tokens}

            else: 
                return {"error": "detected language is not supported"}

        if self.language != None: 

            if self.language in ["en","fr","de","es","pt"]:

                tokens = self.get_tokens(text)
                return {"lang": self.language, "tokens": tokens}

            else: 
                return {"error": "provided language is not supported"}






