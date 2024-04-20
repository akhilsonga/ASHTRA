import streamlit as st
import pygame
from pygame import mixer
import os
import time
# Initialize Pygame mixer
pygame.init()
mixer.init()

# Global variables to keep track of the currently playing audio and index
current_sound = None

# Define podcast data
podcasts = [
    {
    "title": "Tech Talks with Experts",
    "description": "Join us as we delve into the latest trends and innovations in the world of technology. Each episode features interviews with industry experts discussing topics like artificial intelligence, cybersecurity, and emerging tech.",
    "audio_file": "techtalks.mp3",
    "image_url": "image2.jpg"
},
{
    "title": "The Mindfulness Journey",
    "description": "Explore the practice of mindfulness and its impact on mental well-being. This podcast offers guided meditations, personal stories, and discussions on stress reduction, self-awareness, and living in the present moment.",
    "audio_file": "mindfulness_journey.mp3",
    "image_url": "image3.jpg"
},
{
    "title": "Culinary Adventures",
    "description": "Embark on a culinary journey around the world with our passionate hosts. Discover unique recipes, food history, and the stories behind beloved dishes from different cultures and cuisines.",
    "audio_file": "culinary_adventures.mp3",
    "image_url": "image4.jpg"
},
{
    "title": "Health and Fitness Insider",
    "description": "Stay informed on health and fitness trends with expert advice on nutrition, exercise, and mental well-being. Each episode offers practical tips and interviews with fitness professionals and nutritionists.",
    "audio_file": "health_fitness_insider.mp3",
    "image_url": "image5.jpg"
}
]

# Function to play or stop audio based on podcast index
def audio_start(index):
    file_name = "1.txt"
    with open(file_name, 'w') as file:
        file.write(str(podcasts[index]['description']))

def audio_stop():
    file_path = "1.txt"
    if os.path.exists('1.txt'):
        try:
            os.remove(file_path)
            return True
        except OSError:
            return False
    else:
        return True
    
# Main Streamlit app
def upload():
    import sys
    sys.path.append(r"C:\Users\akhil\Downloads\Lablab\Lablab\pages\RAG")
    from RAG import RAG
    with st.status("Uploading the Research Paper...",expanded=False) as status:
        st.write("Uploading the Research Paper")
        time.sleep(1)
        st.write("Creating chunks...")
        status.update(label="Creating Chunks!")
        RAG()
        st.write("Redirecting to the Chat Window...")
        status.update(label="Redirecting to the Chat Window...")
        time.sleep(1)
    print("Done")
    app4_path = os.path.join(os.path.dirname(__file__), "pages/app4.py")
    st.switch_page(app4_path)

def layout():
    st.set_page_config(
    page_title="ASHTRA Podcast",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    )

    st.title("Podcast Player")
    st.sidebar.markdown("# Upload your Research Paper")
    file=st.sidebar.file_uploader("")
    if file:
        # print(str(file.name))
        # with open("./db/file_location.txt", "w") as f:
        #     f.write(str(file))
        with open('./pages/RAG/paper.pdf', 'wb') as f:
            f.write(file.getvalue())
        upload()
    # Display podcasts in rows with 2 cards per row
    for i in range(0, len(podcasts), 2):
        row_podcasts = podcasts[i:i+2]

        # Create a row for each set of 2 podcasts
        col1, col3, col2 = st.columns([6, 1, 6])#st.columns(3)

        for col, podcast in zip([col1, col2], row_podcasts):
            with col:
                st.image(podcast['image_url'], use_column_width=True)
                #st.image(podcast['image_url'], use_column_width=True, output_format='JPG', width=500, style={'border-radius': '10px'})
                #st.markdown(f'<img src="{podcast["image_url"]}" style="border-radius: 10px;" />',unsafe_allow_html=True)
                #st.markdown(f'<img src="{podcast["image_url"]}" style="border-radius: 10px; max-width: 100%;" />', unsafe_allow_html=True)   
                st.write(f"**{podcast['title']}**")
                st.write(podcast['description'])
                # Play button
                if st.button("Play", key=f"play_{podcast['title']}"):
                    index = podcasts.index(podcast)
                    audio_start(index)
                # Stop button (only show if audio is playing)
                if st.button("Stop", key=f"stop_{podcast['title']}"):
                    audio_stop()
        st.write("---")
if __name__ == "__main__":
    print(current_sound)
    layout()