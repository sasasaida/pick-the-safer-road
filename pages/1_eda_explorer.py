import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

st.title("Exploratory Data Analysis")
st.subheader("Accident Data Overview")
st.write("This section allows you to explore the accident dataset interactively.")
st.divider()

train_data = pd.read_csv("data/train.csv")

st.header("Dataset Preview")
n = st.sidebar.slider("Number of rows", 5, 50, 5)
st.table(train_data.head(n))


if st.sidebar.checkbox("Show missing values"):
    st.table(train_data.isnull().sum())

numeric_cols = train_data.select_dtypes(include=['int64', 'float64']).columns.tolist()

selected_col = st.sidebar.selectbox("Select a numeric column", numeric_cols)
st.subheader(f"Summary statistics for {selected_col}")
st.write(train_data[selected_col].describe())

st.divider()

# Histogram of the selected column
st.subheader(f"Histogram of {selected_col}")
fig, ax = plt.subplots()
ax.hist(train_data[selected_col], bins=30)
#ax.set_title(f"Histogram of {selected_col}")
ax.set_xlabel(selected_col)
ax.set_ylabel("Frequency")
st.pyplot(fig)


counts, bin_edges = np.histogram(train_data[selected_col], bins=20)
hist_df = pd.DataFrame({
    "bins": bin_edges[:-1],   # left edge of each bin
    "frequency": counts
})
st.bar_chart(hist_df.set_index("bins"))



#categirical columns
categorical_cols = train_data.select_dtypes(include=['object']).columns.tolist()
selected_cat_col = st.sidebar.selectbox("Select a categorical column", categorical_cols)
st.subheader(f"Value counts for {selected_cat_col}")
st.write(train_data[selected_cat_col].value_counts())

st.divider()

# Bar chart of the selected categorical column
st.subheader(f"Bar chart of {selected_cat_col}")
fig2, ax2 = plt.subplots()
train_data[selected_cat_col].value_counts().plot(kind='bar', ax=ax2)
ax2.set_xlabel(selected_cat_col)
ax2.set_ylabel("Counts")
st.pyplot(fig2)







# Display the entire dataframe
#st.dataframe(train_data)

# Number of rows and columns
print(train_data.shape)

# Column names
print(train_data.columns)

# Data types of each column
print(train_data.dtypes)

# Count missing values per column
print(train_data.isnull().sum())

# Summary stats for numeric columns
print(train_data.describe())

# Example: Road type counts
print(train_data['road_type'].value_counts())
