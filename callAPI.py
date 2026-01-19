import os
import requests
import csv 
API_KEY = "AQEyhmfxKY/OaxFHw0m/n3Q5qf3VaY9UCJ14XWZE03G/k2NFiib/zJrXSECBRHLQQ81lUA4QwV1bDb7kfNy1WIxIIkxgBw==-lwmOPVzOGi4thO1N3dBHPO0+TosJ1cn88AmchcQCAb4=-pq@mK_p>8$E:_9(s"
headers = {
    "x-api-key": API_KEY
}
URL = "https://checkout-test.adyen.com/v71/paymentMethods"
payload = {
    "merchantAccount": "AdyenRecruitmentCOM",
    "shopperReference": "eu-shopper-02"
}

# def myRead():
#     print(os.getcwd())
#     with open("data.txt", "w") as f:
#         f.write("Hello, world!\n")
#         f.write("This is a file.\n")
def callAPI():
    response = requests.post(URL,json=payload,headers=headers,timeout=10)
    if response.status_code == 200 :
        data = response.json()
        print("=== Payment Methods ===")
        with open("output.csv", "w", newline="", encoding="utf-8") as pmf:
            writer = csv.writer(pmf)
            # Optional: write header
            writer.writerow(["name", "type"])
            for pm in data.get("paymentMethods"):
                print(pm["name"], pm["type"])
                writer.writerow([pm["name"], pm["type"]])

        with open("storedpayments.csv","w") as spmf:
            spmf.write("name,id\n")
            for spm in data.get("storedPaymentMethods", []):
                spmf.write(spm["name"])
        # # List stored payment methods
        # print("=== Stored Payment Methods ===")
        # for spm in data.get("storedPaymentMethods", []):
        #     print(f"Name: {spm.get('name')}, Type: {spm.get('type')}, Brand: {spm.get('brand')}, Last4: {spm.get('lastFour')}")

    else:
        print("Error: ",response.status_code)
    #return data

# def writeToFile():
#     data = callAPI()
#     with open("output.csv","w",newline="",encoding="utf-8") as of:
#         writer = csv.writer(of)
#         writer.writerow(["userid","id","title","completed"])
#     for row in :
#         writer.writerow(data["userId"],)    


# writeToFile()

callAPI()