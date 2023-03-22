import requests

url = "https://indeed-jobs-api.p.rapidapi.com/indeed-us/"

print("Enter the location you wish to search for job oppurtunities")
location = input()

querystring = {"offset":"0","keyword":"python","location":location}

headers = {
	"X-RapidAPI-Key": "622f43aa87mshf3fbb459ef3b059p16f66fjsnbb7a12a55c94",
	"X-RapidAPI-Host": "indeed-jobs-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.json()

print("\nBelow are the Company Details received from Indeed!!!")

for i in range(0,len(data)):
    print("\n***************************************")
    dict = data[i]
    for key,value in dict.items():
        print(key,"..................\t",value)
    print("\n***************************************")