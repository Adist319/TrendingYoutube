import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import datetime
import os

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
start_date = st.date_input('Start date', today)
end_date = st.date_input('End date', tomorrow)
if start_date < end_date:
    st.success(f'Start date (Minimum: January 12 2017): {start_date} \n\nEnd date (Maximum: May 31 2018): {end_date}')
else:
    st.error('Error: End date must fall after start date.')

for dirname, _, filenames in os.walk('C:/Users/ongad/OneDrive/Desktop/CruzHacks Data'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
nRowsRead = None  # specify 'None' if want to read whole file
df1 = pd.read_csv('C:/Users/ongad/OneDrive/Desktop/CruzHacks Data/USvideos.csv', delimiter=',', nrows=nRowsRead)
df1.dataframeName = 'USvideos.csv'
nRow, nCol = df1.shape

# define variables for video link, title, views, likes, dislikes, comments, date columns
link = df1.video_id
title = df1.title
views = df1.views
likes = df1.likes
dislikes = df1.dislikes
comments = df1.comment_count
dates = df1.Date_YYMMDD
print(f'There are {nRow} rows and {nCol} columns')
df1.head(5)
# TODO: Create the select boxes to help filter out the videos
descending_views = st.sidebar.selectbox('Input maximum view count:', )
# TODO: Dates start at 17.01.12 and ends at 18.31.05. We need to ensure that the user inputs dates within that range.
# TODO: Once the table is set up properly, with the results filtered by start and end date, we can include a SelectBox
#  to display certain metrics like the ones we defined above sorted in descending order.
# TODO: filter them out based on the given start and end dates.
# TODO if time permits: sort the filtered videos by the given metrics (views, likes, dislikes, comment_count).

st.dataframe({"Link": link, "Trending Date": dates, "Title": title, "Views": views, "Likes": likes, "Dislikes": dislikes, "Comment count": comments})
# Adrian sucks.