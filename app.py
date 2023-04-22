import streamlit as st
import docx
import io
import base64
import openai
import PyPDF2
from docx.shared import Pt

def generate_cover_letter(title, journal, abstract, author):
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

# def assistant extraction tool
def process_outcomes(pdf_file, outcomes, groups, openai_api_key):
    # Extract text from the PDF file
    text = process_pdf(pdf_file, openai_api_key)
    
    # Perform the extraction using the OpenAI API
    extracted_data = {}
    for group in groups:
        extracted_data[group] = {}
        for outcome in outcomes:
            prompt = f"Extract the {outcome} for the {group} from the following research paper: {text}"
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=100,
                n=1,
                stop=None,
                temperature=0.7,
            )
            extracted_data[group][outcome] = response.choices[0].text.strip()
            
    return extracted_data

def save_extracted_data_to_docx(extracted_data, filename):
    doc = docx.Document()

    for group, outcomes in extracted_data.items():
        doc.add_heading(group, level=1)
        for outcome, value in outcomes.items():
            doc.add_paragraph(f"{outcome}: {value}")

    doc.save(filename)    

def process_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    text = ""
    for page_num in range(pdf_reader.numPages):
        text += pdf_reader.getPage(page_num).extractText()

    return text

# Streamlit app
st.set_page_config(page_title="EinsteinAI", layout="wide", initial_sidebar_state="expanded")

# Add logo
st.sidebar.image('https://raw.githubusercontent.com/drazzam/EinsteinAI/main/logo.png')

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

if tool_selection == "Assistant Extraction Tool":
    st.title("Assistant Extraction Tool")

    st.markdown("Upload the research paper as a PDF file:")
    pdf_file = st.file_uploader("", type=["pdf"])

    st.markdown("Enter the desired outcomes to be extracted, separated by commas:")
    outcomes_input = st.text_input("", key="outcomes_input")
    outcomes = [outcome.strip() for outcome in outcomes_input.split(",")]

    st.markdown("Enter the targeted populations for the outcomes within the paper, separated by commas:")
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
    
st.sidebar.markdown("### API Key")
api_key = st.sidebar.text_input("Enter your ChatGPT API key:", type="password")
if api_key:
    openai.api_key = api_key

st.sidebar.markdown("### About")
if st.sidebar.button("Show About"):
    st.sidebar.markdown(
        "This Application Was Developed By:  \n  \n Ahmed Y. Azzam, MD, MEng  \n Muhammed Amir Essibayi, MD  \n  \n Under Supervision of Cerebrovascular Research Lab Principal Investigator:  \n  \n David Altschul, MD"
    )

