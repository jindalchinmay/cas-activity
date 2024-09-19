from crewai import Crew
from textwrap import dedent
from essay_agents import EssayAgents
from essay_tasks import EssayTasks

from dotenv import load_dotenv
load_dotenv()

class TripCrew:

  def __init__(self, subject, topic, tone, additional_info):
    self.subject = subject
    self.topic = topic
    self.tone = tone
    self.additional_info = additional_info

  def run(self):
    agents = EssayAgents()
    tasks = EssayTasks()

    researcher_agent = agents.web_researcher_agent()
    writer_agent = agents.writer_agent()
    # travel_concierge_agent = agents.travel_concierge()

    # identify_task = tasks.identify_task(
    #   city_selector_agent,
    #   self.origin,
    #   self.cities,
    #   self.interests,
    #   self.date_range
    # )
    gather_task = tasks.gather_task(
      researcher_agent,
      self.subject,
      self.topic,
      self.tone, 
      self.additional_info
    )
    write_task = tasks.write_task(
      writer_agent, 
      self.subject,
      self.topic,
      self.tone, 
      self.additional_info
    )

    crew = Crew(
      agents=[
        researcher_agent, writer_agent
      ],
      tasks=[gather_task, write_task],
      verbose=True
    )

    result = crew.kickoff()
    return result

if __name__ == "__main__":
  print("## Welcome to Essay Writer Crew")
  print('-------------------------------')
  subject = input(
    dedent("""
      What school subject is this essay for: 
    """))
  topic = input(
    dedent("""
      Topic to write about: 
    """))
  tone = input(
    dedent("""
      Tone you want for the essay: 
    """))
  additional_info = input( 
    dedent("""
      Additional requests (word count, specific points to include, more format, etc): 
    """))
  
  trip_crew = TripCrew(subject, topic, tone, additional_info)
  result = trip_crew.run()
  # print("\n\n########################")
  print("## Here is your Essay")
  print("########################\n")
  print(result)
  print("\n\n########################")
  print("Essay saved to results.txt")
  with open('results.txt', 'w') as f:
    f.write(str(result))