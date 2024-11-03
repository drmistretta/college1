import streamlit as st
import requests
import json

from utils import show_navigation
show_navigation()

#
# Reordered the variables to reflect the order of the Feature Importance of Predict College - Without Region
#
default_data={
            "H5OD2A":1, #SAAB
             "H5EC9":5, #Ladder of Success
             "H1SE4":3, #Intelligence
             "H5MN3":5, #Things Going Your Way
             "H5PE7":1, #Finish What I Begin
             "H5PE3":1, #Expect Good Things to Happen
             "H5PE1":1, #I am always optimistic about my future
             "H5PE8":1, #I am a hard worker
             "H5PE9":1, #I am diligent. I never give up.
             "H5MN2":5, #Confident to handle personal problems

}
def get_prediction_college_no_region(data):
  with st.sidebar.expander("AI input"):
    st.dataframe(data)
    st.write(json.dumps(data))
  url = 'https://askai.aiclub.world/dedd15bc-65eb-4c7a-9893-0d21d9f00cce'
  r = requests.post(url, data=json.dumps(data))
  response = getattr(r,'_content').decode("utf-8")
  rspjson=json.loads(response)
  print(f"GET-PRED: Response: {response}\n")
  print(f"GET-PRED: Response: {rspjson}\n")
  return rspjson


def main():
    st.title("College without Region")
    col1,col2=st.columns(2)
    with col1:
        userdata=default_data
        #
        #Sex Assigned at Birth
        userdata["H5OD2A"] = st.select_slider(
        '''Pick the number 1 = male or 2 = female for Sex Assigned at Birth.
        \nFeature H5OD2A''',
        options=list(range(1, 3)),  # Values from 1 to 2
        value=1) # Default = 1
        #
        #Ladder of Success
        #
        userdata["H5EC9"] = st.select_slider(
        '''Pick the number for the step on the ladder of success that shows where you think you stand at this time in your life, relative to other people in the U.S. One is the bottom and ten is the top of the ladder of success with the most money, education and respectable jobs:
        \nFeature H5EC9''',
        options=list(range(1, 11)),  # Values from 1 to 10
        value=5) #Default = 5
        #
        #Level of Intelligence
        #
        userdata["H1SE4"] = str(st.select_slider(
        '''Compared with other people your age, how intelligent are you?
        \nChoose a number using the slider below.
        \nFeature H1SE4
        \n1 = moderately below average
        \n2 = slightly below average
        \n3 = about average
        \n4 = slightly above average
        \n5 = moderately above average
        \n6 = extremely above average''',
        options=list(range(1, 7)),  # Values from 1 to 6
        value=3))  # Default = 3
        #
        #Things Going Your Way
        #
        userdata["H5MN3"]=st.select_slider(
        '''In the past 30 days, how often have you felt that things were going your way?
        \nChoose a number on the slider below.
        \nFeature H5MN3
        \n1 = never
        \n2 = almost never
        \n3 = sometimes
        \n4 = fairly often
        \n5 = very often''',
        options=list(range(1,6)),
        value=3) # Default = 3
        #
        #Finish What I Begin
        #
        userdata["H5PE7"]=st.select_slider(
        '''How much do you agree or disagree with the following statement about yourself as you generally are now, not as you wish to be in the future?:
        \nI finish whatever I begin.
        \nChoose a number on the slider below.
        \nFeature H5PE7
        \n1 = strongly agree
        \n2 = agree
        \n3 = neither agree nor disagree
        \n4 = disagree
        \n5 = strongly disagree''',
        options=list(range(1,6)),
        value=3) # Default = 3
        #
        #Expect Good Things to Happen
        #
        userdata["H5PE3"]=st.select_slider(
        '''How much do you agree or disagree with the following statement about yourself as you generally are now, not as you wish to be in the future?:
        \nOverall, I expect more good things to happen to me than bad.
        \nChoose a number on the slider below.
        \nFeature H5PE3
        \n1 = strongly agree
        \n2 = agree
        \n3 = neither agree nor disagree
        \n4 = disagree
        \n5 = strongly disagree''',
        options=list(range(1,6)),
        value=3) # Default = 3
      #
      #I am always optimistic about my future
      #
        userdata["H5PE1"]=st.select_slider(
      '''How much do you agree or disagree with the following statement about yourself as you generally are now, not as you wish to be in the future?:
        \nI am always optimistic about my future.
        \nChoose a number on the slider below.
        \nFeature H5PE1
        \n1 = strongly agree
        \n2 = agree
        \n3 = neither agree nor disagree
        \n4 = disagree
        \n5 = strongly disagree''',
        options=list(range(1,6)),
        value=3) # Default = 3
      #
      #I am a hard worker
      #
        userdata["H5PE8"]=st.select_slider(
        '''How much do you agree or disagree with the following statement about yourself as you generally are now, not as you wish to be in the future?:
        \nI am a hard worker.
        \nChoose a number on the slider below.
        \nFeature H5PE8
        \n1 = strongly agree
        \n2 = agree
        \n3 = neither agree nor disagree
        \n4 = disagree
        \n5 = strongly disagree''',
        options=list(range(1,6)),
        value=3) # Default = 3
      #
      #I am diligent. I never give up.
      #
        userdata["H5PE9"]=st.select_slider(
        '''How much do you agree or disagree with the following statement about yourself as you generally are now, not as you wish to be in the future?:
        \nI am diligent. I never give up.
        \nChoose a number on the slider below.
        \nFeature H5PE8
        \n1 = strongly agree
        \n2 = agree
        \n3 = neither agree nor disagree
        \n4 = disagree
        \n5 = strongly disagree''',
        options=list(range(1,6)),
        value=3) # Default = 3
      #
      #Confident to handle personal problems
      #
        userdata["H5MN2"]==st.select_slider(
        '''In the past 30 days, how often have you felt confident in your ability to handle your personal problems?
        \nChoose a number on the slider below.
        \nFeature H5MN3\2
        \n1 = never
        \n2 = almost never
        \n3 = sometimes
        \n4 = fairly often
        \n5 = very often''',
        options=list(range(1,6)),
        value=3) # Default = 3

    rspjson=get_prediction_college_no_region(userdata)
    print(f"MAIN: RspJSON: {rspjson}\n")
    bodyjson=json.loads(rspjson['body'])
    print(f"MAIN: BodyJSON: {bodyjson}\n")
    confidence_score = bodyjson.get('confidence_score',{})
    print(f"MAIN: Confidence: {confidence_score}\n")
    with col2:
        st.write(f"Prediction: {bodyjson['predicted_label']}")
        st.divider()
        st.write("Confidence Score")
        # Display confidence score if available, otherwise indicate it's not available
        if confidence_score:
            st.dataframe(confidence_score)
        else:
            st.write("Confidence score not available in the API response.")

main()