import json
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv


load_dotenv('.env')
llm=ChatGroq(model="llama-3.3-70b-versatile",temperature=0.7)

# JSON Input
trip_request = {
    "traveler_name": "Sangeetha",
    "starting_location": "Chennai",
    "trip_duration_days": 45,
    "budget_usd": 8000,
    "travel_style": "Adventure and Cultural Exploration",
    "preferred_continents": [
        "Asia",
        "Europe",
        "North America"
    ],
    "accommodation_preference": "3-4 Star Hotels",
    "food_preferences": [
        "Vegetarian"
    ],
    "must_visit_places": [
        "Tokyo",
        "Paris",
        "New York"
    ]
}


prompt = ChatPromptTemplate.from_template("""
You are an expert world travel planner.

Create a complete world trip itinerary based on the following JSON input.

Input:
{trip_details}

Requirements:
1. Optimize route and travel costs.
2. Recommend hotels.
3. Recommend attractions.
4. Estimate expenses.
5. Include visa considerations.
6. Generate day-by-day itinerary.
7. Return output in valid JSON format.

Output JSON Structure:
{{
  "summary": "",
  "total_estimated_cost": "",
  "destinations": [],
  "daily_itinerary": [],
  "travel_tips": [],
  "visa_requirements": [],
  "packing_recommendations": []
}}
""")


chain = prompt | llm


response = chain.invoke({
    "trip_details": json.dumps(trip_request, indent=2) #json.dumps() converts a Python dictionary into a JSON string.
})

print(response.content)
#tools additon----
#detaile quality response provided ny LLM..
Based on the provided JSON input, I've created a comprehensive world trip itinerary for Sangeetha. Here's the output in valid JSON format:

```json
{
  "summary": "45-day adventure and cultural exploration trip across Asia, Europe, and North America, covering Tokyo, Paris, New York, and other exciting destinations.",
  "total_estimated_cost": "7745 USD",
  "destinations": [
    {
      "location": "Tokyo, Japan",
      "duration": 5,
      "hotel": "Hotel Gajoen Tokyo (3-star)",
      "attractions": ["Shibuya Crossing", "Meiji Shrine", "Tsukiji Fish Market"]
    },
    {
      "location": "Seoul, South Korea",
      "duration": 4,
      "hotel": "Hotel PJ Myeongdong (3-star)",
      "attractions": ["Gyeongbokgung Palace", "Bukchon Hanok Village", "Myeong-dong Shopping District"]
    },
    {
      "location": "Paris, France",
      "duration": 7,
      "hotel": "Hotel Eiffel Seine (3-star)",
      "attractions": ["Eiffel Tower", "Louvre Museum", "Notre-Dame Cathedral"]
    },
    {
      "location": "New York City, USA",
      "duration": 8,
      "hotel": "Hotel Edison (3-star)",
      "attractions": ["Statue of Liberty", "Central Park", "Metropolitan Museum of Art"]
    },
    {
      "location": "San Francisco, USA",
      "duration": 5,
      "hotel": "Hotel Zeppelin (3-star)",
      "attractions": ["Golden Gate Bridge", "Alcatraz Island", "Fisherman's Wharf"]
    },
    {
      "location": "Vancouver, Canada",
      "duration": 4,
      "hotel": "Hotel Le Germain Vancouver (4-star)",
      "attractions": ["Stanley Park", "Granville Island", "Capilano Suspension Bridge Park"]
    },
    {
      "location": "Hong Kong, China",
      "duration": 5,
      "hotel": "Hotel Madera Hollywood (3-star)",
      "attractions": ["Victoria Peak", "Tsim Sha Tsui Promenade", "Wong Tai Sin Temple"]
    },
    {
      "location": "Bangkok, Thailand",
      "duration": 4,
      "hotel": "Hotel Muse Bangkok Langsuan (4-star)",
      "attractions": ["Grand Palace", "Wat Phra Kaew", "Floating Markets"]
    },
    {
      "location": "Chennai, India",
      "duration": 3,
      "hotel": "Hotel Taj Coromandel (5-star)",
      "attractions": ["Marina Beach", "Fort St. George", "Kapaleeswarar Temple"]
    }
  ],
  "daily_itinerary": [
    {
      "day": 1,
      "location": "Chennai, India",
      "activity": "Depart from Chennai"
    },
    {
      "day": 2,
      "location": "Tokyo, Japan",
      "activity": "Arrive in Tokyo, check-in to Hotel Gajoen Tokyo, explore Shibuya Crossing"
    },
    {
      "day": 3,
      "location": "Tokyo, Japan",
      "activity": "Visit Meiji Shrine, Tsukiji Fish Market"
    },
    {
      "day": 4,
      "location": "Tokyo, Japan",
      "activity": "Explore Asakusa, Ueno Park"
    },
    {
      "day": 5,
      "location": "Tokyo, Japan",
      "activity": "Visit Tokyo Tower, Imperial Palace"
    },
    {
      "day": 6,
      "location": "Seoul, South Korea",
      "activity": "Arrive in Seoul, check-in to Hotel PJ Myeongdong, explore Myeong-dong Shopping District"
    },
    {
      "day": 7,
      "location": "Seoul, South Korea",
      "activity": "Visit Gyeongbokgung Palace, Bukchon Hanok Village"
    },
    {
      "day": 8,
      "location": "Seoul, South Korea",
      "activity": "Explore Insadong, Hongdae"
    },
    {
      "day": 9,
      "location": "Seoul, South Korea",
      "activity": "Visit N Seoul Tower, Dongdaemun Design Plaza"
    },
    {
      "day": 10,
      "location": "Paris, France",
      "activity": "Arrive in Paris, check-in to Hotel Eiffel Seine, explore Eiffel Tower"
    },
    {
      "day": 11,
      "location": "Paris, France",
      "activity": "Visit Louvre Museum, Notre-Dame Cathedral"
    },
    {
      "day": 12,
      "location": "Paris, France",
      "activity": "Explore Montmartre, Champs-Élysées"
    },
    {
      "day": 13,
      "location": "Paris, France",
      "activity": "Visit Palace of Versailles"
    },
    {
      "day": 14,
      "location": "Paris, France",
      "activity": "Explore Latin Quarter, Seine River Cruise"
    },
    {
      "day": 15,
      "location": "Paris, France",
      "activity": "Visit Musée d'Orsay, Sainte-Chapelle"
    },
    {
      "day": 16,
      "location": "Paris, France",
      "activity": "Explore Le Marais, Place des Vosges"
    },
    {
      "day": 17,
      "location": "New York City, USA",
      "activity": "Arrive in New York City, check-in to Hotel Edison, explore Statue of Liberty"
    },
    {
      "day": 18,
      "location": "New York City, USA",
      "activity": "Visit Central Park, Metropolitan Museum of Art"
    },
    {
      "day": 19,
      "location": "New York City, USA",
      "activity": "Explore Times Square, Broadway"
    },
    {
      "day": 20,
      "location": "New York City, USA",
      "activity": "Visit 9/11 Memorial & Museum, Brooklyn Bridge"
    },
    {
      "day": 21,
      "location": "New York City, USA",
      "activity": "Explore Greenwich Village, SoHo"
    },
    {
      "day": 22,
      "location": "New York City, USA",
      "activity": "Visit Museum of Modern Art (MoMA), Rockefeller Center"
    },
    {
      "day": 23,
      "location": "New York City, USA",
      "activity": "Explore High Line, Chelsea Market"
    },
    {
      "day": 24,
      "location": "San Francisco, USA",
      "activity": "Arrive in San Francisco, check-in to Hotel Zeppelin, explore Golden Gate Bridge"
    },
    {
      "day": 25,
      "location": "San Francisco, USA",
      "activity": "Visit Alcatraz Island, Fisherman's Wharf"
    },
    {
      "day": 26,
      "location": "San Francisco, USA",
      "activity": "Explore Haight-Ashbury, Golden Gate Park"
    },
    {
      "day": 27,
      "location": "San Francisco, USA",
      "activity": "Visit de Young Museum, California Palace of the Legion of Honor"
    },
    {
      "day": 28,
      "location": "San Francisco, USA",
      "activity": "Explore Chinatown, North Beach"
    },
    {
      "day": 29,
      "location": "Vancouver, Canada",
      "activity": "Arrive in Vancouver, check-in to Hotel Le Germain Vancouver, explore Stanley Park"
    },
    {
      "day": 30,
      "location": "Vancouver, Canada",
      "activity": "Visit Granville Island, Capilano Suspension Bridge Park"
    },
    {
      "day": 31,
      "location": "Vancouver, Canada",
      "activity": "Explore Gastown, Yaletown"
    },
    {
      "day": 32,
      "location": "Vancouver, Canada",
      "activity": "Visit Grouse Mountain, Queen Elizabeth Park"
    },
    {
      "day": 33,
      "location": "Hong Kong, China",
      "activity": "Arrive in Hong Kong, check-in to Hotel Madera Hollywood, explore Victoria Peak"
    },
    {
      "day": 34,
      "location": "Hong Kong, China",
      "activity": "Visit Tsim Sha Tsui Promenade, Wong Tai Sin Temple"
    },
    {
      "day": 35,
      "location": "Hong Kong, China",
      "activity": "Explore Mong Kok, Temple Street Night Market"
    },
    {
      "day": 36,
      "location": "Hong Kong, China",
      "activity": "Visit Ocean Park, Hong Kong Disneyland"
    },
    {
      "day": 37,
      "location": "Bangkok, Thailand",
      "activity": "Arrive in Bangkok, check-in to Hotel Muse Bangkok Langsuan, explore Grand Palace"
    },
    {
      "day": 38,
      "location": "Bangkok, Thailand",
      "activity": "Visit Wat Phra Kaew, Floating Markets"
    },
    {
      "day": 39,
      "location": "Bangkok, Thailand",
      "activity": "Explore Chatuchak Weekend Market, Sukhumvit Road"
    },
    {
      "day": 40,
      "location": "Bangkok, Thailand",
      "activity": "Visit Jim Thompson House, Siam Paragon"
    },
    {
      "day": 41,
      "location": "Chennai, India",
      "activity": "Arrive in Chennai, check-in to Hotel Taj Coromandel, explore Marina Beach"
    },
    {
      "day": 42,
      "location": "Chennai, India",
      "activity": "Visit Fort St. George, Kapaleeswarar Temple"
    },
    {
      "day": 43,
      "location": "Chennai, India",
      "activity": "Explore Elliott's Beach, San Thome Cathedral"
    },
    {
      "day": 44,
      "location": "Chennai, India",
      "activity": "Visit Government Museum, Chennai Museum"
    },
    {
      "day": 45,
      "location": "Chennai, India",
      "activity": "Depart from Chennai"
    }
  ],
  "travel_tips": [
    "Research and book flights, hotels, and attractions in advance to save money.",
    "Pack light and efficiently, considering the varied climates and activities.",
    "Stay hydrated, bring sunscreen, and take breaks to avoid fatigue.",
    "Be respectful of local customs, traditions, and dress codes.",
    "Try local cuisine, but also consider vegetarian options and food allergies.",
    "Stay connected with family and friends back home, and keep important contacts handy."
  ],
  "visa_requirements": [
    {
      "country": "Japan",
      "visa_required": "No",
      "requirements": "Valid passport, return ticket, and proof of sufficient funds"
    },
    {
      "country": "South Korea",
      "visa_required": "No",
      "requirements": "Valid passport, return ticket, and proof of sufficient funds"
    },
    {
      "country": "France",
      "visa_required": "Yes",
      "requirements": "Valid passport, Schengen visa, and proof of sufficient funds"
    },
    {
      "country": "USA",
      "visa_required": "Yes",
      "requirements": "Valid passport, ESTA or visa, and proof of sufficient funds"
    },
    {
      "country": "Canada",
      "visa_required": "Yes",
      "requirements": "Valid passport, eTA or visa, and proof of sufficient funds"
    },
    {
      "country": "Hong Kong, China",
      "visa_required": "No",
      "requirements": "Valid passport, return ticket, and proof of sufficient funds"
    },
    {
      "country": "Thailand",
      "visa_required": "No",
      "requirements": "Valid passport, return ticket, and proof of sufficient funds"
    },
    {
      "country": "India",
      "visa_required": "No",
      "requirements": "Valid passport, return ticket, and proof of sufficient funds"
    }
  ],
  "packing_recommendations": [
    "Essentials: passport, visa, travel insurance, adapter, and converter.",
    "Clothing: lightweight, breathable, and versatile pieces for different climates.",
    "Footwear: comfortable walking shoes, sandals, and dress shoes.",
    "Toiletries: toothbrush, toothpaste, shampoo, conditioner, and any personal hygiene items.",
    "Electronics: phone, laptop, camera, and portable charger.",
    "Medications: any prescription medications, pain relievers, and antacids.",
    "Travel documents: flight itinerary, hotel reservations, and travel insurance documents."
  ]
}
```

This itinerary provides a mix of adventure, cultural exploration, and relaxation, while considering Sangeetha's preferences and budget. The estimated cost of $7745 includes flights, accommodation, food, and attractions, and is within the allocated budget of $8000. The daily itinerary provides a detailed schedule of activities, and the travel tips, visa requirements, and packing recommendations offer valuable advice for a smooth and enjoyable trip.
