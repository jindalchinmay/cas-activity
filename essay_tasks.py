from crewai import Task
from textwrap import dedent
from datetime import date

class EssayTasks:

    def gather_task(self, agent, subject, topic, tone, additional_info):
        return Task(
            description=dedent(f"""
                               
                Analyze and select the best links and their information for researching the given topic and subject. 
                This task involves comparing different sources, considering factors like credibility, relevance, and depth of information.
                Your final answer must be a detailed report on the chosen links, and everything you found out about them, including the actual information and sources.
                Make sure that the information you return is deep and insightful, and RELEVANT to the topic, and subject at hand. Also, its relevant to the tone. Make it deep and insightful. 
                You also need to return a list of the sources you used to gather the information at the end of your report. You need to cite atleast 10 sources, but can use more for the actual research. 
                You will be passing this off to a writer agent, so make sure to provide the best information possible. It will be using intext citations, so you need to make sure it knows where each information is from. 

                Subject: {subject}
                topic to write about: {topic}
                intended tone: {tone}
                additional requests and information by author: {additional_info}
            """),
            agent=agent,
            expected_output="DETAILED report on the chosen links (minimum 10), including information and sources relevant to the subject, topic, and tone, alonside a list of sources used"
            # Detailed report on the chosen city including flight costs, weather forecast, and attractions"
        )

    def write_task(self, agent, subject, topic, tone, additional_info):
        return Task(
            description=dedent(f"""
                               
                Write a well-structured, insightful essay based on the information provided by the researcher agent.
                This task involves creating a coherent narrative, integrating the information from the sources, and presenting it in a clear and engaging manner.
                You need to keep in mind of the following:
                - The subject of the essay
                - The topic you are writing about (make a title for this as well)
                - The intended tone of the essay (if its formal, you need paragraphs, more fornal arguements, etc)
                - Any additional requests or information by the author (word count, specific points to include, more format, etc)
                               
                You also need to take the list of sources and provide an MLA-9 citation for each source used in the essay in the end. You also need to provide intext citations for each source used in the essay.
                Be deep, thoughtful, meaningful, and insightful in your essay. Make sure to provide the best information possible.
                Write based on the tone and as much as an human expert as possible. 
                If no word count, make sure to write atleast 300 words.
                
                {self.__tip_section()}

                Subject: {subject}
                topic to write about: {topic}
                intended tone: {tone}
                additional requests and information by author: {additional_info}
            """),
            agent=agent,
            expected_output="Comprehensive essay with a clear narrative, integrating information from sources, and engaging presentation based on the tone. MLA-9 citations for each source used in the essay, and intext citations for each source used. Return markdown"
            # Comprehensive city guide including hidden gems, cultural hotspots, and practical travel tips"
        )

    # def plan_task(self, agent, origin, interests, range):
    #     return Task(
    #         description=dedent(f"""
    #             Expand this guide into a full 7-day travel 
    #             itinerary with detailed per-day plans, including 
    #             weather forecasts, places to eat, packing suggestions, 
    #             and a budget breakdown.
                
    #             You MUST suggest actual places to visit, actual hotels 
    #             to stay and actual restaurants to go to.
                
    #             This itinerary should cover all aspects of the trip, 
    #             from arrival to departure, integrating the city guide
    #             information with practical travel logistics.
                
    #             Your final answer MUST be a complete expanded travel plan,
    #             formatted as markdown, encompassing a daily schedule,
    #             anticipated weather conditions, recommended clothing and
    #             items to pack, and a detailed budget, ensuring THE BEST
    #             TRIP EVER. Be specific and give it a reason why you picked
    #             each place, what makes them special! {self.__tip_section()}

    #             Trip Date: {range}
    #             Traveling from: {origin}
    #             Traveler Interests: {interests}
    #         """),
    #         agent=agent,
    #         expected_output="Complete expanded travel plan with daily schedule, weather conditions, packing suggestions, and budget breakdown"
    #     )

    def __tip_section(self):
        return "If you do your BEST WORK, I'll tip you $100 and a promotion!"