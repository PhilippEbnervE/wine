import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
# Streamlit UI
st.title('Wine Prediction App')
st.write('Enter the following information to whether your selected wine is a red or white wine.')

# loading the first trained model
pickle_in = open('wine.pkl', 'rb') 
classifier = pickle.load(pickle_in)

scaler_file_path = 'wine_scaler.pkl'  

@st.cache_data()

# defining the function which will make the prediction using the data which the user inputs 
def prediction(fixed_acidity ,volatile_acidity , citric_acid ,residual_sugar ,chlorides ,free_sulfur_dioxide ,total_sulfur_dioxide ,pH ,sulphates ,alcohol , quality_3 ,quality_4 ,quality_5 ,quality_6 ,quality_7 ,quality_8 ,quality_9, dtype='object'):   

    # Making predictions 
    prediction = classifier.predict( 
        [[fixed_acidity ,volatile_acidity , citric_acid ,residual_sugar ,chlorides ,free_sulfur_dioxide ,total_sulfur_dioxide ,pH ,sulphates ,alcohol , quality_3 ,quality_4 ,quality_5 ,quality_6 ,quality_7 ,quality_8 ,quality_9]])
     
    if prediction == 0:
        pred = 'White Wine'
    else:
        pred = 'Red Wine'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
   
    """
     
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    
    fixed_acidity = st.number_input("Input Fixed Acidity")
    volatile_acidity = st.number_input('Input Volatile Acidity?')
    citric_acid = st.number_input("Input Citric Acid")
    residual_sugar = st.number_input("Input Residual Sugar")
    chlorides = st.number_input("NInput Chlorides")
    free_sulfur_dioxide = st.number_input("Input free sulfur dioxide level")
    total_sulfur_dioxide = st.number_input('Input total sulfur dioxide level')
    pH = st.number_input('Input ph-Level')
    sulphates = st.number_input('Input sulphates amount')
    alcohol = st.number_input('Input alcohol percentage level')
    quality = st.slider('Input Wine Quality', min_value=0, max_value=10, value=5, step=1)
    result =""




    # Convert categorical values to numerical
    quality_3 = 1 if quality == 3 else 0
    quality_4 = 1 if quality == 4 else 0
    quality_5 = 1 if quality == 5 else 0
    quality_6 = 1 if quality == 6 else 0
    quality_7 = 1 if quality == 7 else 0
    quality_8 = 1 if quality == 8 else 0
    quality_9 = 1 if quality == 9 else 0


    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict Churn"): 
        result = prediction(fixed_acidity ,volatile_acidity , citric_acid ,residual_sugar ,chlorides ,free_sulfur_dioxide ,total_sulfur_dioxide ,pH ,sulphates ,alcohol , quality_3 ,quality_4 ,quality_5 ,quality_6 ,quality_7 ,quality_8 ,quality_9)
        st.success('This wine is a {}'.format(result))

if __name__=='__main__': 
    main()