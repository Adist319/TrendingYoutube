<<<<<<< Updated upstream
import streamlit as st
=======
import datetime
import os

>>>>>>> Stashed changes
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import streamlit as st
import janitor

<<<<<<< Updated upstream
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
start_date = st.date_input('Start date', today)
end_date = st.date_input('End date', tomorrow)
if start_date < end_date:
    st.success(f'Start date (Minimum: January 12 2017): {start_date} \n\nEnd date (Maximum: May 31 2018): {end_date}')
else:
    st.error('Error: End date must fall after start date.')
=======
# st.beta_set_page_config(page_title='YouTube Trending Statistics', page_icon = favicon, layout = 'wide', initial_sidebar_state = 'auto')
start_date = st.date_input('Date range (Minimum: January 12 2017, Maximum: May 31 2018): ',
                           value=datetime.date(2017, 1, 12), min_value=datetime.date(2017, 1, 12),
                           max_value=datetime.date(2018, 5, 31), key=4)
end_date = st.date_input('Date range (Minimum: January 12 2017, Maximum: May 31 2018): ',
                         value=datetime.date(2017, 1, 12), min_value=datetime.date(2017, 1, 12),
                         max_value=datetime.date(2018, 5, 31), key=6)
>>>>>>> Stashed changes

for dirname, _, filenames in os.walk('C:/Users/Minh The Nguyen/Documents/GitHub/TrendingYoutube'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
nRowsRead = None  # specify 'None' if want to read whole file
df1 = pd.read_csv('C:/Users/Minh The Nguyen/Documents/GitHub/TrendingYoutube/USvideos.csv', delimiter=',',
                  nrows=nRowsRead)
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
<<<<<<< Updated upstream
descending_views = st.sidebar.selectbox('Input maximum view count:', )
# TODO: Dates start at 17.01.12 and ends at 18.31.05. We need to ensure that the user inputs dates within that range.
=======
sort_by = st.selectbox("What metric do you want to sort by?",
                       ('Number of views', 'Number of likes', 'Number of dislikes', 'Number of comments'))
df = pd.DataFrame({
    'Trending Date': dates,
    'Link': link,
    'Title': title,
    'Views': views,
    'Likes': likes,
    'Dislikes': dislikes,
    'Comment count': comments
})

# i think the code should be correct, but it isn't actually doing anything :/
cleaned_df = df.filter_date('Trending Date', start_date, end_date)
cleaned_df

>>>>>>> Stashed changes
# TODO: Once the table is set up properly, with the results filtered by start and end date, we can include a SelectBox
#  to display certain metrics like the ones we defined above sorted in descending order.
# TODO: filter them out based on the given start and end dates.
# TODO if time permits: sort the filtered videos by the given metrics (views, likes, dislikes, comment_count).
#   (for the above: you can already sort the videos by certain metrics using the column header, so i think this might be redundant)
# TODO: filter out duplicate titles.


<<<<<<< Updated upstream
st.dataframe({"Link": link, "Trending Date": dates, "Title": title, "Views": views, "Likes": likes, "Dislikes": dislikes, "Comment count": comments})
# Adrian sucks.
=======
df = pd.DataFrame({
    'Trending Date': dates,
    'Link': link,
    'Title': title,
    'Views': views,
    'Likes': likes,
    'Dislikes': dislikes,
    'Comment count': comments
})
if sort_by == 'Number of views':
    df.sort_values(by='Views', ascending=True)
df
>>>>>>> Stashed changes
