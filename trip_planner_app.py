import streamlit as st
from trip_agents import TripAgents
from trip_tasks import TripTasks
from crewai import Crew
from textwrap import dedent
import nltk
from dotenv import load_dotenv
import os

nltk.download('punkt_tab')  # Fixed 'punkt_tab' to 'punkt'
load_dotenv('/Users/deepalijain/Documents/CrewAI_Experiments/crew_ai_project/.env')

class TripCrew:
    def __init__(self, origin, cities, date_range, interests):
        self.cities = cities
        self.origin = origin
        self.interests = interests
        self.date_range = date_range

    def run(self):
        agents = TripAgents()
        tasks = TripTasks()

        city_selector_agent = agents.city_selection_agent()
        local_expert_agent = agents.local_expert()
        travel_concierge_agent = agents.travel_concierge()

        identify_task = tasks.identify_task(
            city_selector_agent,
            self.origin,
            self.cities,
            self.interests,
            self.date_range
        )
        gather_task = tasks.gather_task(
            local_expert_agent,
            self.origin,
            self.interests,
            self.date_range
        )
        plan_task = tasks.plan_task(
            travel_concierge_agent, 
            self.origin,
            self.interests,
            self.date_range
        )

        crew = Crew(
            agents=[
                city_selector_agent, local_expert_agent, travel_concierge_agent
            ],
            tasks=[identify_task, gather_task, plan_task],
            returning_task=plan_task, 
            verbose=True
        )

        result = crew.kickoff()
        return result or "Sorry, no itinerary was generated."


def main():
    st.set_page_config(page_title="Trip Planner", layout="centered")
    st.title("🌍 Trip Planner")
    st.markdown("Plan your perfect adventure with AI-powered agents.")

    with st.form("trip_form"):
        location = st.text_input("🌐 Where are you traveling from?")
        cities = st.text_area("🏙️ What cities or countries are you considering?")
        date_range = st.text_input("📅 What is your date range for travel?")
        interests = st.text_area("🎯 What are your high-level interests or hobbies?")
        submitted = st.form_submit_button("Generate Trip Plan")

    if submitted:
        if not all([location, cities, date_range, interests]):
            st.warning("Please fill out all fields before submitting.")
        else:
            with st.spinner("✨ Please wait while we generate your personalized trip..."):
                trip_crew = TripCrew(location, cities, date_range, interests)
                result = trip_crew.run()
            trip_text = (
                getattr(result, "raw", None)
                or getattr(result, "output", None)
                or str(result)
            )
            trip_text = trip_text.replace("```undefined", "```").strip()
            st.success("Here's your trip plan!")
            st.markdown("----")
            if trip_text and trip_text.lower() != "undefined":
                st.markdown(trip_text, unsafe_allow_html=False)
            else:
                st.error("Oops! It looks like the trip plan couldn't be generated.")

if __name__ == "__main__":
    main()
