# 🧳 Trip Planner AI

An intelligent, Streamlit-based travel planning app powered by [CrewAI](https://github.com/joaomdmoura/crewai) and OpenAI. This tool builds customized travel itineraries based on your origin, interests, destination, and date range using a team of collaborative AI agents.

---

## ✨ Features

- 🗺️ **Smart City Selection** – Chooses the ideal travel destination considering weather, season, and cost
- 🧠 **Local Insights Agent** – Shares hidden gems, practical tips, and must-see landmarks
- 🧳 **Itinerary Planner** – Generates full day-by-day travel plans with restaurants, hotels, transport, and packing suggestions
- 💬 **Natural Language Date Parsing** – Understands date ranges like “July 4 to July 5” or “next weekend”
- 💸 **Budget Breakdown** – Estimates flight, stay, activity, food, and transport costs


```bash
# 1. Clone the repository
git clone git@github.com:jaindeepali010/trip-planner-ai.git
cd trip-planner-ai

# 2. (Optional) Create and activate a virtual environment
python3 -m venv crewenv
source crewenv/bin/activate

# 3. Install all dependencies
pip install -r requirements.txt

# 4. Create a .env file for API keys
echo "OPENAI_API_KEY=your-openai-api-key-here" > .env

# 5. Run the app
streamlit run trip_planner_app.py

---

## 📁  Project Structure

trip_planner/
├── tools/                  # Custom tools (browser, search, calculator)
├── trip_agents.py          # CrewAI agent definitions
├── trip_tasks.py           # Task logic for each agent
├── trip_planner_app.py     # Streamlit frontend
├── main.py                 # Optional CLI entry point
├── requirements.txt        # Python dependencies
├── .gitignore
└── README.md
