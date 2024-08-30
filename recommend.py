import streamlit as st
import pandas as pd

def load_data():
    # Load the star classification data from the CSV file
    return pd.read_csv("star_classification.csv")

def get_similar_stars(star_type, data):
    # Filter the data for similar stars based on the selected type
    similar_stars = data[data['class'] == star_type]
    return similar_stars

def main():
    st.title("✨ Recommend")
    st.write("Recommendation system for similar star types.")

    # Load the star classification data
    data = load_data()

    # Sidebar for user input
    st.sidebar.header("Recommendation Inputs")
    star_type = st.sidebar.selectbox("Select a Star Type", ["GALAXY", "QSO", "STAR"])
    similar_stars_button = st.sidebar.button("Find Similar Stars")

    if similar_stars_button:
        # Get similar stars based on the selected type
        recommendations = get_similar_stars(star_type, data)
        
        # Display recommendations
        st.subheader("Recommended Similar Stars")
        if not recommendations.empty:
            st.write(recommendations[['obj_ID', 'alpha', 'delta', 'redshift']])
        else:
            st.write("No similar stars found.")

if __name__ == "__main__":
    main()
