# AI Powered Customer Support Assistant (Local LLM)

A local AI-powered customer support assistant built with **FastAPI + LangChain + Ollama**, running fully offline using Docker.

It provides tool-based customer support (hotels, flights, refunds, complaints, tracking) and returns structured JSON responses for frontend integration.

---

## Features

- Local LLM inference using Ollama (no external APIs)
- Tool-based agent system (hotel search, flight search, refunds, complaints, tracking)
- Structured JSON output for frontend/UI routing
- Thread-based conversation memory
- Fully containerized with Docker & Docker Compose
- Works fully offline after model download

---

## Architecture
User → FastAPI → LangChain Agent → Tools (hotel/flight/refund/etc.)
↓
Ollama LLM (local)
↓
Structured JSON Response
↓
Frontend/UI Layer

---

## Prerequisites

- Docker
- Docker Compose (included with Docker Desktop)
- 8GB+ RAM recommended (16GB ideal for smoother Llama 3.1 performance)

---

### Setting up environment variable
- cp .env.copy .env

---

### Starting the app
- Build the image
    - `docker build -t ai_powered_customer_support_assistant:latest -f app/Dockerfile app`
- Start the app
    - `docker compose up -d`
- Stop the app
    - `docker compose stop`

---

### Pulling the Ollama model you want to use
- Run in the ollama-1 container (you can use whatever your machine can handle)
    - `docker exec ollama-1 ollama pull llama3.1:latest`
    - You can also use:
        - llama3.2
        - mistral
        - qwen2.5

---

### Calling the API
- User Curl or Postman
    - **Endpoint:** POST `http://localhost:8000/chat`
    - **Sample payload:**
        ``` json 
        {
            "message": "hotels in Dubai",
            "thread_id: "user-1"
        } 
        {
            "message": "I want to refund order 1234",
            "thread_id": "user-1"
        }
    - **Sample response:**
        ``` json 
        {
            "intent": "hotel_search",
            "tool_called": "hotel_search",
            "ui_type": "hotel_search_page",
            "message": "Here are available hotels in Dubai",
            "data": {
                "hotels": [
                    {
                        "name": "Marina View Hotel",
                        "price": "AED 120"
                    }
                ]
            }
        }
