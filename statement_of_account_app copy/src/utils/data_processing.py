import pandas as pd
import os

def load_data(file_path):
    """Load data from an Excel file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file at {file_path} does not exist.")
    else:
        return pd.read_excel(file_path)

def read_excel_file(file_path):
    """Read the Excel file and return a DataFrame."""
    df = pd.read_excel(file_path)
    return df

def filter_transactions(df, customer_name, start_date, end_date):
    """Filter transactions based on customer name and date range."""
    # Ensure the 'Acct.Date' column is in datetime.date format
    df['Acct.Date'] = pd.to_datetime(df['Acct.Date']).dt.date

    # Filter the DataFrame
    filtered_df = df[(df['Name'] == customer_name) & 
                     (df['Acct.Date'] >= start_date) & 
                     (df['Acct.Date'] <= end_date)]
    return filtered_df

def calculate_balance(transactions):
    """Calculate total credit, total debit, and resulting balance."""
    total_credit = transactions['Credit'].sum()
    total_debit = transactions['Debit'].sum()
    balance = total_credit - total_debit
    return total_credit, total_debit, balance