#сайта больше не существует
from bs4 import BeautifulSoup
import requests
import json





def get_data(url):
    headers={
        "user - agent":
    "Mozilla/5.0(Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0"
    }

    # req=requests.get(url,headers)


    # with open("project.html","w",encoding='utf-8') as file:
    #     file.write(req.text)

    with open("project.html",'r',encoding='utf-8') as file:
        src=file.read()

    soup=BeautifulSoup(src,"lxml")
    articles=soup.find_all("article",class_="ib19")

    project_urls=[]
    for article in articles:
        project_url="http://www.edutainme.ru"+article.find("div",class_="txtBlock").get("href")
        project_urls.append(project_url)

    project_data_list=[]
    for project_url in project_urls:
        req=requests.get(project_url,headers)
        project_name=project_url.split("/")[-2]

        with open(f"data/{project_name}.html","w") as file:
            file.write(req.text)

        with open(f"data/{project_name}.html","r") as file:
            src=file.read()

        soup=BeautifulSoup(src,"lxml")
        project_data=soup.find("div",class_="inside")

        try:
            project_logo="http://www.edutainme.ru"+\
                         project_data.find("div",class_="Img logo").find("img").get("src")
        except Exception:
            project_logo="No project logo"

        try:
            project_name=project_data.find("div",class_="txt").find("h1").text
        except Exception:
            project_name="No project name"

        try:
            project_short_description=project_data.find("div",class_="txt").find("h4",class_="head").text
        except Exception:
            project_short_description="No project short description"

        try:
            project_website=project_data.find("div",class_="txt").find("p").find("a").text
        except Exception:
            project_website="No project website"

        try:
            project_full_description=project_data.find("div",class_="textWrap").find("div",class_="rb")
        except Exception:
            project_full_description="No project full description"

        project_data_list.append(
            {
                "Имя проекта":project_name,
                "URL логогтипа" : project_logo,
                "Короткое описание проекта" : project_short_description,
                "Сайт проекта" : project_website,
                "Полное описание проекта" : project_full_description.strip()
            }
        )

    with open("data/projects_data.json","a",encoding='utf-8') as file:
        json.dump(project_data_list,file,indent=4,ensure_ascii=False)











get_data("http://www.edutainme.ru/edindex/")