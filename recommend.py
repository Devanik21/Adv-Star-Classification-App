import streamlit as st
import pandas as pd

def main():
    st.title("✨ Recommend")
    st.write("Recommendation system for similar star types will go here.")
    
    # Load dataset
    @st.cache
    def load_data():
        return pd.read_csv("star_classification.csv")

    data = load_data()

    # Example recommendation input and output
    st.sidebar.header("Recommendation Inputs")
    star_type = st.sidebar.selectbox("Select a Star Type", ["Galaxy", "QSO", "Star"])
    
    alpha = st.sidebar.slider("Alpha", 0.0, 360.0, 180.0)
    delta = st.sidebar.slider("Delta", -90.0, 90.0, 0.0)
    u = st.sidebar.slider("u", 0.0, 30.0, 15.0)
    g = st.sidebar.slider("g", 0.0, 30.0, 15.0)
    r = st.sidebar.slider("r", 0.0, 30.0, 15.0)
    i = st.sidebar.slider("i", 0.0, 30.0, 15.0)
    z = st.sidebar.slider("z", 0.0, 30.0, 15.0)
    redshift = st.sidebar.slider("Redshift", 0.0, 10.0, 0.5)
    
    find_similar_stars = st.sidebar.button("Find Similar Stars")
    
    if find_similar_stars:
        # Filter the dataset based on star type
        filtered_data = data[data["class"] == star_type]
        
        # Find similar stars based on feature proximity
        def calculate_distance(row):
            return abs(row["alpha"] - alpha) + abs(row["delta"] - delta) + \
                   abs(row["u"] - u) + abs(row["g"] - g) + \
                   abs(row["r"] - r) + abs(row["i"] - i) + \
                   abs(row["z"] - z) + abs(row["redshift"] - redshift)
        
        filtered_data["distance"] = filtered_data.apply(calculate_distance, axis=1)
        recommendations = filtered_data.sort_values(by="distance").head(10)
        
        st.subheader("Recommended Similar Stars")
        st.write("Here are the top 10 stars similar to your input:")
        st.write(recommendations[["obj_ID", "alpha", "delta", "u", "g", "r", "i", "z", "redshift"]])

if __name__ == "__main__":
    main()
