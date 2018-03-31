from bs4 import BeautifulSoup
import pandas as pd
import urllib
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from nltk.classify import SklearnClassifier

import data_manipulation
import dictionary_create

import re

data = pd.read_excel('cik_list.xlsx')

data_manipulation.epitome_data()

#temp = [0,1,2,3,4,5,6,7,8,9,10,11];

row_sample = len(data)
row_list = list(range(0,row_sample))

Positive_Score_list = [0] * row_sample
Negative_Score_list = [0] * row_sample
Uncertainity_Score_list = [0] * row_sample
Constraining_Score_list = [0] * row_sample
Complex_Word_Count_list = [0] * row_sample
Polarity_Score_list = [0] * row_sample
Avg_Sentence_Length_list = [0] * row_sample
Percentage_of_Complex_Words_list = [0] * row_sample
Fog_Index_list = [0] * row_sample
num_of_words_list = [0] * row_sample

for i in row_list:
    link = 'https://www.sec.gov/Archives/'+(data['SECFNAME'][i])
    print(link)
    dat = urllib.request.urlopen(link)

    final_str = ""

    num_of_sentences = 0
    for line in dat:
        new_line = str(line, 'utf-8')
        final_str+=new_line
        num_of_sentences+=1

    stop_words = set(stopwords.words('english'))
    words = word_tokenize(final_str)
    filtered_words = []

    for w in words:
        if w not in stop_words:
            filtered_words.append(w)

    num_of_words = len(filtered_words);
    pos,neg,uncer,constrain,comple = dictionary_create.create_dictionary()
    Positive_Score = 0
    Negative_Score = 0
    Uncertainity_Score = 0
    Constraining_Score = 0
    Complex_Score = 0

    for w in filtered_words:
        if w in pos:
            Positive_Score+=1
        if w in neg:
            Negative_Score+=1
        if w in uncer:
            Uncertainity_Score+=1
        if w in pos:
            Constraining_Score+=1
        if w in comple:
            Complex_Score+=1

    print("Positive Score=",Positive_Score)
    print("Negative Score=",Negative_Score)
    print("Uncertainity Score=",Uncertainity_Score)
    print("Constraining Score=",Constraining_Score)
    print("Complex Word Count=",Complex_Score)

    Polarity_Score = ((Positive_Score - Negative_Score) / ((Positive_Score + Negative_Score) + 0.000001))
    print("Polarity Score=",Polarity_Score)

    Avg_Sentence_Length = num_of_words / num_of_sentences
    print("Avg Sentence Length=",Avg_Sentence_Length)

    Percentage_of_Complex_words = Complex_Score / num_of_words
    print("Percentage of Complex Words=",Percentage_of_Complex_words)

    Fog_Index = 0.4 * (Avg_Sentence_Length + Percentage_of_Complex_words)
    print("Fog_Index=",Fog_Index)

    print("Number of Words=",num_of_words)

    Positive_Score_list[i] = Positive_Score
    Negative_Score_list[i] = Negative_Score
    Uncertainity_Score_list[i] = Uncertainity_Score
    Constraining_Score_list[i] = Constraining_Score
    Complex_Word_Count_list[i] = Complex_Score
    Polarity_Score_list[i] = Polarity_Score
    Avg_Sentence_Length_list[i] = Avg_Sentence_Length
    Percentage_of_Complex_Words_list[i] = Percentage_of_Complex_words
    Fog_Index_list[i] = Fog_Index
    num_of_words_list[i] = num_of_words

data['Positive Score'] = Positive_Score_list
data['Negative Score'] = Negative_Score_list
data['Uncertainity Score'] = Uncertainity_Score_list
data['Constraining Score'] = Constraining_Score_list
data['Complex Word Count'] = Complex_Word_Count_list
data['Polarity Score'] = Polarity_Score_list
data['Average Sentence Length'] = Avg_Sentence_Length_list
data['% of Complex Word'] = Percentage_of_Complex_Words_list
data['Fog Index'] = Fog_Index_list
data['Number of Words'] = num_of_words_list

writer = pd.ExcelWriter('New_MasterDictionary_2014.xlsx')
data.to_excel(writer,sheet_name='Sheet1')
writer.save()

print(data.head())
