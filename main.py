import streamlit as st
import pandas

st.set_page_config(layout='wide')

st.title('The Best Company')

lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed finibus eros in arcu commodo efficitur. Etiam 
finibus, tellus et tempus rhoncus, mi augue tempor nisi, eget aliquam nibh diam sit amet ex. Integer venenatis lacus 
vel justo lobortis, non ornare lectus volutpat. Proin blandit egestas elit, sit amet vehicula enim iaculis sit amet."""
st.write(lorem)

st.subheader('Our team')


df = pandas.read_csv('data.csv')
col1, col2, col3 = st.columns(3)

with col1:
    for index, row in df[:4].iterrows():
        full_name = ((row['first name']) + " " + (row['last name'])).title()
        st.header(full_name)
        st.write(row['role'])
        st.image('images/' + row['image'])
with col2:
    for index, row in df[4:8].iterrows():
        full_name = ((row['first name']) + " " + (row['last name'])).title()
        st.header(full_name)
        st.write(row['role'])
        st.image('images/' + row['image'])
with col3:
    for index, row in df[8:].iterrows():
        full_name = ((row['first name']) + " " + (row['last name'])).title()
        st.header(full_name)
        st.write(row['role'])
        st.image('images/' + row['image'])
