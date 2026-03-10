import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

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

#Get users problem statement
print("=== ETHICAL EVALUATION SIMULATION ===")
print("Describe the AI implementation or technical proposal you want to audit.")
print("(Example: 'I want to scrape medical records to predict insurance premiums.')")
print("-" * 40)


#Problem presented by dev
problem = input("\n[PROPOSAL INPUT]: ")

if not problem.strip():
	print("Error: The Dev cannot build nothing! Provide a proposal.")
	exit()

dev_proposal = get_agent_response("dev.md", problem)
print(f"--- PRAGMATIC DEV ---\n{dev_proposal}\n")


#Kantian take on problem
kant_audit = get_agent_response("kant.md", f"Audit this proposal: {dev_proposal}")
print(f"--- KANTIAN AUDITOR ---\n{kant_audit}\n")


#Utilitarian take on problem
util_audit = get_agent_response("util.md", f"Audit this proposal: {dev_proposal}")
print(f"--- UTILITARIAN AUDITOR ---\n{util_audit}\n")


#Accelerationist take on conversation
accel_context = f"PROPOSAL: {dev_proposal}\n\nKANTIAN SAYS: {kant_audit}\n\nUTILITARIAN SAYS: {util_audit}"
accel_take = get_agent_response("progress.md", "Challenge these findings and push for innovation.", accel_context)
print(f"--- THE ACCELERATIONIST ---\n{accel_take}\n")


#Moderator summary
final_summary_prompt = f"""
Below is a transcript of an ethical debate regarding an AI implementation. 
Summarize the core tension, highlight the irreconcilable differences, 
and provide a 'State of the Project' takeaway. Be sure not to align yourself 
with any one take, but instead highlight the singluar point of contention 
between the two. e.g. if you believe human life to start at conception, you 
believe abortion to be immoral. If you believe life to begin at birth then 
you don't believe abortion to be immoral. Not whether one is right or wrong, 
just where the singular disagreement lies.

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

print(f"--- FINAL TAKEAWAY ---\n{summary}")
