import requests
import json
import datetime
from collections import Counter

api_endpoint = 'https://date.nager.at/api/v3/publicholidays/2024/US'

response = requests.get(api_endpoint)
response.raise_for_status()
data = response.json()
earliest_holiday = sorted(data, key=lambda x: x['date'])[0]
print(earliest_holiday)


state_counts = Counter()
for holiday in data:
    state_counts[holiday['countryCode']] += 1
top_states = state_counts.most_common(7)
top_state_codes = [state for state, count in top_states]
print(top_state_codes)

weekends = 0
for i in range(len(data) - 2):
    date1 = datetime.datetime.strptime(data[i]['date'], '%Y-%m-%d').date()
    date2 = datetime.datetime.strptime(data[i + 2]['date'], '%Y-%m-%d').date()
    if date1 == date2 - datetime.timedelta(days=2):
        weekends += 1
print(weekends)
