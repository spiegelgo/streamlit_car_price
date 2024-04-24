import streamlit as st
import pandas as pd

def run_eda():
    st.subheader('탐색적 데이터 분석')
    
    st.text('데이터 프레임 / 통계치 를 확인 할 수 있습니다.')
    
    radio_menu = ['데이터프레임','통계치']
    
    choice_radio = st.radio('선택하세요.', radio_menu)
    df = pd.read_csv('./data/Car_Purchasing_Data.csv')
    if choice_radio == radio_menu[0] :
        st.dataframe(df)
    
    elif choice_radio == radio_menu[1]:
        st.dataframe(df.describe())
        
    # 각 컬럼별로 최대/최소 값을 보여주는 화면 개발
    # 유저가 컬럼을 선택하면, 해당 컬럼의 최대,최소 데이터를 보여주도록 하자
    
    st.text('컬럼을 선택하면, 각 컬럼별 최대/최소 데이터를 보여드립니다')
    column_list = ['Age', 'Annual Salary', 'Credit Card Debt', 'Net Worth', 'Car Purchase Amount']
    choice_columns = st.selectbox('컬럼을 선택하세요', column_list)
 
    if choice_columns == column_list[0] :
        st.text('최대 데이터')
        st.dataframe(df.loc[ df['Age'] == df['Age'].max() , ])
        st.text('최소 데이터')
        st.dataframe(df.loc[ df['Age'] == df['Age'].min() , ])
        
    elif choice_columns == column_list[1] :
        st.text('최대 데이터')
        st.dataframe(df.loc[ df['Annual Salary'] == df['Annual Salary'].max() , ])
        st.text('최소 데이터')
        st.dataframe(df.loc[ df['Annual Salary'] == df['Annual Salary'].min() , ])
        
    elif choice_columns == column_list[2] :
        st.text('최대 데이터')
        st.dataframe(df.loc[ df['Credit Card Debt'] == df['Credit Card Debt'].max() , ])
        st.text('최소 데이터')
        st.dataframe(df.loc[ df['Credit Card Debt'] == df['Credit Card Debt'].min() , ])
        
    elif choice_columns == column_list[3] :
        st.text('최대 데이터')
        st.dataframe(df.loc[ df['Net Worth'] == df['Net Worth'].max() , ])
        st.text('최소 데이터')
        st.dataframe(df.loc[ df['Net Worth'] == df['Net Worth'].min() , ])
        
    elif choice_columns == column_list[4] :
        st.text('최대 데이터')
        st.dataframe(df.loc[ df['Car Purchase Amount'] == df['Car Purchase Amount'].max() , ])
        st.text('최소 데이터')
        st.dataframe(df.loc[ df['Car Purchase Amount'] == df['Car Purchase Amount'].min() , ])
    