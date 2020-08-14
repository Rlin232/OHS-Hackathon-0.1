import requests
import matplotlib.pyplot as plt

url = 'https://data.ca.gov/api/3/action/datastore_search_sql?sql=SELECT * FROM "339d1c4d-77ab-44a2-9b40-745e64e335f2" ORDER BY _id DESC LIMIT 5;'
r = requests.get(url=url, verify=False)

data = r.json()
results = data['result']
records = results['records']

age_groups = [
    '0-17', '18-49', '50-64', '65+'
]
positive = [
    (float(records[4]['totalpositive']) / 22.15),
    (float(records[3]['totalpositive']) / 44.439),
    (float(records[2]['totalpositive']) / 19.211),
    (float(records[1]['totalpositive']) / 14.3)
]

plt.style.use('ggplot')

x_pos = [i for i, _ in enumerate(age_groups)]

plt.bar(x_pos, positive, color='lightskyblue')
plt.xlabel("Age Group")
plt.ylabel("Number of Positive Cases")
plt.title("Total Positive Cases per Age Group")

plt.xticks(x_pos, age_groups)

plt.savefig("positive.png")
plt.close()

deaths = [
    (float(records[4]['deaths']) / 22.15),
    (float(records[3]['deaths']) / 44.439),
    (float(records[2]['deaths']) / 19.211),
    (float(records[1]['deaths']) / 14.3)
]

plt.style.use('ggplot')

x_pos = [i for i, _ in enumerate(age_groups)]

plt.bar(x_pos, deaths, color='lightskyblue')
plt.xlabel("Age Group")
plt.ylabel("Number of Deaths")
plt.title("Total Deaths per Age Group")

plt.xticks(x_pos, age_groups)

plt.savefig("deaths.png")
plt.close()
