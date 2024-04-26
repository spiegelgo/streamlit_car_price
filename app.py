import streamlit as st
from home import run_home
from eda import run_eda
from ml import run_ml

def main():
    st.title('자동차 가격 예측 앱!!')
    
    sidebar_menu = ['Home','EDA','ML']
    choice = st.sidebar.selectbox('메뉴', sidebar_menu)
    
    if choice == sidebar_menu[0] :
        run_home()
    elif choice == sidebar_menu[1] :
        run_eda()
    elif choice == sidebar_menu[2] :
        run_ml()


if __name__ == '__main__':
    main()