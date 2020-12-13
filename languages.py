def get_nlp(language):

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











