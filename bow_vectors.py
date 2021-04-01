#Topic modelling applications recquire another bag: feature vectors
#feature vector = numeric representation of an item important features
#each geature has its own coulmn if feature exists for the item
#represent it with a 1 otherwise you could represent with a 0 
#Turning a text into a BoW vector is known as feature extraction or vectorization

#we generally create a features dict of all vocabularry in our training data 
#(usually several documents) mapped to indices

#with dict on hands we can converto new documents into vectors using
#a vectorization function. 

#soooo lets do it!!!

#First we need a way of generating a features dictionary from a list of 
#training documents

from preprocessing import preprocess_text


#documents is the list of string documents that we pass in
#merged receives the list in training_documents and turn it into a string
def create_features_dictionary(documents):
    features_dictionary  = {}
    merged = " ".join(documents)
    tokens = preprocess_text(merged)
    index = 0
    for token in tokens:
      if token not in features_dictionary:
        features_dictionary[token] = index
        index += 1
    return features_dictionary, tokens


training_documents = ["Five fantastic fish flew off to find faraway functions.", 
                      "Maybe find another five fantastic fish?", "Find my fish with a function please!"]

features_dictionary = create_features_dictionary(training_documents)
print(features_dictionary)

#AAAAnd now the BoW vector

def tokens_to_bow_vector(document_tokens, features_dictionary):
    bow_vector = [0] * len(features_dictionary)
    for token in document_tokens:
      if token in features_dictionary:
        feature_index = features_dictionary[token]
        bow_vector[feature_index] += 1
    return bow_vector

text = "Another five fish find another faraway fish."
print(tokens_to_bow_vector(text, features_dictionary))

# Define training_vectors:
#training_vectors = [tokens_to_bow_vector(training_doc, bow_sms_dictionary) for training_doc in training_spam_docs]

# Define test_vectors:
#test_vectors  = [tokens_to_bow_vector(test_doc, bow_sms_dictionary) for test_doc in test_spam_docs]


#WE CAN USE LIBRARIES FOR THE STUFF ABOVE
#For text_to_bow(), you can approximate the functionality with the collections 
#module’s Counter() function

#For vectorization, you can use CountVectorizer from the machine learning 
#library scikit-learn. You can use fit() to train the features dictionary and 
#then transform() to transform text into a vector


