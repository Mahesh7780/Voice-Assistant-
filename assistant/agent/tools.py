from langchain.tools import Tool
from langchain_community.tools import DuckDuckGoSearchRun

search = Tool(
    name="DuckDuckGo Search",
    func=DuckDuckGoSearchRun().run,
    description="Useful for answering general search queries"
)
