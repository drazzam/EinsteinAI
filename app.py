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
 section_to_criticize = st.text_input("The Section Within The Paper To Be Criticized: (e.g. introduction, methods, results, discussion)")
 section = st.text_input("Paste The Section From Manuscript Here:")

 # Button to generate the prompt
 generate_button = st.button("Generate Prompt")

 # Function to create the prompt
 def create_prompt(manuscript_title, research_paper_type, section_to_criticize):
     prompt = f'''This a draft manuscript proposed for a research paper entitled "{manuscript_title}" which is a {research_paper_type} article.

 Could you criticize and review the following {section_to_criticize} section in the manuscript draft, and provide a detailed feedback report on how to improve it from all aspects including: appropriate writing and proofreading, appropriate methodology and sequence, and the science within the section itself. Generate a comprehensive professional report and recommendations for this manuscript, please!

 That's the {section_to_criticize} section:
 {section}'''

     return prompt

 # Function to create a Word document with the prompt
 def create_word_document(prompt):
     doc = docx.Document("https://github.com/drazzam/EinsteinAI/blob/main/templates/Research_Advisor.docx?raw=true")
     p = doc.add_paragraph()
     p.add_run("\n\n")
     p.add_run(prompt).bold = True
     p.space_before = Pt(12)
     p.space_after = Pt(12)
     p.add_run().add_break(WD_BREAK.PAGE)
     return doc

 # Function to export the Word document to a PDF
 def export_to_pdf(doc):
     options = {
         'quiet': '',
         'dpi': 300,
     }
     filename = "generated_prompt.pdf"
     docx_filename = "generated_prompt.docx"
     doc.save(docx_filename)
     pdfkit.from_file(docx_filename, filename, options=options)
     return filename

 if generate_button:
     # Generate the prompt
     prompt = create_prompt(manuscript_title, research_paper_type, section_to_criticize)
     st.write(prompt)

     # Offer download options
     download_option = st.selectbox("Download as:", ["Word Document", "PDF"])

     # Create the Word document and download
     doc = create_word_document(prompt)

     if download_option == "Word Document":
         with BytesIO() as docx_data:
             doc.save(docx_data)
             b64 = base64.b64encode(docx_data.getvalue()).decode()
             href = f'<a href="data:application/octet-stream;base64,{b64}" download="generated_prompt.docx">Download as Word Document</a>'
             st.markdown(href, unsafe_allow_html=True)

     if download_option == "PDF":
         pdf_filename = export_to_pdf(doc)
         with open(pdf_filename, "rb") as pdf_data:
             b64 = base64.b64encode(pdf_data.read()).decode()
             href = f'<a href="data:application/octet-stream;base64,{b64}" download="generated_prompt.pdf">Download as PDF</a>'
             st.markdown(href, unsafe_allow_html=True)

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
    
st.sidebar.markdown("### API Key")
api_key = st.sidebar.text_input("Enter your OpenAI API key:", type="password")
if api_key:
    openai.api_key = api_key

st.sidebar.markdown("### About")
if st.sidebar.button("Show About"):
    st.sidebar.markdown(
        "This Application Was Developed By:  \n  \n Ahmed Y. Azzam, MD, MEng  \n Muhammed Amir Essibayi, MD  \n  \n Under Supervision of Cerebrovascular Research Lab Principal Investigator:  \n  \n David Altschul, MD"
    )

