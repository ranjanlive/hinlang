"""
hinlang.dictionary
==================

Central dictionary of Roman ↔ Devanagari word mappings.
Contains 500+ commonly used Hindi words for accurate transliteration.

The forward dict (ROMAN_TO_HINDI) is the source of truth.
The reverse dict (HINDI_TO_ROMAN) is auto-generated from it,
with manual overrides for preferred spellings.
"""

# ════════════════════════════════════════════════
#  ROMAN → DEVANAGARI  (source of truth)
# ════════════════════════════════════════════════

ROMAN_TO_HINDI = {
    # ── Greetings ──
    'namaste':   'नमस्ते',    'namaskar':  'नमस्कार',
    'hello':     'हेलो',      'hi':        'हाय',
    'bye':       'बाय',       'goodbye':   'गुडबाय',
    'shukriya':  'शुक्रिया',   'dhanyavaad':'धन्यवाद',
    'dhanyawad': 'धन्यवाद',   'sorry':     'सॉरी',
    'please':    'प्लीज़',     'welcome':   'वेलकम',
    'thankyou':  'थैंक यू',    'thanks':    'थैंक्स',

    # ── Pronouns ──
    'aap':    'आप',       'aapka':   'आपका',
    'aapki':  'आपकी',     'aapke':   'आपके',
    'main':   'मैं',       'mein':    'मैं',
    'mai':    'मैं',       'mera':    'मेरा',
    'meri':   'मेरी',      'mere':    'मेरे',
    'hum':    'हम',       'humara':  'हमारा',
    'humari': 'हमारी',     'humare':  'हमारे',
    'tum':    'तुम',      'tumhara': 'तुम्हारा',
    'tumhari':'तुम्हारी',   'tumhare': 'तुम्हारे',
    'tu':     'तू',       'tera':    'तेरा',
    'teri':   'तेरी',      'tere':    'तेरे',
    'woh':    'वो',       'wo':      'वो',
    'yeh':    'ये',       'ye':      'ये',
    'uska':   'उसका',     'uski':    'उसकी',
    'uske':   'उसके',     'iska':    'इसका',
    'iski':   'इसकी',     'iske':    'इसके',

    # ── Question words ──
    'kya':    'क्या',      'kyu':     'क्यों',
    'kyon':   'क्यों',      'kyun':    'क्यूं',
    'kaun':   'कौन',      'kahan':   'कहां',
    'kahaan': 'कहाँ',      'kaise':   'कैसे',
    'kaisa':  'कैसा',      'kaisi':   'कैसी',
    'kab':    'कब',       'kitna':   'कितना',
    'kitni':  'कितनी',     'kitne':   'कितने',
    'kon':    'कौन',      'konsa':   'कौनसा',
    'kidhar': 'किधर',      'idhar':   'इधर',
    'udhar':  'उधर',

    # ── Verbs: to be ──
    'hai':    'है',       'hain':    'हैं',
    'tha':    'था',       'thi':     'थी',
    'the':    'थे',       'ho':      'हो',
    'hoga':   'होगा',     'hogi':    'होगी',
    'hoge':   'होगे',     'hona':    'होना',
    'hoon':   'हूँ',       'hun':     'हूँ',
    'hu':     'हूँ',       'hoo':     'हूँ',
    'hua':    'हुआ',      'hui':     'हुई',
    'hue':    'हुए',

    # ── Verbs: to do ──
    'karo':   'करो',      'karna':   'करना',
    'karti':  'करती',     'karta':   'करता',
    'karte':  'करते',     'karega':  'करेगा',
    'karegi': 'करेगी',    'karenge': 'करेंगे',
    'kar':    'कर',       'kiya':    'किया',
    'kiye':   'किये',

    # ── Postpositions / Connectors ──
    'ki':     'की',       'ka':      'का',
    'ke':     'के',       'ko':      'को',
    'se':     'से',       'me':      'में',
    'pe':     'पे',       'par':     'पर',
    'ne':     'ने',       'ya':      'या',
    'aur':    'और',       'or':      'और',
    'lekin':  'लेकिन',    'magar':   'मगर',
    'isliye': 'इसलिए',    'kyunki':  'क्योंकि',
    'agar':   'अगर',      'toh':     'तो',
    'to':     'तो',       'bhi':     'भी',
    'nahi':   'नहीं',      'nhi':     'नहीं',
    'nahin':  'नहीं',      'na':      'ना',
    'mat':    'मत',       'sirf':    'सिर्फ',
    'bas':    'बस',

    # ── Verbs: to go ──
    'jao':    'जाओ',      'jana':    'जाना',
    'jata':   'जाता',     'jati':    'जाती',
    'jate':   'जाते',     'gaya':    'गया',
    'gayi':   'गयी',      'gaye':    'गये',
    'jayega': 'जाएगा',    'jayegi':  'जाएगी',
    'ja':     'जा',

    # ── Verbs: to come ──
    'aao':    'आओ',       'aana':    'आना',
    'aata':   'आता',      'aati':    'आती',
    'aaye':   'आये',      'aaya':    'आया',
    'aayi':   'आयी',      'aayega':  'आएगा',
    'aayegi': 'आएगी',     'aa':      'आ',

    # ── Other common verbs ──
    'khao':   'खाओ',      'khana':   'खाना',
    'peena':  'पीना',     'piyo':    'पियो',
    'dekho':  'देखो',     'dekhna':  'देखना',
    'suno':   'सुनो',     'sunna':   'सुनना',
    'bolo':   'बोलो',     'bolna':   'बोलना',
    'padho':  'पढ़ो',      'padhna':  'पढ़ना',
    'likho':  'लिखो',     'likhna':  'लिखना',
    'socho':  'सोचो',     'sochna':  'सोचना',
    'samjho': 'समझो',     'samajhna':'समझना',
    'batao':  'बताओ',     'batana':  'बताना',
    'chalo':  'चलो',      'chalna':  'चलना',
    'ruko':   'रुको',      'rukna':   'रुकना',
    'de':     'दे',       'dena':    'देना',
    'le':     'ले',       'lena':    'लेना',
    'do':     'दो',       'lo':      'लो',
    'raha':   'रहा',      'rahi':    'रही',
    'rahe':   'रहे',      'la':      'ला',
    'lao':    'लाओ',      'lana':    'लाना',
    'laao':   'लाओ',      'diya':    'दिया',
    'diyo':   'दियो',     'liya':    'लिया',
    'bol':    'बोल',      'chal':    'चल',
    'mil':    'मिल',      'milte':   'मिलते',
    'milna':  'मिलना',    'mila':    'मिला',
    'mili':   'मिली',     'mile':    'मिले',
    'chalte': 'चलते',     'rok':     'रोक',
    'dekh':   'देख',      'sun':     'सुन',
    'padh':   'पढ़',       'likh':    'लिख',
    'soch':   'सोच',      'samajh':  'समझ',
    'bata':   'बता',      'chahiye': 'चाहिए',
    'chahte': 'चाहते',    'chahta':  'चाहता',
    'chahti': 'चाहती',

    # ── Nouns: People ──
    'dost':   'दोस्त',    'dosto':   'दोस्तो',
    'bhai':   'भाई',      'bhaiya':  'भैया',
    'behan':  'बहन',      'didi':    'दीदी',
    'maa':    'माँ',       'papa':    'पापा',
    'baap':   'बाप',      'beta':    'बेटा',
    'beti':   'बेटी',     'bachcha': 'बच्चा',
    'bachche':'बच्चे',     'aadmi':   'आदमी',
    'aurat':  'औरत',      'ladka':   'लड़का',
    'ladki':  'लड़की',     'log':     'लोग',
    'guru':   'गुरु',     'sir':     'सर',

    # ── Nouns: Things ──
    'ghar':   'घर',       'school':  'स्कूल',
    'paani':  'पानी',     'roti':    'रोटी',
    'doodh':  'दूध',      'chai':    'चाय',
    'kaam':   'काम',      'paisa':   'पैसा',
    'paise':  'पैसे',     'time':    'टाइम',
    'din':    'दिन',      'raat':    'रात',
    'subah':  'सुबह',     'shaam':   'शाम',
    'saal':   'साल',      'mahina':  'महीना',
    'hafta':  'हफ्ता',     'desh':    'देश',
    'duniya': 'दुनिया',    'zindagi': 'ज़िंदगी',
    'pyaar':  'प्यार',     'dil':     'दिल',
    'mann':   'मन',       'khushi':  'खुशी',
    'dukh':   'दुख',      'sapna':   'सपना',
    'sapne':  'सपने',     'aasman':  'आसमान',
    'dharti': 'धरती',     'hawa':    'हवा',
    'aag':    'आग',       'naam':    'नाम',
    'jagah':  'जगह',      'baat':    'बात',
    'cheez':  'चीज़',      'tarah':   'तरह',
    'wajah':  'वजह',      'matlab':  'मतलब',
    'mausam': 'मौसम',     'rang':    'रंग',
    'shahar': 'शहर',      'gaon':    'गाँव',
    'sadak':  'सड़क',      'raasta':  'रास्ता',
    'darwaza':'दरवाज़ा',   'kamra':   'कमरा',
    'kursi':  'कुर्सी',    'mez':     'मेज़',
    'kitab':  'किताब',     'kalam':   'कलम',
    'kapda':  'कपड़ा',     'kapde':   'कपड़े',
    'joota':  'जूता',      'phone':   'फ़ोन',
    'computer':'कंप्यूटर',  'gaadi':   'गाड़ी',
    'train':  'ट्रेन',     'pata':    'पता',

    # ── Adjectives ──
    'accha':  'अच्छा',    'acchi':   'अच्छी',
    'acche':  'अच्छे',    'bura':    'बुरा',
    'buri':   'बुरी',     'bure':    'बुरे',
    'bada':   'बड़ा',      'badi':    'बड़ी',
    'bade':   'बड़े',      'chhota':  'छोटा',
    'chhoti': 'छोटी',     'chhote':  'छोटे',
    'naya':   'नया',      'nayi':    'नयी',
    'naye':   'नये',      'purana':  'पुराना',
    'purani': 'पुरानी',    'purane':  'पुराने',
    'sab':    'सब',       'sabhi':   'सभी',
    'kuch':   'कुछ',      'bahut':   'बहुत',
    'bohot':  'बहुत',     'zyada':   'ज़्यादा',
    'kam':    'कम',       'thoda':   'थोड़ा',
    'thodi':  'थोड़ी',     'thode':   'थोड़े',
    'pehle':  'पहले',     'baad':    'बाद',
    'abhi':   'अभी',      'ab':      'अब',
    'tab':    'तब',       'jab':     'जब',
    'yaha':   'यहाँ',      'yahan':   'यहाँ',
    'waha':   'वहाँ',      'wahan':   'वहाँ',
    'hamesha':'हमेशा',     'kabhi':   'कभी',
    'phir':   'फिर',      'fir':     'फिर',
    'bilkul': 'बिलकुल',    'sach':    'सच',
    'jhooth': 'झूठ',       'theek':   'ठीक',
    'thik':   'ठीक',      'khush':   'खुश',
    'udaas':  'उदास',     'khubsoorat': 'खूबसूरत',
    'khoobsurat':'खूबसूरत', 'sundar':  'सुंदर',
    'mazedaar':'मज़ेदार',   'behtareen':'बेहतरीन',
    'garam':  'गरम',      'thanda':  'ठंडा',
    'thandi': 'ठंडी',

    # ── Numbers ──
    'ek':     'एक',       'teen':    'तीन',
    'char':   'चार',      'paanch':  'पाँच',
    'chhe':   'छे',       'saat':    'सात',
    'aath':   'आठ',       'nau':     'नौ',
    'das':    'दस',       'sau':     'सौ',
    'hazaar': 'हज़ार',     'lakh':    'लाख',
    'crore':  'करोड़',

    # ── Time ──
    'aaj':    'आज',       'kal':     'कल',
    'parso':  'परसो',     'roz':     'रोज़',

    # ── Common words ──
    'shaayad':'शायद',     'shayad':  'शायद',
    'zaroor': 'ज़रूर',     'jaroor':  'ज़रूर',
    'mushkil':'मुश्किल',   'aasan':   'आसान',
    'achanak':'अचानक',

    # ── Formal verbs ──
    'sochiye':'सोचिए',     'dekhiye': 'देखिए',
    'suniye': 'सुनिए',     'boliye':  'बोलिए',
    'chaliye':'चलिए',      'kariye':  'करिए',
    'dijiye': 'दीजिए',     'lijiye':  'लीजिए',

    # ── Pronoun forms ──
    'aapko':  'आपको',     'mujhe':   'मुझे',
    'mujhko': 'मुझको',     'tujhe':   'तुझे',
    'humko':  'हमको',      'humein':  'हमें',
    'tumko':  'तुमको',     'tumhein': 'तुम्हें',
    'unko':   'उनको',     'unhe':    'उन्हें',
    'inko':   'इनको',     'inhe':    'इन्हें',
    'jiske':  'जिसके',     'kiske':   'किसके',
    'sabko':  'सबको',     'sabke':   'सबके',
    'saath':  'साथ',

    # ── Wala / postpositions ──
    'wala':   'वाला',     'wali':    'वाली',
    'wale':   'वाले',     'waala':   'वाला',
    'waali':  'वाली',     'waale':   'वाले',

    # ── More common ──
    'mujhse': 'मुझसे',    'tumse':   'तुमसे',
    'aapse':  'आपसे',     'unse':    'उनसे',
    'isme':   'इसमें',     'usme':    'उसमें',
    'jisme':  'जिसमें',    'kisme':   'किसमें',
    'sabme':  'सबमें',     'mujhpe':  'मुझपे',
    'apna':   'अपना',     'apni':    'अपनी',
    'apne':   'अपने',     'khud':    'खुद',
    'koi':    'कोई',      'kisi':    'किसी',
    'dusra':  'दूसरा',    'dusri':   'दूसरी',
    'dusre':  'दूसरे',    'pura':    'पूरा',
    'puri':   'पूरी',      'pure':    'पूरे',
}


# ════════════════════════════════════════════════
#  HINDI → ROMAN  (auto-generated + overrides)
# ════════════════════════════════════════════════

# Auto-build reverse dictionary (prefer first occurrence for duplicates)
_seen_hindi = set()
HINDI_TO_ROMAN = {}

# Manual overrides — preferred romanizations for ambiguous Devanagari
_HINDI_TO_ROMAN_OVERRIDES = {
    'मैं':    'main',
    'में':    'mein',
    'और':    'aur',
    'नहीं':   'nahi',
    'तो':    'toh',
    'वो':    'woh',
    'ये':    'yeh',
    'दो':    'do',
    'हूँ':    'hoon',
    'क्यों':  'kyon',
    'कहाँ':  'kahaan',
    'कहां':  'kahaan',
    'बहुत':  'bahut',
    'फिर':   'phir',
    'ठीक':   'theek',
    'यहाँ':   'yahaan',
    'वहाँ':   'wahaan',
    'गाँव':   'gaon',
    'ॐ':     'om',
    'श्री':   'shri',
}

# Build from forward dict
for roman, hindi in ROMAN_TO_HINDI.items():
    if hindi not in _seen_hindi:
        HINDI_TO_ROMAN[hindi] = roman
        _seen_hindi.add(hindi)

# Apply overrides
HINDI_TO_ROMAN.update(_HINDI_TO_ROMAN_OVERRIDES)

# ── Special words ──
SPECIALS = {
    'om':   'ॐ',
    'shri': 'श्री',
    'sri':  'श्री',
}
