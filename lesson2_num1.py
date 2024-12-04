# List each flight itinerary.

def format_itineraries(itinerary_list):
    result = ""
    for index, (traveler_name, origin, destination) in enumerate(itinerary_list, start=1):
        result += f"Itinerary {index}: {traveler_name} - Fron {origin} to {destination}\n "
    return result.strip()

# Use function format_itineraries

itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
formatted_itineraries = format_itineraries(itineraries)
print(formatted_itineraries)