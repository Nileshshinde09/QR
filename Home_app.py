import qrcode
import streamlit as st
import os
st.set_page_config(
    page_title="QRcode",
    page_icon="QR",
        layout="wide",
        initial_sidebar_state="collapsed",
        menu_items={
            'Get Help': 'https://www.extremelycoolapp.com/help',
            'Report a bug': "https://www.extremelycoolapp.com/bug",
            'About': "# This is a header. This is an *extremely* cool app!"}
)




class Qrcode(): 
    def __init__(self,data,name) -> None:
        with st.spinner('Wait for it...'):
            image_ = qrcode.make(data)
            image_.save(name+'.png')
            st.image(name+'.png', caption=f'{name}')
        with open(name+'.png', "rb") as file:
            st.download_button(
                    label="Download image",
                    data=file,
                    file_name=name+'.png',
                    mime="image/png"
                )
        os.remove(name+'.png')


if __name__=="__main__":
    hide_menu_style ="""
            <style>
             #MainMenu {visibility: hidden;}
             </style>
             """

    st.markdown(hide_menu_style, unsafe_allow_html=True)
    no_sidebar_style = """
    <style>
        div[data-testid="collapsedControl"] {display: none;}
    </style>
    """
    st.markdown(no_sidebar_style, unsafe_allow_html=True)
    URL_link = st.text_input("Enter the link or URL :")
    QRName = st.text_input("Enter name for QRCode :")
    if st.button("Enter"):
        if 'https:' not in URL_link or ' ' in URL_link or QRName =='' or QRName ==" ":
            st.error("Wrong input") 
        else:
            Qrcode(URL_link,QRName)
