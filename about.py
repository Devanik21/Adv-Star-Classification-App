import streamlit as st

def main():
    st.title("📚 About This App")

    st.write("""
        Welcome to the **Star Classification App**! 🌟🔭

        This application is designed to classify astronomical objects into different categories such as galaxies, quasars, and stars based on various input features. 

        ### Purpose
        The primary goal of this app is to help users understand and classify different types of celestial objects using machine learning models. It allows for interactive exploration of star data and provides recommendations based on user inputs.

        ### Features
        - **Predict**: Classify astronomical objects using a trained model.
        - **Recommend**: Get recommendations for similar star types.
        - **Visualize**: Visualize star data with charts and graphs.
        - **Analyze**: Perform data analysis to gain insights.
        - **Insights**: Get insights from the data and predictions.
        - **Gallery**: View images and examples of different star types.
        - **Feedback**: Provide feedback or get in touch with us.

        ### Team
        This app was developed by [Your Name] and is currently maintained by a dedicated team of astronomy enthusiasts and data scientists. We are passionate about bringing the wonders of the universe to your fingertips.
        
        ### Acknowledgments
        We would like to thank the open-source community and the contributors to the various libraries used in this app, including Streamlit, Pandas, and CatBoost.
        
        ### Contact
        If you have any questions, suggestions, or feedback, feel free to reach out to us via the **Feedback** page.
    """)

if __name__ == "__main__":
    main()
