import os
import streamlit as st
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load API Key
load_dotenv()
client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))
model_id = "gemini-2.5-flash-lite"

def get_agent_response(role_file, prompt, context = ""):
    with open(f"agents/{role_file}", "r") as f:
        instructions = f.read()

    #Combining new prompt w context
    full_prompt = f"{context}\n\nCURRENTTASK:\n{prompt}" if context else prompt

    response = client.models.generate_content(
        model=model_id,
        config=types.GenerateContentConfig(system_instruction=instructions),
        contents=full_prompt
    )
    return response.text

# --- STREAMLIT UI ---
st.set_page_config(page_title="Ethical AI Auditor", page_icon="🎩")

st.title("⚖️ Ethical AI Evaluation Simulation")
st.markdown("""
Describe the AI implementation or technical proposal you want to audit.
*(Example: 'I want to scrape medical records to predict insurance premiums.')*
""")

# Input section
problem = st.text_area("AI Proposal Input", placeholder="Type your technical proposal here...")

if st.button("Run Audit"):
    if not problem.strip():
        st.error("Error: Please provide a proposal to audit.")
    else:
        with st.spinner("Analyzing ethical frameworks..."):
            # 1. Pragmatic Dev
            dev_proposal = get_agent_response("dev.md", problem)
            st.subheader("🛠️ Pragmatic Architect")
            st.info(dev_proposal)

            # 2. Kantian
            kant_audit = get_agent_response("kant.md", f"Audit this proposal: {dev_proposal}")
            st.subheader("⚖️ Kantian Auditor")
            st.warning(kant_audit)

            # 3. Utilitarian
            util_audit = get_agent_response("util.md", f"Audit this proposal: {dev_proposal}")
            st.subheader("📊 Utilitarian Auditor")
            st.success(util_audit)

            # 4. Accelerationist
            accel_context = f"PROPOSAL: {dev_proposal}\n\nKANTIAN SAYS: {kant_audit}\n\nUTILITARIAN SAYS: {util_audit}"
            accel_take = get_agent_response("progress.md", "Challenge these findings and push for innovation.", accel_context)
            st.subheader("🚀 The Accelerationist")
            st.error(accel_take)

            # 5. Final Summary
            final_summary_prompt = f"""
            Below is a transcript of an ethical debate regarding an AI implementation. 
            Summarize the core tension, highlight the irreconcilable differences, 
            and provide a 'State of the Project' takeaway. Be sure not to align yourself 
            with any one take, but instead highlight the singluar point of contention 
            between the two.

            TRANSCRIPT:
            Dev: {dev_proposal}
            Kant: {kant_audit}
            Utility: {util_audit}
            Accel: {accel_take}
            """

            summary = client.models.generate_content(
                model=model_id,
                contents=final_summary_prompt
            ).text

            st.divider()
            st.header("🏁 Final Takeaway")
            st.write(summary)
