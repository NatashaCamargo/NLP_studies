from preprocessing import preprocess_text


def text_to_bow(some_text):
    bow_dictionary = {}
    tokens = preprocess_text(some_text)
    for token in tokens:
        if token in bow_dictionary:
            bow_dictionary[token] += 1
        else:
            bow_dictionary[token] = 1
    return bow_dictionary


my_text = '''Athena or Athene, often given the epithet Pallas, is 
an ancient Greek goddess associated with wisdom, handicraft, and warfare who
 was later syncretized with the Roman goddess Minerva. Athena was regarded as
 the patron and protectress of various cities across Greece, particularly the
 city of Athens, from which she most likely received her name. The Parthenon
 on the Acropolis of Athens is dedicated to her. Her major symbols include 
 owls, olive trees, snakes, and the Gorgoneion. In art, she is generally 
 depicted wearing a helmet and holding a spear.'''
 
print(text_to_bow(my_text))