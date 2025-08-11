# openai-chat-assignment

Query -> Answer Mini App
======

A simple React + FastAPI app that accepts a query input, sends it to a backend, and displays a stubbed response (mimicking an OpenAI call).

Setup and Run Instructions
--------------------------

### Prerequisites

*   Node.js (v22 or higher)
*   Python (3.11 or higher)
*   npm (included with Node.js)

### Backend Setup

1.  Navigate to the backend folder:
    
        cd backend
        
    
2.  Create and activate a virtual environment:
    
        python -m venv venv
        source venv/bin/activate  # On Windows: venv\Scripts\activate
        
    
3.  Install dependencies:
    
        pip install -r requirements.txt
        
    
4.  create a .env file in the folder. Add the following environment variables:
    -   OPENAI_API_KEY (REQUIRED)
    -   OPENAI_MODEL (OPTIONAL)
    -   BACKEND_URL (REQUIRED) (http://localhost:5173 is the default)
    -   PORT (OPTIONAL) (8000 is the default) 

5.  Run the FastAPI server:
    
        uvicorn main:app --host 0.0.0.0 --port 8000
        
    

### Frontend Setup

1.  Navigate to the frontend folder:
    
        cd frontend
        
    
2.  Install dependencies:
    
        npm install
        
    

3.  Run the development server:
    
        npm run dev
        
    
4.  Open `http://localhost:5173` in your browser.



### Notes

*   The backend is modularized into `models.py` (Pydantic validation), `services.py` (stubbed response logic), and `main.py` (FastAPI routing).
*   The frontend runs on port 5173, backend on 8000, as suggested.
*   The app validates queries (non-empty, <2000 chars), shows a character count, and handles loading/error states.
*   The backend uses a stubbed response, as allowed by the exercise, due to no OpenAI API key.

Assumptions and Trade-offs
--------------------------
