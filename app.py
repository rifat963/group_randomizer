import streamlit as st
import random

# Set page configuration
st.set_page_config(
    page_title="Random Item Pair Generator",
    page_icon="🔀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Apply custom CSS styles
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
    }
    .stTextArea textarea {
        border: 2px solid #4CAF50;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title with emoji
st.markdown('### :sparkles: Random Item Pair Generator :sparkles:')

# Layout: Two columns for input
col1, col2 = st.columns(2)

with col1:
    list1_input = st.text_area('Enter items for List 1 (separated by commas):')
    list1 = [item.strip() for item in list1_input.split(',') if item.strip()]

with col2:
    list2_input = st.text_area('Enter items for List 2 (separated by commas):')
    list2 = [item.strip() for item in list2_input.split(',') if item.strip()]

# Generate button
if st.button('Generate Random Pairs'):
    if list1 and list2:
        # Determine the number of pairs to generate
        num_pairs = min(len(list1), len(list2))

        # Randomly sample items from both lists
        sampled_list1 = random.sample(list1, num_pairs)
        sampled_list2 = random.sample(list2, num_pairs)

        # Create pairs
        pairs = list(zip(sampled_list1, sampled_list2))

        st.write('### Randomized Item Pairs:')
        for idx, (item1, item2) in enumerate(pairs, start=1):
            col1, col2 = st.columns(2)
            col1.write(f'**Pair {idx}:**')
            col2.write(f'**{item1}** - **{item2}**')
    else:
        st.warning('Please enter items in both lists.')
