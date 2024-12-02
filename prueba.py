
import nltk
texto=input("texto:")
def preprocess_input(text):
	sentences = nltk.sent_tokenize(text)
	tokens = [nltk.word_tokenize(sentence) for sentence in sentences]
	return tokens

print(preprocess_input(texto))