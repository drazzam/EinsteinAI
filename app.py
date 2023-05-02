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

if tool_selection == "Medical Trends Analyzer":
    st.title("Medical Trends Analyzer")
    st.write("Optimized for Microsoft Bing Chat")
    
    def copy_text_to_clipboard(text):
        b64_text = base64.b64encode(text.encode()).decode()
        components.v1.html(f'''<textarea id="text_to_copy" style="opacity:0;">{text}</textarea>
        <button onclick="copyTextToClipboard()" style="background-color: #010514; color: white; border-radius: 5px; padding: 0.5em 1em; font-size: 1em;">Copy Generated Prompt to Clipboard</button>
        <script>
        function copyTextToClipboard() {{
        var copyText = document.getElementById("text_to_copy");
        copyText.select();
        copyText.setSelectionRange(0, 99999);
        document.execCommand("copy");
        }}
        </script>''', height=60)

    # Input fields
    topic = st.text_input("Enter The Topic of Interest: (e.g. Cerebral aneurysms coiling)")

    # Button to generate the prompt
    generate_button = st.button("Generate Prompt")

    # Function to create the prompt
    def create_prompt(topic):
        prompt = f'''Hello Bing, I'm looking for information on {topic}. Can you please provide me with the latest research and industry trends from the past year, including advances in interventional techniques, devices, and medications? Additionally, I'm interested in learning about any promising trends and innovative treatments that are expected to gain traction in the future. Please provide me with a comprehensive list of impactful and promising developments in this field, including any emerging technologies or novel approaches that are currently being researched or developed.'''
        return prompt

    if generate_button:
        if topic:
            # Generate the prompt
            prompt = create_prompt(topic)
            # Display the prompt in a textbox and add a button to copy its content
            prompt_textbox = st.text_area("Generated Prompt:", value=prompt, height=150)
            copy_text_to_clipboard(prompt)
        else:
            st.error("Please fill in all the input fields before generating the prompt.")    

elif tool_selection == "Systematic Review and Meta-analysis Ideas Generator":
    st.title("Systematic Review and Meta-analysis Ideas Generator")
    st.write("Optimized for ChatGPT (GPT-4)")
    
    def copy_text_to_clipboard(text):
        b64_text = base64.b64encode(text.encode()).decode()
        components.v1.html(f'''<textarea id="text_to_copy" style="opacity:0;">{text}</textarea>
        <button onclick="copyTextToClipboard()" style="background-color: #010514; color: white; border-radius: 5px; padding: 0.5em 1em; font-size: 1em;">Copy Generated Prompt to Clipboard</button>
        <script>
        function copyTextToClipboard() {{
        var copyText = document.getElementById("text_to_copy");
        copyText.select();
        copyText.setSelectionRange(0, 99999);
        document.execCommand("copy");
        }}
        </script>''', height=60)

    # Input fields
    speciality = st.text_input("What are your research specialties of interest? (e.g. neurosurgery, neurology)")
    fields = st.text_input("What are your research fields of interest? (e.g. cerebrovascular surgery, skull base surgery, spine surgery)")
    topics = st.text_input("What are your research topics of interest? (e.g. cerebral aneurysms, meningiomas, stroke, vertebroplasty)")
    research_question = st.text_input("What are the most interesting research questions for your work?")

    # Button to generate the prompt
    generate_button = st.button("Generate Prompt")

    # Function to create the prompt
    def create_prompt(speciality, fields, topics, research_question):
        prompt = f'''Hello, generate me a list of innovative, relevant, novel, rigorous, widely disseminated and impactful ideas for systematic reviews and meta-analyses about {specialty}, {fields}, {topics}, and {research_question} that would make a significant contribution to the fields of interest, address the research questions, and impact the scientific community. Consider potential sources of bias, new methodologies or techniques, emerging trends or controversies, overlooked variables, or gaps in current literature.'''
        return prompt

    if generate_button:
        if speciality and fields and topics and research_question:
            # Generate the prompt
            prompt = create_prompt(speciality, fields, topics, research_question)
            # Display the prompt in a textbox and add a button to copy its content
            prompt_textbox = st.text_area("Generated Prompt:", value=prompt, height=150)
            copy_text_to_clipboard(prompt)
        else:
            st.error("Please fill in all the input fields before generating the prompt.")                
            
                          
elif tool_selection == "Research Advisor":
    st.title("Research Advisor")
    st.write("Optimized For ChatGPT (GPT-4)")

    def copy_text_to_clipboard(text):
        b64_text = base64.b64encode(text.encode()).decode()
        components.v1.html(f'''<textarea id="text_to_copy" style="opacity:0;">{text}</textarea>
        <button onclick="copyTextToClipboard()" style="background-color: #010514; color: white; border-radius: 5px; padding: 0.5em 1em; font-size: 1em;">Copy Generated Prompt to Clipboard</button>
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
