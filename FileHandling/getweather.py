import csv
import json
from urllib.request import urlopen


def get_city_data(city_name):
    base_url = "https://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
    url = base_url + city_name
    response = urlopen(url)

    city_data = {"record": json.loads(response.read())}

    return city_data


def write_csv_file(city_data):
    with open('get_city_data.csv', 'a', newline="") as file:
        reader = csv.writer(file)


        for data in city_data.values():
            reader.writerow([data['name'], data['coord']['lon'], data['coord']['lat'], data['main']['temp'],
                             data['main']['temp_max'], data['main']['temp_min']])
        return {"message": "csv file is updated"}


if __name__ == '__main__':
    city = input("enter city ")
    data = get_city_data(city)
    print(data)
    updated = write_csv_file(data)
    print(updated)
