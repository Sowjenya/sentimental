import numpy as np
import pandas as pd
import os
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob
lemmatizer = WordNetLemmatizer()
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import nltk
nltk.download('punkt')
import nltk
nltk.download('wordnet')
import nltk
nltk.download('omw-1.4')
import nltk
nltk.download('vader_lexicon');

def analysis(data_value):
    var=stopwords.words('english');
    var.remove('not')
    pd.read_csv('C:\\Users\\sowjenya\\Downloads\\chrome_reviews.csv')
    data = data_value;
    data.head()
    clean_text =[]
    for review in data['Text']:
        review= re.sub(r'[^\w\s]', '', str(review));
        review_token = re.sub(r'\d','',review);
        review_without_stopwords=[]
        for token in review_token:
            if token not in var:
                token= lemmatizer.lemmatize(token)
                review_without_stopwords.append(token)
        cleaned_review = " ".join(review_without_stopwords)
        clean_text.append(cleaned_review)


    data["cleaned_review"] = clean_text
    Single_star_reviews = data[data.Star ==1]

    sia = SentimentIntensityAnalyzer()
    senti_list = []

    for i in Single_star_reviews["Text"]:
        score = sia.polarity_scores(i)
        blob_score = TextBlob(i).sentiment.polarity
        if (score['pos'] >= 0.5):
            senti_list.append('Positive')
        else:
            senti_list.append('Negative/Neutral')
            
    Single_star_reviews["sentiment"]= senti_list

    Single_star_reviews.head()

    positive_review_with_1_star = Single_star_reviews[Single_star_reviews.sentiment == 'Positive']

    positive_review_with_1_star.drop("cleaned_review",axis = 1,inplace=True)

    return positive_review_with_1_star.head();
