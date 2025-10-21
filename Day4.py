
web_dev = ["John", "Asha", "Ravi"]
data_science = ["Priya", "Karan", "Meena"]
ui_ux = ["Anita", "Rahul", "Divya"]


all_participants = [web_dev, data_science, ui_ux]


web_dev.append("Sonia")


data_science.insert(1, "Nikhil")

ui_ux.pop()


copied_data_science = data_science.copy()
data_science.clear()


first_two_web = web_dev[:2]


name_lengths = [len(name) for name in copied_data_science]


asha_present = (
    ("Asha" in web_dev) or 
    ("Asha" in copied_data_science) or 
    ("Asha" in ui_ux)
)


first_participants = (
    web_dev[0] if web_dev else None,
    copied_data_science[0] if copied_data_science else None,
    ui_ux[0] if ui_ux else None
)


print("Web Development:", web_dev)
print("Data Science (original cleared):", data_science)
print("Copied Data Science:", copied_data_science)
print("UI/UX Design:", ui_ux)
print("All participants:", all_participants)
print("First two Web Dev participants:", first_two_web)
print("Lengths of Data Science names:", name_lengths)
print("Is Asha in any list?:", asha_present)
print("First participants tuple:", first_participants)
