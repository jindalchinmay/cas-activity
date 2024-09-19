from crewai import Agent
from langchain.llms import OpenAI

from tools.browser_tools import BrowserTools
# from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools


class EssayAgents():
  
  def web_researcher_agent(self):
    return Agent(
        role='Essay Topic Researcher',
        goal='Given a detailed topic and subject to write the essay for, research and provide the most relevant, deep, insightful information',
        # Provide the latest news about a given startup with a user query',
        backstory='An expert researcher with a keen eye for gathering insightful information based on subjects and topics',
        tools=[
            SearchTools.search_internet, 
            BrowserTools.scrape_and_summarize_website,
            ],
        verbose=True
    )
  
  def writer_agent(self):
    return Agent(
        role='Essay Writer',
        goal='Given researched information, subject and topic to write on, write a well-structured, insightful essay. Make the tone depending on the subject, eg. if it is english then formal and deep thoughtful ideas. if it is for a volunteer reflection, then a little bit more information. ETC',
        # Provide the latest news about a given startup with a user query',
        backstory='An expert writer with years of expierence in writing essays and articles of all sorts of different subjects and topics',
        # researcher with a keen eye for gathering insightful information based on client prompts',
        tools=[
            SearchTools.search_internet, 
            BrowserTools.scrape_and_summarize_website,
            ],
        verbose=True
    )

#   def city_selection_agent(self):
#     return Agent(
#         role='City Selection Expert',
#         goal='Select the best city based on weather, season, and prices',
#         backstory=
#         'An expert in analyzing travel data to pick ideal destinations',
#         tools=[
#             SearchTools.search_internet,
#             BrowserTools.scrape_and_summarize_website,
#         ],
#         verbose=True)

#   def local_expert(self):
#     return Agent(
#         role='Local Expert at this city',
#         goal='Provide the BEST insights about the selected city',
#         backstory="""A knowledgeable local guide with extensive information
#         about the city, it's attractions and customs""",
#         tools=[
#             SearchTools.search_internet,
#             BrowserTools.scrape_and_summarize_website,
#         ],
#         verbose=True)

#   def travel_concierge(self):
#     return Agent(
#         role='Amazing Travel Concierge',
#         goal="""Create the most amazing travel itineraries with budget and 
#         packing suggestions for the city""",
#         backstory="""Specialist in travel planning and logistics with 
#         decades of experience""",
#         tools=[
#             SearchTools.search_internet,
#             BrowserTools.scrape_and_summarize_website,
#             CalculatorTools.calculate,
#         ],
#         verbose=True)