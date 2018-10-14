
John = {"name": "John", "age": 52, "department": "Marketing", "phone": "555-1234", "salary": "$85,000"}
Frank = {"name": "Frank", "age": 36, "department": "Management", "phone": "555-6789", "salary": "$76,000"}
Rachel = {"name": "Rachel", "age": 41, "department": "Administration", "phone": "555-2345", "salary": "$80,000"}
employees = [John, Frank, Rachel]

for employee in employees:
    print (employee["name"] + " in " + (employee["department"]) + " can be reached at " + (employee["phone"]))
