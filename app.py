# app.py
import streamlit as st
from bank import Bank  # Make sure bank.py exists in same directory

Bank.load_data()

st.title("🏦 Simple Bank Management System")

menu = st.sidebar.selectbox(
    "Choose an option",
    ["Create Account", "Deposit Money", "Withdraw Money", "View Details", "Update Details", "Delete Account"]
)

if menu == "Create Account":
    st.subheader("Open a New Account")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    email = st.text_input("Email")
    pin = st.text_input("4-digit PIN", type="password")

    if st.button("Create Account"):
        if name and email and pin and len(pin) == 4:
            success, result = Bank.create_account(name, int(age), email, int(pin))
            if success:
                st.success("Account Created Successfully!")
                st.write("Your Account Details:")
                st.json(result)
            else:
                st.error(result)
        else:
            st.warning("Please fill in all fields correctly.")

elif menu == "Deposit Money":
    st.subheader("Deposit Money")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        success, message = Bank.deposit(acc, int(pin), amount)
        if success:
            st.success(f"Deposit successful! New balance: ₹{message}")
        else:
            st.error(message)

elif menu == "Withdraw Money":
    st.subheader("Withdraw Money")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        success, message = Bank.withdraw(acc, int(pin), amount)
        if success:
            st.success(f"Withdrawal successful! New balance: ₹{message}")
        else:
            st.error(message)

elif menu == "View Details":
    st.subheader("Account Details")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show Details"):
        success, data = Bank.get_details(acc, int(pin))
        if success:
            st.json(data)
        else:
            st.error(data)

elif menu == "Update Details":
    st.subheader("Update Account Info")
    acc = st.text_input("Account Number")
    pin = st.text_input("Current PIN", type="password")
    name = st.text_input("New Name (optional)")
    email = st.text_input("New Email (optional)")
    new_pin = st.text_input("New PIN (optional)", type="password")

    if st.button("Update"):
        success, message = Bank.update_details(acc, int(pin), name or None, email or None, int(new_pin) if new_pin else None)
        if success:
            st.success(message)
        else:
            st.error(message)

elif menu == "Delete Account":
    st.subheader("Delete Account")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):
        success, message = Bank.delete_account(acc, int(pin))
        if success:
            st.success(message)
        else:
            st.error(message)







            #For running this ---  streamlit run app.py
            # 
