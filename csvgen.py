import streamlit as st
import pandas as pd
st.title("School Dropout data generator :")
# Create dropdown menus and integer input fields
Year = st.selectbox('Year', ['2023', '2022', '2021', '2020'])
Class = st.selectbox('Class', ['1', '2', '3', '4', '5'])
No_of_Student = st.number_input('No. of Students', min_value=0, step=1)
Social = st.number_input('Social', min_value=0, step=1)
Poverty = st.number_input('Poverty', min_value=0, step=1)
Health = st.number_input('Health', min_value=0, step=1)

# Generate a DataFrame from the selected options
data = {
    'Year': [Year],
    'Class': [Class],
    'No. of Students': [No_of_Student],
    'Social': [Social],
    'Poverty': [Poverty],
    'Health': [Health]
}

df = pd.DataFrame(data)

# Button to generate and download CSV
if st.button('Generate CSV'):
    st.write('Generated Data:')
    st.write(df)

    # Download the generated data as a CSV file
    csv_data = df.to_csv(index=False, encoding='utf-8-sig')
    st.download_button(
        label='Download CSV',
        data=csv_data,
        key='csv_data',
        file_name='generated_data.csv'
    )
