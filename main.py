import streamlit as st
import pandas

st.title('The Best Company')

lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed finibus eros in arcu commodo efficitur. Etiam 
finibus, tellus et tempus rhoncus, mi augue tempor nisi, eget aliquam nibh diam sit amet ex. Integer venenatis lacus 
vel justo lobortis, non ornare lectus volutpat. Proin blandit egestas elit, sit amet vehicula enim iaculis sit amet."""

st.write(lorem)


st.subheader('Our team')
df = pandas.read_csv('data.csv')


col1, col2, col3 = st.columns(3)

for index, row in df.iterrows():
    st.write(row['first name'])

