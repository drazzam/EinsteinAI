import streamlit as st
import docx
import io
import base64
import openai
import PyPDF2
from docx.shared import Pt
import pdfkit
from io import BytesIO
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.text import WD_BREAK
import requests

# Streamlit app
st.set_page_config(page_title="EinsteinAI", layout="wide", initial_sidebar_state="expanded")

# Add logo
st.sidebar.image('https://raw.githubusercontent.com/drazzam/EinsteinAI/main/logo.png')

st.sidebar.markdown("##### Developed by Cerebrovascular Research Lab at Albert Einstein College of Medicine")

tool_selection = st.sidebar.radio("Select a tool:", [
    "Risk of Bias Assessment Tool",
    "Cover Letter Generator",
    "Systematic Review and Meta-analysis Ideas Generator",
    "Research Advisor Tool",
    "Statistical Plan Consultant Tool",
    "Meta-analysis Statistical Plan Consultant",
    "Sample Size Calculator Tool",
    "Abstract and Keywords Generator",
    "Virtual Librarian Tool",
    "Assistant Extraction Tool",
])

if tool_selection == "Research Advisor Tool":
    st.title("Research Advisor Tool")
    st.write("Optimized For ChatGPT (GPT-4)")

    # Input fields
    manuscript_title = st.text_input("Manuscript Title:")
    research_paper_type = st.text_input("Type of Research Paper: (e.g. systematic review, meta-analysis, review article, retrospective study)")
    section_to_criticize = st.text_input("The Section Within The Draft To Be Criticized: (e.g. introduction, methods, results, discussion)")
    section = st.text_area("Paste The Section From Manuscript Here:")

    # Button to generate the prompt
    generate_button = st.button("Generate Prompt")

    # Function to create the prompt
    def create_prompt(manuscript_title, research_paper_type, section_to_criticize):
        prompt = f'''This a draft manuscript proposed for a research paper entitled "{manuscript_title}" which is a {research_paper_type} article.
    Could you criticize and review the following {section_to_criticize} section in the manuscript draft, and provide a detailed feedback report on how to improve it from all aspects including: appropriate writing and proofreading, appropriate methodology and sequence, and the science within the section itself. Generate a comprehensive professional report and recommendations for this manuscript, please!
    That's the {section_to_criticize} section:
    {section}'''

        return prompt

    if generate_button:
        if manuscript_title and research_paper_type and section_to_criticize and section:
            # Generate the prompt
            prompt = create_prompt(manuscript_title, research_paper_type, section_to_criticize)
            st.write("Generated Prompt:")
            st.write(prompt)
        else:
            st.error("Please fill in all the input fields before generating the prompt.")
      # Display the prompt in a textbox and add a button to copy its content
            prompt_textbox = st.text_area("Generated Prompt (You can copy it from here):", value=prompt, height=150)
            copy_button = st.button("Copy Generated Prompt to Clipboard")
            if copy_button:
                st.caching.cache.clear_cache()  # To avoid clipboard caching issue
                st.experimental_set_query_params()  # Reset the query params to avoid copying multiple times
                st.copy(prompt)  # Copy the text to the clipboard
                st.success("Generated Prompt copied to clipboard!")

if tool_selection == "Assistant Extraction Tool":
    st.title("Assistant Extraction Tool")

    st.markdown("Upload the research paper as a PDF file:")
    pdf_file = st.file_uploader("", type=["pdf"])

    st.markdown("Enter The Outcomes To Be Extracted From The Paper (separated by commas):")
    outcomes_input = st.text_input("", key="outcomes_input")
    outcomes = [outcome.strip() for outcome in outcomes_input.split(",")]

    st.markdown("Enter The Targeted Populations For The Outcomes Within The Paper (separated by commas):")
    groups_input = st.text_input("", key="groups_input")
    groups = [group.strip() for group in groups_input.split(",")]

    if pdf_file and outcomes and groups:
        if api_key:
            openai.api_key = api_key
            extracted_data = process_outcomes(pdf_file, outcomes, groups, api_key)
            st.write(extracted_data)

            filename = "extraction_results.docx"
            save_extracted_data_to_docx(extracted_data, filename)
            st.markdown(f"[Download Extraction Results]({filename})", unsafe_allow_html=True)
        else:
            st.error("Please enter your OpenAI API key in the sidebar.")
    else:
        st.warning("Please complete all fields and upload a PDF file.")
    
st.sidebar.markdown("### About")
if st.sidebar.button("Show About"):
    st.sidebar.markdown(
        "This Application Was Developed By:  \n  \n Ahmed Y. Azzam, MS  \n Muhammed Amir Essibayi, MD  \n  \n Under Supervision of Cerebrovascular Research Lab Principal Investigator:  \n  \n David Altschul, MD"
    )

