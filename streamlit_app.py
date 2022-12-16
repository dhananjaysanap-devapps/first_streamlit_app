
import streamlit
import pandas

streamlit.title('My parent new healty dinner')
streamlit.header('Breakfast Menu')
streamlit.text ('🥣Omega 3 & bulberry otmeal')
streamlit.text ( '🥗Spinach & Rrocket Somuthi ')
streamlit.text( '🐔Heard bolied eggs')
streamlit.text('🥑🍞Advaco toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
