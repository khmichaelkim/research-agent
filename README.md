## Research Agent

### Description
Agent built using LangChain's Runnable interfaces and FastAPI. The agent can perform web searches, scrape content, summarize information, and generate detailed reports based on user queries. Defaults to OpenAI's GPT-3.5-turbo model and DuckDuckGo's search API to provide a comprehensive research experience.

### Tech Stack
__Python__: Core programming language used for scripting and backend logic. \
__LangChain/LangSmith/LangServe__: Framework and tools for developing applications powered by language models and serving APIs. \
__OpenAI__: Provider of the GPT-3.5-turbo model used for generating natural language responses. \
__DuckDuckGo Search API__: API for performing web searches and retrieving search results. \
__BeautifulSoup__: Library for parsing HTML and XML documents to extract data. \
__Uvicorn__: Lightning-fast server implementation, used to serve the FastAPI application.

### How To Use
1. Clone the repo
2. Set up the virtual environment `python -m venv venv` `source venv/bin/activate`
3. Install dependencies `pip install -r requirements.txt`
4. Set environment variables in an .env file (e.g., OPENAI_API_KEY, LANGCHAIN_API_KEY)
5. Run the application
6. Interact with locally hosted agent `https://localhost:8000/research-agent/playground`