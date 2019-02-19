


class Select:

    def __init__(self):
        index = My_Gui.listbox.curselection()[0]



class Listbox:

    def __init__(self):
       self.Large = Listbox(window, height=12, width=70)
       self.Large.grid()


My_Gui.stocklistbox.delete(0, END)
                count = 0
                items_ids = backend.View.stock()
                run_time = len(items_ids)
                no_of_assigned = len(backend.View.assigned())
                for i in range(len(items_ids)):
                    chunk = items_ids[i:i:1]
                    if View.is_item_id(chunk):
                        print("Item id found! "+ chunk)
                        My_Gui.stocklistbox.insert(END, " ".join(chunk))
                        while count == 0:
                            for row in backend.Search.assigned_taken(items_ids[0][count]):
                                amount_took = int(row[3])
                                amount_total = int(row[6])
                                currently_available = amount_total - amount_took
                                information = [row[5], str(currently_available), "/", row[6], row[7], row[8]]
                                debugging = [">>>>Runtime,count,id=", str(run_time), str(count), str(items_ids)]
                                My_Gui.stocklistbox.insert(END, " ".join(information) + "   |" + " ".join(debugging))
                                count = count + 1

                if no_of_assigned <= 0:
                    My_Gui.stocklistbox.delete(0, END)
                    for row in backend.View.stock():
                        My_Gui.stocklistbox.insert(END, row)
