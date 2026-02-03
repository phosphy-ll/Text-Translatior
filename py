pip install translate

from translate import Translator

def translate_text(text, from_lang='ru', to_lang='en'):
    translator = Translator(from_lang=from_lang, to_lang=to_lang)
    try:
        translated_text = translator.translate(text)
        return translated_text  
    except Exception as e:
        return f"Error: {e}"
