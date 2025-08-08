import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Excel Column Adder", layout="centered")

st.title("📄 Excel Column Adder Tool")

# Step 1: File Upload
uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx", "xls"])

if uploaded_file:
    # Read Excel into DataFrame
    df = pd.read_excel(uploaded_file)

    st.subheader("Preview of Uploaded File")
    st.dataframe(df.head())

    # Step 2: Input for column name
    new_col_name = st.text_input("Enter New Column Name")

    # Step 3: Add Column Button
    if st.button("➕ Add Column"):
        if new_col_name.strip() == "":
            st.error("Please enter a valid column name!")
        else:
            if new_col_name in df.columns:
                st.warning(f"Column '{new_col_name}' already exists.")
            else:
                df[new_col_name] = ""  # Empty column
                st.success(f"Column '{new_col_name}' added successfully!")
                st.dataframe(df.head())

                # Step 4: Download option
                output = BytesIO()
                df.to_excel(output, index=False)
                output.seek(0)

                st.download_button(
                    label="📥 Download Updated Excel",
                    data=output,
                    file_name="updated_file.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
