import streamlit as st

import requests
import json

from utils import show_navigation
show_navigation()

default_data={
             "H5OD2A":2,
             "H1SE4":"3",
             "W5REGION":4,
             "H1FS1":"2",
             "H1FS2":"0",
             "H5PE1":2,
             "H5PE3":2,
             "H5PE7":2,
             "H5PE8":2,
             "H5PE9":2,
             "H5EC9":5,
             "H5MN2":5,
             "H5MN3":4,
             }

def get_prediction_college_with_region(data):
  url = 'https://askai.aiclub.world/dedd15bc-65eb-4c7a-9893-0d21d9f00cce'
  r = requests.post(url, data=json.dumps(data))
  response = getattr(r,'_content').decode("utf-8")
  rspjson=json.loads(response)

  return rspjson


def main():
    st.title("College with Region")
    col1,col2=st.columns(2)
    with col1:
        userdata=default_data
        userdata["H5OD2A"]=st.number_input("H5OD2A",value=2)
        userdata["H1SE4"]=st.selectbox("H1SE4",("2","3","4","5","6"))
        userdata["W5REGION"]=st.number_input("W5REGION",value=4)
        userdata["H1FS1"]=st.selectbox("H1SE4",("0","1","2","3","8"))
        userdata["H1FS2"]=st.selectbox("H1SE4",("0","1","2","3"))
        userdata["H5MN2"]=st.number_input("H5MN2",value=5)
        userdata["H5MN3"]=st.number_input("H5MN3",value=4)
        userdata["H5PE1"]=st.number_input("H5PE1",value=8)
        userdata["H5PE3"]=st.number_input("H5PE3",value=7)
        userdata["H5PE7"]=st.number_input("H5PE7",value=6)
        userdata["H5PE8"]=st.number_input("H5PE8",value=8)
        userdata["H5PE9"]=st.number_input("H5PE9",value=9)
        userdata["H5EC9"]=st.number_input("H5EC9",value=9)
    rspjson=get_prediction_college_with_region(userdata)
    bodyjson=json.loads(rspjson['body'])
    print(bodyjson)
    with col2:
        st.write(f"Prediction: {bodyjson['predicted_label']}")
        st.divider()
        st.write("Confidence Score")
        st.dataframe(bodyjson['confidence_score'])

main()