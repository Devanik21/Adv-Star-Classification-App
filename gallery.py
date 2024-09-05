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
    
    # Image paths for QSO
    qso_images = [
        "Gallery/QSO/1.jpg",
        "Gallery/QSO/2.png",
        "Gallery/QSO/3.jpg"
    ]
    
    # Image paths for Star
    star_images = [
        "Gallery/STAR/1.jpg",
        "Gallery/STAR/2.jpg",
        "Gallery/STAR/3.jpg",
        "Gallery/STAR/4.jpg"
    ]
    
    # Display images for each category
    display_images("Galaxy", galaxy_images)
    display_images("QSO", qso_images)
    display_images("Star", star_images)

if __name__ == "__main__":
    main()
