# Pydatabase

# TM database built in python

This programs main goal is to create a database of road works for a traffic management company and to keep track of stock being used.

1. database for road works (set up completed)
      ~ info taken
      ~ Location {stored as text ATM}, Client, Start Date, End Date
  
2. database for all items currently in stock (Set up completed)
      ~ info needed for database
      ~ Item Name, Item amount, Warning level(ie 15% send a warning text), {optional} weight. 
 
3. Expand the database for road works to take more info such as
      ~ Length in Km {used to calculate cones needed}, 
      ~ Static or Temporary by nature {Doubled at 18m and lamped at 18m cone spacing 9m},
      ~ Breaks in the mainline {How many slip roads will the job cover? This will require attention}
      ~ Cost per day {Optional}
      ~ Hwm Men required 
      ~ Total average workmen including 3rd parties. {Optional}
      
4. Make calculations with the information collected by the database
      ~ Count down to time left on a job and send out reminders/warnings
      ~ Job percentage completed on time NO delays
      ~ Job cancelations and reasons why
      
5. When adding a new job to the database it will ask for the information required to calculate approx item useage.
 
 
