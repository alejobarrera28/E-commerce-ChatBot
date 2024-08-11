from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE_PATH = os.path.join(BASE_DIR, '../data/ecommerce_data.xlsx')

def load_data():
    return pd.read_excel(CSV_FILE_PATH, header=0)

def process_input(input_text):
    data = load_data()
    itemsList = data.to_dict(orient='records')

    chat = ChatGroq(temperature=0.3, groq_api_key="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", model_name="llama3-8b-8192")

    human_prompt = input_text+": {items}"
    system_prompt = "You are a helpful eCommerce assistant and your task is to listen to the query carefully and provide analytical answer"
    prompt = ChatPromptTemplate.from_messages([("system", system_prompt), ("human", human_prompt)])

    chain = prompt | chat
    return chain.invoke({"items": itemsList}).content