import streamlit as st

# Set the app title and icon
st.set_page_config(page_title="EinsteinAI", page_icon=":brain:")

# Define the sidebar menu
menu_items = ["Risk of Bias Assessment Tool", "Cover Letter Generator", 
              "Systematic Review and Meta-analysis Ideas Generator", 
              "Research Methodology Advisor, Reviewer and Proofreading Tool", 
              "Statistical Plan Consultant Tool", "Meta-analysis Statistical Plan Consultant", 
              "Sample Size Calculator Tool", "Abstract and Keywords Generator", 
              "Virtual Librarian Tool", "Assistant Extraction Tool"]
selected_item = st.sidebar.selectbox("Select a tool", menu_items)

# Define the settings menu
st.sidebar.subheader("Settings")
api_key = st.sidebar.text_input("ChatGPT API Key")
if st.sidebar.button("Connect API"):
    # Code to connect to the ChatGPT API using the provided key
    st.success("API connected!")
if st.sidebar.button("Switch theme"):
    # Code to switch between dark mode and light mode
    if st.get_theme() == "dark":
        st.set_theme("light")
    else:
        st.set_theme("dark")

# Define the about menu
st.sidebar.subheader("About")
st.sidebar.write("This application was developed by Cerebrovascular Research Lab at Albert Einstein College of Medicine")

# Render the selected tool
if selected_item == "Risk of Bias Assessment Tool":
    # Code to render the Risk of Bias Assessment Tool
    st.write("Risk of Bias Assessment Tool")
elif selected_item == "Cover Letter Generator":
    # Code to render the Cover Letter Generator
    st.write("Cover Letter Generator")
elif selected_item == "Systematic Review and Meta-analysis Ideas Generator":
    # Code to render the Systematic Review and Meta-analysis Ideas Generator
    st.write("Systematic Review and Meta-analysis Ideas Generator")
elif selected_item == "Research Methodology Advisor, Reviewer and Proofreading Tool":
    # Code to render the Research Methodology Advisor, Reviewer and Proofreading Tool
    st.write("Research Methodology Advisor, Reviewer and Proofreading Tool")
elif selected_item == "Statistical Plan Consultant Tool":
    # Code to render the Statistical Plan Consultant Tool
    st.write("Statistical Plan Consultant Tool")
elif selected_item == "Meta-analysis Statistical Plan Consultant":
    # Code to render the Meta-analysis Statistical Plan Consultant
    st.write("Meta-analysis Statistical Plan Consultant")
elif selected_item == "Sample Size Calculator Tool":
    # Code to render the Sample Size Calculator Tool
    st.write("Sample Size Calculator Tool")
elif selected_item == "Abstract and Keywords Generator":
    # Code to render the Abstract and Keywords Generator
    st.write("Abstract and Keywords Generator")
elif selected_item == "Virtual Librarian Tool":
    # Code to render the Virtual Librarian Tool
    st.write("Virtual Librarian Tool")
elif selected_item == "Assistant Extraction Tool":
    # Code to render the Assistant Extraction Tool
    st.write("Assistant Extraction Tool")
