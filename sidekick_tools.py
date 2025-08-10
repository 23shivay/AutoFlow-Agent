from playwright.async_api import async_playwright
from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
from dotenv import load_dotenv
import os
import requests
from langchain.agents import Tool
from langchain_community.agent_toolkits import FileManagementToolkit
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_experimental.tools import PythonREPLTool
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type



load_dotenv(override=True)
pushover_token = os.getenv("PUSHOVER_TOKEN")
pushover_user = os.getenv("PUSHOVER_USER")
pushover_url = "https://api.pushover.net/1/messages.json"
serper = GoogleSerperAPIWrapper()

async def playwright_tools():
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=False)
    toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=browser)
    return toolkit.get_tools(), browser, playwright


def push(text: str):
    """Send a push notification to the user
    
    Args:
        text (str): The message to send in the push notification
    """
    requests.post(pushover_url, data = {"token": pushover_token, "user": pushover_user, "message": text})
    return "success"


class PushNotificationInput(BaseModel):
    text: str = Field(description="The message to send in the push notification")


class PushNotificationTool(BaseTool):
    name: str = "send_push_notification"
    description: str = "Use this tool when you want to send a push notification. The input should be the message text to send in the push notification."
    args_schema: Type[BaseModel] = PushNotificationInput

    def _run(self, text: str) -> str:
        requests.post(pushover_url, data = {"token": pushover_token, "user": pushover_user, "message": text})
        return "success"

    async def _arun(self, text: str) -> str:
        # Use the synchronous version to avoid duplicate notifications
        return self._run(text)


class SearchInput(BaseModel):
    query: str = Field(description="The search query to look up information")


class SearchTool(BaseTool):
    name: str = "search"
    description: str = "Use this tool when you want to get the results of an online web search"
    args_schema: Type[BaseModel] = SearchInput

    def _run(self, query: str) -> str:
        return serper.run(query)

    async def _arun(self, query: str) -> str:
        return serper.run(query)

## tools for llm to rom around in directory
def get_file_tools():
    toolkit = FileManagementToolkit(root_dir="sandbox")
    return toolkit.get_tools()


async def other_tools():
    push_tool = PushNotificationTool()
    file_tools = get_file_tools()

    tool_search = SearchTool()

    wikipedia = WikipediaAPIWrapper()
    wiki_tool = WikipediaQueryRun(api_wrapper=wikipedia)

    python_repl = PythonREPLTool()  ## we are gingin llm to run python code  open to world
    
    return file_tools + [push_tool, tool_search, python_repl,  wiki_tool]