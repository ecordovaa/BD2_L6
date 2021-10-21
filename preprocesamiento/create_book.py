import nltk
from nltk.stem.snowball import SnowballStemmer

# Abrimos y registramos las stopwords
def define_stopwords():
	with open('preprocesamiento/stoplist.txt') as stoplist:
		return nltk.word_tokenize(stoplist.read().lower())

# Añadimos algunos símbolos considerados innecesarios para el ejercicio
def remove_symbols(word):
	symbols = {"<", ">", ",", "º", ":", ";", "«", "»", ".", "!", "¿", "?", ")", "("}
	filter = ""
	for statement in word:
		if(statement in symbols):
			statement = statement.replace(statement, "")
		filter += statement
	return filter

# Lee un libro y crea una copia preprocesada según lo visto en clase
def read_book(book_id):
	stopwords = define_stopwords()
	stemmer = SnowballStemmer(language='spanish') # Ver informe
	with open("preprocesamiento/books/"+str(book_id)+".txt") as book, open("preprocesamiento/preprocesados/"+str(book_id)+".txt", 'w') as result:
		for term in book.read().split():
			term = term.lower()
			term = remove_symbols(term)
			if term not in stopwords:
				term = stemmer.stem(term)
				result.write(term + "\n")