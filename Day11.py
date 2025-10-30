import json
from datetime import datetime

def create_record(city, comment, date):
    """
    Returns a travel record as a dictionary.
    Args:
        city (str): Name of the city visited
        comment (str): Comment about the visit
        date (str): Visit date in "dd-mm-yyyy" format
    """
    return {
        "city": city,
        "comment": comment,
        "date": date
    }


records = [
    create_record("Paris", "Visited the Eiffel Tower!", "05-06-2022"),
    create_record("Tokyo", "Loved the cherry blossoms!", "12-04-2023"),
    create_record("New York", "Enjoyed Times Square!", "20-09-2021")
]


for record in records:
    old_date = datetime.strptime(record["date"], "%d-%m-%Y")
    record["date"] = old_date.strftime("%B %d, %Y")  # e.g. June 05, 2022


json_data = json.dumps(records, indent=4)
print("JSON string:\n", json_data)


parsed_records = json.loads(json_data)

print("\nParsed Records:")
for record in parsed_records:
    print(record)
