import qrcode
import streamlit as st

#import the necessary libraries - qrcode for qr generation and stramlit for web design

st.title('UPI QR Code Generator')

def generate_upi_qr_code(upi_id: str, amount: float, currency: str) -> None:
#This function takes in the user input from the form and creates the upi qr code image
    
    upi_string = f"upi://pay?pa={upi_id}&am={amount}&cu={currency}"
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(upi_string)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("upi_qr_code.png")
    st.image('upi_qr_code.png')

#Here we define the form fields for name, amount and currency
with st.form("my_form"):
    upi_id = st.text_input("Enter your UPI Id : ")
    amount = st.number_input("Enter the amount : ")
    currency = st.text_input("Enter the currency : ")
    submit = st.form_submit_button("Generate QR Code")

#Executes the function when the user clicks the submit button
    if submit:
        generate_upi_qr_code(upi_id, amount, currency)
