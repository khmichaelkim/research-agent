from dotenv import load_dotenv
import os
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
langchain_api_key = os.getenv('LANGSCHAIN_API_KEY')
from langchain_openai import ChatOpenAI, OpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
import requests
from bs4 import BeautifulSoup
from langchain.schema.runnable import RunnablePassthrough

# Template for summarization
SUMMARY_TEMPLATE = """{text}

------------

Using the above text, answer in short the following question:

> {question}

------------
If the question cannot be answered using the text, simply summarize the text"""

SUMMARY_PROMPT = ChatPromptTemplate.from_template(SUMMARY_TEMPLATE)

def scrape_text(url: str):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            page_text = soup.get_text(separator=" ", strip=True)
            return page_text
        else:
            return f"Failed to retrieve the webpage: Status code {response.status_code}"
    except Exception as e:
        print(e)
        return f"Failed to retrieve the webpage: {e}"

url = "https://blog.langchain.dev/announcing-langsmith/"


chat_openai = ChatOpenAI(model="gpt-3.5-turbo-0125", openai_api_key=openai_api_key)

chain = RunnablePassthrough.assign(
    text=lambda x: scrape_text(x["url"])[:10000]
) | SUMMARY_PROMPT | chat_openai | StrOutputParser()

print("Chain created successfully")

# Invoke the chain and print the result
try:
    result = chain.invoke(
        {
            "question": "What is LangSmith?",
            "url": url
        }
    )
    print(f"Output: {result}")
except Exception as e:
    print(f"Error invoking chain: {e}")
