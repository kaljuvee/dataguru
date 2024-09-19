import streamlit as st
import pandas as pd
import io

def get_excel_sheets(file):
    xls = pd.ExcelFile(file)
    return xls.sheet_names

def read_excel_sheet(file, sheet_name):
    return pd.read_excel(file, sheet_name=sheet_name)

def to_excel(df):
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
    processed_data = output.getvalue()
    return processed_data

st.title('Dataguru - Excel File Merger')

# File uploads
file1 = st.file_uploader("Upload first Excel file", type=['xlsx', 'xls'])
file2 = st.file_uploader("Upload second Excel file", type=['xlsx', 'xls'])

if file1 and file2:
    # Get sheet names
    sheets1 = get_excel_sheets(file1)
    sheets2 = get_excel_sheets(file2)

    # Sheet selection
    sheet1 = st.selectbox("Select sheet from first file", sheets1)
    sheet2 = st.selectbox("Select sheet from second file", sheets2)

    if sheet1 and sheet2:
        # Read selected sheets
        df1 = read_excel_sheet(file1, sheet1)
        df2 = read_excel_sheet(file2, sheet2)

        # Column selection for merging
        merge_col1 = st.selectbox("Select merge column from first file", df1.columns)
        merge_col2 = st.selectbox("Select merge column from second file", df2.columns)

        if st.button("Merge"):
            # Perform merge
            merged_df = pd.merge(df1, df2, left_on=merge_col1, right_on=merge_col2, how='left')

            # Display merged dataframe
            st.write("Merged Data:")
            st.dataframe(merged_df)

            # Provide download buttons
            csv = merged_df.to_csv(index=False)
            st.download_button(
                label="Download merged data as CSV",
                data=csv,
                file_name="merged_data.csv",
                mime="text/csv",
            )

            excel_file = to_excel(merged_df)
            st.download_button(
                label="Download merged data as XLSX",
                data=excel_file,
                file_name="merged_data.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

st.write("Upload two Excel files, select sheets and merge columns, then click 'Merge' to see and download the result.")
