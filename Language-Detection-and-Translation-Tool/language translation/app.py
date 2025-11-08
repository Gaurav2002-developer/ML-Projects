from flask import Flask,request, render_template
from langdetect import detect
from googletrans import Translator, LANGUAGES

app = Flask(__name__)

def detect_And_Translator(text, target_lang):
    result_lang = detect(text)


    translator = Translator()
    # Previous error occoured- then , Use synchronous version, also pip install googletrans==4.0.0rc1
    # translated_text = translator.translate(text, dest=target_lang).text
    translated_text = translator.translate(text, dest=target_lang)
    return translated_text.text, translated_text.src
    # return result_lang, translated_text

@app.route('/')
def index():
    return render_template('first.html', languages = LANGUAGES  )


@app.route('/trans', methods = ['POST'])
def trans():
    translation = " "
    detected_lang = " "
    if request.method =="POST":
        text = request.form['text']
        target_lang = request.form['target_lang']

        translation, detected_lang = detect_And_Translator(text, target_lang)
    return render_template('first.html', translation = translation, detected_lang = detected_lang, languages = LANGUAGES)

if __name__ == "__main__":
    app.run(debug= True)


