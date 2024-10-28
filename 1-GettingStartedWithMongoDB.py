from pymongo import MongoClient

uri = "mongodb://localhost:27017/"
client = MongoClient(uri)

try:
    database = client.get_database("flights")
    flights = database.get_collection("flightDataCollection")

    # Query for a movie that has the title 'Back to the Future'
    query = {"aircraft": "Airbus A380"}
    flight = flights.find_one(query)

    print(flight)

    client.close()

except Exception as e:
    raise Exception("Unable to find the document due to the following error: ", e)
