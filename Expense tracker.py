import pandas as pd 
import tkinter as tk
from tkinter import messagebox,ttk
import pandas as pd
import matplotlib.pyplot as plt

cexpense=0
income=0
remaining=0
pandl=[]
cre_deb=[]
total=[]
df=None
profit=[]
loss=[]

# get graph
def get_data():
    global df,profit,loss
    data={
        "P&L type":pandl,
        "P&L Amount":cre_deb,
        "Total":total
    }
    df=pd.DataFrame(data)
    df.to_excel("Expense Tracker.xlsx",index=False)
    text.delete("1.0","end")
    text.insert(tk.END,df.to_string())
    # label=["Income","Expense"]
    # values=[profit,loss]
    plt.plot(profit,label="Income",marker="o")
    plt.plot(loss,label="Expense",marker="o")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.show()

# get plan to save money
def plan():
    text.delete("1.0","end")
    plans="""
💡 1. Track Every Expense:
Write down or log every rupee
Even small things like chai, snacks, etc.
👉 Why it matters:
Most people don’t realise where their money is going.

📊 2. Follow the 50-30-20 Rule
50% → Needs (rent, food, travel)
30% → Wants (movies, eating out)
20% → Savings
👉 If 20% feels too high, start with 5–10%, then increase.

💳 3. Avoid Impulse Buying
Before buying something, ask:
Do I really need this?
Will I still want it after 2 days?
👉 Try the “24-hour rule” for non-essential purchases.

🍔 4. Reduce Eating Out
Eating outside frequently = biggest money leak 💸
Try:
Cooking more at home
Limiting eating out to weekends

🛒 5. Make a Budget Before Shopping
Always go with a list
Avoid “just browsing”

👉 Supermarkets are designed to make you overspend.
💰 6. Pay Yourself First
As soon as you get money:
Transfer a portion to savings
👉 Don’t save what’s left—
👉 Spend what’s left after saving.

📉 7. Cut Unnecessary Subscriptions
OTT, apps, games, etc.
Ask:
Am I actually using this?
🏦 8. Use Separate Accounts
One account → spending
One account → savings
👉 Makes it harder to accidentally spend savings."""
    text.insert(tk.END,plans)

def income_gain():
    global remaining,profit
    try:
        income_type=combo1.get()
        if income_type=="Select type of income":
            messagebox.showinfo("Error","Select income type")
        else:
            pandl.append(income_type)
            remaining+=income
            profit.append(income)
            cre_deb.append(+income)
            total.append(remaining)
            balance_label.config(text=f"Balance: ₹{remaining}")
    except Exception:
        messagebox.showinfo("Failed","Value is not added!")

def expense_happen():
    global remaining,loss
    try:
        exp_type=combo.get()
        if exp_type=="Select Expense Type":
            messagebox.showinfo("Error","Select Expense type")
        else:
            if (remaining-cexpense)<0:
                messagebox.showinfo("Don't","You not have much money to expense")
            else:
                remaining-=cexpense
                loss.append(cexpense)
                pandl.append(exp_type)
                cre_deb.append(cexpense)
                total.append(remaining)
                balance_label.config(text=f"Balance: ₹{remaining}")
    except Exception:
        messagebox.showinfo("Failed","Value is not added!")
        
def tincome():
    global income
    try:
        income=int(incomerec.get())
        income_gain()
        incomerec.delete(0,tk.END)
    except ValueError:
        messagebox.showinfo("error","The Value is ,not numeric data")
        return

def expense():
    global cexpense
    try:
        cexpense=int(expensehappen.get())
        expensehappen.delete(0,tk.END)
        expense_happen()
    except ValueError:
        messagebox.showinfo("Error","The value in not numeric data")
        return

# Fronted
root=tk.Tk()
root.title("Expense Recogniser")
root.geometry("1360x766")
# theme
style=ttk.Style()
style.theme_use("alt")
style.configure("TButton",
                background="black",
                foreground="yellow",
                padding=0,
                width=-5,
                height=0)
style.map("TButton",
            background=[("active","darkgreen")])

style.configure("Big.TLabel", font=("Arial", 30),bg="None")
style.configure("mid.TLabel", font=("Arial", 20))
style.configure("bal.TLabel",font=("Arial",14))
# Big Lable
balance_label = ttk.Label(root, text=f"Balance: ₹{remaining}",style="bal.TLabel")
balance_label.place(x=1201,y=-1)
# balance_label.config(text=f"Balance: ₹{remaining}")
introduction=ttk.Label(root,text="Don't Forget Any Penny",style="Big.TLabel",padding=20)
introduction.pack(side='top',pady=20)

# input Area
# income
lableframe1=ttk.LabelFrame(root,text="Income").place(x=10,y=185,height=130,width=365)
income_label=ttk.Label(root,text="how much money you have:",style="mid.TLabel").place(x=20,y=200)
incomerec=tk.Entry(root)
incomerec.place(x=55,y=252)
# combobox
combo1=ttk.Combobox(root)
combo1['values']=("Savings","Salary","Sundry Income","other")
combo1.set("Select type of income")
combo1.place(x=185,y=252)
submit1=ttk.Button(root,text="Submit",command=tincome).place(x=155,y=275)

# expenses
lableframe2=ttk.LabelFrame(root,text="Expense").place(x=375,y=185,height=130,width=450)
expense_lable=ttk.Label(root,text="How much you Expense this time:",style="mid.TLabel").place(x=388,y=200)
expensehappen=tk.Entry(root)
expensehappen.place(x=468,y=252)
# Combobox
combo=ttk.Combobox(root)
combo['values']=("Food","Stationary","Travel","other")
combo.set("Select Expense Type")
combo.place(x=599,y=252)
# submit button
submit2=ttk.Button(root,text="Submit",command=expense).place(x=570,y=275)

# get Data
lableframe3=ttk.LabelFrame(root,text="Data").place(x=825,y=185,height=130,width=260)
data=ttk.Label(root,text="Get Data",style="mid.TLabel").place(x=900,y=200)
get_data_button=ttk.Button(root,text="Data",command=get_data).place(x=940,y=275)

# get plan
lableframe4=ttk.LabelFrame(root,text="Plan").place(x=1085,y=185,height=130,width=260)
graph=ttk.Label(root,text="""Get Plan to save 
        money""",style="mid.TLabel").place(x=1120,y=200)
graph_Button=ttk.Button(root,text="plan",command=plan).place(x=1200,y=275)

# Text bar
lableframe5=ttk.LabelFrame(root,text="Quick Review").place(x=5,y=350,height=330,width=1350)
text=tk.Text(root,width=167,height=19)
text.place(x=10,y=363)
tk.mainloop()
