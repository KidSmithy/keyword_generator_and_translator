import pandas as pd
import streamlit as st
from st_aggrid import AgGrid    

from deep_translator import GoogleTranslator

st.set_page_config(
    page_title = ' Keyword Generation',
    page_icon = ':a:',
    layout = 'wide'
)

words = ["limited","affordable","unique","singapore"]
Languages = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'assamese': 'as', 'aymara': 'ay', 'azerbaijani': 'az', 'bambara': 'bm', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bhojpuri': 'bho', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-CN', 'chinese (traditional)': 'zh-TW', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dhivehi': 'dv', 'dogri': 'doi', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'ewe': 'ee', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'guarani': 'gn', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'iw', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'ilocano': 'ilo', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'kinyarwanda': 'rw', 'konkani': 'gom', 'korean': 'ko', 'krio': 'kri', 'kurdish (kurmanji)': 'ku', 'kurdish (sorani)': 'ckb', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lingala': 'ln', 'lithuanian': 'lt', 'luganda': 'lg', 'luxembourgish': 'lb', 'macedonian': 'mk', 'maithili': 'mai', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'meiteilon (manipuri)': 'mni-Mtei', 'mizo': 'lus', 'mongolian': 'mn', 'myanmar': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia (oriya)': 'or', 'oromo': 'om', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'quechua': 'qu', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'sanskrit': 'sa', 'scots gaelic': 'gd', 'sepedi': 'nso', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'tatar': 'tt', 'telugu': 'te', 'thai': 'th', 'tigrinya': 'ti', 'tsonga': 'ts', 'turkish': 'tr', 'turkmen': 'tk', 'twi': 'ak', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}

# Print list of words
products = ['reed diffuser', 'Pure Essential Oil', 'Skin-safe Essential Oils', 'reed diffuser gift sets']

if "button_click" not in st.session_state:
    st.session_state.button_click = False

if "output" not in st.session_state:
    st.session_state.output = False

if "translate" not in st.session_state:
    st.session_state.translate = False

def onClickFunction():
    st.session_state.button_click = True

def onoutputFunction():
    st.session_state.output = True
    st.session_state.button_click = True
    st.session_state.data = keywords_df
    

def ontranslateFunction():
    st.session_state.output = True
    st.session_state.button_click = True
    st.session_state.translate = True
    # st.session_state.data = keywords_df


if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

word_df =  pd.DataFrame(words)
# print(word_df)
products_df =  pd.DataFrame(products)
word_df = word_df.rename(columns={0: 'Words'})

products_df = products_df.rename(columns={0: 'Products'})


# grid_return_word = AgGrid(word_df, editable=True)
# grid_return_products = AgGrid(products_df, editable=True)
# new_word_df = grid_return_word['data']
# new_products_df = grid_return_products['data']
# print(new_word_df)
# print(new_products_df)
st.title("Keyword Generation Application + Translation")
col1,col3, col2 = st.columns((10,2,10))
with col1:
    st.header("Add , Edit, and Delete the Words You want to add before the product ")
    grid_return_word = st.experimental_data_editor(word_df, num_rows='dynamic')
with col2:
    st.header("Here lies the Product List, feel free to Add, Edit, and Delete  ")
    grid_return_products = st.experimental_data_editor(products_df, num_rows='dynamic')
# Create an empty list
keywords_list = []

new_words = grid_return_word["Words"].values.tolist()
new_products = grid_return_products["Products"].values.tolist()
# Loop through products

# def function_words():
for product in new_products:
    # Loop through words    
    for word in new_words:
        # Append combinations
        # keywords_list.append([product, product + ' ' + word])
        keywords_list.append([product, word + ' ' + product])
    
# Inspect keyword list

keywords_df = pd.DataFrame.from_records(keywords_list)

keywords_df = keywords_df.rename(columns={0: 'Product', 1: 'Keyword'})

# function_words.keywords_df = keywords_df

# keywords_df['Campaign'] = 'SEM_Sofas'

# keywords_df['Criterion Type'] = 'Exact'
reload_data = False

if "data" not in st.session_state:
    st.session_state.data = keywords_df
# function_words()
# keywords_df_2 = function_words.keywords_df
st.button('Start Keyword Generation', on_click=onClickFunction)
if  (st.session_state.button_click == True or st.session_state.button_click):
        
        


        option2 = st.selectbox('Choose which language you want to change your keyword to',
                            ('indonesian','malayalam', 'afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish', 'dutch', 'english', 'esperanto', 'estonian', 'filipino', 'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo',  'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish (kurmanji)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy', 'malay', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 'norwegian', 'odia', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'turkmen', 'ukrainian', 'urdu', 'uyghur', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu')
                                    ,on_change=onoutputFunction)


        value2 = Languages[option2]
        

        translate = st.button('Translate keywords', on_click=ontranslateFunction)
        if translate:
            keywords_df = st.session_state.data
            new_keywords_list = []

            new_words = keywords_df["Keyword"].values.tolist()
            for newword in new_words:
                translate_word = GoogleTranslator(source='auto', target=value2).translate(newword)
                # print(translate_word)
                new_keywords_list.append(translate_word)
            keywords_df[option2] = new_keywords_list
            keywords_df = keywords_df
            st.session_state.data = keywords_df
            

        AgGrid(st.session_state.data, editable=True,reload_data=True)
      
            
