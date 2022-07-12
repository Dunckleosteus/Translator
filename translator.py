from deep_translator import GoogleTranslator
import pandas as pd 
import numpy as np

df = pd.read_excel (r"input.xlsx")# import excel into pandas  
df["en"] = "null"
df["fr"] = "null"
print(df) 
for ind in df.index : 
    english = GoogleTranslator(source='auto', target='en').translate(df['a'][ind])
    french = GoogleTranslator(source='auto', target='fr').translate(df['a'][ind])
    df["en"][ind] = english 
    df["fr"][ind] = french 
    per = round((ind/len(df.index))*100,2) 
    print ("{}/{}({}%) = {}/{}".format (ind, len(df.index),per ,english, french)) 
df.to_excel(r"translated_1.xlsx")
