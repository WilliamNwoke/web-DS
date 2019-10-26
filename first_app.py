import streamlit as st
import pandas as pd
import numpy as np
import time

st.title('My first app')

st.write()
st.write("Here's our first attempt at using data to create a table:")

st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

#or 
#python 3 streamlit magic commands

"""
# My first app
Here's our first attempt at uing data to create a table:
"""

df = pd.DataFrame({
    'third column': [1,2,3,4],
    'fourth column': [10,20,30,40]
})

df

#draw a line chart 
#using st.line_chart()

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a','b','c']
)

st.line_chart(chart_data)
#plot a map
#use st.map()
map_data = pd.DataFrame(
    np.random.randn(1000,2) / [50,50] + [37.76, -122.4],
    columns=['lat','lon'])

st.map(map_data)

#adding Interactivity
#check boxes
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

#select boxes
option = st.selectbox(
    'Which number do you like best?',
     df['third column'])

'You selected: ', option

#putting widgets  sidebar
option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['fourth column'])

'You selected:', option

st.progress()

## Time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'