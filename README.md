# TrustCare AI 🤖

## Intelligent Customer Support and Human Escalation System

TrustCare AI is an intelligent customer-support system designed to improve customer service by analyzing customer frustration, searching a support knowledge base, generating appropriate responses, calculating a trust score, and automatically escalating high-risk conversations to human support.

The system combines a web-based customer chatbot, a Python Flask backend, intelligent support agents, and a human-support dashboard into a single customer-support platform.

---

## 🚀 Features

* 🤖 Customer-support chatbot
* 😊 Customer frustration detection
* 📚 Knowledge-base search
* 🧠 Intelligent response generation
* 🤝 Customer trust scoring
* 🚨 Automatic human-support escalation
* 👨‍💼 Human-support dashboard
* 📊 Customer analysis
* 📝 Escalation history
* ✅ Case resolution
* 🔗 Frontend and backend integration
* 🌐 REST API communication

---

## 🎯 Project Objectives

The main objectives of TrustCare AI are to:

* Understand customer messages automatically.
* Detect customer frustration.
* Identify the category of the customer's problem.
* Search a support knowledge base for relevant information.
* Generate an appropriate customer-support response.
* Evaluate whether the AI can reliably handle the request.
* Automatically escalate high-risk conversations.
* Allow human support representatives to manage escalated cases.
* Track and resolve customer-support cases.

---

## 🏗️ System Architecture

```text
                    Customer
                       │
                       ▼
              ┌─────────────────┐
              │ Customer Chatbot│
              └────────┬────────┘
                       │
                       │ HTTP Request
                       ▼
              ┌─────────────────┐
              │  Flask Backend  │
              └────────┬────────┘
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
   ┌────────────┐ ┌───────────┐ ┌────────────┐
   │ Frustration│ │ Knowledge │ │   Trust    │
   │   Agent    │ │   Agent   │ │   Agent    │
   └──────┬─────┘ └─────┬─────┘ └─────┬──────┘
          │             │             │
          └─────────────┼─────────────┘
                        │
                        ▼
               ┌─────────────────┐
               │ Resolution Agent│
               └────────┬────────┘
                        │
               ┌────────┴────────┐
               │                 │
               ▼                 ▼
        ┌─────────────┐   ┌─────────────┐
        │ AI Response │   │ Escalation  │
        └─────────────┘   └──────┬──────┘
                                 │
                                 ▼
                        ┌─────────────────┐
                        │ Support         │
                        │ Dashboard       │
                        └────────┬────────┘
                                 │
                                 ▼
                            Resolve Case
```

---

## 🧩 How the System Works

When a customer sends a message, the system follows this workflow:

```text
Customer Message
       ↓
Frustration Analysis
       ↓
Knowledge Search
       ↓
Trust Evaluation
       ↓
Response Generation
       ↓
     Decision
    /        \
   /          \
AI Response   Human Escalation
                 ↓
          Support Dashboard
                 ↓
             Resolution
```

---

## 🤖 Intelligent Agents

### Frustration Agent

The Frustration Agent analyzes the customer's message and detects indicators of frustration.

It can identify:

* Anger
* Disappointment
* Delays
* Waiting
* Repeated support problems
* Strong punctuation

It produces:

* Frustration score
* Frustration level
* Reasons for detected frustration

Example:

```text
Customer:
I am furious! This is unacceptable! Nobody is helping me!

Frustration Score: 75
Frustration Level: HIGH
```

---

### Knowledge Agent

The Knowledge Agent searches the customer-support knowledge base to find relevant information.

The knowledge base contains support information for topics such as:

* Delivery
* Orders
* Returns
* Refunds
* Payments
* Customer-support issues

Example:

```text
Customer:
My order is late.

Category:
delivery

Knowledge Confidence:
100

Answer:
Standard delivery normally takes 5 to 7 business days.
```

---

### Trust Agent

The Trust Agent evaluates whether the AI should continue handling the customer's request.

It considers factors such as:

* Customer frustration
* Knowledge confidence
* Ability of the system to provide a reliable answer

Example:

```text
Trust Score: 100
Trust Level: HIGH
Escalation Required: FALSE
```

For a high-risk conversation:

```text
Trust Score: 0
Trust Level: LOW
Escalation Required: TRUE
```

---

### Resolution Agent

The Resolution Agent generates the final customer-support response.

It uses:

* Customer message
* Frustration analysis
* Knowledge-base result

Example:

```text
Customer:
My order is late.

TrustCare AI:
Standard delivery normally takes 5 to 7 business days.
Please let me know if you need any further assistance.
```

---

## 🚨 Human Escalation

TrustCare AI does not attempt to handle every conversation automatically.

When the system detects a high level of customer frustration combined with low AI confidence, it recommends human support.

Example:

```text
Customer:
I am furious! This is unacceptable! Nobody is helping me!
```

The system can produce:

```text
Frustration Level: HIGH
Trust Level: LOW
Escalation Required: TRUE
```

The customer then receives:

```text
🚨 Human Support Recommended

A human support representative should assist with this conversation.
```

---

## 👨‍💼 Support Dashboard

The human-support dashboard allows support representatives to monitor escalated conversations.

The dashboard can display:

* Customer message
* Frustration score
* Frustration level
* Trust score
* Trust level
* Knowledge confidence
* Category
* Escalation reason
* Case status
* Resolution time

Support representatives can resolve an escalated case.

```text
OPEN
  ↓
Resolve Case
  ↓
RESOLVED
```

---

## 📁 Project Structure

```text
TrustCare AI/
│
├── backend/
│   │
│   ├── app.py
│   │
│   ├── agents/
│   │   ├── frustration_agent.py
│   │   ├── knowledge_agent.py
│   │   ├── resolution_agent.py
│   │   └── trust_agent.py
│   │
│   ├── data/
│   │   ├── knowledge_base.json
│   │   └── escalations.json
│   │
│   └── test_resolution.py
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   ├── style.css
│   └── dashboard.html
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🛠️ Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript
* Fetch API

### Backend

* Python
* Flask
* Flask-CORS
* JSON

### Development

* Visual Studio Code
* PowerShell
* Git
* GitHub

---

## 💻 Installation

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

Navigate into the project:

```bash
cd "TrustCare AI"
```

---

### 2. Create a Virtual Environment

Windows:

```powershell
python -m venv .venv
```

---

### 3. Activate the Virtual Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

---

### 4. Install Dependencies

```powershell
pip install -r requirements.txt
```

---

## ▶️ Running the Application

The application requires two local servers.

### Start the Flask Backend

Open the first terminal:

```powershell
python backend\app.py
```

The backend should start at:

```text
http://127.0.0.1:5000
```

You should see:

```text
* Running on http://127.0.0.1:5000
```

---

### Start the Frontend

Open a second terminal:

```powershell
python -m http.server 5500 --directory frontend
```

The frontend will be available at:

```text
http://127.0.0.1:5500/
```

---

## 🌐 Application URLs

### Customer Chatbot

```text
http://127.0.0.1:5500/
```

or:

```text
http://127.0.0.1:5500/index.html
```

### Human Support Dashboard

```text
http://127.0.0.1:5500/dashboard.html
```

### Flask Backend

```text
http://127.0.0.1:5000/
```

Expected response:

```text
TrustCare AI Backend is running!
```

---

## 🔌 API Endpoints

### Health Check

```http
GET /
```

Checks whether the Flask backend is running.

---

### Customer Chat

```http
POST /chat
```

Example request:

```json
{
    "message": "My order is late"
}
```

Example response:

```json
{
    "response": "Standard delivery normally takes 5 to 7 business days.",
    "frustration": {},
    "knowledge": {},
    "trust": {}
}
```

---

### Get Escalations

```http
GET /escalations
```

Returns stored customer escalations.

---

### Resolve Escalation

```http
PUT /escalations/<id>/resolve
```

Updates the selected escalation and marks it as:

```text
RESOLVED
```

---

## 🧪 Testing

### Test 1 — Normal Request

Input:

```text
Where is my order?
```

Expected behavior:

```text
Low frustration
AI handles the request
```

---

### Test 2 — Frustrated Customer

Input:

```text
My order is late and I am very disappointed!
```

Expected behavior:

```text
Frustration Score: 35
Frustration Level: MEDIUM
Category: delivery
Knowledge Confidence: HIGH
Trust Level: HIGH
```

The AI should provide a delivery-related response.

---

### Test 3 — High-Risk Customer

Input:

```text
I am furious! This is unacceptable! Nobody is helping me!
```

Expected behavior:

```text
Frustration Level: HIGH
Trust Level: LOW
Escalation Required: TRUE
```

The system should display:

```text
🚨 Human Support Recommended
```

The case should also appear on the support dashboard.

---

### Test 4 — Resolve a Case

1. Open the support dashboard.
2. Find the escalated case.
3. Click **Resolve Case**.
4. Confirm the action.
5. Verify that the status changes from:

```text
OPEN
```

to:

```text
RESOLVED
```

---

## 🧪 Backend Testing

Run:

```powershell
python backend\test_resolution.py
```

The test checks the customer-support processing flow, including:

* Customer message
* Frustration analysis
* Knowledge-base result
* AI response

---

## 📊 Example Customer Analysis

For a message such as:

```text
My order is late and I am very disappointed!
```

The system can produce:

```text
Customer Analysis

Frustration Score: 35
Frustration Level: MEDIUM

Trust Score: 100
Trust Level: HIGH

Category: delivery
Knowledge Confidence: 100
```

The AI then generates an appropriate response based on the knowledge base.

---

## 🚨 Example Escalation

For:

```text
I am furious! This is unacceptable! Nobody is helping me!
```

The system can detect:

```text
Frustration Score: 75
Frustration Level: HIGH

Trust Score: 0
Trust Level: LOW
```

The system recommends human intervention and stores the escalation for the support team.

---

## 🔐 Security Considerations

This project is currently designed for local development, education, and demonstration.

For production deployment, additional security should be implemented, including:

* User authentication
* Role-based access control
* HTTPS
* Secure API configuration
* Input validation
* Secure secret management
* Database security
* Production WSGI server
* Protection of customer information

Do not commit passwords, API keys, secrets, or real customer information to GitHub.

---

## 🚫 Files Not Committed to GitHub

The Python virtual environment should not be uploaded.

The `.gitignore` file should include:

```text
.venv/
__pycache__/
*.pyc
.vscode/
.env
```

---

## 🔮 Future Enhancements

Possible future improvements include:

* Real AI/LLM integration
* Advanced sentiment analysis
* Improved intent classification
* PostgreSQL or MySQL database
* User authentication
* Support-agent login
* Role-based access control
* Email notifications
* Real-time dashboard updates
* Customer ticket management
* Analytics and reporting
* Multi-language support
* Cloud deployment
* Conversation history stored in a database
* Automatic ticket assignment

---

## 🎓 Project Impact

TrustCare AI demonstrates how automated customer support can be combined with intelligent risk evaluation and human intervention.

Instead of automatically answering every customer message, the system evaluates the conversation and determines whether:

```text
AI can safely handle the request
```

or:

```text
Human support should intervene
```

This approach can help improve customer experience while reducing the risk of inappropriate automated responses in highly frustrated situations.

---

## 👥 Team

TrustCare AI is developed collaboratively as a team project.

The project combines:

* Frontend development
* Backend development
* AI agent development
* Knowledge retrieval
* Trust evaluation
* Customer-support automation
* Human escalation
* Dashboard development

---

## 📌 Conclusion

TrustCare AI provides an end-to-end customer-support workflow:

```text
Customer
   ↓
Chatbot
   ↓
Flask API
   ↓
Frustration Analysis
   ↓
Knowledge Search
   ↓
Trust Evaluation
   ↓
Response Generation
   ↓
┌─────────────────────┐
│                     │
▼                     ▼
AI Response       Human Escalation
                      │
                      ▼
              Support Dashboard
                      │
                      ▼
                   RESOLVED
```

The project demonstrates how a customer-support application can combine automation, intelligent analysis, and human intervention in a single platform.

---

## 📄 License

This project is developed for educational, academic, and demonstration purposes.
