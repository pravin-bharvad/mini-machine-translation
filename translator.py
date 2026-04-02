import re
import unicodedata

EN_HI_DICT = {
    "i":"मैं","me":"मुझे","my":"मेरा","we":"हम","you":"तुम","he":"वह","she":"वह","they":"वे","it":"यह","this":"यह","that":"वह",
    "is":"है","are":"हैं","was":"था","were":"थे","have":"है","has":"है","had":"था",
    "go":"जाना","come":"आना","do":"करना","learn":"सीखना","learning":"सीख रहा है",
    "speak":"बोलना","write":"लिखना","read":"पढ़ना","eat":"खाना","drink":"पीना",
    "know":"जानना","think":"सोचना","work":"काम करना","love":"प्यार करना",
    "study":"पढ़ाई करना","teach":"पढ़ाना","understand":"समझना","help":"मदद करना",
    "student":"छात्र","teacher":"शिक्षक","school":"विद्यालय","university":"विश्वविद्यालय",
    "family":"परिवार","mother":"माँ","father":"पिता","brother":"भाई","sister":"बहन","friend":"मित्र",
    "country":"देश","city":"शहर","home":"घर","water":"पानी","food":"खाना","book":"किताब",
    "computer":"कंप्यूटर","phone":"फ़ोन","language":"भाषा","word":"शब्द","sentence":"वाक्य",
    "natural":"प्राकृतिक","processing":"प्रसंस्करण","translation":"अनुवाद","machine":"मशीन",
    "data":"डेटा","text":"पाठ","grammar":"व्याकरण","system":"प्रणाली","input":"इनपुट","output":"आउटपुट",
    "good":"अच्छा","bad":"बुरा","big":"बड़ा","small":"छोटा","new":"नया","old":"पुराना",
    "happy":"खुश","sad":"दुखी","beautiful":"सुंदर","important":"महत्वपूर्ण","simple":"सरल",
    "today":"आज","now":"अभी","morning":"सुबह","night":"रात","year":"साल","day":"दिन",
    "and":"और","or":"या","but":"लेकिन","if":"अगर","with":"के साथ","from":"से",
    "to":"को","in":"में","on":"पर","of":"का","for":"के लिए","by":"द्वारा",
    "people":"लोग","time":"समय","life":"जीवन","world":"दुनिया","problem":"समस्या",
    "result":"परिणाम","project":"परियोजना","name":"नाम","india":"भारत",
}

EN_GU_DICT = {
    "i":"હું","me":"મને","my":"મારો","we":"અમે","you":"તું","he":"તે","she":"તે","they":"તેઓ","it":"આ","this":"આ","that":"તે",
    "is":"છે","are":"છે","was":"હતો","were":"હતા","have":"છે","has":"છે","had":"હતું",
    "go":"જવું","come":"આવવું","do":"કરવું","learn":"શીખવું","learning":"શીખી રહ્યો છે",
    "speak":"બોલવું","write":"લખવું","read":"વાંચવું","eat":"ખાવું","drink":"પીવું",
    "know":"જાણવું","think":"વિચારવું","work":"કામ કરવું","love":"પ્રેમ કરવું",
    "study":"ભણવું","teach":"ભણાવવું","understand":"સમજવું","help":"મદદ કરવી",
    "student":"વિદ્યાર્થી","teacher":"શિક્ષક","school":"શાળા","university":"વિશ્વવિદ્યાલય",
    "family":"કુટુંબ","mother":"માં","father":"પિતા","brother":"ભાઈ","sister":"બહેન","friend":"મિત્ર",
    "country":"દેશ","city":"શહેર","home":"ઘર","water":"પાણી","food":"ખોરાક","book":"પુસ્તક",
    "computer":"કમ્પ્યૂટર","phone":"ફોન","language":"ભાષા","word":"શબ્દ","sentence":"વાક્ય",
    "natural":"કુદરતી","processing":"પ્રક્રિયા","translation":"અનુવાદ","machine":"મશીન",
    "data":"ડેટા","text":"લખાણ","grammar":"વ્યાકરણ","system":"પ્રણાલી","input":"ઇનપુટ","output":"આઉટપુટ",
    "good":"સારો","bad":"ખરાબ","big":"મોટો","small":"નાનો","new":"નવો","old":"જૂનો",
    "happy":"ખુશ","sad":"દુઃખી","beautiful":"સુંદર","important":"મહત્વપૂર્ણ","simple":"સરળ",
    "today":"આજ","now":"હવે","morning":"સવાર","night":"રાત","year":"વર્ષ","day":"દિવસ",
    "and":"અને","or":"અથવા","but":"પણ","if":"જો","with":"સાથે","from":"થી",
    "to":"ને","in":"માં","on":"પર","of":"નો","for":"માટે","by":"દ્વારા",
    "people":"લોકો","time":"સમય","life":"જીવન","world":"દુનિયા","problem":"સમસ્યા",
    "result":"પરિણામ","project":"પ્રોજેક્ટ","name":"નામ","india":"ભારત","gujarat":"ગુજરાત",
}

HI_EN_DICT = {v: k for k, v in EN_HI_DICT.items()}
HI_EN_DICT.update({"मैं":"I","हम":"we","तुम":"you","वह":"he/she","है":"is","और":"and","छात्र":"student","भाषा":"language","अनुवाद":"translation"})

GU_EN_DICT = {v: k for k, v in EN_GU_DICT.items()}
GU_EN_DICT.update({"હું":"I","અમે":"we","તું":"you","તે":"he/she","છે":"is","અને":"and","વિદ્યાર્થી":"student","ભાષા":"language","અનુવાદ":"translation"})

EN_STOPWORDS = {"a","an","the","is","are","was","were","be","been","have","has","had","do","does","did","will","would","could","should","may","might","to","of","in","on","at","by","for","with","and","but","or","not","that","this","these","those","i","me","my","we","our","you","your","he","him","his","she","her","they","them","their","it","its","so","just","very","also","both","each","all","any","no","too","than","as","if","while","then"}
HI_STOPWORDS = {"है","हैं","था","थे","और","या","लेकिन","पर","में","को","से","का","की","के","ने","तो","भी","ही","यह","वह","मैं","हम","तुम","कि","जो","एक","नहीं"}
GU_STOPWORDS = {"છે","હતો","હતી","હતા","અને","અથવા","પણ","પર","માં","ને","થી","નો","ની","ના","તો","આ","તે","હું","અમે","તું","કે","જે","એક","નહીં"}

def normalize_unicode(text):
    return unicodedata.normalize("NFC", text)

def detect_script(text):
    d = sum(1 for c in text if '\u0900' <= c <= '\u097F')
    g = sum(1 for c in text if '\u0A80' <= c <= '\u0AFF')
    l = sum(1 for c in text if c.isascii() and c.isalpha())
    return max({'devanagari':d,'gujarati':g,'latin':l}, key=lambda k:{'devanagari':d,'gujarati':g,'latin':l}[k])

def tokenize(text):
    return re.findall(r'[\w\u0900-\u097F\u0A80-\u0AFF]+', normalize_unicode(text), re.UNICODE)

def sentence_tokenize(text):
    return [s.strip() for s in re.split(r'[।॥.!?]+', text) if s.strip()]

def remove_stopwords(tokens, language='english'):
    sw = {'english':EN_STOPWORDS,'hindi':HI_STOPWORDS,'gujarati':GU_STOPWORDS}.get(language.lower(), EN_STOPWORDS)
    return [t for t in tokens if t.lower() not in sw]

def translate_token(token, dictionary):
    if token in dictionary: return dictionary[token]
    if token.lower() in dictionary: return dictionary[token.lower()]
    return f"[{token}]"

def translate(text, source_lang, target_lang):
    dictionary_map = {
        ('english','hindi'): EN_HI_DICT,
        ('english','gujarati'): EN_GU_DICT,
        ('hindi','english'): HI_EN_DICT,
        ('gujarati','english'): GU_EN_DICT,
    }
    result = {
        'input_text': text, 'source_lang': source_lang, 'target_lang': target_lang,
        'normalized_text': '', 'tokens': [], 'tokens_no_stopwords': [],
        'script_detected': '', 'translated_text': '',
        'oov_count': 0, 'word_count': 0, 'coverage': 0.0,
    }
    norm = normalize_unicode(text)
    result['normalized_text'] = norm
    result['script_detected'] = detect_script(norm)
    dictionary = dictionary_map.get((source_lang.lower(), target_lang.lower()), {})
    sentences = sentence_tokenize(norm) or [norm]
    all_tokens, all_filtered, parts = [], [], []
    for sentence in sentences:
        tokens = tokenize(sentence)
        filtered = remove_stopwords(tokens, language=source_lang)
        all_tokens.extend(tokens)
        all_filtered.extend(filtered)
        parts.append(' '.join([translate_token(t, dictionary) for t in filtered]))
    result['tokens'] = all_tokens
    result['tokens_no_stopwords'] = all_filtered
    result['translated_text'] = ' । '.join(parts) if len(parts) > 1 else (parts[0] if parts else '')
    result['word_count'] = len(all_filtered)
    oov = [t for t in all_filtered if translate_token(t, dictionary).startswith('[')]
    result['oov_count'] = len(oov)
    result['coverage'] = round(((result['word_count'] - result['oov_count']) / result['word_count'] * 100) if result['word_count'] > 0 else 0, 1)
    return result