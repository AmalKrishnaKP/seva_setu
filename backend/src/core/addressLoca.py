import requests




def addressLocator(lati,longi):
    try:
            response = requests.get(
                url="https://nominatim.openstreetmap.org/reverse",
                params={
                    "lat": lati,
                    "lon": longi,
                    "format": "jsonv2",
                    "addressdetails": 1
                },
                headers = {
                    "User-Agent": "SevaSetu/1.0"
                }
            )

            response.raise_for_status()

            data = response.json()
            # print(data)

            return {
                "address": data.get("display_name"),
                "latitude": lati,
                "longitude": longi
            }
    except Exception as e:
            print(e)