from flask import Flask, render_template, request, jsonify
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from translator import translate, EN_HI_DICT, EN_GU_DICT

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/translate', methods=['POST'])
def translate_api():
    data = request.get_json(force=True)
    text        = data.get('text', '').strip()
    source_lang = data.get('source_lang', 'english')
    target_lang = data.get('target_lang', 'hindi')

    if not text:
        return jsonify({'error': 'Input text is empty.'}), 400

    valid_pairs = [
        ('english', 'hindi'), ('english', 'gujarati'),
        ('hindi', 'english'), ('gujarati', 'english')
    ]
    if (source_lang, target_lang) not in valid_pairs:
        return jsonify({'error': f'Language pair {source_lang} to {target_lang} not supported.'}), 400

    result = translate(text, source_lang, target_lang)
    return jsonify(result)


@app.route('/info')
def info():
    return jsonify({
        'en_hi_vocab': len(EN_HI_DICT),
        'en_gu_vocab': len(EN_GU_DICT),
        'supported_pairs': [
            'English → Hindi',
            'English → Gujarati',
            'Hindi → English',
            'Gujarati → English',
        ]
    })


if __name__ == '__main__':
    print("=" * 60)
    print("  Mini Machine Translation System")
    print("  Silver Oak University — CLIL Project")
    print("  Open: http://127.0.0.1:5000")
    print("=" * 60)
    app.run(debug=True, port=5000)
