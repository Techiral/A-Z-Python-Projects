import streamlit as st
import google.generativeai as genai
import os
import pyperclip
import time  # for simulating progress

# Set up Gemini API key (replace with your own key)
os.environ["API_KEY"] = 'GEMINI_API_KEY'
genai.configure(api_key=os.environ["API_KEY"])

# Initialize a cache to store versions of the story
if 'story_versions' not in st.session_state:
    st.session_state.story_versions = []
if 'current_version' not in st.session_state:
    st.session_state.current_version = -1

# Function to call Gemini API to generate a story
def generate_story(prompt):
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    response = model.generate_content(prompt)
    return response.text

# Add a new story version to session state
def add_story_version(new_story):
    st.session_state.story_versions.append(new_story)
    st.session_state.current_version = len(st.session_state.story_versions) - 1

# Navigate between story versions
def navigate_story_version(direction):
    if direction == 'prev' and st.session_state.current_version > 0:
        st.session_state.current_version -= 1
    elif direction == 'next' and st.session_state.current_version < len(st.session_state.story_versions) - 1:
        st.session_state.current_version += 1

# UI Setup
st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-size: 36px;
        color: #4A90E2;
        margin-bottom: 20px;
    }
    .section-title {
        font-size: 24px;
        color: #333;
    }
    .expander-header {
        font-size: 18px;
        color: #2C3E50;
    }
    .sidebar .sidebar-content {
        background-color: #F7F9FA;
        padding: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar for story settings
st.sidebar.header("Story Settings")

# Sidebar options for user inputs
age_group = st.sidebar.selectbox("Choose Age Group", ['Children', 'Teenagers', 'Adults'])
genre = st.sidebar.selectbox("Choose Genre", ['Adventure', 'Mystery', 'Fantasy', 'Sci-Fi', 'Horror', 'Romance'])
user_prompt = st.sidebar.text_input("Enter a story prompt or idea:")


# Display app heading
st.markdown('<div class="title">StoryCraft: Your Personal Story Generator</div>', unsafe_allow_html=True)

# Button to generate a story based on the user input
if st.sidebar.button("Generate Story"):
    if user_prompt:
        prompt = f"Generate a {genre} story for {age_group}. {user_prompt}"

        with st.spinner('Generating your story...'):
            # Simulate a loading progress bar
            progress = st.progress(0)
            for i in range(100):
                time.sleep(0.02)  # Simulating the delay
                progress.progress(i + 1)

            generated_story = generate_story(prompt)
            add_story_version(generated_story)
    else:
        st.sidebar.warning("Please enter a prompt to generate a story.")

# Show generated story if one exists
if st.session_state.current_version >= 0:
    st.markdown('<div class="section-title">Generated Story</div>', unsafe_allow_html=True)

    # Display collapsible story content
    with st.expander("Show/Hide Story", expanded=True):
        current_story = st.session_state.story_versions[st.session_state.current_version]
        st.text_area("Your Story", value=current_story, height=300)

        # Copy the story to clipboard
        if st.button("Copy Story"):
            pyperclip.copy(current_story)
            st.success("Story copied to clipboard!")

    # Show 'Modify the Story' section only after the first story has been generated
    st.markdown('<div class="section-title">Modify the Story</div>', unsafe_allow_html=True)
    with st.expander("Suggest Changes", expanded=False):
        modification_prompt = st.text_input("Suggest changes or add a new prompt to modify the story:")
        if st.button("Update Story"):
            if modification_prompt:
                with st.spinner('Updating the story...'):
                    modified_story = generate_story(modification_prompt + " " + current_story)
                    add_story_version(modified_story)
                    st.success("Story updated!")
            else:
                st.warning("Please enter a modification prompt.")

    # Show navigation buttons only if more than one version exists
    if len(st.session_state.story_versions) > 1:
        st.markdown('<div class="section-title">Version History</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("← Previous Version"):
                navigate_story_version('prev')
        with col2:
            if st.button("Next Version →"):
                navigate_story_version('next')
else:
    st.info("Generate a story to start!")
