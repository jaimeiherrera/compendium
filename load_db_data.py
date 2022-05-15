import requests

URL = "http://127.0.0.1:9001/demons/"
PARAMS = [
    {
        'name': 'Jack Frost',
        'description': 'Jack Frost is a spirit originating from England. He is a snow elf who brings in cold weather during the winter and is thought to be responsible for the frost that forms on the windows of homes and buildings.',
        'url_image': 'https://i.imgur.com/fAMd0W8.png'
    },
    {
        'name': 'Shadow',
        'description': 'Shadow probably refers to a part of the unconscious mind that symbolizes repressed weaknesses or faults, as outlined by the Swiss psychiatrist Carl Jung. It could also be related to a kind of ghost called the Shade.',
        'url_image': 'https://i.imgur.com/rjr62Yu.jpg'
    },
    {
        'name': 'Sakahagi',
        'description': "Before the Conception, Sakahagi's previous life was that of a successful businessman. Though he seemed to be living the ideal life everyone strives to obtain, his fortune eventually collapsed and this left him consumed with thoughts of killing, his hostility directed towards a young man who he vehemently claims was responsible for his downfall. His was one of the strong emotions that lingered and lent itself to the earth after Tokyo transforms into the Vortex World, and his desired persona emerged, taking the form of a Manikin with a single-minded thirst for power and blood.",
        'url_image': 'https://i.imgur.com/ev0jqyW.png'
    },
    {
        'name': 'Phantom',
        'description': 'Phantom is a spirit or soul of a deceased person or animal that will occasionally show itself to the living. Their manifestation varies from shadows and wisps to lifelike forms of their former selves.',
        'url_image': 'https://i.imgur.com/pwnzAwJ.jpg'
    },
    {
        'name': 'Black Ooze',
        'description': 'Origin: Unknown. A body of black muciferous gel. This demon failed to materialize and lost control of itself, thirsting for blood.',
        'url_image': 'https://i.imgur.com/ZARGoRe.jpg'
    }
]

for params in PARAMS:
    response = requests.post(URL, json=params)
    print(response.text)
