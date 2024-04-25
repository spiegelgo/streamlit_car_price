import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

def run_eda():
    st.subheader('탐색적 데이터 분석')
    
    st.text('데이터프레임 / 통계치 를 확인 할 수 있습니다.')
    
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
 
    
    st.info(f'선택하신 {choice_columns}의 최대 데이터 입니다')
    st.dataframe(df.loc[ df[choice_columns] == df[choice_columns].max() , ])
    st.info(f'선택하신 {choice_columns}의 최소 데이터 입니다')
    st.dataframe(df.loc[ df[choice_columns] == df[choice_columns].min() , ])
    
    st.subheader('상관관계 분석')
    st.text('컬럼들을 2개 이상 선택하면 컬럼들간의 상관계수를 보여드립니다')
    
    corr_column_list = ['Age', 'Annual Salary', 'Credit Card Debt', 'Net Worth']
    selected_columns = st.multiselect('컬럼을 선택하세요', corr_column_list)
    
    # 2개 이상 선택했을때와 그렇지 않을때로 개발
    if len(selected_columns) >= 2:
        # 1.페어플롯을 그린다
        fig1 = sb.pairplot(data = df, vars=selected_columns )
        st.pyplot(fig1)

        # 2.상관계수를 보여준다
        st.write(df[selected_columns].corr())
    else:
        st.text('컬럼을 2개 이상 선택하세요.')
