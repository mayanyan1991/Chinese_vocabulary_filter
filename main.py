# coding = utf-8
import pandas as pd

def search_vol(list_char, list_dic):
    list_learned_vol = []
    for char in list_char: 
        for vol in list_dic:
            if char in vol:
                if all(item in list_char for item in vol):
                    list_learned_vol.append(vol)
    list_learned_vol = list(dict.fromkeys(list_learned_vol))
    return list_learned_vol
                    
            

# input all the vocabulary into dictionary
vol_dic = {}
keys = ["HSK1", "HSK2", "HSK3", "HSK4", "HSK5", "HSK6"]
for key in keys:
    vol_dic[key] = pd.read_csv(key+'.txt', sep='\t',
                        names=["simp_chinese", 
                        "trad_chinese", "pinyin_n", 
                        "pinyin", "meaning"])  
    vol_dic[key].dropna(subset=['simp_chinese'], inplace=True) 

# import the list of characters that have been learned
with open('learned.txt','r',encoding='utf-8') as f:
    learned_list = f.read()
learned_list = learned_list.split('\n')
#imput of new characters from users

new_char = input('Enter new characters you \
                have learned (using space to separeate):')

# append the new characters into list if not in the old list
learned_list.extend(new_char.split(' '))

# search for learned words in dictionary
vol_dic_learned = {}
   
for level in keys:
    vol_dic_learned [level]['simpl_chinese'] = search_vol(learned_list, vol_dic[level]
                                           ['simp_chinese'].values)
          
    
