import streamlit as st
from streamlit import components
import io
import base64
from io import BytesIO
import requests

# Add logo
st.sidebar.image('https://raw.githubusercontent.com/drazzam/EinsteinAI/main/logo.png')

st.sidebar.markdown("##### An Artificial Intelligence Prompt Engineering Tool Developed by Cerebrovascular Research Lab at Albert Einstein College of Medicine")

tool_selection = st.sidebar.radio("Select a tool:", [
    "Risk of Bias Assessment",
    "Medical Trends Analyzer",
    "Systematic Review and Meta-analysis Ideas Generator",
    "Research Advisor",
    "Statistical Plan Consultant",
    "Sample Size Calculator",
    "Abstract and Keywords Generator",
    "Search Strategy Formulator",
    "Funding Opportunities Finder",
])

if tool_selection == "Risk of Bias Assessment":
    st.title("Risk of Bias Assessment")
    st.write("Optimized for Humata AI")
    options = ["Cochrane RoB 2.0", "ROBINS-I", "STROBE For Observational Studies"]
    selected_option = st.selectbox("Select a Risk of Bias Assessment Scale:", options)
    paper_title = st.text_input("Enter The Research Paper Tile:")
    research_type = st.text_input("Enter The Research Paper Type: (e.g. Randomized Controlled Trial, Clinical Trial, Retrospective Study, Cohort Study)")
    
    if selected_option == "Cochrane RoB 2.0":
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

        # Button to generate the prompt
        generate_button = st.button("Generate Prompt")

        # Function to create the prompt
        def create_prompt(paper_title, research_type):
            prompt = f'''Please assess the risk of bias in the {research_type}, the study's name is "{paper_title}". Assess the study provided according to Version 2 of the Cochrane risk-of-bias tool for randomized trials (RoB 2) tool. Please rate the bias for each of the following domains as low risk of bias, high risk of bias, and unclear risk of bias:

Random sequence generation:
Allocation concealment:
Blinding of participants and personnel:
Binding of outcome assessment:
Incomplete outcome data:
Selective reporting:
Other bias:

Note 1: The only condition that the overall risk of bias assessment is low when all of items are low.
Note 2: If there is at least one item classified as high, then the overall assessment for risk of bias is high.

After rating the bias, fill the following template with the results:

1. Random sequence generation:
2. Allocation concealment:
3. Blinding of participants and personnel:
4. Binding of outcome assessment:
5. Incomplete outcome data:
5. Selective reporting:
6. Other bias:'''
            return prompt

        if generate_button:
            if paper_title and research_type:
                # Generate the prompt
                prompt = create_prompt(paper_title, research_type)
                # Display the prompt in a textbox and add a button to copy its content
                prompt_textbox = st.text_area("Generated Prompt:", value=prompt, height=150)
                copy_text_to_clipboard(prompt)
            else:
                st.error("Please fill in all the input fields before generating the prompt.")     
   
    if selected_option == "ROBINS-I":
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

        # Button to generate the prompt
        generate_button = st.button("Generate Prompt")

        # Function to create the prompt
        def create_prompt(paper_title, research_type):
            prompt = f'''Please assess the risk of bias in the study provided according to the ROBINS-I tool. The study's name is "{paper_title}", which is a {research_type} study. Please rate the bias for each of the following domains as low, moderate, serious, critical, or no information:

D1: Bias due to confounding
D2: Bias due to selection of participants
D3: Bias in classification of interventions
D4: Bias due to deviation from intended interventions
D5: Bias due to missing data
D6: Bias in measurement of outcomes
D7: Bias in selection of the reported results

After assessing each domain, please provide an overall risk of bias assessment for the study. Please fill out the table below with the domain ratings and overall assessment:

Study Name: {paper_title}

1. Bias due to confounding:
2. Bias due to selection of participants:
3. Bias in classification of interventions:
4. Bias due to deviation from intended interventions:
5. Bias due to missing data:
6. Bias in measurement of outcomes:
7. Bias in selection of the reported results:
8. Overall:
 
Note 1: The only condition that the overall risk of bias assessment is low when all of items from D1 to D7 are low.
Note 2: If there is at least one item classified as serious, then the overall assessment for risk of bias is serious.
Note 3: If there is at least one item classified as critical, then the overall assessment for risk of bias is critical.'''
            return prompt

        if generate_button:
            if paper_title and research_type:
                # Generate the prompt
                prompt = create_prompt(paper_title, research_type)
                # Display the prompt in a textbox and add a button to copy its content
                prompt_textbox = st.text_area("Generated Prompt:", value=prompt, height=150)
                copy_text_to_clipboard(prompt)
            else:
                st.error("Please fill in all the input fields before generating the prompt.") 

    if selected_option == "STROBE For Observational Studies":
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

        # Button to generate the prompt
        generate_button = st.button("Generate Prompt")

        # Function to create the prompt
        def create_prompt(paper_title, research_type):
            prompt = f'''Please assess the risk of bias in the study provided according to the STROBE for Observational Studies tool. The study's name is "{paper_title}", which is a {research_type} study. Please rate the bias for each of the following domains as low risk, moderate risk or high risk:

Methods for selecting study participants:
Methods for measuring exposure and outcome variables:
Methods to control cofounding:
Design-specific sources of bias:
Statistical methods:
Risk of bias:

After assessing each domain, please provide an overall risk of bias assessment for the study. Please fill out the table below with the domain ratings and overall assessment:

Study Name: {paper_title}

1. Methods for selecting study participants:
2. Methods for measuring exposure and outcome variables:
3. Methods to control cofounding:
4. Design-specific sources of bias:
5. Statistical methods:
6. Risk of bias:
 
Note 1: The only condition that the overall risk of bias assessment is low when all of items are low.
Note 2: If there is at least one item classified as high, then the overall assessment for risk of bias is high.'''
            return prompt

        if generate_button:
            if paper_title and research_type:
                # Generate the prompt
                prompt = create_prompt(paper_title, research_type)
                # Display the prompt in a textbox and add a button to copy its content
                prompt_textbox = st.text_area("Generated Prompt:", value=prompt, height=150)
                copy_text_to_clipboard(prompt)
            else:
                st.error("Please fill in all the input fields before generating the prompt.")  

if tool_selection == "Medical Trends Analyzer":
    st.title("Medical Trends Analyzer")
    st.write("Optimized for Microsoft Bing Chat")
    st.markdown("[Click Here For Tutorial](https://www.youtube.com/watch?v=VIDEO_ID)")
    
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
    specialty = st.text_input("What are your research specialties of interest? (e.g. neurosurgery, neurology)")
    fields = st.text_input("What are your research fields of interest? (e.g. cerebrovascular surgery, skull base surgery, spine surgery)")
    topics = st.text_input("What are your research topics of interest? (e.g. cerebral aneurysms, meningiomas, stroke, vertebroplasty)")
    research_question = st.text_input("What are the most interesting research questions for your work?")

    # Button to generate the prompt
    generate_button = st.button("Generate Prompt")

    # Function to create the prompt
    def create_prompt(specialty, fields, topics, research_question):
        prompt = f'''Hello, generate me a list of innovative, relevant, novel, rigorous, widely disseminated and impactful ideas for systematic reviews and meta-analyses about {specialty} as research specialty/specialties of interest, {fields} as research field(s) of interest, {topics} as research topic(s) of interest, and {research_question} as the most interesting research question(s) for our work that would make a significant contribution to the fields of interest, address the research questions, and impact the scientific community. Consider potential sources of bias, new methodologies or techniques, emerging trends or controversies, overlooked variables, or gaps in current literature.'''
        return prompt

    if generate_button:
        if specialty and fields and topics and research_question:
            # Generate the prompt
            prompt = create_prompt(specialty, fields, topics, research_question)
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

elif tool_selection == "Statistical Plan Consultant":
    st.title("Statistical Plan Consultant")
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
    summary = st.text_input("Please provide a brief summary of your research question:")
    scope = st.text_input("What is the scope of your research? Is it exploratory, descriptive, or explanatory?")
    primary_objectives = st.text_input("What are the primary objectives of your study?")
    secondary_objectives = st.text_input("What are the secondary objectives of your study?")
    hypothesis = st.text_input("What is your research hypothesis?")
    null_hypothesis = st.text_input("What is your null hypothesis?")
    data_type = st.text_input("What type of data do you have? Is it continuous, categorical, binary, or mixed?")
    level = st.text_input("What is the level of measurement of the variables in your study? Are they nominal, ordinal, interval, or ratio?")
    collection = st.text_input("How was the data collected? Was it retrospective, prospective, or a combination of both?")
    sampling = st.text_input("What is the sampling method? Is it random, stratified, or cluster sampling?")
    sample_size = st.text_input("What is the size of your sample?")
    desired_sample = st.text_input("Was your sample size the desired number for the study, or less than the desired sample size number?")
    bias = st.text_input("Are there any potential biases in the data?")
    missing_data = st.text_input("Do you have any missing data? If so, what percentage of your data is missing")
    limitations = st.text_input("What are the limitations of your study?")
    outliers = st.text_input("Does your data have any outliers or influential observations that need to be addressed?")
    normality = st.text_input("Have you checked for normality or other assumptions of the statistical tests you plan to use?")
    study_design = st.text_input("What is your study design? Is it experimental, observational, or a combination of both?")
    groups = st.text_input("Are the groups independent or dependent?")
    cofounding_variables = st.text_input("Are there any confounding variables that need to be controlled for in your analysis?")
    variables_interactions = st.text_input("Are there any interactions between variables that need to be considered in your analysis?")
    dependent_variables = st.text_input("What are the dependent variables in your study?")
    independent_variables = st.text_input("What are the independent variables in your study?")
    recommendations = st.text_input("What are the recommendations for future research?")
    data_format = st.text_input("What is the data format? Is it in raw form, cleaned, or transformed?")
    desired_significance = st.text_input("What is the desired level of significance and power?")
    effect_size = st.text_input("What is the effect size you are interested in detecting?")
    population_parameter = st.text_input("Are you interested in estimating a population parameter or making a prediction?")
    multiple_comparisons = st.text_input("Do you need to adjust for multiple comparisons in your analysis?")
    implications = st.text_input("What are the expected implications of your study for theory and practice?")
    
    # Button to generate the prompt
    generate_button = st.button("Generate Prompt")

    # Function to create the prompt
    def create_prompt(summary, scope, primary_objectives, secondary_objectives, hypothesis, null_hypothesis, data_type, level, collection, sampling, sample_size, desired_sample, bias, missing_data, limitations, outliers, normality, study_design, groups, cofounding_variables, variables_interactions, dependent_variables, independent_variables, recommendations, data_format, desired_significance, effect_size, population_parameter, multiple_comparisons, implications):
        prompt = f'''1. Please provide a brief summary of your research question: {summary} 2. What is the scope of your research? Is it exploratory, descriptive, or explanatory? {scope} 3. What are the primary objectives of your study? {primary_objectives} 4. What are the secondary objectives of your study? {secondary_objectives} 5. What is your research hypothesis? {hypothesis} 6. What is your null hypothesis? {null_hypothesis} 7. What type of data do you have? Is it continuous, categorical, binary, or mixed?  {data_type} 8. What is the level of measurement of the variables in your study? Are they nominal, ordinal, interval, or ratio? {level} 9. How was the data collected? Was it retrospective, prospective, or a combination of both? {collection} 10. What is the sampling method? Is it random, stratified, or cluster sampling? {sampling} 11. What is the size of your sample? {sample_size} 12. Was your sample size the desired number for the study, or less than the desired sample size number? {desired_sample} 13. Are there any potential biases in the data? {bias} 14. Do you have any missing data? If so, what percentage of your data is missing? {missing_data} 15. What are the limitations of your study? {limitations} 16. Does your data have any outliers or influential observations that need to be addressed? {outliers} 17. Have you checked for normality or other assumptions of the statistical tests you plan to use? {normality} 18. What is your study design? Is it experimental, observational, or a combination of both? {study_design} 19. Are the groups independent or dependent? {groups} 20. Are there any confounding variables that need to be controlled for in your analysis? {cofounding_variables} 21. Are there any interactions between variables that need to be considered in your analysis? {variables_interactions} 22. What are the dependent variables in your study? {dependent_variables} 23. What are the independent variables in your study? {independent_variables} 24. What are the recommendations for future research? {recommendations} 25. What is the data format? Is it in raw form, cleaned, or transformed? {data_format} 26. What is the desired level of significance and power? {desired_significance} 27. What is the effect size you are interested in detecting? {effect_size} 28. Are you interested in estimating a population parameter or making a prediction? {population_parameter} 29. Do you need to adjust for multiple comparisons in your analysis? {multiple_comparisons} 30. What are the expected implications of your study for theory and practice? {implications} Based on the answers to these questions, a comprehensive statistical plan should be generated to address the specific needs of the study. The plan should include a detailed description of the statistical methods to be used, as well as any necessary assumptions, procedures, and tests. It should also outline the specific steps to be taken to analyze the data and report the results in a clear and concise manner. The statistical plan should be comprehensive, organized in a step-by-step manner and easy to follow and apply.'''
        return prompt

    if generate_button:
        if summary and scope and primary_objectives and secondary_objectives and hypothesis and null_hypothesis and data_type and level and collection and sampling and sample_size and desired_sample and bias and missing_data and limitations and outliers and normality and study_design and groups and cofounding_variables and variables_interactions and dependent_variables and independent_variables and recommendations and data_format and desired_significance and effect_size and population_parameter and multiple_comparisons and implications:
            # Generate the prompt
            prompt = create_prompt(summary, scope, primary_objectives, secondary_objectives, hypothesis, null_hypothesis, data_type, level, collection, sampling, sample_size, desired_sample, bias, missing_data, limitations, outliers, normality, study_design, groups, cofounding_variables, variables_interactions, dependent_variables, independent_variables, recommendations, data_format, desired_significance, effect_size, population_parameter, multiple_comparisons, implications)
            # Display the prompt in a textbox and add a button to copy its content
            prompt_textbox = st.text_area("Generated Prompt:", value=prompt, height=150)
            copy_text_to_clipboard(prompt)
        else:
            st.error("Please fill in all the input fields before generating the prompt.")            

elif tool_selection == "Statistical Plan Consultant":
    st.title("Statistical Plan Consultant")
    st.write("Optimized for ChatGPT (GPT-4)")
    st.markdown("[Click Here For Tutorial](https://www.youtube.com/watch?v=VIDEO_ID)")
    
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
    summary = st.text_input("Please provide a brief summary of your research question:")
    scope = st.text_input("What is the scope of your research? Is it exploratory, descriptive, or explanatory?")
    primary_objectives = st.text_input("What are the primary objectives of your study?")
    secondary_objectives = st.text_input("What are the secondary objectives of your study?")
    hypothesis = st.text_input("What is your research hypothesis?")
    null_hypothesis = st.text_input("What is your null hypothesis?")
    expected_effect = st.text_input("What is the expected effect size of the intervention or relationship you are studying?")
    sig_level = st.text_input("What is the significance level you want to use? (e.g. 0.05, 0.01)")
    power = st.text_input("What is the power you want to achieve? (e.g. 0.8, 0.9)")
    population_size = st.text_input("What is the population size you are sampling from?")
    res_rate = st.text_input("What is the expected response rate from the population?")
    tail = st.text_input("Is this a one-tailed or two-tailed test?")
    var_source = st.text_input("Are there any known sources of variation or stratification in the population that need to be accounted for in the sample size calculation?")
    const = st.text_input("Do you have any constraints on the maximum sample size you can use for your study (e.g. budget, time, resources)?")
    ethical = st.text_input("Are there any ethical considerations that need to be taken into account when determining the sample size for your study?")
    sampling_method = st.text_input("What type of sampling method will you use (e.g. random, stratified, cluster)?")
    drop_out = st.text_input("What is the expected rate of attrition or drop-out from the study?")
    complex_analysis = st.text_input("Will the study involve any complex or multi-level analyses that may impact the required sample size?")
    subgroup = st.text_input("Are there any specific subgroups or populations within the overall population that need to be accounted for in the sample size calculation?")
    bias_source = st.text_input("Are there any other potential sources of bias or confounding factors that may impact the sample size calculation?")
    covar_size = st.text_input("What is the expected effect size of the covariates in the study (if any)?")
    dep_corr = st.text_input("Are there any known dependencies or correlations between the response variable and the covariates?")

    # Button to generate the prompt
    generate_button = st.button("Generate Prompt")

    # Function to create the prompt
    def create_prompt(summary, scope, primary_objectives, secondary_objectives, hypothesis, null_hypothesis, expected_effect, sig_level, power, population_size, res_rate, tail, var_source, const, ethical, sampling_method, drop_out, complex_analysis, subgroup, bias_source, covar_size, dep_corr):
        prompt = f'''1. Please provide a brief summary of your research question: {summary}
2. What is the scope of your research? Is it exploratory, descriptive, or explanatory? {scope}
3. What are the primary objectives of your study? {primary_objectives}
4. What are the secondary objectives of your study? {secondary_objectives}
5. What is your research hypothesis? {hypothesis}
6. What is your null hypothesis? {null_hypothesis}
7. What is the expected effect size of the intervention or relationship you are studying? {expected_effect}
8. What is the significance level you want to use? {sig_level}
9. What is the power you want to achieve? {power}
10. What is the population size you are sampling from? {population_size}
11. What is the expected response rate from the population? {res_rate}
12. Is this a one-tailed or two-tailed test? {tail}
13. Are there any known sources of variation or stratification in the population that need to be accounted for in the sample size calculation? {var_source}
14. Do you have any constraints on the maximum sample size you can use for your study? {const}
15. Are there any ethical considerations that need to be taken into account when determining the sample size for your study? {ethical}
16. What type of sampling method will you use? {sampling_method}
17. What is the expected rate of attrition or drop-out from the study? {drop_out}
18. Will the study involve any complex or multi-level analyses that may impact the required sample size? {complex_analysis}
19. Are there any specific subgroups or populations within the overall population that need to be accounted for in the sample size calculation? {subgroup}
20. Are there any other potential sources of bias or confounding factors that may impact the sample size calculation? {bias_source}
21. What is the expected effect size of the covariates in the study (if any)? {covar_size}
22. Are there any known dependencies or correlations between the response variable and the covariates? {dep_corr}

Based on the previous questions and their answers, please provide the following information: The required sample size for each group of patients, calculated based on the specified significance level, power, and effect size.

Note: Please keep the response concise without explanation.'''
        return prompt

    if generate_button:
        if summary and scope and primary_objectives and secondary_objectives and hypothesis and null_hypothesis and expected_effect and sig_level and power and population_size and res_rate and tail and var_source and const and ethical and sampling_method and drop_out and complex_analysis and subgroup and bias_source and covar_size and dep_corr:
            # Generate the prompt
            prompt = create_prompt(summary, scope, primary_objectives, secondary_objectives, hypothesis, null_hypothesis, expected_effect, sig_level, power, population_size, res_rate, tail, var_source, const, ethical, sampling_method, drop_out, complex_analysis, subgroup, bias_source, covar_size, dep_corr)
            # Display the prompt in a textbox and add a button to copy its content
            prompt_textbox = st.text_area("Generated Prompt:", value=prompt, height=150)
            copy_text_to_clipboard(prompt)
        else:
            st.error("Please fill in all the input fields before generating the prompt.")             
            
elif tool_selection == "Abstract and Keywords Generator":
    st.title("Abstract and Keywords Generator")
    st.write("Optimized for Humata AI")
    st.markdown("[Click Here For Tutorial](https://www.youtube.com/watch?v=VIDEO_ID)")
    
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
    manuscript_title = st.text_input("Enter The Manuscript/Draft Title:")
    paper_type = st.text_input("Enter The Research Paper/Draft Type: (e.g. meta-analysis, retrospective study, review article)")

    # Button to generate the prompt
    generate_button = st.button("Generate Prompt")

    # Function to create the prompt
    def create_prompt(manuscript_title, paper_type):
        prompt = f'''Please generate an abstract and relevant keywords for a draft manuscript titled "{manuscript_title}". The manuscript is a {paper_type} research paper in PDF format. The abstract should be around 250 words and should follow the format of Introduction, Methods, Results, and Conclusions. Additionally, please provide five appropriate keywords for the manuscript. Your help is greatly appreciated.'''
        return prompt

    if generate_button:
        if manuscript_title and paper_type:
            # Generate the prompt
            prompt = create_prompt(manuscript_title, paper_type)
            # Display the prompt in a textbox and add a button to copy its content
            prompt_textbox = st.text_area("Generated Prompt:", value=prompt, height=150)
            copy_text_to_clipboard(prompt)
        else:
            st.error("Please fill in all the input fields before generating the prompt.")  

elif tool_selection == "Search Strategy Formulator":
    st.title("Search Strategy Formulator")
    st.write("Optimized for ChatGPT (GPT-4)")
    st.markdown("[Click Here For Tutorial](https://www.youtube.com/watch?v=VIDEO_ID)")
    
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
    overview = st.text_input("Please provide a concise overview of your research topic and research idea:")
    criteria = st.text_input("Please outline your inclusion and exclusion criteria for the literature search, specifying the characteristics that the relevant studies should possess and the ones that should be excluded:")
    databases = st.text_input("Please list the literature databases that you intend to search, considering the most appropriate options for your research topic:")
    
    # Button to generate the prompt
    generate_button = st.button("Generate Prompt")

    # Function to create the prompt
    def create_prompt(overview, criteria, databases):
        prompt = f'''1. Please provide a concise overview of your research topic and research idea: {overview}

2. Please outline your inclusion and exclusion criteria for the literature search, specifying the characteristics that the relevant studies should possess and the ones that should be excluded: {criteria}

3. Please list the literature databases that you intend to search, considering the most appropriate options for your research topic: {databases}

Based on the information you provided, please generate the appropriate MeSH terms, search formula, and search strategy for your literature review, ensuring that your search is comprehensive and targeted to capture all relevant studies while excluding irrelevant ones.'''
        return prompt

    if generate_button:
        if overview and criteria and databases:
            # Generate the prompt
            prompt = create_prompt(overview, criteria, databases)
            # Display the prompt in a textbox and add a button to copy its content
            prompt_textbox = st.text_area("Generated Prompt:", value=prompt, height=150)
            copy_text_to_clipboard(prompt)
        else:
            st.error("Please fill in all the input fields before generating the prompt.")              

elif tool_selection == "Funding Opportunities Finder":
    st.title("Funding Opportunities Finder")
    st.write("Optimized for Microsoft Bing Chat")
    st.markdown("[Click Here For Tutorial](https://www.youtube.com/watch?v=VIDEO_ID)")
    
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
    field = st.text_input("Enter The Specialty/Subspecialty of Your Research: (e.g. cerebrovasular surgery, skull base surgery)")
    country = st.text_input("Enter The Country of Your Work:")
    topics = st.text_input("Enter The Topics of Interest For Your Research: (e.g. cerebral aneurysms, stroke, brain tumors)")
    
    # Button to generate the prompt
    generate_button = st.button("Generate Prompt")

    # Function to create the prompt
    def create_prompt(field, country, topics):
        prompt = f'''Hello Bing, could you please help me find a comprehensive and up-to-date list of grant and funding opportunities for {field} research in {country}? Specifically, I am interested in funding options for {topics} research. Please provide links and websites for all potential funding and grant options, including both private and government funding sources. Additionally, could you provide me with information on general research funding authorities and options available in {country}? Thank you.'''
        return prompt

    if generate_button:
        if field and country and topics:
            # Generate the prompt
            prompt = create_prompt(field, country, topics)
            # Display the prompt in a textbox and add a button to copy its content
            prompt_textbox = st.text_area("Generated Prompt:", value=prompt, height=150)
            copy_text_to_clipboard(prompt)
        else:
            st.error("Please fill in all the input fields before generating the prompt.")
            
st.sidebar.markdown("### About")
if st.sidebar.button("Show About"):
    st.sidebar.markdown(
        "This Application Was Developed By:  \n  \n Ahmed Y. Azzam, MD(c), MEng(c)  \n Muhammed Amir Essibayi, MD  \n  \n Under Supervision of Cerebrovascular Research Lab Principal Investigator:  \n  \n David Altschul, MD"
    )            
