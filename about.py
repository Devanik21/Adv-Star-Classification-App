import streamlit as st

def main():

    # Custom CSS for styling
    st.markdown("""
        <style>
            body {
                background-color: #f0f4f8;
                font-family: 'Arial', sans-serif;
            }
            .sidebar .sidebar-content {
                background-color: #f7f7f7;
            }
            .css-1lcbmhc {
                overflow: auto;
            }
            .stButton button {
                background-color: #007bff;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px 20px;
                cursor: pointer;
            }
            .stButton button:hover {
                background-color: #0056b3;
            }
            .info-box {
                background-color: #333;
                border: 1px solid #fff;
                border-radius: 10px;
                padding: 20px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                color: #fff;
            }
            .info-box h3 {
                color: #ff6347;
            }
            .info-box p {
                font-size: 1.2rem;
            }
            .team-member {
                display: flex;
                align-items: center;
                margin-bottom: 20px;
            }
            .team-member img {
                border-radius: 50%;
                width: 80px;
                height: 80px;
                margin-right: 20px;
            }
            .team-member h4 {
                margin: 0;
                color: #ffd700;
            }
        </style>
    """, unsafe_allow_html=True)

    # Title of the page
    st.title("📚 About the App")

    # Information about the app
    st.markdown("""
        <div class="info-box">
            <h3>Welcome to the Star Classification App!</h3>
            <p>This advanced web application is designed to classify astronomical objects into three categories: Galaxies, Quasars, and Stars. Utilizing cutting-edge machine learning models, our app provides accurate and insightful predictions based on various astronomical features.</p>
            <p>With features like Predict, Recommend, Visualize, Analyze, Insights, Gallery, Feedback, and About, this app offers a comprehensive and professional platform for exploring and understanding astronomical data.</p>
            <p>Whether you're a researcher, student, or astronomy enthusiast, our app aims to provide valuable insights and a user-friendly experience for all your star classification needs.</p>
        </div>
    """, unsafe_allow_html=True)

    # Information about the team
    st.markdown("""
        <div class="info-box">
            <h3>Meet the Team</h3>
            <div class="team-member">
                <img src="https://via.placeholder.com/80" alt="Devanik">
                <div>
                    <h4>Devanik</h4>
                    <p>Aspiring AI Ops Engineer</p>
                </div>
            </div>
            <div class="team-member">
                <img src="https://via.placeholder.com/80" alt="Niki(AI)">
                <div>
                    <h4>AI</h4>
                    <p>Advanced  Copilot</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Contact details or links
    st.markdown("""
        <div class="info-box">
            <h3>Contact Us</h3>
            <p>If you have any questions or feedback, feel free to reach out:</p>
            <p>Email: <a href="mailto:devanik2005@gmail.com" style="color: #ffd700;">devanik2005@gmail.com</a></p>
            <p>LinkedIn: <a href="https://www.linkedin.com/in/devanik/" style="color: #ffd700;" target="_blank">Devanik</a></p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
