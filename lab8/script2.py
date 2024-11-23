#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

import json

with open('schacon.repos.json', 'r') as file:
    data = json.load(file)

with open('chacon.csv', 'w') as csv_file:    
    for item in data[:5]:
        name = item.get('name', 'N/A')
        html_url = item.get('html_url', 'N/A')
        updated_at = item.get('updated_at', 'N/A')
        visibility = item.get('visibility', 'N/A')

        csv_line = f"{name},{html_url},{updated_at},{visibility}\n"
        csv_file.write(csv_line)
