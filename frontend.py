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
            def job(*args):
                global selected_roadworks
                index = My_Gui.joblistbox.curselection()[0]
                selected_roadworks = My_Gui.joblistbox.get(index)
                My_Gui.location_entry.delete(0, END)
                My_Gui.location_entry.insert(END, selected_roadworks[1])
                My_Gui.client_entry.delete(0, END)
                My_Gui.client_entry.insert(END, selected_roadworks[2])
                My_Gui.startdate_entry.delete(0, END)
                My_Gui.startdate_entry.insert(END, selected_roadworks[3])
                My_Gui.enddate_entry.delete(0, END)
                My_Gui.enddate_entry.insert(END, selected_roadworks[4])
                return selected_roadworks

            @staticmethod
            def stock(*args):
                global selected_item
                index = My_Gui.stocklistbox.curselection()[0]
                selected_item = My_Gui.stocklistbox.get(index)
                My_Gui.stockname_entry.delete(0, END)
                My_Gui.stockname_entry.insert(END, selected_item[1])
                My_Gui.stockname_entry.delete(0, END)
                My_Gui.stockname_entry.insert(END, selected_item[2])
                My_Gui.stockweight_entry.delete(0, END)
                My_Gui.stockweight_entry.insert(END, selected_item[3])
                My_Gui.stockwarning_entry.delete(0, END)
                My_Gui.stockwarning_entry.insert(END, selected_item[4])
                return selected_item

            @staticmethod
            def vehicle(*args):
                global selected_vehicle
                index = My_Gui.vehiclelistbox.curselection()[0]
                selected_vehicle = My_Gui.vehiclelistbox.get(index)
                return selected_vehicle

            @staticmethod
            def assigned_stock(*args):
                global selected_assigned
                index = My_Gui.assignedlistbox.curselection()[0]
                selected_assigned = My_Gui.assignedlistbox.get(index)
                return selected_assigned

        class View(object):
            """View """

            @staticmethod
            def job():
                My_Gui.joblistbox.delete(0, END)
                for row in backend.View.job():
                    My_Gui.joblistbox.insert(END, row)

            @staticmethod
            def stock():
                My_Gui.stocklistbox.delete(0, END)
                for row in backend.View.stock():
                    My_Gui.stocklistbox.insert(END, row)

            @staticmethod
            def vehicles():
                My_Gui.vehiclelistbox.delete(0, END)
                for row in backend.View.vehicle():
                    My_Gui.vehiclelistbox.insert(END, row)

            @staticmethod
            def assigned():
                My_Gui.assignedlistbox.delete(0, END)
                for row in backend.View.assigned():
                    My_Gui.assignedlistbox.insert(END, row)

        def job_search_bar():
            My_Gui.joblistbox.delete(0, END)
            for row in backend.Search.job(search_text.get()):
                My_Gui.joblistbox.insert(END, row)

        class Delete(object):
            """Delete job, stock or vehicle."""

            @staticmethod
            def job():
                backend.Delete.job(Selected.job()[0])
                My_Gui.joblistbox.delete(0, END)
                for row in backend.View.job():
                    My_Gui.joblistbox.insert(END, row)

            @staticmethod
            def stock():
                backend.Delete.stock(Selected.stock()[0])
                My_Gui.stocklistbox.delete(0, END)
                for row in backend.View.stock():
                    My_Gui.stocklistbox.insert(END, row)

            @staticmethod
            def vehicle():
                backend.Delete.vehicle(Selected.vehicle()[0])
                vehiclelistbox.delete(0, END)
                for row in backend.View.vehicle():
                    vehiclelistbox.insert(END, row)

        class InsertEntry(object):

            @staticmethod
            def job():
                backend.Insert.job(My_Gui.location_text.get(), My_Gui.client_text.get(),
                                   My_Gui.startdate_text.get(), My_Gui.enddate_text.get())
                My_Gui.joblistbox.delete(0, END)
                for row in backend.View.job():
                    My_Gui.joblistbox.insert(END, row)

            @staticmethod
            def stock():
                backend.stock_insert(My_Gui.stockname_text.get(), My_Gui.stockamount_text.get(),
                                    My_Gui.stockweight_text.get(), My_Gui.stockwarning_text.get())
                My_Gui.stocklistbox.delete(0, END)
                for row in backend.View.stock():
                    My_Gui.stocklistbox.insert(END, row)

            def stocktest():
                def add_to_inventory():
                    backend.stock_insert(ITEM_Name_Text.get(), ITEM_Amount_Text.get(),
                                         ITEM_Weight_Text.get(), ITEM_Warning_Text.get())
                    stock_list.delete(0, END)
                    for row in backend.stock_view():
                        stock_list.insert(END, row)

            @staticmethod
            def additional():
                pass

        class Update(object):

            @staticmethod
            def job():
                backend.Update.job(Selected.job(), My_Gui.location_text.get(),
                                   My_Gui.client_text.get(), My_Gui.startdate_text.get(),
                                   My_Gui.enddate_text.get())
                My_Gui.joblistbox.delete(0, END)
                for row in backend.View.job():
                    My_Gui.joblistbox.insert(END, row)

            @staticmethod
            def stock():
                backend.Update.stock(Selected.stock()[0], My_Gui.itemname_text.get(),
                                     My_Gui.itemamount_text.get(), My_Gui.itemweight_text.get(),
                                     My_Gui.itemwarning_text.get())
                My_Gui.stocklistbox.delete(0, END)
                for row in backend.View.stock():
                    My_Gui.stocklistbox.insert(END, row)

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
        self.view_job = Button(window, text="View Job", width=12,
                               command=View.job)
        self.view_job.grid(row=4, column=0)

        self.delete_job = Button(window, text= "Delete Job", width= 12,
                                 command=Delete.job)
        self.delete_job.grid(row=5, column=0)

        self.insert_job = Button(window, text="Create Job", width=12,
                                command=InsertEntry.job)
        self.insert_job.grid(row=17, column=4)

        self.update_job = Button(window, text="Update Job", width=12,
                                command=Update.job)
        self.update_job.grid(row=18, column=4)

        """Main Stock buttons"""
        self.view_stock = Button(window, text="View Stock", width=12,
                                 command=View.stock)
        self.view_stock.grid(row=25, column=0)

        self.remove_stock = Button(window, text="Remove Stock", width=12,
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
        self.startdate_label.grid(row=17, column=2)
        self.startdate_text = StringVar()
        self.startdate_entry = Entry(window, textvariable=self.startdate_text)
        self.startdate_entry.grid(row=17, column=3)

        self.enddate_label = Label(window, text="End Date \nYYYY-MM-DD 00:00")
        self.enddate_label.grid(row=18, column=2)
        self.enddate_text = StringVar()
        self.enddate_entry = Entry(window, textvariable=self.enddate_text)
        self.enddate_entry.grid(row=18, column=3)

        """Stock Entry Fields"""

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
        self.stockwarning_text = StringVar()
        self.stockwarning_entry = Entry(window, textvariable=self.stockwarning_text)
        self.stockwarning_entry.grid(row=21, column=3)

        """Stock Entry buttons"""

        self.create_stock = Button(window, text="Create Stock", width=12,
                                        command=InsertEntry.stock)
        self.create_stock.grid(row=20, column=4)

        self.update_stock = Button(window, text="Update Stock", width=12,
                                        command=Update.stock)
        self.update_stock.grid(row=21, column=4)


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
                                               width=16)
        self.update_additional_button.grid(row=20, column=19)


window = Tk()
My_Gui = GUI(window)
window.mainloop()
