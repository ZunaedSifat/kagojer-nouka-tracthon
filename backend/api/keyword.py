import nltk
from summa import keywords
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from string import punctuation
from nltk.corpus import wordnet as wn

'''
Utils
'''


def read_file(file_name):
    file1 = open(file_name, "r", encoding='UTF-8')
    return file1.read()


'''
returns a list of tuples (word, weight)
'''


def sort_based_on_weight(words: dict):
    return sorted(words.items(), key=lambda x: x[1], reverse=True)


def remove_leading_and_trailing_special_chars(s: str):
    s = s.replace('“', "")  # replacing weird unicode character (u8220) that often comes out in articles
    s = s.replace('‘', "")  # replacing weird unicode character (u8216) that often comes out in articles

    return s.strip(punctuation)


'''
nltk:
All functions except init_nltk() returns a dictionary where key==word_string and value==weight_float
'''


def init_nltk():
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('words')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('punkt')
    # nltk.download('maxent_ne_chunker')


'''
nltk multi-pass utils
'''


def remove_stopwords(input_words: dict):
    words = dict()
    stop_words = set(stopwords.words("english"))
    # print('StopWords:\n', stop_words)

    for k, v in input_words.items():
        lowered = str(k).lower()

        contains_stop_word = False

        for item in stop_words:
            sw = str(item)
            if (sw.__len__() >= 4 and lowered.find(sw) != -1) or (
                    lowered.__len__() >= 4 and sw.find(lowered) != -1) or (lowered == sw):
                contains_stop_word = True
                # print('(removed,responsible-sw)', lowered, ":", sw)
                break

        if contains_stop_word:
            pass
        else:
            words[k] = v
    return words


def lemmatize(words: dict):
    lem = WordNetLemmatizer()
    lemmatized_words = dict()

    words = dict(words)

    for k in words:
        # lemmatized = lem.lemmatize(k, 'v')
        lemmatized = lem.lemmatize(k)
        if lemmatized not in lemmatized_words:
            lemmatized_words[lemmatized] = words.get(k)

    return lemmatized_words


'''
nltk single-pass utils
'''


def generate_summa_keywords(text):
    _keywords = list()
    try:
        _keywords = dict(keywords.keywords(text, scores=True))
    except UnicodeDecodeError:
        print('UnicodeDecodeError: generating keywords')

    return _keywords


def find_unique_proper_nouns(text):
    tokenized = sent_tokenize(text)
    stop_words = set(stopwords.words("english"))
    parts_of_speech_tagged_words = list()
    for i in tokenized:
        words_list = nltk.word_tokenize(i)
        words_list = [w for w in words_list if not w in stop_words]
        parts_of_speech_tagged_words = parts_of_speech_tagged_words + pos_tag(nltk.word_tokenize(i))

    # print('pos-tagged:\n', parts_of_speech_tagged_words, '\n')
    proper_nouns = [word for word, pos in parts_of_speech_tagged_words if pos == 'NNP']

    result = dict()
    for item in proper_nouns:
        upper_cased = remove_leading_and_trailing_special_chars(str(item)).upper()

        if upper_cased.__len__() < 3: continue
        if result.get(upper_cased) is None:
            result[upper_cased] = 1
        else:
            result[upper_cased] = result[upper_cased] + 1

    return result


def get_keywords(text, max_number_of_proper_nouns=3, max_number_of_keywords=3):
    raw_keywords = generate_summa_keywords(text)
    # print('Summa Generated Keywords: Total:', raw_keywords.__len__(), '\n', raw_keywords)

    l = lemmatize(raw_keywords)
    # print('Lemmatized Keywords: Total:', l.__len__(), '\n', l)

    keywords_after_removing_stopwords = remove_stopwords(l)
    # print('stop words removed keywords: Total:', keywords_after_removing_stopwords.__len__(), '\n', keywords_after_removing_stopwords)

    sorted_keywords = sort_based_on_weight(keywords_after_removing_stopwords)
    # print('KEYWORDS:\n', sorted_keywords)

    proper_nouns = find_unique_proper_nouns(text)
    proper_nouns_after_removing_stop_words = remove_stopwords(proper_nouns)
    lemmatized_proper_nouns = lemmatize(proper_nouns_after_removing_stop_words)

    sorted_nouns = sort_based_on_weight(lemmatized_proper_nouns)
    # print('NOUNS:\n', sorted_nouns)
    sorted_nouns = sorted_nouns[:min(sorted_nouns.__len__(), max_number_of_proper_nouns)]
    sorted_nouns = [(str(x[0]).lower(), x[1]) for x in sorted_nouns]

    nouns_without_weight = [x[0] for x in sorted_nouns]
    keywords_not_in_nouns = list()
    for it, w in sorted_keywords:
        if it not in nouns_without_weight:
            keywords_not_in_nouns.append((it, w))

    total = sorted_nouns + keywords_not_in_nouns[:min(keywords_not_in_nouns.__len__(), max_number_of_keywords)]
    return total


# init_nltk()
# print(get_keywords(read_file('input.txt')))

# Keyword:
# find keywords : DONE
# remove stopwords : DONE
# lemmatize based on noun : DONE

# Proper Noun:
# find distinct proper nouns : DONE
# give them weight based on count : DONE
# lemmatize proper nouns : DONE
# remove stop_words from proper nouns : DONE

# Results:
# filter out the keywords that are already in proper nouns
# final result = proper nouns UNION keywords
