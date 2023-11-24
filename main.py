# Initialisation
import requests, json
token = 
databaseID =
headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2022-02-22"
}

#<script async data-nf='{"formurl":"https://notionforms.io/forms/registre-des-promesses-dachat-p59kj8","emoji":"📃","position":"right","bgcolor":"#000000","width":"500"}' src='https://d3n1rwgcdu2uk.cloudfront.net/be5dbaa4-10cb-4bc3-93a0-6ed94e7010f5/widgets/embed-min.js'></script>

# Response a Database
def responseDatabase(databaseID,headers):
    readUrl=f"https://api.notion.com/v1/databases/{databaseID}"
    res=requests.request("GET",readUrl,headers=headers)
    print(res.status_code)

def readDatabase(databaseID, headers):
    readUrl = f"https://api.notion.com/v1/databases/{databaseID}/query"
    res = requests.request("POST", readUrl, headers=headers)
    data = res.json()
    print(res.status_code)
    # print(res.text)
    for i in data['results']:
      for j in i['properties']:
        for key, value in zip(i['properties'][j].keys(), i['properties'][j].values()):
          type = key
          answer = value
        if answer == None or not answer:
          None
        else:
          print(j,":",type)
          if isinstance(answer, bool):
            print(bool(answer))
          else:
            try:
              print(answer[0]["text"]["content"])
            except:
              try:
                for l in range(len(answer)):
                  print(answer[l]["name"])
              except:
                try:
                  print(answer["name"])
                except:
                  try:
                    print(answer["start"])
                  except:
                    print(answer)
    #with open('./full-properties.json', 'w', encoding='utf8') as f:
    #   json.dump(data, f, ensure_ascii=False)
    return data

readDatabase(databaseID,headers)


