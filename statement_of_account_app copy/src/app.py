import streamlit as st
import pandas as pd
from datetime import datetime
from utils.data_processing import load_data, filter_transactions, calculate_balance

# Load transaction data
data_file = "/Users/diogo/Desktop/streamlit_30days/SOA/statement_of_account_app/data/transactions.xlsx"
transactions_df = load_data(data_file)

# Streamlit app title
st.title("Customer Statement of Account")

# Dropdown for customer selection
customers = transactions_df['Name'].unique()
selected_customer = st.selectbox("Select a customer", customers)

# Date range selection
start_date = st.date_input("Start date", datetime.now())
end_date = st.date_input("End date", datetime.now())

# Filter transactions based on selected customer and date range
filtered_transactions = filter_transactions(transactions_df, selected_customer, start_date, end_date)

# Display the statement of account
if not filtered_transactions.empty:
    st.subheader(f"Statement of Account for {selected_customer}")
    st.write(filtered_transactions)

    # Calculate and display balance sheet
    total_credit, total_debit, balance = calculate_balance(filtered_transactions)
    balance_data = {
        "Total Credit": [total_credit],
        "Total Debit": [total_debit],
        "Balance": [balance]
    }
    balance_df = pd.DataFrame(balance_data)
    st.subheader("Balance Sheet")
    st.write(balance_df)
else:
    st.write("No transactions found for the selected customer in the specified date range.")