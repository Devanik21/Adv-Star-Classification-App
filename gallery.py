import streamlit as st

def display_images(category, image_list):
    st.subheader(category)
    cols = st.columns(5)  # Display 5 images per row
    for idx, image in enumerate(image_list):
        with cols[idx % 5]:  # Display in a grid format
            st.image(image, use_column_width=True)

def main():
    st.title("Gallery")
    
    # Example image lists, replace with actual file paths or URLs
    galaxy_images = ["path_to_galaxy_image1.jpg", "path_to_galaxy_image2.jpg", ..., "path_to_galaxy_image10.jpg"]
    qso_images = ["path_to_qso_image1.jpg", "path_to_qso_image2.jpg", ..., "path_to_qso_image10.jpg"]
    star_images = ["path_to_star_image1.jpg", "path_to_star_image2.jpg", ..., "path_to_star_image10.jpg"]
    
    # Display 10 images from each category
    display_images("Galaxy", galaxy_images)
    display_images("QSO", qso_images)
    display_images("Star", star_images)

if __name__ == "__main__":
    main()
