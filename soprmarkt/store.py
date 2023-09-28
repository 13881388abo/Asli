from pyfiglet import Figlet
def load():
    print("loading...")
    myfile = open("database.txt" , "r")
    data = myfile.read().split("\n")

    for i in range (len(data)):
        product_info=data[i].split(",")
        PRODUCTS.append({'id':int(input(product_info[0])),
                        "name"  :product_info[i],
                        "price" : float(product_info[2]),
                        "count":int(product_info[3])})
    print(" welcome ")
PRODUCTS=[]

def add_new_product():
    id=int(input("plase type id new product:"))
    name=(input("plase type name new product:"))
    price=float(input("plase type price new product:"))
    count=int(input("plase type conut new product:"))
    PRODUCTS.append({"id":id,"name":name,"price":price,"count":count})
    print(PRODUCTS)
    print("new product added successfully")
def show_all():
    for i in range(len(PRODUCTS)):
        print(PRODUCTS[i]["id"],"\t",PRODUCTS[i]["name"],"\t",PRODUCTS[i]["price"],"\t",PRODUCTS[i]["count"],"\t")
def add_edit_product():
    print("1.name")
    print("2.price")
    print("3.count")
    print("4.exit")
def edit_product():
    id=int(input("please type id product:"))
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]["id"]==id:
            while True:
                    add_edit_product()
                    select=int(input("please select a number of menu:"))
                    if select==1:
                        PRODUCTS[i]["name"]=input("please type rename product")
                    elif select==2:
                        PRODUCTS[i]["price"]=float(input("please type rename product"))
                    elif select==3:
                        PRODUCTS[i]["count"]=int(input("please type rename product"))
                    elif select==4:
                        break
                    else:
                        print("your selection is not defined!")
def show_menu():
    print("1- Add product")
    print("2- Edit product")
    print("3- Delete product")
    print("4- Search")
    print("5- Show list")
    print("6- Buy")
    print("7- exit")


load()
f = Figlet(font= "standard")
print(f.renderText("asli"))

show_menu()
choice = int(input("please chosse a number:"))
if choice == 1:
    add_new_product()
elif choice == 2:
    edit_product()
elif choice == 3:
    pass
elif choice == 4:
    pass
elif choice == 5:
    show_all()
elif choice == 6:
    pass
elif choice ==7:
    pass