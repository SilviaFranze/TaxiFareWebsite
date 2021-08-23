import streamlit as st
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
    # Taxifare
    ## by Le Wagon
''')
       
'''
 ## Select a parameter
'''

if st.checkbox('date and time'):
    st.write()
if st.checkbox('pickup longitude'):
    st.write()
if st.checkbox('pickup latitude'):
    st.write()
if st.checkbox('dropoff longitude'):
    st.write()
if st.checkbox('dropoff latitude'):
    st.write()
if st.checkbox('passenger count'):
    st.write()

title = st.text_input('date and time','2012-10-06 10:20')


data=  {"pickup_datetime": ['date_and_time'],
        "pickup_longitude": ['pickup_longitude'],
        "pickup_latitude": ['pickup_latitude'],
        "dropoff_longitude": ['dropoff_longitude'],
        "dropoff_latitude": ['dropoff_latitude'],
        "passenger_count": ['passenger_count']} 



url = 'https://taxifare.lewagon.ai/predict'
response = requests.get(url, params = data)
responsejson = response.json()
print(responsejson)


'''
2. Let's build a dictionary containing the parameters for our API...
3. Let's call our API using the `requests` package...
4. Let's retrieve the prediction from the **JSON** returned by the API...
## Finally, we can display the prediction to the user
'''

