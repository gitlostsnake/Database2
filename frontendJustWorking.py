from tkinter import *
import backend
from tkinter import messagebox


# CONTENTS
# 1. RoadWorks functions
# 2a. Stock Buttons with commands
# 2b. Roadwork buttons with commands
# 3. Search bar
# 4a. Road work Main view window with scroll bar
# 4b. Stock Main view window with scroll bar
# 5a. DATAFIELDS AND ENTRY BOXES
# 5b. ADDITIONAL DATA
#         Length in KM, Countdown till startdate OR enddate,
#         print off paperwork function??


# 1. ROADWORKS FUNCTIONS
# Click an item in the main window and have it return its values
# to the fields below the main window for appending
class Selected(object):
    """Selected item in the list boxes"""
    @staticmethod
    def job():
        global selected_roadworks
        index = list1.curselection()[0]
        selected_roadworks = list1.get(index)
        Location_Entry.delete(0, END)
        Location_Entry.insert(END, selected_roadworks[1])
        Client_Entry.delete(0, END)
        Client_Entry.insert(END, selected_roadworks[2])
        Start_Date_Entry.delete(0, END)
        Start_Date_Entry.insert(END, selected_roadworks[3])
        End_Date_Entry.delete(0, END)
        End_Date_Entry.insert(END, selected_roadworks[4])
        return selected_roadworks

    @staticmethod
    def stock():
        global selected_item
        index = stock_list.curselection()[0]
        selected_item = stock_list.get(index)
        ITEM_STOCK_Entry.delete(0, END)
        ITEM_STOCK_Entry.insert(END, selected_item[1])
        ITEM_Amount_Entry.delete(0, END)
        ITEM_Amount_Entry.insert(END, selected_item[2])
        ITEM_Weight_Entry.delete(0, END)
        ITEM_Weight_Entry.insert(END, selected_item[3])
        ITEM_Warning_Entry.delete(0, END)
        ITEM_Warning_Entry.insert(END, selected_item[4])
        return selected_item

    @staticmethod
    def vehicle():
        global selected_vehicle
        index = VehicleList.curselection()[0]
        selected_vehicle = VehicleList.get(index)
        return selected_vehicle

    @staticmethod
    def assigned_stock():
        global selected_assigned
        index = assigned_list.curselection()[0]
        selected_assigned = assigned_list.get(index)
        return selected_assigned


class View(object):
    """View """
    @staticmethod
    def job():
        list1.delete(0, END)
        for row in backend.View.job():
            list1.insert(END, row)

    @staticmethod
    def stock():
        stock_list.delete(0, END)
        for row in backend.View.stock():
            stock_list.insert(END, row)

    @staticmethod
    def vehicles():
        VehicleList.delete(0, END)
        for row in backend.View.vehicle():
            VehicleList.insert(END, row)


# FUNCTIONS for buttons
def view_roadworks():
    # Deleting from index 0 to the end so we don't duplicate items on display
    list1.delete(0, END)
    for row in backend.view.job():
        list1.insert(END, row)  # END means every new row is added at the end


# Displays Stock items from inventory DB and displays them on seperate listbox
def view_inventory():
    stock_list.delete(0, END)
    for row in backend.view.stock():
        stock_list.insert(END, row)


def view_vehicles():
    VehicleList.delete(0, END)
    for row in backend.view.vehicle():
        VehicleList.insert(END, row)


def view_assigned():
    assigned_list.delete(0, END)
    for row in backend.assigned_view():
        assigned_list.insert(END, row)


# Currently only searches location column
def search_roadworks():
    list1.delete(0, END)
    for row in backend.search.job(search_text.get()):
        list1.insert(END, row)


#
def delete_roadworks():
    backend.delete.job(Selected.job()[0])
    list1.delete(0, END)
    for row in backend.view.job():
        list1.insert(END, row)


def delete_inventory():
    backend.Delete.stock(Selected.stock()[0])
    stock_list.delete(0, END)
    for row in backend.View.stock():
        stock_list.insert(END, row)


# Adds info in the Entry boxes to the database
def add_to_roadworks():
    backend.job_insert(Location_Text.get(), Client_Text.get(),
                       Start_Date_Text.get(), End_Date_Text.get())
    list1.delete(0, END)
    for row in backend.job_view():
        list1.insert(END, row)


def add_to_inventory():
    backend.stock_insert(ITEM_Name_Text.get(), ITEM_Amount_Text.get(),
                         ITEM_Weight_Text.get(), ITEM_Warning_Text.get())
    stock_list.delete(0, END)
    for row in backend.stock_view():
        stock_list.insert(END, row)


# Update function takes items in the entry fields and uses
# the UPDATE function from backend to edit the rows
def update_roadworks():
    backend.job_update(selected_roadworks[0], Location_Text.get(),
                       Client_Text.get(), Start_Date_Text.get(), End_Date_Text.get())
    list1.delete(0, END)
    for row in backend.job_view():
        list1.insert(END, row)


def update_inventory():
    backend.stock_update(selected_item[0], ITEM_Name_Text.get(),
                         ITEM_Amount_Text.get(), ITEM_Weight_Text.get(),
                         ITEM_Warning_Text.get())
    stock_list.delete(0, END)
    for row in backend.stock_view():
        stock_list.insert(END, row)


def message2_user():
    messagebox.showinfo("Advice", "Tough")


def howmuchtaken():
    taken_text = StringVar()
    messagebox.showinfo("Taken?", "Input coming soon")
    return assign_item_job()


def assign_item_job():
    backend.assigned_insert(Selected.stock()[0], Selected.job()[0])
    assigned_list.delete(0, END)
    for row in backend.view.assigned():
        assigned_list.insert(END, row)


def add_additional():
    backend.insert.additional(selected_roadworks[0],
                              km_text, job_type, crew_text)

# def assign_vehicle_job():
#     backend.assigned_insert


# Main
window = Tk()
window.title("DB")

# 2. BUTTONS WITH FUNCTIONS
# Inventory Buttons
view_stk_b = Button(window, text="View Stock", width=14,
                    command=View.stock)
view_stk_b.grid(row=25, column=0)

Create_Stock_Button = Button(window, text="Create Stock Entry", width=14)
Create_Stock_Button.grid(row=20, column=4)

Remove_Stock_Button = Button(window, text="Remove Stock", width=14,
                             command= delete_inventory)
Remove_Stock_Button.grid(row=27, column=0)

update_stock_button = Button(window, text="Update Stock", width=14,
                             command=update_inventory)
update_stock_button.grid(row=21, column=4)

# Road works Buttons on the right side NOW ON LEFT
view_wrks_b = Button(window, text="View Road Works", width=14,
                     command=view_roadworks)
view_wrks_b.grid(row=4, column=0)

Delete_Roadworks_Button = Button(window, text="Del Road Works", width=14,
                                 command=delete_roadworks)
Delete_Roadworks_Button.grid(row=6, column=0)

Create_Roadworks_Button = Button(window, text="Create Job Entry", width=14,
                                 command=add_to_roadworks)
Create_Roadworks_Button.grid(row=17, column=4)

Print_Out_Button = Button(window, text="Print Details", width=14)
Print_Out_Button.grid(row=15, column=0)

# PLUS Data Update using the same boxes as add to database.
Update_RDatabaseButton = Button(window, text="Update Job", width=14,
                                command=update_roadworks)
Update_RDatabaseButton.grid(row=18, column=4)

# Vehicle Buttons
ViewVehicles_Button = Button(window, text="View Vehicles", width=14,
                             command=view_vehicles)
ViewVehicles_Button.grid(row=41, column=0)

# This button will be used for adding inventory items to the road works
# using start date and end date you can give a stock forcast to see what
# inventory will look like 5 months from now and when your going to struggle
# CREATE TABLE in ROADWORKS selected_Roadworks[] + selected_item[]
assign_vehicle_button = Button(window, text="Assign Vehicle", width=14)
assign_vehicle_button.grid(row=13, column=0)

assign_stock_button = Button(window, text="Assign Stock", width=14,
                             command=howmuchtaken)
assign_stock_button.grid(row=14, column=0)

# 3. SEARCH BAR
# Search bar at the top with an entry box to type into
# search_label = Label(window, text= "")
# search_label.grid(row=0, column=1)

search_text = StringVar()
e1 = Entry(window, textvariable=search_text)
e1.grid(row=0, column=1)

search_button = Button(window, text="Search", width=8,
                       command=search_roadworks)
search_button.grid(row=0, column=2)

#   4a. MAIN BOX FOR ROADWORKS WITH SCROLL BAR
# Main view box listing items with scroll bar
list1 = Listbox(window, height=12, width=70)
list1.grid(row=1, column=1, rowspan=15, columnspan=15)

sb1 = Scrollbar(window)
# sb1.grid(row=3, column=16, rowspan=4)

list1.bind('<<ListboxSelect>>', Selected.job)

# scroll set to sb1
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

#   4b. MAIN BOX FOR ASSIGNED ITEMS
assigned_label = Label(window, text="Assigned")
assigned_label.grid(row=0, column=18)

assigned_list = Listbox(window, height=12, width=30)
assigned_list.grid(row=1, column=18, rowspan=15, columnspan=7)

assigned_list.bind('<<ListboxSelect>>', Selected.assigned_stock)

#   4c. MAIN BOX FOR STOCK ITEMS
Stock_list_label = Label(window, text="")
Stock_list_label.grid(row=22, column=2)

stock_list = Listbox(window, height=5, width=70)
stock_list.grid(row=23, column=1, rowspan=15, columnspan=15)

spacer_label = Label(window, text="")
spacer_label.grid(row=40, column=0)

sb2 = Scrollbar(window)
# sb2.grid(row=25, column=16, rowspan=4)

stock_list.configure(yscrollcommand=sb2.set)
sb2.configure(command=stock_list.yview)

stock_list.bind('<<ListboxSelect>>', Selected.stock)

#   4d. MAIN BOX FOR VEHICLES
VehicleList = Listbox(window, height=5, width=70)
VehicleList.grid(row=41, column=1, rowspan=15, columnspan=15)

VehicleList.bind('<<ListboxSelect>>', Selected.vehicle)

#   4e. MAIN BOX FOR PERSONEL
# personel_label = Label(window, text="Personel")
# personel_label.grid(row=25, column=18)

# personel_list = Listbox(window, height=12, width=30)
# personel_list.grid(row=26, column=18, rowspan=15, columnspan=7)

#   5a. DATA AND ENTRY BOXES
# data entry to use add roadworks using labels instead of buttons
# so we can rig all of them up to the "Add to database" button
HEYlisten_ADD = Label(window, text="""
                        Fill in the fields, press Create for a new entry""")
HEYlisten_ADD.grid(row=16, column=0, columnspan=4)

Location_Text = StringVar()

Location_Label = Label(window, text="Location")
Location_Label.grid(row=17, column=0)
Location_Entry = Entry(window, textvariable=Location_Text)
Location_Entry.grid(row=17, column=1)

Client_Text = StringVar()

Client_Label = Label(window, text="Client")
Client_Label.grid(row=18, column=0)
Client_Entry = Entry(window, textvariable=Client_Text)
Client_Entry.grid(row=18, column=1)

Start_Date_Text = StringVar()

Start_Date_Label = Label(window, text="Start Date \nYY-MM-DD 00:00")
Start_Date_Label.grid(row=17, column=2)
Start_Date_Entry = Entry(window, textvariable=Start_Date_Text)
Start_Date_Entry.grid(row=17, column=3)

End_Date_Text = StringVar()

End_Date_Label = Label(window, text="End Date \nYY-MM-DD 00:00")
End_Date_Label.grid(row=18, column=2)
End_Date_Entry = Entry(window, textvariable=End_Date_Text)
End_Date_Entry.grid(row=18, column=3)

# Info for the user to edit or create new entry in the database
hey_listen = Label(window, text="""
                           Or press the Update button to change info""")
hey_listen.grid(row=19, column=0, columnspan=4)

Help_Button = Button(window, text="Need help?", width=14,
                     command=message2_user)
Help_Button.grid(row=57, column=19)

# STOCK ENTRY
ITEM_Name_Text = StringVar()

ITEM_Name_Label = Label(window, text="Stock item\nname")
ITEM_Name_Label.grid(row=20, column=0)
ITEM_STOCK_Entry = Entry(window, textvariable=ITEM_Name_Text)
ITEM_STOCK_Entry.grid(row=20, column=1)

ITEM_Amount_Text = StringVar()

ITEM_Amount_Label = Label(window, text="Amount")
ITEM_Amount_Label.grid(row=21, column=0)
ITEM_Amount_Entry = Entry(window, textvariable=ITEM_Amount_Text)
ITEM_Amount_Entry.grid(row=21, column=1)

ITEM_Weight_Text = StringVar()

ITEM_Weight_Label = Label(window, text="Weight")
ITEM_Weight_Label.grid(row=20, column=2)
ITEM_Weight_Entry = Entry(window, textvariable=ITEM_Weight_Text)
ITEM_Weight_Entry.grid(row=20, column=3)

ITEM_Warning_Text = StringVar()

ITEM_Warning_Label = Label(window, text="Warning %")
ITEM_Warning_Label.grid(row=21, column=2)
ITEM_Warning_Entry = Entry(window, textvariable=ITEM_Warning_Text)
ITEM_Warning_Entry.grid(row=21, column=3)
# Stock interface section will be merged into the main window alongside
# The roadworks interface.. but for ease of reading I will have it seperated
# In the code.

# 5b. ADDITIONAL DATA
#         Length in KM, Countdown till startdate OR enddate,
#         print off paperwork function??
# Additional_Data = Label(window, text="ADDITIONAL DATA")
# Additional_Data.grid(row = 20, column = 2)


Additional_data_label = Label(window, text="Additional\nData")
Additional_data_label.grid(row=16, column=19)

km_text = StringVar()
km_label = Label(window, text="Km")
km_label.grid(row=17, column=18)
km_entry = Entry(window, textvariable=km_text)
km_entry.grid(row=17, column=19)

job_type_label = Label(window, text="Type")
job_type_label.grid(row=18, column=18)

job_type_choices = {'Temporary', 'Static', 'Traffic Control', 'Other'}
job_type = StringVar()
job_type.set('Temporary')
job_choice_popup = OptionMenu(window, job_type, *job_type_choices)
job_choice_popup.grid(row=18, column=19)

# job_type_entry = Entry(window, textvariable=job_type_text)
# job_type_entry.grid(row=18, column=19)


crew_text = StringVar()
crew_label = Label(window, text="Crew Size")
crew_label.grid(row=19, column=18)
crew_entry = Entry(window, textvariable=crew_text)
crew_entry.grid(row=19, column=19)

update_additonal_button = Button(window, text="Update Additional",
                                 width=14)
update_additonal_button.grid(row=20, column=19)
# Length_KM = Label(window, text="Length(km)")
# Length_KM.grid(row = 21, column = 0)

# Traffic_lights_required = Label(window, text="Traffic lights?")
# Traffic_lights_required.grid(row = 21, column = 2)

created_by_label = Label(window, text="+")
created_by_label.grid(row=57, column=0)


View.job()
View.stock()
View.vehicles()
window.mainloop()
