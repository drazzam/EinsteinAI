import streamlit as st
from streamlit import components
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

# Add logo
st.sidebar.image('https://raw.githubusercontent.com/drazzam/EinsteinAI/main/logo.png')

st.sidebar.markdown("##### Developed by Cerebrovascular Research Lab at Albert Einstein College of Medicine")

tool_selection = st.sidebar.radio("Select a tool:", [
    "Risk of Bias Assessment Tool",
    "Medical Trends Analyzer",
    "Systematic Review and Meta-analysis Ideas Generator",
    "Research Advisor",
    "Statistical Plan Consultant Tool",
    "Meta-analysis Statistical Plan Consultant",
    "Sample Size Calculator Tool",
    "Abstract and Keywords Generator",
    "Virtual Librarian Tool",
    "Funding Opportunities Finder",
])

if tool_selection == "Research Advisor":
    st.title("Research Advisor")
    st.write("Optimized For ChatGPT (GPT-4)")

def copy_text_to_clipboard(text):
    b64_text = base64.b64encode(text.encode()).decode()
    components.v1.html(f'''<textarea id="text_to_copy" style="opacity:0;">{text}</textarea>
    <button onclick="copyTextToClipboard()" style="background-color: #f63366; color: white; border-radius: 5px; padding: 0.5em 1em; font-size: 1em;">Copy Generated Prompt to Clipboard</button>
    <script>
    function copyTextToClipboard() {{
    var copyText = document.getElementById("text_to_copy");
    copyText.select();
    copyText.setSelectionRange(0, 99999);
    document.execCommand("copy");
    }}
    </script>''', height=60)

# Input fields
manuscript_title = st.text_input("Manuscript Title:")
research_paper_type = st.text_input("Type of Research Paper: (e.g. systematic review, meta-analysis, review article, retrospective study)")
section_to_criticize = st.text_input("The Section Within The Draft To Be Criticized: (e.g. introduction, methods, results, discussion)")
section = st.text_area("Paste The Section From Manuscript Here:")

# Button to generate the prompt
generate_button = st.button("Generate Prompt")

# Function to create the prompt
def create_prompt(manuscript_title, research_paper_type, section_to_criticize):
    prompt = f'''This a draft manuscript proposed for a research paper entitled "{manuscript_title}" which is a {research_paper_type} article. Could you criticize and review the following {section_to_criticize} section in the manuscript draft, and provide a detailed feedback report on how to improve it from all aspects including: appropriate writing and proofreading, appropriate methodology and sequence, and the science within the section itself. Generate a comprehensive professional report and recommendations for this manuscript, please! That's the {section_to_criticize} section: {section}'''
    return prompt

if generate_button:
    if manuscript_title and research_paper_type and section_to_criticize and section:
        # Generate the prompt
        prompt = create_prompt(manuscript_title, research_paper_type, section_to_criticize)
        # Display the prompt in a textbox and add a button to copy its content
        prompt_textbox = st.text_area("Generated Prompt:", value=prompt, height=150)
        copy_text_to_clipboard(prompt)
    else:
        st.error("Please fill in all the input fields before generating the prompt.")
    
st.sidebar.markdown("### About")
if st.sidebar.button("Show About"):
    st.sidebar.markdown(
        "This Application Was Developed By:  \n  \n Ahmed Y. Azzam, MS  \n Muhammed Amir Essibayi, MD  \n  \n Under Supervision of Cerebrovascular Research Lab Principal Investigator:  \n  \n David Altschul, MD"
    )
