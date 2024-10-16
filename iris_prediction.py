import streamlit as st

st.title("IRIS flower Predictor")
col1, col2 = st.columns(2)

with col1:
    sepal_len = st.number_input("Sepal lenght", min_value=0, max_value=15)
    sepal_width = st.number_input("Sepal width", min_value=0, max_value=15)
with col2:
    petal_len = st.number_input("Petal lenght", min_value=0, max_value=15)
    petal_width = st.number_input("Petal width", min_value=0, max_value=15)



if st.button('Make a prediction!'):
    from joblib import load
    model = load('data/iris_model.joblib')
    
    prediction = model.predict([[1, 2, 3, 4]])
    
    if prediction == 0:
      st.image("images/iris_setosa.png", caption="Iris Setosa")
    if prediction == 1:
        st.image("images/iris_versicolor.png", caption="Iris Versicolor")
    if prediction == 2:
        st.image("images/iris_virginica.png", caption="Iris Virginica")




        
        