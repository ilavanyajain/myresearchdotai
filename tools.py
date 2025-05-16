
from dotenv import load_dotenv
load_dotenv() 
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper, SerpAPIWrapper
from langchain.tools import Tool
from datetime import datetime
import os

serpapi_wrapper = SerpAPIWrapper(search_engine="google_scholar", serpapi_api_key=os.getenv("SERPAPI_API_KEY"))
google_scholar_tool = Tool(
    name="google_scholar",
    func=serpapi_wrapper.run,
    description="Use this to search for academic papers, theses, and scholarly articles from Google Scholar."
)

def save_to_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"
    
    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
        
    return f"Data successfully saved to {filename}"

save_tool = Tool(
    name="save_text_to_file", 
    func=save_to_txt,
    description="Saves structured research data to a text file.",
)

search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    func=search.run,
    description="Search the web for information"
)


api_wrapper = WikipediaAPIWrapper(top_k_results=7, doc_content_chars_max=1000)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)