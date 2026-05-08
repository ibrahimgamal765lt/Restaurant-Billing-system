from tkinter import *
from tkinter import messagebox

menu = {
    "pizza": 20.50,
    "Pasta": 11,
    "Rice": 12.50,
    "Chicken": 25.25,
    "Meat": 27.50,
    "Fried Chicken": 22.50,
    "Fries": 7.50
}

order = []


window = Tk()
window.title("Country Food")
window.geometry("800x600")
window.config(bg="#f7f5f2")

title = Label(window, text="Joey Does not share food", font=("Arial", 28, "bold"))
title.grid(row=0)

menulist = Listbox(window, width=40, height=10, relief=SOLID)
menulist.grid(row=1, column=0)

orderlist = Listbox(window, width=40, height=10, relief=SOLID)
orderlist.grid(row=1, column=1)

def viewmenu():
    for dish, price in menu.items():
        menulist.insert(END, f"{dish}: ${price}")
viewmenu()

def addtoorder():
    try:
        selecteditem = menulist.get(menulist.curselection())
        order.append(selecteditem)
        orderlist.insert(END, selecteditem)
    except:
        messagebox.showerror("error", "Please select an item from the menu to add it to your order.")

addorderbutton = Button(window, relief=RAISED, font=("Arial", 14, "bold"), command=addtoorder, text="Add to order", width=20, height=2)
addorderbutton.grid(row=2, column=0)

def generatebill():
    if not order:
        messagebox.showerror("Fen ltalab", "YOu haven't ordered anything yet.")
    total = 0
    billdetails = "Bill Details\n\n"
    for item in order:
        dish, price = item.split(": $")
        price = float(price)
        total += price
        billdetails += f"{dish}: ${price}\n"
    billdetails += f"\nTotall: ${total}"
    messagebox.showinfo("Bill", billdetails)
    orderlist.delete(0, END)
    order.clear()

generatebillbutton = Button(window, relief=RAISED, text="Generate Bill", command= generatebill, font=("Arial", 14, "bold"), width=20, height=2, bg="#006400", fg="#FFFFFF")
generatebillbutton.grid(row=2, column=1)

end = Label(window, text="Enjoy Your Food", font=("Arial", 18, "italic"))
end.grid(row=4, column=0)




    

window.mainloop()