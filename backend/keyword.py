import nltk
from summa import keywords
from nltk.corpus import stopwords
from nltk.tag import pos_tag, pos_tag_sents
from nltk.stem.wordnet import WordNetLemmatizer

# from nltk.tokenize import sent_tokenize, word_tokenize

'''
Utils
'''
def read_file(file_name):
    file1 = open(file_name, "r", encoding='UTF-8')
    return file1.read()

def sort_based_on_weight(words):
    return sorted(words.items(), key=lambda x: x[1], reverse=True)


'''
Nltk:
All functions except init_nltk() returns a dictionary where key==word_string and value==weight_float
'''
def init_nltk():
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('words')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('maxent_ne_chunker')

def remove_stopwords(input_words: dict):
    words = dict()
    stop_words = set(stopwords.words("english"))
    for k,v in input_words.items():
        if k in stop_words:
            print('Removed StopWord', k)
        else:
            words[k]=v
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


def generate_summa_keywords(text):
    _keywords = list()
    try:
        _keywords = dict(keywords.keywords(text, scores=True))
    except UnicodeDecodeError:
        print('UnicodeDecodeError: generating keywords')

    return _keywords


def find_proper_nouns(text):

    parts_of_speech_tagged_words = pos_tag(text.split())
    print('\n', parts_of_speech_tagged_words, '\n')
    proper_nouns = [word for word,pos in parts_of_speech_tagged_words if pos == 'NNP']

    # remove
    # for item in proper_nouns:
    #     if str(item[0]).isalnum():

    return proper_nouns


def process(text):
    raw_keywords = generate_summa_keywords(text)
    print('Summa Generated Keywords: Total:', raw_keywords.__len__(), '\n', raw_keywords)

    l = lemmatize(raw_keywords)
    print('Lemmatized Keywords: Total:', l.__len__(), '\n', l)

    after_removing_stopwords = remove_stopwords(l)
    print('stop words removed keywords: Total:', after_removing_stopwords.__len__(), '\n', after_removing_stopwords)

    proper_nouns = find_proper_nouns(text)
    print(proper_nouns)


init_nltk()
process(read_file('input.txt'))


# TODO Keyword:
# find keywords : DONE
# remove stopwords : DONE
# lemmatize based on noun : DONE
# idea: filter out keywords that are not nouns?

# TODO Proper Noun:
# find proper nouns
# remove special characters at the beginning or end of proper nouns
# give them weight based on count

# TODO Union Both Results:
# weight of proper nouns = max_weight of keywords * count
# final result = distinct(top x keywords with non-negligible weight (Union) top x proper nouns)