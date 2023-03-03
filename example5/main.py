import requests
import img2pdf

def get_data():

    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33"
    }

    img_list=[]
    for i in range(1,49):
        url=f"https://www.recordpower.co.uk/flip/Winter2020/files/mobile/{i}.jpg"
        req=requests.get(url=url,headers=headers)
        response=req.content

        with open(f"media/{i}.jpg","wb") as file:
            file.write(response)
            img_list.append(f"media/{i}.jpg")
            print(f"Downloaded {i} of 48")

    print('#'*20)
    print(img_list)

    # create PDF file
    with open("result.pdf","wb") as file:
        file.write(img2pdf.convert(img_list))

    print("PDF file created successfully!")



if __name__ == '__main__':
    get_data()