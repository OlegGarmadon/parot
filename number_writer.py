import json

namber = [2, 3, 3, 5, 11, 12, 65, 55]


filename = 'nambers.json'
with open(filename, 'w') as f:
	json.dump(namber, f)