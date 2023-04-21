import streamlit as st
import docx
from docx.shared import Pt

def generate_cover_letter(title, journal, abstract, author):
    # Add GPT API call here to generate cover letter based on the input
    # For now, we will return a simple cover letter template
    cover_letter = f"""Dear Editor,

I am submitting our manuscript entitled "{title}" for consideration for publication in {journal}. Our paper presents the following research:

{abstract}

We believe our research significantly contributes to the field and would be of interest to the readers of {journal}. We kindly request you to consider our manuscript for publication.

Thank you for your time and consideration.

Sincerely,
{author}
"""

    return cover_letter


def save_cover_letter_to_docx(cover_letter, filename):
    doc = docx.Document()
    doc.add_paragraph(cover_letter)
    doc.save(filename)


# Streamlit app
st.set_page_config(page_title="EinsteinAI", layout="wide", initial_sidebar_state="expanded")

# Add logo to sidebar
st.sidebar.image('https://raw.githubusercontent.com/drazzam/EinsteinAI/main/logo.png')

st.sidebar.title("EinsteinAI")

st.sidebar.markdown("##### Developed by Cerebrovascular Research Lab at Albert Einstein College of Medicine")

tool_selection = st.sidebar.radio("Select a tool:", [
    "Risk of Bias Assessment Tool",
    "Cover Letter Generator",
    "Systematic Review and Meta-analysis Ideas Generator",
    "Research Methodology Advisor, Reviewer and Proofreading Tool",
    "Statistical Plan Consultant Tool",
    "Meta-analysis Statistical Plan Consultant",
    "Sample Size Calculator Tool",
    "Abstract and Keywords Generator",
    "Virtual Librarian Tool",
    "Assistant Extraction Tool",
])

if tool_selection == "Cover Letter Generator":
    st.title("Cover Letter Generator")

    title = st.text_input("Enter the title of the manuscript:")
    journal = st.text_input("Enter the name of the targeted journal:")
    abstract = st.text_area("Enter the abstract of the paper:")
    author = st.text_input("Enter the name of the corresponding author:")

    if st.button("Generate Cover Letter"):
        if title and journal and abstract and author:
            cover_letter = generate_cover_letter(title, journal, abstract, author)
            st.write(cover_letter.replace("\n", "  \n"))

            filename = "generated_cover_letter.docx"
            save_cover_letter_to_docx(cover_letter, filename)
            st.markdown(f"[Download Cover Letter]({filename})", unsafe_allow_html=True)
        else:
            st.error("Please fill in all the fields.")

st.sidebar.markdown("### API Key")
api_key = st.sidebar.text_input("Enter your ChatGPT API key:", type="password")
if api_key:
    openai.api_key = api_key

st.sidebar.markdown("### About")
if st.sidebar.button("Show About"):
    st.sidebar.markdown(
        "This application was developed by Cerebrovascular Research Lab at Albert Einstein College of Medicine."
    )
