import streamlit as st
st.set_page_config(page_title= "calculator",page_icon="./2.jfif")
st.title("Calculator")
st.write("By Musab")
a = st.number_input("Enter No.1")
b = st.selectbox("Select A Choice",["+","-","x","/"])
c = st.number_input("Enter No.2")
if st.button(label = "Calculate"):
    if b == "+":
        st.sucsses(a+c)
    elif b == "-":
        st.sucsses(a-c)
    elif b == "x":
        st.sucsses(a*c)
    elif b == "/":
        st.sucsses(a/c)
    else:
        st.error("Unspoorted")
