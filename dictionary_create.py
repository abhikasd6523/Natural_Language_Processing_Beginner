import pandas as pd

def create_dictionary():
    data = pd.read_excel('MasterDictionary_editted_2014.xlsx')



    positive_words = []
    negative_words = []
    uncertainty_words = []
    constraining_words = []
    complex_words = []

    for index,row in data.iterrows():
        if (row['Positive'] != 0):
            positive_words.append(row['Word'])

        if (row['Negative'] != 0):
            negative_words.append(row['Word'])

        if (row['Uncertainty'] != 0):
            uncertainty_words.append(row['Word'])

        if (row['Constraining'] != 0):
            constraining_words.append(row['Word'])

        if (row['Syllables'] > 2):
            complex_words.append(row['Word'])

    return positive_words,negative_words,uncertainty_words,constraining_words,complex_words
