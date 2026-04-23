import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="Sociology GEM Agent", page_icon="🎓")

# Sidebar for API Key
with st.sidebar:
    st.title("Settings")
    api_key = st.text_input("Enter your Gemini API Key:", type="password")
    st.info("Get your key at: aistudio.google.com")

# Main Interface
st.title("🎓 Sociology PEEEL Agent")
st.markdown("### Powered by the Sociology GEM Logic")

# The "GEM" System Instructions (The Brain)
gem_prompt = """
You are a specialist A-Level Sociology Examiner. 
Structure: You strictly require PEEEL (Point, Explanation, Evidence, Evaluation, Link).
IMPORTANT: Explanation MUST come before Evidence.

Mark Band Logic:
- 25–30: Sound, conceptually detailed (AO1), sophisticated analysis (AO3), explicit evaluation (debate).
- 19–24: Accurate, broad but incomplete knowledge. Linear analysis. Limited evaluation.
- 13–18: Largely accurate but basic/superficial. Tending towards descriptive. Evaluation is juxtaposition.
- 7–12: Underdeveloped, tangential, thin/disjointed.

Task:
Analyze the student's paragraph. 
1. Assign a Mark Band.
2. Identify each PEEEL component and if they are in the correct order.
3. Audit the 'Chain of Reasoning' (AO3).
4. Provide 'Missing Elements' suggestions to help them reach the next band.
Tone: Academic, authoritative, yet supportive peer.
"""

user_text = st.text_area("Paste your paragraph for the GEM Agent to assess:", height=300)

if st.button("Analyze with GEM"):
    if not api_key:
        st.error("Please enter your API Key in the sidebar first!")
    elif not user_text:
        st.warning("Please paste a paragraph to analyze.")
    else:
        try:
            genai.configure(api_key=api_key)
           model = genai.GenerativeModel('gemini-1.5-flash-latest')
            
            with st.spinner("The Agent is reviewing your AO1, AO2, and AO3..."):
                response = model.generate_content([gem_prompt, user_text])
                
                st.success("Analysis Complete!")
                st.divider()
                st.markdown(response.text)
                
        except Exception as e:
            st.error(f"An error occurred: {e}")
