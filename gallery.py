import streamlit as st

def display_images(category, image_list):
    st.subheader(category)
    cols = st.columns(5)  # Display 5 images per row
    for idx, image in enumerate(image_list):
        with cols[idx % 5]:  # Display in a grid format
            st.image(image, use_column_width=True)

def main():
    st.title("Gallery")
    
    # Image paths for Galaxy
    galaxy_images = [
        "Gallery/Galaxy/2.jpg",
        "Gallery/Galaxy/3.jpg",
        "Gallery/Galaxy/4.jpg",
        "Gallery/Galaxy/5.jpg",
        "Gallery/Galaxy/6.jpg"
    ]
    
    # You can add more image paths for QSO and Star in the same format.
    
    # Display Galaxy images
    display_images("Galaxy", galaxy_images)
    
    # For QSO and Star, repeat the process by adding their respective images.

if __name__ == "__main__":
    main()
