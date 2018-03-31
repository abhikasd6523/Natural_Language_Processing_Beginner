import pandas as pd
import openpyxl

def epitome_data():
    data = pd.read_excel('MasterDictionary_2014.xlsx')

    new_data = data[['Word','Negative','Positive','Uncertainty','Constraining','Syllables']]

    writer = pd.ExcelWriter('MasterDictionary_editted_2014.xlsx')
    new_data.to_excel(writer,sheet_name='Sheet1')
    writer.save()