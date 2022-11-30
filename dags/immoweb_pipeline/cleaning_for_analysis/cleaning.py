import pandas as pd
import numpy as np
from utils.up_load import upload_file
from utils.download import download_file
import os

downloaded_file = os.path.join(os.getcwd(),'data/downloaded_entries.csv')

download_file(downloaded_file,'ahmet_newentries.csv')

df = pd.read_csv(downloaded_file)

df.drop_duplicates(inplace=True)

df.dropna(subset=['Price'], inplace=True)

df.replace(to_replace=['Null'], value=np.nan, inplace=True)

df['Furnished'].fillna(False, inplace=True)
df['Swimming_pool'].fillna(False, inplace=True)
df['Open_fire'].fillna(False, inplace=True)


to_int = ['Number_of_bedrooms', 'Number_of_facades', 'Garden_surface', 'Postal_code', 'Land_surface',
          'Terrace_surface', 'Surface', 'Price', 'Indoor_parking', 'Outdoor_parking']
for column in to_int:
    df[column] = df[column].astype('Int64')

cleaned_file = os.path.join(os.getcwd(),'data/cleaned_entries.csv')

with open(cleaned_file, 'w') as file:
    df.to_csv(file, index=False)

upload_file(cleaned_file,'ahmet_new_cleaned.csv')