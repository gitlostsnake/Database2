from tkinter import *
import backend


class GUI:
    """Tkinter"""

    def __init__(self, master):
        self.master = master
        master.title("TM database")

        class Selected(object):
            """Selected item in the list boxes"""

            @staticmethod
            def job():
                global selected_roadworks
                index = joblistbox.curselection()[0]
                selected_roadworks = joblistbox.get(index)
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
                index = stocklistbox.curselection()[0]
                selected_item = stocklistbox.get(index)
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
                index = vehiclelistbox.curselection()[0]
                selected_vehicle = vehiclelistbox.get(index)
                return selected_vehicle

            @staticmethod
            def assigned_stock():
                global selected_assigned
                index = assignedlistbox.curselection()[0]
                selected_assigned = assignedlistbox.get(index)
                return selected_assigned

        class View(object):
            """View """

            @staticmethod
            def job():
                joblistbox.delete(0, END)
                for row in backend.View.job():
                    joblistbox.insert(END, row)

            @staticmethod
            def stock():
                stocklistbox.delete(0, END)
                for row in backend.View.stock():
                    stocklistbox.insert(END, row)

            @staticmethod
            def vehicles():
                vehiclelistbox.delete(0, END)
                for row in backend.View.vehicle():
                    vehiclelistbox.insert(END, row)

            @staticmethod
            def assigned():
                assignedlistbox.delete(0, END)
                for row in backend.View.assigned():
                    assignedlistbox.insert(END, row)

        def job_search_bar():
            joblistbox.delete(0, END)
            for row in backend.Search.job(search_text.get()):
                joblistbox.inbsert(END, row)

        class Delete(object):
            """Delete job, stock or vehicle."""

            @staticmethod
            def job():
                backend.Delete.job(Selected.job()[0])
                joblistbox.delete(0, END)
                for row in backend.View.job():
                    joblistbox.insert(END, row)

            @staticmethod
            def stock():
                backend.Delete.stock(Selected.stock()[0])
                stocklistbox.delete(0, END)
                for row in backend.View.stock():
                    stocklistbox.insert(END, row)

            @staticmethod
            def vehicle():
                backend.Delete.vehicle(Selected.vehicle()[0])
                vehiclelistbox.delete(0, END)
                for row in backend.View.vehicle():
                    vehiclelistbox.insert(END, row)

        class InsertEntry(object):

            @staticmethod
            def job():
                backend.Insert.job(location_text.get(), client_text.get(),
                                   startdate_text.get(), enddate_text.get())
                joblistbox.delete(0, END)
                for row in backend.View.job():
                    joblistbox.insert(END, row)

            @staticmethod
            def stock():
                backend.Insert.stock(itemname_text.get(), itemamount_text.get(),
                                     itemweight_text.get(), itemwarning_text.get())
                stocklistbox.delete(0, END)
                for row in backend.View.stock():
                    stocklistbox.insert(END, row)

            @staticmethod
            def additional():
                pass

        class Update(object):

            @staticmethod
            def job():
                backend.Update.job(Selected.job()[0], location_text.get(),
                                   client_text.get(), startdate_text.get(),
                                   enddate_text.get())
                joblistbox.delete(0, END)
                for row in backend.View.job():
                    joblistbox.insert(END, row)

            @staticmethod
            def stock():
                backend.Update.stock(Selected.stock()[0], itemname_text.get(),
                                     itemamount_text.get(), itemweight_text.get(),
                                     itemwarning_text.get())
                stocklistbox.delete(0, END)
                for row in backend.View.stock():
                    stocklistbox.insert(END, row)

        class Assign(object):

            @staticmethod
            def stock():
                backend.Insert.assigned(Selected.stock()[0], Selected.job()[0])
                assignedlistbox.delete(0, END)
                for row in backend.View.assigned():
                    assignedlistbox.insert(END, row)

            @staticmethod
            def vehicle():
                pass

            @staticmethod
            def person():
                pass

        """Main Job buttons"""
        self.view_job = Button(window, text="View Job", width=14,
                               command=View.job)
        self.view_job.grid(row=4, column=0)

        self.delete_job = Button(window, text= "Delete Job", width= 14,
                                 command=Delete.job)

        """Main Stock buttons"""
        self.view_stock = Button(window, text="View Stock", width=14,
                                 command=View.stock)
        self.view_stock.grid(row=25, column=0)

        self.remove_stock = Button(window, text="Remove Stock", width=14,
                                   command=Delete.stock)
        self.remove_stock.grid(row=27, column=0)

        """List boxes"""
        """Job"""
        self.joblistbox = Listbox(window, height=12, width=70)
        self.joblistbox.grid(row=1, column=1, rowspan=15, columnspan=15)

        self.job_scrollbar = Scrollbar(window)
        self.job_scrollbar.configure(command=self.joblistbox.yview)

        self.joblistbox.configure(yscrollcommand=self.job_scrollbar.set)
        self.joblistbox.bind('<<ListboxSelect>>', Selected.job)

        """Assigned"""
        self.assigned_label = Label(window, text="Assigned Stock")
        self.assigned_label.grid(row=0, column=18)

        self.assignedlistbox = Listbox(window, height=12, width=30)
        self.assignedlistbox.grid(row=1, column=18, rowspan=15, columnspan=7)

        self.assignedlistbox.bind('<<ListboxSelect>>', Selected.assigned_stock)

        """Stock"""
        self.stock_label = Label(window, text="")
        self.stock_label.grid(row=22, column=2)

        self.stocklistbox = Listbox(window, height=5, width=70)
        self.stocklistbox.grid(row=23, column=1, rowspan=15, columnspan=15)

        self.spacer_label = Label(window, text="")
        self.spacer_label.grid(row=40, column=0)

        self.stock_scrollbar = Scrollbar(window)
        self.stocklistbox.configure(yscrollcommand=self.stock_scrollbar.set)
        self.stock_scrollbar.configure(command=self.stocklistbox.yview)

        self.stocklistbox.bind('<<ListboxSelect>>', Selected.stock)

        """Vehicles"""
        self.vehiclelistbox = Listbox(window, height=5, width=70)
        self.vehiclelistbox.grid(row=41, column=1, rowspan=15, columnspan=15)

        self.vehiclelistbox.bind('<<ListboxSelect>>', Selected.vehicle)

        """Entry Mid section"""
        """Job Entry Fields"""

        self.help = Label(window, text="""
                            Fill in the fields, press Create for a new entry""")
        self.help.grid(row=16, column=0, columnspan=4)

        self.location_label = Label(window, text="Location")
        self.location_label.grid(row=17, column=0)
        self.location_text = StringVar()
        self.location_entry = Entry(window, textvariable=self.location_text)
        self.location_entry.grid(row=17, column=1)

        self.client_label = Label(window, text="Client")
        self.client_label.grid(row=18, column=0)
        self.client_text = StringVar()
        self.client_entry = Entry(window, textvariable=self.client_text)
        self.client_entry.grid(row=18, column=1)

        self.startdate_label = Label(window, text="Start Date \nYYYY-MM-DD 00:00")
        self.startdate_label.grid(row=18, column=2)
        self.startdate_text = StringVar()
        self.startdate_entry = Entry(window, textvariable=self.startdate_text)
        self.startdate_entry.grid(row=18, column=3)

        self.enddate_label = Label(window, text="End Date \nYYYY-MM-DD 00:00")
        self.enddate_label.grid(row=18, column=2)
        self.enddate_text = StringVar()
        self.enddate_entry = Entry(window, textvariable=self.enddate_text)
        self.enddate_entry.grid(row=18, column=3)

        """Stock Entry Fields"""

        self.help2 = Label(window, text="""
                            Or press the Update button to change info
                            """)
        self.help2.grid(row=19, column=2)

        self.stockname_label = Label(window, text="Stock name")
        self.stockname_label.grid(row=20, column=0)
        self.stockname_text = StringVar()
        self.stockname_entry = Entry(window, textvariable=self.stockname_text)
        self.stockname_entry.grid(row=20, column=1)

        self.stockamount_label = Label(window, text="Amount")
        self.stockamount_label.grid(row=21, column=0)
        self.stockamount_text = StringVar()
        self.stockname_entry = Entry(window, textvariable=self.stockamount_text)
        self.stockname_entry.grid(row=21, column=1)

        self.stockweight_label = Label(window, text="Weight kg")
        self.stockweight_label.grid(row=20, column=2)
        self.stockweight_text = StringVar()
        self.stockweight_entry = Entry(window, textvariable=self.stockweight_text)
        self.stockweight_entry.grid(row=20, column=3)

        self.stockwarning_label = Label(window, text="Warning %")
        self.stockwarning_label.grid(row=21, column=2)
        self.stockwarning_text = StringVar
        self.stockwarning_entry = Entry(window, textvariable=self.stockwarning_text)
        self.stockwarning_entry.grid(row=21, column=3)

        """Additional Entry section"""

        self.additional_label = Label(window, text="Additional \nData")
        self.additional_label.grid(row=16, column=19)

        self.joblength_label = Label(window, text="km")
        self.joblength_label.grid(row=17, column=18)
        self.joblength_text = StringVar()
        self.joblength_entry = Entry(window, textvariable=self.joblength_text)
        self.joblength_entry.grid(row=17, column=19)

        self.additional_types_label = Label(window, text="Type")
        self.additional_types_label.grid(row=18, column=18)
        self.additional_types = {'Temporary', 'Static', 'Traffic Control', 'Other'}
        self.jobtype_text = StringVar()
        self.jobtype_text.set('Temporary')
        self.jobtype_dropdown = OptionMenu(window, self.jobtype_text,
                                            *self.additional_types)
        self.jobtype_dropdown.grid(row=18, column=19)

        self.crewrequired_label = Label(window, text="Crew Size")
        self.crewrequired_label.grid(row=19, column=18)
        self.crewrequired_text = StringVar()
        self.crewrequired_entry = Entry(window, textvariable=self.crewrequired_text)
        self.crewrequired_entry.grid(row=19, column=19)

        self.update_additional_button = Button(window, text="Update Additional",
                                               width=14)
        self.update_additional_button.grid(row=20, column=19)


window = Tk()
My_Gui = GUI(window)
window.mainloop()
