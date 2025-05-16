# # app.py
# from fastapi import FastAPI
# from pydantic import BaseModel
# from dotenv import load_dotenv
# import os

# load_dotenv()  # ensures environment variables are loaded

# # Import your AI agent and tools (adjust import paths if needed)
# from main import agent_executor, parser

# app = FastAPI()

# class QueryModel(BaseModel):
#     query: str

# @app.post("/ask")
# async def ask_agent(data: QueryModel):
#     """
#     Endpoint to ask our AI agent a question.
#     """
#     try:
#         # Pass user query to agent
#         raw_response = agent_executor.invoke({"query": data.query})
#         # Parse the AI response with your Pydantic parser
#         structured_response = parser.parse(raw_response.get("output")[0]["text"])
#         return {"result": structured_response.dict()}
#     except Exception as e:
#         return {"error": str(e)}
    
    
# # @app.post("/get")
# # async def 