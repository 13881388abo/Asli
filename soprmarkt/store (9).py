import math
from pyfiglet import Figlet
f = Figlet(font= "standard")
print(f.renderText("abolfzl asli 1000"))
def show_menu():
    print("1- Add product")
    print("2- Edit product")
    print("3- Delete product")
    print("4- Search")
    print("5- Show list")
    print("6- Buy")
    print("7- exit")

myfile = open("database.txt" , "r")
data = myfile.read()

PRODUCT = []
product_list = data.split("\n")
for i in range (len(product_list)):

    mydict = {}
    mydict["id"] = product_list[0]
    mydict["name"] = product_list[1]
    mydict["price"] = product_list[2]
    mydict["count"] = product_list[3]
    PRODUCT.append(mydict)
    print(mydict)
show_menu()
choice = int(input("please chosse a number:"))

if choice == 1:
    myfile = open("database.txt" , "r")
    data = myfile.read()
    product_list = data.split("\n")
    f=open("database.txt","a")
    f.write(input())
    f.close()
    f= open("database.txt","r")
    print(f.read())
elif choice == 2:
        print(PRODUCT)
        for x in range(len(PRODUCT)):
            print(PRODUCT[x]["name"])

        name = input("Enter the preffered product name : ")

        for i in range(len(PRODUCT)-1):
            print(i)
            if name == PRODUCT[i]["name"]:
                PRODUCT.pop(i)
        id = input("Enter your product id : ")
        name = input("Enter your product name : ")
        price = input("Enter your product price : ")
        count = input("Enter your product quantity : ")
        mydict = {"id":id,"name":name,"price":price,"count":count}
        PRODUCT.append(mydict)
        data = ""#madebyfarhan
        for y in range(len(PRODUCT)):
            data += PRODUCT[y]["id"] + "," + PRODUCT[y]["name"] + "," + PRODUCT[y]["price"] + "," + PRODUCT[y]["count"] 
            if y != len(PRODUCT)-1:
                #made by farhan
                data += "\n"
        myfile = open("database.txt" , "w")
        myfile.write(data)
        myfile.close()
        print("Product edited!")
elif choice == 3:
    for x in range(len(PRODUCT)):
            print(PRODUCT[x]["name"])

            name = input("Enter the preffered product name : ")

            for i in range(len(PRODUCT)):
                if name == PRODUCT[i]["name"]:
                    #made by farhan
                    PRODUCT.pop(i)
            data = ""
            for y in range(len(PRODUCT)):
                data += PRODUCT[y]["id"] + "," + PRODUCT[y]["name"] + "," + PRODUCT[y]["price"] + "," + PRODUCT[y]["count"] + "\n"
            myfile = open("database.txt" , "w")
            myfile.write(data)
            myfile.close()
            print("Product deleted!")
elif choice == 4:
    def search(database,txt): 
    
        for i in range (len(arr)): 
            if (arr[i] == x): 
                return i; 
        return -1; 
        if __name__ == '__main__':
            arr = [ 2, 3, 4, 10, 40 ]; 
            x = 10; 
            result = search(arr, x) 
        if(result == -1): 
            print("Element is not present in array") 
        else: 
            print("Element is present at index", result)
elif choice == 5:
    name = input("Please enter your product name : ")
    for i in range(len(PRODUCT)):
            if PRODUCT[i]["name"] == name:
                print("Here is your product details :")
                print("Id :",PRODUCT[i]["id"])
                print("Name :",PRODUCT[i]["name"])
                print("Price :",PRODUCT[i]["price"])
                print("Quantity :",PRODUCT[i]["count"])
            else :#made by farhan
                print("Product not found !")
elif choice == 6:
        print("List of products in {id/name} order :")
        #made by farhan
        for i in range(len(PRODUCT)):
            #made by farhan
            print(PRODUCT[i]["id"],"/",PRODUCT[i]["name"]) 

        id = input("Enter the id of the bought product : ")
        quan = input("Enter the quantity of the bought product : ")
        for i in range(len(PRODUCT)):
           if id == PRODUCT[i]["id"]:
               count = int(PRODUCT[i]["count"])
               count -=quan
               PRODUCT[i]["count"]=str(count)
        print("Product bought!")
elif choice == 7:
    exit