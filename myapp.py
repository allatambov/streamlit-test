import streamlit as st

from string import punctuation
from wordcloud import WordCloud, STOPWORDS
from matplotlib import pyplot as plt

files = {"hamlet.txt" : "Hamlet",
         'macbeth.txt': "Macbeth", 
         'midsummer.txt' : "A Midsummer Night's Dream", 
         "romeo-juliet.txt" : "Romeo and Juliet"}

def read_clean_text(filename):
    file = open(filename)
    lines = file.readlines()
    clean = [line.strip() for line in lines]
    final = list(filter(lambda x: x != '', clean))
    text = "\n".join(final)
    return text

def get_cleaned_words(text):
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, " ")
    words = text.split()
    words_str = " ".join(words)
    return words_str

def show_cloud(choice, color):
    fig, ax = plt.subplots(figsize = (8, 4.5), dpi = 200) 
    wcloud = WordCloud(stopwords = STOPWORDS, 
                       background_color = color,
                       max_words=50).generate(words[choice])
    plt.imshow(wcloud, interpolation="bilinear")
    plt.axis("off")
    fig.savefig("cloud.png")

texts = {}
for file, name in files.items():
    texts[name] = read_clean_text(file)
    
words = {}
for name, text in texts.items():
    words[name] = get_cleaned_words(text)    

plays = list(files.values())

st.title("Now we will generate wordclouds for Shakespeare's plays!")
box = st.selectbox('Choose a play', plays)
color = st.radio('Choose backgroud color', ['white', 'black'])
button = st.button("Get the cloud!")

show_cloud(box, color)

if button:
    st.image('cloud.png', use_column_width=True)
else:
    st.write("Just wait")



