# Statement of Account Application

This project is a Streamlit application that allows users to view and manage customer statements of account based on transaction data stored in an Excel file. The application provides an intuitive interface for selecting customers and date ranges, displaying transaction details, and calculating balances.

## Project Structure

```
statement_of_account_app
├── data
│   └── transactions.xlsx       # Contains transaction data with date, customer name, address, amount, credit, and debit.
├── src
│   ├── app.py                  # Main entry point of the Streamlit application.
│   └── utils
│       └── data_processing.py   # Utility functions for processing Excel data.
├── requirements.txt             # Lists the dependencies required for the project.
└── README.md                    # Documentation for the project.
```

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd statement_of_account_app
   ```

2. **Install the required dependencies**:
   Make sure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare the data**:
   Ensure that the `data/transactions.xlsx` file is present and contains the necessary columns: date, customer name, customer address, amount, credit, and debit.

## Usage Guidelines

1. **Run the application**:
   To start the Streamlit application, run:
   ```bash
   streamlit run src/app.py
   ```

2. **Interact with the application**:
   - Select a customer from the dropdown menu.
   - Choose a date range to filter transactions.
   - View the statement of account, which includes transaction details and a balance sheet showing total credit, total debit, and resulting balance.

## Additional Information

- The application is designed to be user-friendly and provides real-time updates as selections are made.
- For any issues or contributions, please refer to the project's issue tracker or contact the maintainer.