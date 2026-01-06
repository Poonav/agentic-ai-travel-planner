- Agentic AI Travel Planner

An agentic AI-based travel planning assistant built using LangChain tools and Streamlit.
It autonomously generates trip itineraries by recommending flights, hotels, places to visit, weather info, and budgeting based on user input.

- Features

Flight Search: Finds the cheapest flight between two cities.

Hotel Recommendation: Suggests hotels based on city and budget.

Places Discovery: Recommends attractions based on user interests.

Weather Lookup: Provides weather forecasts for travel dates.

Budget Estimation: Calculates trip cost combining flight, hotel, and local expenses.

Interactive UI: Collects user preferences through a Streamlit interface.

- Skills & Technologies

Programming Languages: Python

Frameworks & Libraries: LangChain, Streamlit

Data Handling: JSON

Agentic AI Concepts: Multi-step reasoning, tool orchestration

Domain: Travel

- Project Structure
travel_agent/
│
├── app.py                # Streamlit UI
├── agent.py              # Core agent logic calling tools
├── tools/                # LangChain tools
│   ├── flight_tool.py
│   ├── hotel_tool.py
│   ├── places_tool.py
│   ├── weather_tool.py
│   └── budget_tool.py
├── data/                 # JSON datasets
│   ├── flights.json
│   ├── hotels.json
│   └── places.json
├── venv/                 # Python virtual environment
└── requirements.txt      # Dependencies

- Installation

Clone the repository:

git clone https://github.com/yourusername/agentic-ai-travel-planner.git
cd agentic-ai-travel-planner


Create a virtual environment:

python -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate        # Windows


Install dependencies:

pip install -r requirements.txt

- Running Locally

Start the Streamlit app:

streamlit run app.py


Open your browser at http://localhost:8501 to interact with the travel planner.

- Usage

Enter Source and Destination cities.

Select Trip Duration in days.

Enter Budget.

Choose your Interests (Nature, Adventure, Food, etc.).

Click Generate Itinerary.

The app will output a structured itinerary including:

Recommended flight

Hotel options

Places to visit

Weather forecast

Estimated budget

- Business Use Cases

Travel agencies can automate itinerary creation.

Users save time comparing flights, hotels, and attractions.

AI-driven planning improves personalization and cost-efficiency.

⚙ Notes

All tools are LangChain-based, but this version does not require an LLM.

JSON datasets (flights.json, hotels.json, places.json) provide sample data.

Weather information is generated via a free API (Open-Meteo).

- License

This project is open-source and free to use for learning and personal projects.
