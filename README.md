# ⚖️ Phi Auditor: An Ethical AI Evaluation Simulation

**Phi Auditor** is a Streamlit-powered dashboard that uses Large Language Models (LLMs) to perform multi-perspective ethical audits on technical proposals. 

By simulating a debate between four distinct philosophical and pragmatic personas, this tool helps developers identify potential "downstream externalities" and ethical contradictions before a model is deployed.

---

## 🎭 The Auditors

- **🛠️ Pragmatic Architect**: A Senior AI Engineer who values system integrity, accuracy, and metric-driven performance. Treats ethics as "bureaucratic noise."
- **⚖️ Kantian Auditor**: Embodies Deontological Ethics. Evaluates proposals based on the Categorical Imperative and the inherent dignity of human beings.
- **📊 Utilitarian Auditor**: A cold strategist who calculates Aggregate Utility (Greatest Happiness Principle). Morality is a mathematical equation: (Total Benefit - Total Suffering).
- **🚀 The Accelerationist**: Challenges the auditors' findings and pushes for rapid innovation. Focuses on the "Will to Technicity" and the inevitability of progress.

---

## 🛠️ Tech Stack

- **Python 3.12**
- **Streamlit**: For the interactive web dashboard.
- **Google Gemini API**: To power the auditor personas.
- **Docker**: For containerized, cross-platform deployment.
- **python-dotenv**: For secure environment variable management.

---

## 🚀 Getting Started

### Prerequisites

- A **Google Gemini API Key** (Get one at [Google AI Studio](https://aistudio.google.com/)).
- **Docker** (Optional, but recommended for clean execution).

### Option 1: Running with Docker (Recommended)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ashwinsundaram1/phi-auditor.git
   cd phi-auditor
   ```

2. **Create a `.env` file** with your API key:
   ```bash
   echo "GOOGLE_API_KEY=your_actual_key_here" > .env
   ```

3. **Build the Docker image**:
   ```bash
   docker build -t phi-auditor .
   ```

4. **Run the container**:
   ```bash
   docker run -p 8501:8501 --env-file .env phi-auditor
   ```
   Now, open your browser and go to `http://localhost:8501`.

### Option 2: Running Locally

1. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   streamlit run main.py
   ```

---

## 📜 License

This project is open-source and intended for educational and research purposes in the field of AI Ethics and Data Science.

---

*“Reason is, and ought only to be the slave of the passions.”* — David Hume (probably not while he was debugging Docker).
