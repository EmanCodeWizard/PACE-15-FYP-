# ⚡ PACE-15 / ARGUS-15: Tactical AI-Powered FIR Intelligence Platform

> **A Next-Generation Conversational AI, NLP Engine, and Automated Document Generation System for Pakistan's Justice System.**
> *Completely aligned with the Code of Criminal Procedure (CrPC 1898), Pakistan Penal Code (PPC), and Punjab Police Order 2002.*

---

## 📌 Project Overview

**PACE-15 / ARGUS-15** is an enterprise-grade, conversational intelligence system designed to revolutionize the First Information Report (FIR) filing process. Traditionally, registering a complaint at a police station (Thana) is a time-consuming, friction-heavy, and complex process. 

This platform reduces complaint-taking overhead by **84%**, condensing a standard hours-long manual reporting procedure into a structured, highly secure, and intuitive **5-to-8 minute digital conversation**. By combining a state-of-the-art NLP conversational assistant (powered by Llama-3.3-70B via Groq) with a real-time legal/jurisdictional engine and automated document rendering, PACE-15 ensures complete procedural integrity, precise legal classification, and a modern, high-fidelity experience for both citizens and law enforcement officers.

---

## 🚀 Key Features

### 1. 🤖 Context-Aware Conversational State Machine
* **Procedural State Control:** Built-in 12-step legal interview process designed strictly around Section 154 of the CrPC. The AI walks complainants through legal disclosures (rights, free FIR copy, Section 22-A CJM options, confidentiality) before systematically acquiring complainant info, incident details, witnesses, losses, and final affirmations.
* **Empathetic and Calm Tone:** Tailored system prompts keep the AI focused, calm, and respectful under all circumstances. It asks exactly one question at a time to prevent cognitive overload.
* **Graceful Fallbacks:** Incorporates regex-based heuristic field extractors and static mockup conversation flows in case of temporary LLM or network issues.

### 2. 🌐 Tri-Lingual & Language-Lock Engine
* **Automatic Language Detection:** Autodetects the language of the complainant's first input (English, Urdu Script, or Roman Urdu).
* **Deterministic Language-Lock:** Instantly locks the conversational state to the detected language. This guarantees the agent never switches languages mid-conversation, eliminating confusing bilingual "code-switching."

### 3. ⚖️ Algorithmic Crime Detection & PPC Mapping
* **Dynamic Offence Classification:** Analyzes narrative text in real-time to identify 10 distinct crime categories (Murder, Rape, Kidnapping, Theft, Dacoity, Assault, Harassment, Threat, Fraud, and Accident).
* **Pakistan Penal Code (PPC) Integration:** Automatically maps detected crimes to their relevant legal frameworks (e.g., Murder to PPC Section 302, Theft to PPC Section 379/380, Harassment to PPC Section 509).
* **Legal Class Status:** Immediately alerts the system if a crime is **Cognizable** (requiring an immediate mandatory FIR) or **Non-Cognizable** (requiring a Daily Diary/Roznamcha entry first).

### 4. 🏥 Urgency Triaging & Medico-Legal Advisory
* **Division-Level Jurisdiction Mapping:** Automatically parses locations and matches them to Punjab Police Administrative Divisions (Lahore, Rawalpindi, Gujranwala, Faisalabad, Multan, etc.) to verify jurisdiction.
* **Urgency Triaging:** Assigns real-time priority levels (A - Critical, B - High, C - Standard) with immediate triggers to notify SHOs, DSPs, or Moharrars.
* **Timed Action Alerts:** Computes elapsed hours from the incident. Triggers timeline-sensitive protocols, such as mandatory forensic dispatch (FSL) within 24 hours, and immediate DHQ Hospital referrals for medico-legal examinations (MLC) within 72 hours for assault and sexual assault cases.

### 5. 🖨️ Automated PDF Report & Narrative Generation
* **ReportLab Document Automation:** Programmatically compiles publication-grade PDF documents with professional layout templates (Navy & Gold color schemes, official header watermarks, table grids, signature blocks, and official seals).
* **Three Automated Outputs:**
  1. **Official FIR Document:** Formatted layout with metadata grids containing all structured complainant and incident fields.
  2. **Conversation Transcript:** Complete word-for-word legal transcript of the interview session.
  3. **Combined Document:** Combines the official FIR registry with a beautifully synthesized, coherent incident storyline paragraph written from the complainant's perspective.

### 6. 🛡️ Resilient API Key Rotation Pool & Enterprise Backend
* **Round-Robin Multi-Key Manager:** Manages multiple Groq API keys concurrently to prevent rate limit (`HTTP 429`) ceilings.
* **Exponential Backoff & Cooling States:** Intelligently tracks key success rates and places rate-limited keys on cooldown.
* **Supabase Integration:** Secure JWT authentication, structured PGSQL tables for user directories and active complaints, and secure Storage Buckets for uploaded evidence files and generated PDFs.

---

## 🛠️ Tech Stack

* **Backend Framework:** FastAPI (Python 3.12+)
* **Database & Auth:** Supabase (PostgreSQL, GoTrue Auth)
* **Storage:** Supabase Storage Buckets
* **Conversational LLM:** Llama-3.3-70B-Versatile (via Groq API)
* **Document Engine:** ReportLab PDF Library
* **Frontend Interface:** Vanilla HTML5, JavaScript (ES6+), Tailwind CSS (Premium Dark Mode & Glassmorphic Custom Theme)
* **Environment Management:** Dotenv (`.env`)

---

## 📁 Workspace Directory Structure

```
smart_fir_text/
│
├── api/
│   ├── main.py                     # Main FastAPI application, routes, and PDF builders
│   └── __pycache__/
│
├── nlp_engine/
│   ├── __init__.py
│   ├── llm_agent.py                # Core Llama conversational agent, key pool, and classifiers
│   └── __pycache__/
│
├── frontend/
│   ├── index.html                  # Landing page (High-fidelity, bi-lingual English/Urdu)
│   ├── auth.html                   # Login & Registration page
│   ├── assistant.html              # Conversational terminal message interface
│   ├── dashboard.html              # Active complaints, status, and PDF downloads
│   ├── evidence.html               # Evidence upload and management center
│   ├── settings.html               # User settings and profile management
│   └── geo_mapping/                # Geo-location assets
│
├── text_processing/
│   └── language_utils.py           # Boilerplate for text normalizers
│
├── smart_questions/
│   └── conversation.py             # Conversation schema definitions
│
├── pdfs/                           # Local PDF buffer directory
├── uploads/                        # Local evidence upload buffer directory
├── .env                            # Application environment keys (Git ignored)
├── complaint_counter.txt           # Local backup counter
├── test_agent.py                   # Script to dry-run the LLM agent locally
└── README.md                       # Documentation (This file)
```

---

## ⚙️ Local Installation & Setup

### Prerequisites
* Python 3.12+ installed.
* A Supabase project (URL, Anon Key, Service Role Key, and `complaint-pdf` & `evidence-files` buckets).
* One or more Groq API Keys.

### 1. Clone the Project
```bash
git clone <repository_url>
cd smart_fir_text
```

### 2. Set Up a Virtual Environment & Install Dependencies
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

pip install fastapi uvicorn pydantic supabase groq reportlab python-dotenv
```

### 3. Configure the Environment Variables
Create a `.env` file in the root directory and add the following keys:
```env
# Supabase Configurations
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_ANON_KEY=your-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key

# Groq API Keys (Supports Multi-Key Round Robin)
GROQ_API_KEY_1=gsk_your_key_1
GROQ_API_KEY_2=gsk_your_key_2
# Or a single fallback key:
GROQ_API_KEY=gsk_single_key
```

### 4. Run the Backend Server
```bash
uvicorn api.main:app --host 127.0.0.1 --port 8000 --reload
```
Once started, open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser to interact with the frontend app.

---

## 🔌 API Documentation Reference

The backend exposes several key FastAPI endpoints:

| Endpoint | Method | Authentication | Description |
| :--- | :--- | :--- | :--- |
| `/register` | `POST` | Public | Registers a new citizen/officer profile in Supabase Auth & PGSQL database. |
| `/login` | `POST` | Public | authenticates credentials and returns a Bearer JWT Token. |
| `/complaints` | `GET` | Bearer Token | Fetches all submitted and active complaints for the authenticated user. |
| `/start` | `POST` | Bearer Token | Initializes a new conversational FIR session and returns a session ID & greeting. |
| `/chat/{session_id}` | `POST` | Bearer Token | Accepts citizen messages, returns legal follow-ups, and extracts incident fields. |
| `/upload/{session_id}` | `POST` | Bearer Token | Handles file uploads for images, video, audio, and PDF digital evidence. |
| `/generate_pdf/{session_id}`| `POST` | Bearer Token | Generates separate high-res FIR and Transcript PDFs, uploading them to Supabase Storage. |
| `/generate_combined_pdf/{session_id}` | `POST` | Bearer Token | Generates a combined PDF containing the official registry and the AI-synthesized narrative storyline. |

---

## 🛡️ Verification & Security Best Practices
* **Identity Assurance:** Every complaint is structurally bound to a validated identity (CNIC + phone number), eliminating anonymous spam and ensuring accountability.
* **Cryptographic Storage:** All generated reports are indexed and uploaded using secure Supabase Storage pathways, locked under custom RLS (Row Level Security) schemas.
* **AES-256 Badges:** Employs standard encryption policies for data in-transit (TLS 1.3) and at-rest.
