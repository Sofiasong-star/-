import requests

url = "https://opensky-network.org/api/states/all"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    flights = data.get('states', [])
    print(f"Найдено самолётов в воздухе: {len(flights)}")
    

    for plane in flights[:5]:
        print(f"Позывной: {plane[1]}")  
        print(f"Широта: {plane[6]}")     
        print(f"Долгота: {plane[5]}")    
        print(f"Высота: {plane[7]} м")  
        print("-" * 30)
else:
    print(f"Ошибка: {response.status_code}")
    print(response.text)
