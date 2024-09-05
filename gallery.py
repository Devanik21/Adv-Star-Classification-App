import streamlit as st
import os

def display_images(category, image_list):
    st.subheader(category)
    if image_list:
        cols = st.columns(5)  # Display 5 images per row
        for idx, image in enumerate(image_list):
            with cols[idx % 5]:  # Display in a grid format
                st.image(image, use_column_width=True)
    else:
        st.write(f"No images found for {category}.")

def main():
    st.title("Gallery")

    # Ensure paths are correct and files exist
    galaxy_images = [
        os.path.join("Gallery/Galaxy", file) for file in ["2.jpg", "3.jpg", "4.jpg", "5.jpg", "6.jpg"]
        if os.path.exists(os.path.join("Gallery/Galaxy", file))
    ]
    
    qso_images = [
        os.path.join("Gallery/QSO", file) for file in ["1.jpg", "2.png", "3.jpg"]
        if os.path.exists(os.path.join("Gallery/QSO", file))
    ]
    
    star_images = [
        os.path.join("Gallery/STAR", file) for file in ["1.jpg", "2.jpg", "3.jpg", "4.jpg"]
        if os.path.exists(os.path.join("Gallery/STAR", file))
    ]

    # Display images for each category
    display_images("Galaxy", galaxy_images)
    display_images("QSO", qso_images)
    display_images("Star", star_images)

if __name__ == "__main__":
    main()
