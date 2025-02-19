import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


st.title("Nadpis - Cheers mate")
st.write(
    "Write pro nejaky text - Cau bro menim text"
)

#Klasicka pandas DataFrame
data = pd.DataFrame({
    "Kategorie" : ["A","B","C","D"],
    "Hodnoty" : [25,40,50,70]
})

# tady nadpis ve streamlitu 
st.write("Tabulka s datama:")

# st.dataframe vytvari tabulku ve streamlitu (tzn. zobrazí ji v aplikaci) - POZOR rozlisovat pd.DataFrame pro pandas a st.dataframe pro streamlit
st.dataframe(data)


#Graf 
# object fig - odporně "figure", můžu samozřejmě si to pojmenovat, jak chci, ale jsem profesionál :D
# btw zalamuju kód jako profik :D jinak je to tohle fig = px.bar(data, x="Kategorie", y="Hodnoty", title= "Sloupcovy graf plotlib")
#Graf sloupcovy bar()
fig = px.bar(
    data, x="Kategorie",
    y="Hodnoty",
    title= "Sloupcovy graf plotlib"
)

st.plotly_chart(fig)


# Buttony / Tlačítka

if st.button("Informacni okno:"):

    # informacni okno se dela pres st.info
    st.info("Ahoj, kliknul jsi - toto je informacni okno")

if st.button("Upozorneni okno"):
    # upozornovaci okno pres warning()
    st.warning("Kliknul jsi - tohle je varovani/warning")

if st.button("Chybove okno"):
    # chybove okno se dela pres error()
    st.error("Kliknul jsi - tohle je error okno")


# Vstup/user input (textový vstup od uzivatele)

# textový vstup od uzivatele
user_input = st.text_input("Jak se jmenujes:")
st.write(f"Jmenuje se: {user_input}")

# Editovatelna tabulka
# V kontextu - výše v kódu jsme si vyrobili tabulku a nyní ji chci editovat
#"data" je pro me ta promenna z vyse ...
edited_table = st.data_editor(data, num_rows="dynamic", use_container_width=True)

st.write("Nova editovana tabulka")
st.dataframe(edited_table, use_container_width=True)

#Graf upraveny
# CO je cíl, výše je editovatelná tabulka a my chceme kolacovy graf, aby mel ty hodnoty z te editovane tabulky

fig = px.bar(
    edited_table, 
    x="Kategorie",
    y="Hodnoty",
    title= "Upraveny sloupcovy graf plotlib"
)

st.plotly_chart(fig)

#Graf kolacovy

fig_pie = px.pie(
    edited_table, 
    names = "Kategorie",
    values = "Hodnoty",
    title = "Kolacovy graf plotlib"
)

st.plotly_chart(fig_pie)

#
