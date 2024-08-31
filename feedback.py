import streamlit as st
import pandas as pd

def main():
    # Set the page layout and background color
   
    # Background color styling
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #000000;
        }
        .slider-container {
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .slider-labels {
            display: flex;
            justify-content: space-between;
            width: 100%;
            margin: 0 20px;
            font-size: 1.2rem;
        }
        .star {
            font-size: 2rem;
            color: #ffd700;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Title with emoji
    st.title("💬 Feedback")

    # Subtitle with color
    st.markdown(
        "<h3 style='color: #ff6347;'>We'd love to hear from you!</h3>", 
        unsafe_allow_html=True
    )

    # Instructions with color
    st.markdown(
        "<p style='color: #4682b4;'>Please fill out the form below to provide your valuable feedback or reach out to us through the provided contact details.</p>", 
        unsafe_allow_html=True
    )

    # Text input for Name
    name = st.text_input("👤 Your Name", "")

    # Text input for Email
    email = st.text_input("✉️ Your Email", "")

    # Text area for Feedback
    feedback = st.text_area("📝 Your Feedback", "")

    # Real-time Feedback Character Count
    feedback_length = len(feedback)
    st.markdown(f"Character count: **{feedback_length}**")

    # Modern Rating System using Select Slider
    st.markdown("<h4 style='color: #4682b4;'>⭐ Rate your experience</h4>", unsafe_allow_html=True)
    
   
    star_labels = [f"{i}⭐" for i in range(1, 6)]
    
    # Create a select slider with star labels
    rating = st.select_slider(
        "",
        options=star_labels,
        value="3⭐",
        format_func=lambda x: x
    )

    # Extract numerical rating from selected label
    numeric_rating = int(rating.replace("⭐", "").strip())

    # Checkbox for Consent
    consent = st.checkbox("I agree to the terms and conditions")

    # Button to submit the form
    if st.button("Send Feedback"):
        if name and email and feedback and consent:
            st.success(f"Thank you, {name}! Your feedback has been received. 🎉")
            # Simulate saving feedback data
            feedback_data = {
                "Name": [name],
                "Email": [email],
                "Feedback": [feedback],
                "Rating": [numeric_rating]
            }
            df = pd.DataFrame(feedback_data)
            st.write("Here's a preview of your feedback:")
            st.dataframe(df)
        else:
            st.error("Please fill out all fields and agree to the terms before submitting. 🚫")

    # Contact details section
    st.markdown("---")
    st.markdown(
        "<h4 style='color: #32cd32;'>📞 Contact Us</h4>", 
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='color: #6a5acd;'>Email: <a href='mailto:devanik2005@gmail.com'>devanik2005@gmail.com</a><br>LinkedIn: <a href='https://www.linkedin.com/in/devanik/' target='_blank'>Devanik</a></p>", 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
