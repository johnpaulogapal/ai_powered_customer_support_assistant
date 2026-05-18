# AI Powered Customer Support Assistant Prototype
Local AI-powered customer support assistant using Python (FastAPI), Ollama (local LLM)

### Prerequisites
- Install Docker & Docker Compose

### Setting up environment variable
- remove `.copy` in .env.copy and fill the variable appropriately

### Starting the app
- Build the image
    - `docker build -t ai_powered_customer_support_assistant:latest -f app/Dockerfile app`
- Start the app
    - `docker compose up -d`
- Stop the app
    - `docker compose stop`

### Pulling the Ollama model you want to use
- Run in the ollama-1 container (you can use whatever your machine can handle)
    - `docker exec ollama-1 ollama pull llama3.1:latest`

### Calling the API
- User Curl or Postman
    - `http://localhost:8000/chat`
    - Sample payload
        - {
            "message": "hotels in Dubai",
            "thread_id: "user-1"
        }
