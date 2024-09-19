# Dataguru

This Streamlit app allows users to merge two Excel files based on a selected column, similar to an Excel VLOOKUP operation. Users can upload Excel files, select sheets, choose merge columns, and download the result in CSV or XLSX format (more tasks to come!).

## Prerequisites

- Python 3.7 or higher

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/kaljuvee/dataguru.git
   cd dataguru
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the App

To run the Streamlit app:

```
streamlit run Home.py
```

This will start the app and open it in your default web browser.

## Using the App

1. Upload two Excel files (XLSX or XLS format).
2. Select a sheet from each file.
3. Choose a column from each sheet to use as the merge key.
4. Click the "Merge" button to perform the merge operation.
5. View the merged data in the app.
6. Download the merged data as CSV or XLSX using the provided buttons.

## File Structure

- `Home.py`: The main Streamlit app file
- `requirements.txt`: List of Python dependencies
- `README.md`: This file

## Contributing

Feel free to fork this repository and submit pull requests to contribute to this project. For major changes, please open an issue first to discuss what you would like to change.
