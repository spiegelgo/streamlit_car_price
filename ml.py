import streamlit as st
import joblib
import numpy as np
import pandas as pd

def run_ml():
    st.subheader('자동차 가격 예측하기')
    
    # 1. 예측하기 위해, 유저한테 입력 받는다
    # Gender	Age	Annual Salary	Credit Card Debt	Net Worth	
    
    st.text('성별을 선택하세요')
    gender = st.radio('성별 선택', ['남자','여자'])
    if gender =='남자':
        gender = 1
    elif gender == '여자' :
        gender = 0
    
    st.text('나이를 입력하세요')
    age = st.number_input('나이 입력', min_value= 18, max_value= 120, value= 25)
    
    st.text('연봉을 입력하세요')
    salary = st.number_input('연봉 입력', min_value= 10000, value= 50000, step= 1000)
    
    st.text('카드빚을 입력하세요')
    debt = st.number_input('카드빚 입력', min_value= 0, value= 0, step= 100)
    
    st.text('자산을 입력하세요')
    worth = st.number_input('자산 입력', min_value= 5000, value= 20000, step= 1000)
    
    
    st.subheader('버튼을 누르면 예측합니다.')
    
    if st.button('예측하기') :
        # 2. 예측한다
        # 2-1. 모델이 있어야 한다
        regressor = joblib.load('./model/regressor.pkl')
        #print(regressor)
        
        # 2-2. 유저가 입력한 데이터를 모델이 예측하기 위해 가공해야 한다
        new_data = [gender, age, salary, debt, worth]
        #print(new_data)
        new_data = np.array(new_data).reshape( 1, -1 )
        #print(new_data)
        
        # 2-3. 모델의 predict 함수로 예측한다
        y_pred = regressor.predict(new_data)

        
        # 위의 데이터로 예측한 자동차 구매가능 금액은 7,588달러 입니다. 출력
        y_pred = y_pred[0] # 숫자만 가져오기
        #print(y_pred)
        y_pred = round(y_pred) # 소수점 반올림 처리
        #print(y_pred)
        y_pred = format(y_pred, ',') # 3자리마다 콤마 넣기
        #print(y_pred)
        
        
        st.text(f'위의 데이터로 예측되는 자동차 구매가능 예상 금액은 {y_pred}달러 입니다')
