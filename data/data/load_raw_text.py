import pandas
import re
import numpy
from nltk.corpus import stopwords
import string
from nltk.stem import WordNetLemmatizer

def normalize(df):
    stop_words=stopwords.words("english")
    stop_words.extend(['the','at','well','here'," com"])
    lemmatizer = WordNetLemmatizer()
    return_val=[]
    regex=r'<.*?>|{.*?}'
    pattern  = re.compile(regex)
    regrex2=r'\w*\d+\w*|\s{2,}|http\S+|https\S+|[a-z]+\'+[a-z]|[a-z]+/+[a-z]|\s+[a-zA-Z]\s+'
    pattern2= re.compile(regrex2)
    regrex3=r'\b\w{1,3}\b'
    pattern3= re.compile(regrex3)
    for sen in df:
        
        val=(tf.strings.lower(sen)).numpy()
        val=val.decode('utf-8')
        val=val.encode('ascii','ignore').decode()
        val=re.sub(pattern2," ", val)
        val=re.sub(pattern, " ", val)
        val=re.sub('[%s]' % re.escape(string.punctuation), ' ', val) # remove punctutation
        val=' '.join([word for word in val.split(' ') if word not in stop_words])
        
        word_list=nltk.word_tokenize(val)
        val=' '.join([lemmatizer.lemmatize(w) for w in word_list])
        
        val=re.sub(pattern3," ",val)
        return_val.append(val)
    return seqs

def load_pretrain(path):
    data = pandas.read_csv(path).values
    return normalize(data[:, 1].astype('str')), normalize(data[:, 2].astype('str'))

def load(path):
    def cut_of90(labels):
        val_y = list(set(labels))
        val_y.sort()
        l_dict = dict()
        for i, val in enumerate(val_y): l_dict[int(val)] = i

        count_y = [0] * len(val_y)
        for label in labels:
            count_y[l_dict[int(label)]] += 1

        n_samples = len(labels)
        s, threshold = 0, 0
        for i, c in enumerate(count_y):
            s += c
            if s * 10 >= n_samples * 9:
                threshold = val_y[i]
                break
        for i, l in enumerate(labels):
            labels[i] = min(threshold, l)

        return labels.astype('float32')

    data = pandas.read_csv(path).values
    title = normalize(data[:, 1].astype('str'))
    description = normalize(data[:, 2].astype('str'))
    labels = data[:, 3].astype('float32')

    return title, description, cut_of90(labels)

'''
val_y
[1.0, 2.0, 3.0, 5.0, 8.0]
l_dict
{1: 0, 2: 1, 3: 2, 5: 3, 8: 4}
count_y
[0, 0, 0, 0, 0]
count_y
[160, 115, 573, 1134, 937]
'''