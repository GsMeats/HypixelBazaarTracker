import requests
import os


def menu():
    os.system('cls')
    print("1: Enter without weekly volume filter")
    print("2: Enter with weekly volume filter")
    print("3: End program")
    
    choice = input("Enter Choice: ")
    return choice


def action(choice):
    os.system('cls')
    if choice == "1":
        margin = input("Enter the margin multiplier for your search: ")
        try: 
            a=float(margin)
        except:
            main()            
        search(margin)
    elif choice == "2":
        margin = input("Enter the multiplier between buy and sell: ")
        bfilter = input("Enter weekly insta-buy volume: ")
        sfilter = input("Enter weekly insta-sell volume: ")

        try: 
            a=int(bfilter)
            a=int(sfilter)
            a=float(margin)
        except:
            print("Invalid Entry")
            main()
        search(margin,bfilter,sfilter)



def search(amount,buyfilter=0,sellfilter=0):
    os.system('cls')
    amount = float(amount)
    link = "https://api.hypixel.net/skyblock/bazaar"
    data = requests.get(link).json()
    products = data['products']
    del(products['ENCHANTED_CARROT_ON_A_STICK'])
    del(products['BAZAAR_COOKIE'])
    for key in products:
        id = products[key].get('product_id')
        sell = products[key].get('sell_summary')[0].get('pricePerUnit')
        buy = products[key].get('buy_summary')[0].get('pricePerUnit')
        if sell*amount <= buy and products[key].get('quick_status').get('sellMovingWeek') >= int(sellfilter) and products[key].get('quick_status').get('buyMovingWeek') >= int(buyfilter):
            print(id,"Buy: ",buy)
            print(id,"Sell: ",sell)
    print("Search Complete!")
    print("Press enter to continue: ")
    e = input("")
    main()
                

def main():
    choice = menu()
    action(choice)


main()

            
