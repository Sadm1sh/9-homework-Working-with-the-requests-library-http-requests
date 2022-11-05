import requests
HTTPS_STATUS_CREATE:int = 201
TOKEN = "" #вставить токен

list_of_superheroes = ["Hulk", "Captain America", "Thanos"]

def super_hero(list_of_superheroes):
    url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    request = requests.get(url).json()
    super_intelligence = {}
    for superhero in request:
        if superhero["name"] in list_of_superheroes:
            super_intelligence[superhero["name"]] = {"intelligence": superhero["powerstats"]["intelligence"]}
    return sorted(super_intelligence.items(), key=lambda x: x[1]["intelligence"], reverse=True)
def smartest_superhero():
    super_intelligence_list = []
    for name, value in super_hero(list_of_superheroes):
        print(f"Имя героя: {name} (Интелект: {value['intelligence']})")
        super_intelligence_list.append(value['intelligence'])
        if value['intelligence'] == max(super_intelligence_list):
            megamozg = f"Самый умный герой: {name} (Интелект: {value['intelligence']})"
            with open("Megamozg.txt", 'w', encoding='utf-8') as file:
                file.write(megamozg)
    print("\nУпаковка Самого Умного Супера в файл в формате .txt прошла успешно\n")

#######################Задача №2#########################
class YaUploader:
    URI:str = "https://cloud-api.yandex.net/v1/disk/resources"
    URL_UPLOAD_LINK:str = f"{URI}/upload"
    def __init__(self, token: str):
        self.token = token

    @property
    def header(self):
        return {
            "Content_Type": "application/json",
            "Authorization": f"OAuth {self.token}"
        }
    def get_upload_link(self, ya_disk_path:str):
        params = {"path": ya_disk_path, "overwrite": "true"}
        resource = requests.get(self.URL_UPLOAD_LINK, params=params, headers=self.header)
        upload_url = resource.json().get("href")
        return upload_url
    def upload_file(self, ya_disk_path:str , file_path:str):
        upload_link = self.get_upload_link(ya_disk_path)
        with open(file_path, "rb") as file_obj:
            responce = requests.put(upload_link, data=file_obj)
            if responce.status_code == HTTPS_STATUS_CREATE:
                print("\nЗагрузка файла на ЯндексДиск прошла успешно!!!\n")
        return responce.status_code
########################Задание №3##############################
def last_questions():
    url = 'https://api.stackexchange.com/2.3/questions'
    params = {'order': 'desc', 'fromdate': '1667174400', 'sort': 'creation', 'tagged': 'python', 'site': 'stackoverflow'}
    response = requests.get(url, params=params)
    print('Вопросы с тегом "python" с 31 октября в порядке от самых новых до более старых:')
    for item in response.json()["items"]:
        print(item["link"])

if __name__ == '__main__':
  smartest_superhero()
  instance = YaUploader(TOKEN)
  instance.upload_file('/Megamozg.txt', "Megamozg.txt")
  last_questions()