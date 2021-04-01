import nltk, re
from nltk.corpus import wordnet
#from nltk.corpus import stopwords i got an error that told me to use the nltk downloader below
#nltk.download('stopwords') now is up to date just import
#nltk.download('punkt') had to download this for the tokenize
#nltk.download('wordnet') anf this for wordnet
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter

#Targeting stopwords in order to remove them this totally works and in
#my opinion is crucial for BoW
stop_words = stopwords.words('english')

#Now lets lemmatize it transforming words to their root forms
normalizer = WordNetLemmatizer()

#synset is like a dictionary, not py dict a real world dict itt gets meaning ans synonims
#counter builds a py dict count the no of times each obj appears
#the n v a r part I have to figure out cause this was built for a 
#specific exercise

def get_part_of_speech(word):
  probable_part_of_speech = wordnet.synsets(word)
  pos_counts = Counter()
  pos_counts["n"] = len(  [ item for item in probable_part_of_speech if item.pos()=="n"]  )
  pos_counts["v"] = len(  [ item for item in probable_part_of_speech if item.pos()=="v"]  )
  pos_counts["a"] = len(  [ item for item in probable_part_of_speech if item.pos()=="a"]  )
  pos_counts["r"] = len(  [ item for item in probable_part_of_speech if item.pos()=="r"]  )
  most_likely_part_of_speech = pos_counts.most_common(1)[0][0]
  return most_likely_part_of_speech


#removing everything that is not a string with re
#tokenize the text
#mormalize with lemmatization
def preprocess_text(text):
  cleaned = re.sub(r'\W+', ' ', text).lower()
  tokenized = word_tokenize(cleaned)
  normalized = [normalizer.lemmatize(token, get_part_of_speech(token)) for token in tokenized]
  return normalized