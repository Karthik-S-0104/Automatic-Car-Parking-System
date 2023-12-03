import requests

def entryMessage(slotNO):
    url = "https://www.fast2sms.com/dev/bulkV2"
    mylist = ["https://drive.google.com/file/d/1SuQV8Vg9uMrtebObak42b_uvX-SwZVTP/view?usp=sharing","https://drive.google.com/file/d/1YUz0wOotahjK8OrcQztcP3zi5a3MDvYK/view?usp=sharing","https://drive.google.com/file/d/1xoPsAZVSiEfHpdOgwfNunskQfBmhP96A/view?usp=sharing","https://drive.google.com/file/d/1v6Ko8fKS5v0wmoQeRhZHqE3li_6Ua2zH/view?usp=sharing","https://drive.google.com/file/d/1v6Ko8fKS5v0wmoQeRhZHqE3li_6Ua2zH/view?usp=sharing","https://drive.google.com/file/d/1FCOWvis5bWFwSEMYpvWCGTfBLlzVZwu4/view?usp=sharing","https://drive.google.com/file/d/1Um3EnrnQLPcHPe89PspY9WylX7XtVbZ1/view?usp=sharing","https://drive.google.com/file/d/1Nuzuln7T37rm_aXh0WY4KhwK_56vcmIF/view?usp=sharing","https://drive.google.com/file/d/1Nuzuln7T37rm_aXh0WY4KhwK_56vcmIF/view?usp=sharing","https://drive.google.com/file/d/1_NCWosFQScL-6L-jkodW1ZDBv-6_PRvL/view?usp=sharing","https://drive.google.com/file/d/1WVzmBTe-oVZtDfPZK5MzxpkT-EP1xqvy/view?usp=sharing","https://drive.google.com/file/d/1FLohvywECYuNBFhkK1aPlmRBWuf8cNlU/view?usp=sharing","https://drive.google.com/file/d/1FvglWMkcvydsjDxlnyVqNJ65Eb4KHJNI/view?usp=sharing","https://drive.google.com/file/d/1y3pdOHgBmmmXGEyc-v7Qcr8GSvquqUcb/view?usp=sharing","https://drive.google.com/file/d/1QYyPufglNYUr5vJRyiMNJxESuapsxEP_/view?usp=sharing","https://drive.google.com/file/d/10cpdJAiUDOZY-438w3Dvxv3SKbjMQPlf/view?usp=sharing","https://drive.google.com/file/d/16H4fG9VCGFGwg1WCs0ldAmfxWBtdNO0y/view?usp=sharing","https://drive.google.com/file/d/1TD3EDjTWm9zyAfHBoRKgM2Xj8tjSnaZL/view?usp=sharing"]
    name = "Nishith P Shetty"
    number = 8310659391
    url2= mylist[slotNO]
    message = "Hello {} Your allocated parking slot is {}. To see the map visit : {}".format(name,slotNO,url2)
    querystring = {"authorization":"CD1rsoVcqH0ROQgafUhPlA9xwMpSWTyXub7I2Nn6tKzkiLdejBu6YyQgJEskzrnwl7ZdxKe8W4a0cLAb",
                    "message":message,
                    "language":"english",
                    "route":"q","numbers":number}
    headers = {
        'cache-control': "no-cache"
    }
    #response = requests.request("GET", url, headers=headers, params=querystring)
    #print(response.text)
    print()
    print(message)
    print()

def exitMessage(amount):
    url = "https://www.fast2sms.com/dev/bulkV2"
    upiID = "nishithpshetty@oksbi"
    upiUrl = "https://upayi.ml/{}/{}".format(upiID, amount)
    number = 8310659391
    message = "Your parking fee is {}. Please pay it using below link {}".format(amount, upiUrl)
    querystring = {"authorization":"CD1rsoVcqH0ROQgafUhPlA9xwMpSWTyXub7I2Nn6tKzkiLdejBu6YyQgJEskzrnwl7ZdxKe8W4a0cLAb",
                    "message":message,
                    "language":"english",
                    "route":"q","numbers":number}
    headers = {
        'cache-control': "no-cache"
    }
    #response = requests.request("GET", url, headers=headers, params=querystring)
    #print(response.text)
    print()
    print(message)
    print()