from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
from collections import deque


class PriorityQueue:

    def __init__(self):
        self.queue = list()

    def is_empty(self):
        return self.size() == 0

    def enqueue(self, node):
        print(node)
        if not self.is_empty():
            self.queue.append(node)
        else:
            for x in range(0, self.size()):
                if node.priority >= self.queue[x].priority:
                    if x == (self.size() - 1):
                        self.queue.enqueue(x + 1, node)
                    else:
                        continue
                else:
                    self.queue.enqueue(x, node)
                    return True

    def dequeue(self):
        return self.queue.pop(0)

    def print(self):
        for x in self.queue:
            print(str(x.priority))

    def size(self):
        return len(self.queue)


class LinkedList:
    def __init__(self, max_size=10):
        self.head = -1
        self.next = +1
        self.max_size = max_size
        self.items = ["" for x in range(max_size)]

    def is_full(self):
        return self.head == self.max_size - 1

    def is_empty(self):
        return self.head == - 1

    def insert(self, item):
        if not self.is_full():
            self.head = self.head + self.next
            self.items[self.head] = item

    def remove(self, item):
        if not self.is_full():
            if item in self.items:
                self.items[item] = ""

    def size(self):
        return self.head + 1

    def print(self):
        if self.is_empty():
            raise LinkedList
        else:
            return "\n".join(self.items) + "\n"


class Staff:
    def __init__(self, priority, lastName, firstName, role, event):
        self.lastName = lastName
        self.firstName = firstName
        self.role = role
        self.event = event
        self.priority = priority


class Event:
    def __init__(self, name, location, date, staffRequired):
        self.name = name
        self.location = location
        self.date = date
        self.staffRequired = staffRequired

    def __str__(self):
        return f'{self.name}'


# declare

priorityCount = 0
staffList = PriorityQueue()
eventList = LinkedList()
eventListForDropdown = []
base = Event("Shop Shift", "Retail Location", "Monday-Friday", "2")
eventListForDropdown.append(base)
eventList.insert(base)


def submitStaff():
    global priorityCount
    priorityCount = priorityCount + 1
    priority = priorityCount
    first_name = firstname.get()
    print(str(first_name))  # test
    last_name = lastname.get()
    role = roleclicked.get()
    event = eventclicked.get()
    print(str(event))
    s = Staff(priority, first_name, last_name, role, event)
    print(str(priority))
    staffList.enqueue(s)


def submitEvent():
    global eventListForDropdown

    event_name = eventName.get()
    print(str(event_name))  # test
    location = eventLocation.get()
    date = eventDate.get()
    staff = staffreq.get()
    e = Event(event_name, location, date, staff)
    eventListForDropdown.append(e)  # LinkedLists are not able to be used in dropdowns, so there is a separate list
    eventList.insert(e)
    print(str(eventListForDropdown))


def refresh1():
    global drop2
    drop2.destroy()
    # events dropdown
    # Create Dropdown menu
    drop2 = OptionMenu(tab1, eventclicked, *eventListForDropdown)
    drop2.grid(row=1, column=2)


def refresh2():
    global drop3
    drop3.destroy()
    # events dropdown
    # Create Dropdown menu
    drop3 = OptionMenu(tab3, eventclicked2, *eventListForDropdown)
    drop3.grid(row=1, column=2)


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        return arr


def generateReport():
    sortedStaffList = []
    sortedStaffList = insertionSort(staffList.queue)
    for x in sortedStaffList:
        print(x)


main = Tk()
main.title("Staffing Application")
main.geometry("500x400")

tabControl = ttk.Notebook(main)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Event Sign Up')
tabControl.add(tab2, text='Event Creation')
tabControl.add(tab3, text='View Event Reports')
tabControl.pack(expand=1, fill="both")

# Staff Gui
elabel = Label(tab1, text="Event: ")
elabel.grid(row=1, column=1)

flabel = Label(tab1, text="First Name: ")
flabel.grid(row=2, column=1)

llabel = Label(tab1, text="Last Name: ")
llabel.grid(row=3, column=1)

rlabel = Label(tab1, text="Role: ")
rlabel.grid(row=4, column=1)

firstname = Entry(tab1, width=30)
firstname.grid(row=2, column=2)

lastname = Entry(tab1, width=30)
lastname.grid(row=3, column=2)

staff_btn = Button(tab1, text="Sign Up", command=lambda: submitStaff())
staff_btn.grid(row=5, column=2)

refresh_button = Button(tab1, text="Refresh", command=lambda: refresh1())
refresh_button.grid(row=1, column=3)

# Role dropdown menu options
roles = [
    "None",
    "Employee",
    "Shift Lead",
    "Manager",
]

# roles dropdown
# datatype of menu text
roleclicked = StringVar(tab1)
# initialize menu text to none
roleclicked.set(roles[0])
# Create Dropdown menu
drop = OptionMenu(tab1, roleclicked, *roles)
drop.grid(row=4, column=2)

# events dropdown
# datatype of menu text
eventclicked = StringVar(tab1)
# initialize menu text to none
eventclicked.set("None Selected")
# Create Dropdown menu
drop2 = OptionMenu(tab1, eventclicked, *eventListForDropdown)
drop2.grid(row=1, column=2)

# Event Gui
enlabel = Label(tab2, text="Event Name: ")
enlabel.grid(row=2, column=1)

loclabel = Label(tab2, text="Location: ")
loclabel.grid(row=3, column=1)

dlabel = Label(tab2, text="Date: ")
dlabel.grid(row=4, column=1)

srlabel = Label(tab2, text="Staff Required: ")
srlabel.grid(row=5, column=1)

eventName = Entry(tab2, width=30)
eventName.grid(row=2, column=2)

eventLocation = Entry(tab2, width=30)
eventLocation.grid(row=3, column=2)

eventDate = Entry(tab2, width=10)
eventDate.grid(row=4, column=2)

staffreq = Entry(tab2, width=3)
staffreq.grid(row=5, column=2)

event_btn = Button(tab2, text="Create Event", command=lambda: submitEvent())
event_btn.grid(row=6, column=2)

# Event Generation GUI
# events dropdown
# datatype of menu text
eventclicked2 = StringVar(tab3)
# initialize menu text to none
eventclicked2.set("None Selected")
# Create Dropdown menu
drop3 = OptionMenu(tab3, eventclicked2, *eventListForDropdown)
drop3.grid(row=1, column=2)

evlabel = Label(tab3, text="Select Event to Generate Report: ")
evlabel.grid(row=1, column=1)

refresh_button = Button(tab3, text="Refresh", command=lambda: refresh2())
refresh_button.grid(row=1, column=3)

report_btn = Button(tab3, text="Generate Event Report", command=lambda: generateReport())
report_btn.grid(row=2, column=2)

evName = Label(tab3, text="Event Name: ")
evName.grid(row=3, column=1)

evLocation = Label(tab3, text="Event Location: ")
evLocation.grid(row=4, column=1)

evDate = Label(tab3, text="Event Date: ")
evDate.grid(row=5, column=1)

eventstaffreq = Label(tab3, text="Staff Required: ")
eventstaffreq.grid(row=6, column=1)

staffhired = Label(tab3, text="Staff Scheduled: ")
staffhired.grid(row=7, column=1)

staffwait = Label(tab3, text="Staff Waitlisted: ")
staffwait.grid(row=8, column=1)

evNameResult = Label(tab3, text="Waiting...")
evNameResult.grid(row=3, column=2)

evLocationResult = Label(tab3, text="Waiting...")
evLocationResult.grid(row=4, column=2)

evDateResult = Label(tab3, text="Waiting...")
evDateResult.grid(row=5, column=2)

eventstaffreqResult = Label(tab3, text="Waiting...")
eventstaffreqResult.grid(row=6, column=2)

staffhiredResult = Label(tab3, text="Waiting...")
staffhiredResult.grid(row=7, column=2)

staffwaitResult = Label(tab3, text="Waiting...")
staffwaitResult.grid(row=8, column=2)

main.mainloop()
