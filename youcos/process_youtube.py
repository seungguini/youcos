import pandas as pd
import numpy as np
import nltk
nltk.download('punkt')
nltk.download('stopwords')

nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
from nltk.corpus import stopwords
import string
import contractions
import langdetect
from langdetect import detect 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer

def process_data():
    
    # Open file
    with open('../../data/youtube_comments.csv',encoding="utf8") as file:
        df = pd.read_csv(file,dtype=str,index_col=0)
    file.close()

    
    # processing values for video like, dislike, and comment upvotes
    # fill null values as 0 and replace abbreviations for k, m
    df['likes'].fillna("0", inplace=True)
    df['dislikes'].fillna("0", inplace=True)
    df['upvotes'].fillna("0", inplace=True)
    df['upvotes'].replace({'K': '*1e3', 'M': '*1e6'}, regex=True).map(pd.eval).astype(int)
   
  
    ### expanding contractions = don't --> do not ###
    # add a column with contractions removed
    df['no_contract'] = df['comment'].apply(lambda x: [contractions.fix(word) for word in x.split() ])
    
    # though sentences are tokenized, the contractions are tokenized into one token
    # i.e. We've --> ["we have"] instead of ["we", "have"]
    # we'll join the tokens back into singular strings so we can tokenize them later
    
    # map(str,l) takes the iterable l (all values in df['no_contract']) and stringifies it w/ str
    df['comments_str'] = [' '.join(map(str, l)) for l in df['no_contract']]

    # function to detect the language
    def detectLang(corpus) :
      try:
        lang = detect(corpus)
        if lang == 'en':
          return detect(corpus)
        else:
          return None
      except:
        return None
    
    # remove non-English comments
    df['lang'] = df['comments_str'].apply(lambda comment: detectLang(comment))
    df = df.dropna(subset=['lang'])
    
    #tokenize the comments using NLTK
    df['tokenized'] = df['comments_str'].apply(lambda x : word_tokenize(x))
    
    
    # convert characters to lowercase
    df['lower'] = df['tokenized'].apply(lambda x: [word.lower() for word in x])
    
    # remove punctuations
    punct = string.punctuation
    # make a list only if token is not a punctuation
    df['no_punct'] = df['lower'].apply(lambda x: [word for word in x if word not in punct])
    
    # remove stopwords
    stop_words = stopwords.words('english')
    df['no_stopwords'] = df['no_punct'].apply(lambda x: [word for word in x if word not in stop_words])
    
       
    # Normalization - lemmatizing
    df['pos_tags'] = df['no_stopwords'].apply(nltk.tag.pos_tag)
       
    # we convert the speech tags into the appropriate wordnet format
    def get_wordnet_pos(tag):
        if tag.startswith('J'):
            return wordnet.ADJ
        elif tag.startswith('V'):
            return wordnet.VERB
        elif tag.startswith('N'):
            return wordnet.NOUN
        elif tag.startswith('r'):
            return wordnet.ADV
        else:
            return wordnet.NOUN
    # replace the pos tag with wordnet tags
    df['wordnet_pos'] = df['pos_tags'].apply(lambda x : [(word, get_wordnet_pos(pos_tag)) for (word, pos_tag) in x])
    
    
    # lemmatize comments
    lemmatizer = WordNetLemmatizer()
    df['lemmatized'] = df['wordnet_pos'].apply(lambda x: [lemmatizer.lemmatize(word,tag) for (word,tag) in x])
    
    # drop unnecessary columns
    df.drop(['comment_posted','no_of_replies','downvotes','author','no_contract','tokenized','lower','no_punct','no_stopwords','pos_tags','wordnet_pos','lang'],axis=1, inplace=True)

    
    # finally, save cleaned data into csv file
    df.to_csv('../../data/youtube_comments_clean.csv')