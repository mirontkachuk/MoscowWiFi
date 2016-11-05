import requests, json, math
adress = input()
result = requests.get("https://maps.google.com/maps/api/geocode/json?address="+str(adress)+"&sensor=false&key=AIzaSyDYN1XAbJ0t3hTYxvrVyel6esomYLhmHY0")
ADRESS = json.loads(result.text)
try:
    x = ADRESS['results'][0]['geometry']['bounds']['southwest']['lat']
    y = ADRESS['results'][0]['geometry']['bounds']['southwest']['lng']
    f=open('Locations.txt','r')
    text = f.read();
    data=json.loads(text.replace("'", "\""))
    min=1000
    for i in range (len(data)):
        gipotenuza=math.sqrt((data[i]['lng']-y)*(data[i]['lng']-y)+(data[i]['lat']-x)*(data[i]['lat']-x))
        if min>gipotenuza:
            min=gipotenuza
            name=data[i]['Location']
    print (name)
except:
    print ("Вы не в Москве((")
    x = ADRESS['results'][0]['geometry']['location']['lat']
    y = ADRESS['results'][0]['geometry']['location']['lng']
    f = open('Locations.txt', 'r')
    text = f.read();
    data = json.loads(text.replace("'", "\""))
    min = 1000
    for i in range(len(data)):
        gipotenuza = math.sqrt(
            (data[i]['lng'] - y) * (data[i]['lng'] - y) + (data[i]['lat'] - x) * (data[i]['lat'] - x))
        if min > gipotenuza:
            min = gipotenuza
            name = data[i]['Location']
    print(name)