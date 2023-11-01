import streamlit as st
import pandas as pd 
import time

st.title('Startup Dashboard')
st.header('I am learning Streamlit')
st.subheader('And I am loving it')

st.write('normal body of text')

#displaying different types of text
st.markdown("""
            ### My favorite movies            
            - Race 3
            - Housefull
            - Ghosted
""")

#displaying codes
st.code("""
def foo(input):
        return foo**2

x = foo(2)
""")

#displaying mathematical operations
st.latex('x^2 + y^2 + 10 = 0')

#displaying dataframe 
df = pd.DataFrame({
    'name':['Nitish','Ankit','Anupam'],
    'marks': [50,60,70],
    'package':[10,12,14]
})

st.dataframe(df)

st.metric('Revenue','Rs 3Lac', '3%')

#displaying image
st.image('sample_img.png')
#displaying video
#st.video()

#sidebar
st.sidebar.subheader('sidebar bhi hai')


col1, col2 = st.columns(2)
with col1:
    st.header('sample chart')

with col2:
    st.image('sample_img.png')



#error and success warning and info messages
st.error('Login Failed')
st.success('Login success')
st.warning('warning')
st.info('info')


#progress bar
bar = st.progress(0)

for i in range(1,101):
    time.sleep(0.1)
    bar.progress(i)

#taking user inputs

email = st.text_input('Enter email')
numbers = st.number_input('Enter Age')
DOB = st.date_input('Enter DOB')

#file uploader

file = st.file_uploader('Upload csv file here')

if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())



email = st.text_input('Enter email')
password = st.text_input('Enter password')
gender  = st.selectbox('select gender', ['male','female'])

btn = st.button('Login')

if btn:
    if email == 'satviksinghal@gmail.com' and password == '1234':
        st.success('Login successful')
        st.write(gender)
        st.balloons()

    else:
        st.error('Login failed')