# Company Chatbot API

This API provides an AI-powered chatbot that helps customers interact with the company in a faster and more efficient way.  
It uses **FastAPI** and integrates with **OpenAI** to deliver intelligent responses. The chatbot can also be trained with company-specific data and documents, so answers are more accurate and relevant.  

## Features
- AI-powered chatbot for customer support.  
- Integration with company data for personalized responses.  
- FastAPI for high performance and scalability.  
- Token-based authentication for secure access.  

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/company-chatbot-api.git
Navigate into the project folder:

bash
Copiar
Editar
cd company-chatbot-api
Install dependencies:

bash
Copiar
Editar
pip install -r requirements.txt
Running the API
Start the server with:

bash
Copiar
Editar
uvicorn main:app --reload
The API will be available at: http://127.0.0.1:8000

Endpoints
POST /chat → Send a message to the chatbot and get a response.

POST /train → Train the chatbot with company documents.

POST /token → Generate an authentication token.

GET /users/me → Get the logged-in user info.

Benefits
Improves customer communication.

Reduces response times.

Provides accurate answers by using internal company knowledge.

