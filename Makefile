# Name: Ryan Gelston
# Assignment: Lab 5

clean:
	rm *.pyc 

textVectorizer: textVectorizer.py Vector.py Document.py Corpus.py
	python3 textVectorizer.py ./C50 -sw ./StopWords/stopwords-mysql.txt \
	--ground-truth ./ground_truth.csv
