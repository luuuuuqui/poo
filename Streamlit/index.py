import streamlit as st

st.title("Agenda")
st.write("Bem-vindo à sua agenda!")

# Exibir conteúdo de um arquivo .txt
with open("beemovie.txt", "r", encoding="utf-8") as f:
    beemoviescript = f.read()


st.subheader("Bee Movie:")
st.write(beemoviescript)

with open("bark.txt", "r", encoding="utf-8") as f:
    bark = f.read()

st.subheader("Bark:")
st.write(bark)

with open("thegame.txt", "r", encoding="utf-8") as f:
    aioshdioasd = f.read()

st.subheader("Conteúdo do arquivo:")
st.write(aioshdioasd)
st.image('https://github.com/dy0gu/dy0gu/blob/main/shrek.gif?raw=true', caption='Shrek')