from client import FtxClient
from time import sleep

def checkAvlSRM(restBot:FtxClient):
    bal = restBot.get_balances()
    srmAvailable = dict.fromkeys(["SRM", "SRM_LOCKED", "MSRM", "MSRM_LOCKED"])
    for i in bal:
        if(i['coin'] == "SRM" and float(i["free"]) >= 0.00000001):
            srmAvailable["SRM"] = float(i["free"])
        elif(i['coin'] == "SRM_LOCKED" and float(i["free"]) >= 0.00000001):
            srmAvailable["SRM_LOCKED"] = float(i["free"])
        elif(i['coin'] == "MSRM" and float(i["free"]) >= 0.00000001):
            srmAvailable["MSRM"] = float(i["free"])
        elif(i['coin'] == "MSRM_LOCKED" and float(i["free"]) >= 0.00000001):
            srmAvailable["MSRM_LOCKED"] = float(i["free"])
    return srmAvailable

def main():
    print("----------------------------------------------------------------------------------------------------")
    print("Please Note: This program will stake ALL of your available SRM/LSRM/MSRM/LMSRM.")
    print("So maybe you want to make a subaccount just for the staking purpose, in case you're using SRM as collateral.")
    print("And please make sure you DID NOT enable the withdrawal ability of your API key.")
    print("----------------------------------------------------------------------------------------------------")
    apiKey = input("Enter your api Key:")
    apiSecret = input("Enter your api Secret:")
    subName = input("Enter your subaccount name(if any), or just press enter:")
    restBot = FtxClient(apiKey, apiSecret,subName)
    bal = None
    try:
        bal = restBot.get_balances()
    except Exception as e:
        print(e)
        print("Please check your API key and secret.")
    while True:
        srmAvailable = checkAvlSRM(restBot)
        if(srmAvailable["SRM"] != None):
            print("Staking",srmAvailable["SRM"],"SRM")
            restBot.stake_request("SRM",srmAvailable["SRM"])
        if(srmAvailable["SRM_LOCKED"] != None):
            print("Staking",srmAvailable["SRM_LOCKED"],"SRM_LOCKED")
            restBot.stake_request("SRM_LOCKED",srmAvailable["SRM_LOCKED"])
        if(srmAvailable["MSRM"] != None):
            print("Staking",srmAvailable["MSRM"],"MSRM")
            restBot.stake_request("MSRM",srmAvailable["MSRM"])
        if(srmAvailable["MSRM_LOCKED"] != None):
            print("Staking",srmAvailable["MSRM_LOCKED"],"MSRM_LOCKED")
            restBot.stake_request("MSRM_LOCKED",srmAvailable["MSRM_LOCKED"])
        print("Stake complete, waiting for the next hour...")
        sleep(3600)
if __name__ == '__main__':
    main()