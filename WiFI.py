import requests, json

f=open('data-9776-2016-10-10.json','r')
data=json.load(f)
a = []
f2=open('Locations.txt','w')
for i in range (len(data)):
    if "Location" in data[i].keys():
        b = {}
        result=requests.get("https://maps.google.com/maps/api/geocode/json?address="+str(data[i]["Location"])+"&sensor=false&key=AIzaSyDYN1XAbJ0t3hTYxvrVyel6esomYLhmHY0")
        result=result.text
        coor=json.loads(result)

        try:
            b["lng"]=coor['results'][0]['geometry']['viewport']['southwest']["lng"]
            b["lat"]=coor["results"][0]["geometry"]['viewport']['southwest']["lat"]
            b["Location"]=data[i]["Location"]
            a.append(b)

        except:
            pass
f2.write(str(a))