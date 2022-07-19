import translators as ts 
import pandas as pd 
import numpy as np
from tqdm import tqdm

tqdm.pandas() # used to create completion progress bar 

df = pd.read_excel (r"translated_1.xlsx")# import excel into pandas  
#df['en_deepL'] = df['a'].progress_apply(lambda x: ts.deepl(x, from_language= 'zh', to_language='en'))
df['en_cayun'] = df['a'].progress_apply(lambda x: ts.caiyun(x, from_language='zh', to_language='fr', professional_field = 'law'))
'''
print("google translate mandarin to english...")
df['en_google'] = df['a'].progress_apply(lambda x: ts.google(x, from_language='zh', to_language='en'))
print("google translate mandarin to french...")
df['fr_googgle'] = df['a'].progress_appy(lambda x: ts.google(x,from_language='zh', to_language='fr'))
'''
df.to_excel(r"translated.xlsx") # save output to excel 
