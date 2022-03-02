from gensim.parsing.preprocessing import remove_stopwords

text = "Nick likes to play football, however he is not too fond of tennis."
filtered_sentence = remove_stopwords(text)

print(filtered_sentence)
