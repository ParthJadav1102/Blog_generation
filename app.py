import streamlit as st
import cohere

# Initialize Cohere Model
cohere_api_key = "faL2fOKUjjuyNGO7WnkJc4HoA4Vh1BErSeH3aBSh"  # Replace with your actual API key
co = cohere.Client(cohere_api_key)

# Function to get response from Cohere Model
def getCohereResponse(input_text, no_words, blog_style):
    try:
        # Prompt Template
        prompt = f"""
        Write a blog for a {blog_style} job profile on the topic "{input_text}" 
        within {no_words} words.
        """

        # Generate response
        response = co.generate(
            model='command',  # Use Cohere's latest model
            prompt=prompt,
            max_tokens=no_words * 4  # Rough estimate (1 word ≈ 4 tokens)
        )

        return response.generations[0].text if response.generations else "No response generated."
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.set_page_config(
    page_title="Generate Blogs",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.header("Generate Blogs 🤖")

input_text = st.text_input("Enter the Blog Topic")

# Creating two columns for additional fields
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input("Number of Words")
with col2:
    blog_style = st.selectbox("Writing the blog for", ("Researchers", "Data Scientist", "Common People"), index=0)

submit = st.button("Generate")

# Final response
if submit:
    if input_text and no_words.isdigit():
        st.write(getCohereResponse(input_text, int(no_words), blog_style))
    else:
        st.error("Please enter a valid topic and number of words.")
