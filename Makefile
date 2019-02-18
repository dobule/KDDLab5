# Name: Ryan Gelston
# Assignment: Lab 5

clean:
	rm *.pyc 

textVectorizer: textVectorizer.py Vector.py Document.py Corpus.py
	python3 textVectorizer.py ./TestData -sw ./StopWords/stopwords-onyx.txt \
	--ground-truth ./ground_truth.csv


textVectorizer-onyx: textVectorizer.py Vector.py Document.py Corpus.py \
	./StopWords/stopwords/onyx.txt
	python3 textVectorizer.py ./C50 -sw ./StopWords/stopwords-onyx.txt \
	--ground-truth ./C50_Vectors/onyx/ground_truth.csv \
	--output ./C50_Vectors/onyx/vectors.csv

textVectorizer-onyx-stem: textVectorizer.py Vector.py Document.py Corpus.py \
	./StopWords/stopwords/onyx.txt
	python3 textVectorizer.py ./C50 -sw ./StopWords/stopwords-onyx.txt \
	--ground-truth ./C50_Vectors/onyx-stem/ground_truth.csv \
	--output ./C50_Vectors/onyx-stem/vectors.csv \
    --stem


textVectorizer-mysql: textVectorizer.py Vector.py Document.py Corpus.py \
	./StopWords/stopwords/mysql.txt
	python3 textVectorizer.py ./C50 -sw ./StopWords/stopwords-mysql.txt \
	--ground-truth ./C50_Vectors/mysql/ground_truth.csv \
	--output ./C50_Vectors/mysql/vectors.csv

textVectorizer-mysql-stem: textVectorizer.py Vector.py Document.py Corpus.py \
	./StopWords/stopwords/mysql.txt
	python3 textVectorizer.py ./C50 -sw ./StopWords/stopwords-mysql.txt \
	--ground-truth ./C50_Vectors/mysql-stem/ground_truth.csv \
	--output ./C50_Vectors/mysql-stem/vectors.csv \
    --stem

textVectorizer-short: textVectorizer.py Vector.py Document.py Corpus.py \
	./StopWords/stopwords/short.txt
	python3 textVectorizer.py ./C50 -sw ./StopWords/stopwords-short.txt \
	--ground-truth ./C50_Vectors/short/ground_truth.csv \
	--output ./C50_Vectors/short/vectors.csv 

textVectorizer-short-stem: textVectorizer.py Vector.py Document.py Corpus.py \
	./StopWords/stopwords/short.txt
	python3 textVectorizer.py ./C50 -sw ./StopWords/stopwords-short.txt \
	--ground-truth ./C50_Vectors/short-stem/ground_truth.csv \
	--output ./C50_Vectors/short-stem/vectors.csv \
    --stem

textVectorizer-medium: textVectorizer.py Vector.py Document.py Corpus.py \
	./StopWords/stopwords/medium.txt
	python3 textVectorizer.py ./C50 -sw ./StopWords/stopwords-medium.txt \
	--ground-truth ./C50_Vectors/medium/ground_truth.csv \
	--output ./C50_Vectors/medium/vectors.csv

textVectorizer-medium-stem: textVectorizer.py Vector.py Document.py Corpus.py \
	./StopWords/stopwords/medium.txt
	python3 textVectorizer.py ./C50 -sw ./StopWords/stopwords-medium.txt \
	--ground-truth ./C50_Vectors/medium-stem/ground_truth.csv \
	--output ./C50_Vectors/medium-stem/vectors.csv \
    --stem

textVectorizer-long: textVectorizer.py Vector.py Document.py Corpus.py \
	./StopWords/stopwords/long.txt
	python3 textVectorizer.py ./C50 -sw ./StopWords/stopwords-long.txt \
	--ground-truth ./C50_Vectors/long/ground_truth.csv \
	--output ./C50_Vectors/long/vectors.csv

textVectorizer-long-stem: textVectorizer.py Vector.py Document.py Corpus.py \
	./StopWords/stopwords/long.txt
	python3 textVectorizer.py ./C50 -sw ./StopWords/stopwords-long.txt \
	--ground-truth ./C50_Vectors/long-stem/ground_truth.csv \
	--output ./C50_Vectors/long-stem/vectors.csv \
    --stem

