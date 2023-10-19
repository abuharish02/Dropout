import subprocess
import sys

required_packages = [
    "streamlit",
    "pandas",
    "scikit-learn",
    "matplotlib"
]

def install_required_packages():
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)

    if missing_packages:
        print("Installing missing packages...")
        for package in missing_packages:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print("All required packages installed.")
    else:
        print("All required packages are already installed.")

install_required_packages()

import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

data = pd.read_csv("d1.csv")
st.title("School Dropout prediction ")
X = data[['No_student', 'Class', 'Social', 'Poverty', 'Health']]
y = data['Year']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_prediction = model.predict(X_test)
rtwo = r2_score(y_test, y_prediction)
year_numeric = st.number_input("Enter a Numeric Year", min_value=2000)
if year_numeric >= 2000:
    predicted_students = model.predict([[year_numeric, 0, 0, 0, 0]])[0]
    st.write(f"Predicted Number of Students for {year_numeric}: {predicted_students:.2f}")
    fig, ax = plt.subplots()
    x_values = X_test['No_student']
    bar_width = 0.1
    bar1 = ax.bar(x_values - bar_width/2, y_test, bar_width, label="Actual")
    bar2 = ax.bar(x_values + bar_width/2, y_prediction, bar_width, label="Predicted")
    ax.set_xlabel("Number of Students")
    ax.set_ylabel("Year")
    ax.set_title("Actual vs. Predicted")
    ax.legend()
    st.pyplot(fig)
else:
    st.write("Please enter a valid year (greater than or equal to 2000).")
