from tkinter import *

global result


def run_gui():
    # Function to set focus (cursor)

    # Function to set focus
    def focus2(event):
        # Age: The citizen age
        age_field.focus_set()

    # Function to set focus
    def focus3(event):
        # Working condition: The citizen working condition (Private / StateGovernment / SelfEmployedNotIncluded etc...)
        WorkCond_field.focus_set()

    # Function to set focus
    def focus5(event):
        # Education: Where the citizen learning right now
        educ_field.focus_set()

    # Function to set focus
    def focus6(event):
        # YearsOfEducation: How many years of education the citizen have
        YearsOfEducation_field.focus_set()

    def focus7(event):
        # MaritalStatus: The citizen relationship status
        MaritalStatus_field.focus_set()

    def focus8(event):
        # Occupation: The citizen job
        Occupation_field.focus_set()

    def focus9(event):
        # Relationship: The citizen family relationship
        Relationship_field.focus_set()

    def focus11(event):
        # Gender: the citizen gender
        Gender_field.focus_set()

    def focus12(event):
        # InvestmentGains: The citizen gains from investments
        InvestmentGains_field.focus_set()

    def focus13(event):
        # InvestmentLosses: The citizen losses from investments
        InvestmentLosses_field.focus_set()

    def focus14(event):
        # WeeklyWorkHours: The citizen weekly work hours
        WeeklyWorkHours_field.focus_set()

    def focus15(event):
        # CountryOfOrigin: Where the citizen is born
        CountryOfOrigin_field.focus_set()

    def focus16(event):
        # MonthlyIncome: Does the citizen have monthly income or not
        MonthlyIncome_field.focus_set()

    # Function for clearing the
    # contents of text entry boxes
    def clear():
        # clear the content of text entry box
        id_field.delete(0, END)
        age_field.delete(0, END)
        WorkCond_field.delete(0, END)
        educ_field.delete(0, END)
        YearsOfEducation_field.delete(0, END)
        MaritalStatus_field.delete(0, END)
        Occupation_field.delete(0, END)
        Relationship_field.delete(0, END)
        Gender_field.delete(0, END)
        InvestmentGains_field.delete(0, END)
        InvestmentLosses_field.delete(0, END)
        WeeklyWorkHours_field.delete(0, END)
        CountryOfOrigin_field.delete(0, END)
        MonthlyIncome_field.delete(0, END)

        # MonthlyIncome_field
        # CountryOfOrigin_field
        # WeeklyWorkHours_field
        # InvestmentLosses_field
        # InvestmentGains_field
        # Gender_field
        # Relationship_field
        # Occupation_field
        # MaritalStatus_field
        # YearsOfEducation_field
        # educ_field
        # WorkCond_field
        # age_field
        # id_field

    # Function to take data from GUI

    def validate_that_all_entries_filled():
        print(MonthlyIncome_field.get())
        print(CountryOfOrigin_field.get())
        print(WeeklyWorkHours_field.get())
        print(InvestmentLosses_field.get())
        print(InvestmentGains_field.get())
        print(Gender_field.get())
        print(Relationship_field.get())
        print(Occupation_field.get())
        print(MaritalStatus_field.get())
        print(YearsOfEducation_field.get())
        print(educ_field.get())
        print(WorkCond_field.get())
        print(age_field.get())
        print(id_field.get())

        return (MonthlyIncome_field.get() == "" or
                CountryOfOrigin_field.get() == "" or
                WeeklyWorkHours_field.get() == "" or
                InvestmentLosses_field.get() == "" or
                InvestmentGains_field.get() == "" or
                Gender_field.get() == "" or
                Relationship_field.get() == "" or
                Occupation_field.get() == "" or
                MaritalStatus_field.get() == "" or
                YearsOfEducation_field.get() == "" or
                educ_field.get() == "" or
                WorkCond_field.get() == "" or
                age_field.get() == "" or
                id_field.get() == "")

    def insert():
        global result
        # if user not fill any entry
        # then print "empty input"
        if validate_that_all_entries_filled():
            print("empty input")
        else:
            result = f"{id_field.get()},{age_field.get()},{WorkCond_field.get()},e,{educ_field.get()},{YearsOfEducation_field.get()},{MaritalStatus_field.get()},{Occupation_field.get()},{Relationship_field.get()},W,{Gender_field.get()},{InvestmentGains_field.get()},{InvestmentLosses_field.get()},{WeeklyWorkHours_field.get()},{CountryOfOrigin_field.get()}"
            # call the clear() function
            print(result)

        clear()

    # create a GUI window
    root = Tk()
    # set the background colour of GUI window
    root.configure(background='light green')
    # set the title of GUI window
    root.title("registration form")
    # set the configuration of GUI window
    root.geometry("500x400")
    # create a Form label
    heading = Label(root, text="Form", bg="light green")
    # create a Name label
    id = Label(root, text="id", bg="light green")
    age = Label(root, text="age", bg="light green")
    # create a Course label
    WorkCond = Label(root, text="WorkCond", bg="light green")
    MaritalStatus = Label(root, text="MaritalStatus", bg="light green")
    # create a Semester label
    # create a Form No. label
    educ = Label(root, text="educ", bg="light green")
    # create a Contact No. label
    YearsOfEducation = Label(root, text="YearsOfEducation", bg="light green")
    # create a Email id label
    Occupation = Label(root, text="Occupation", bg="light green")
    # create a address label
    Relationship = Label(root, text="Relationship", bg="light green")
    Gender = Label(root, text="Gender", bg="light green")
    InvestmentGains = Label(root, text="InvestmentGains", bg="light green")
    InvestmentLosses = Label(root, text="InvestmentLosses", bg="light green")
    WeeklyWorkHours = Label(root, text="WeeklyWorkHours", bg="light green")
    CountryOfOrigin = Label(root, text="CountryOfOrigin", bg="light green")
    MonthlyIncome = Label(root, text="MonthlyIncome", bg="light green")
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    heading.grid(row=0, column=1)
    id.grid(row=1, column=0)
    age.grid(row=2, column=0)
    WorkCond.grid(row=3, column=0)
    educ.grid(row=5, column=0)
    YearsOfEducation.grid(row=6, column=0)
    MaritalStatus.grid(row=7, column=0)
    Occupation.grid(row=8, column=0)
    Relationship.grid(row=9, column=0)
    Gender.grid(row=11, column=0)
    InvestmentGains.grid(row=12, column=0)
    InvestmentLosses.grid(row=13, column=0)
    WeeklyWorkHours.grid(row=14, column=0)
    CountryOfOrigin.grid(row=15, column=0)
    MonthlyIncome.grid(row=16, column=0)

    # create a text entry box
    # for typing the information
    id_field = Entry(root)
    age_field = Entry(root)
    WorkCond_field = Entry(root)
    educ_field = Entry(root)
    YearsOfEducation_field = Entry(root)
    MaritalStatus_field = Entry(root)
    Occupation_field = Entry(root)
    Relationship_field = Entry(root)
    Gender_field = Entry(root)
    InvestmentGains_field = Entry(root)
    InvestmentLosses_field = Entry(root)
    WeeklyWorkHours_field = Entry(root)
    CountryOfOrigin_field = Entry(root)
    MonthlyIncome_field = Entry(root)

    id_field.bind("<Return>", id_field.focus_set())
    age_field.bind("<Return>", focus2)
    WorkCond_field.bind("<Return>", focus3)
    educ_field.bind("<Return>", focus5)
    YearsOfEducation_field.bind("<Return>", focus6)
    MaritalStatus_field.bind("<Return>", focus7)
    Occupation_field.bind("<Return>", focus8)
    Relationship_field.bind("<Return>", focus9)
    Gender_field.bind("<Return>", focus11)
    InvestmentGains_field.bind("<Return>", focus12)
    InvestmentLosses_field.bind("<Return>", focus13)
    WeeklyWorkHours_field.bind("<Return>", focus14)
    CountryOfOrigin_field.bind("<Return>", focus15)
    MonthlyIncome_field.bind("<Return>", focus16)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    id_field.grid(row=1, column=1, ipadx="100")
    age_field.grid(row=2, column=1, ipadx="100")
    WorkCond_field.grid(row=3, column=1, ipadx="100")

    educ_field.grid(row=5, column=1, ipadx="100")

    YearsOfEducation_field.grid(row=6, column=1, ipadx="100")

    MaritalStatus_field.grid(row=7, column=1, ipadx="100")

    Occupation_field.grid(row=8, column=1, ipadx="100")

    Relationship_field.grid(row=9, column=1, ipadx="100")
    Gender_field.grid(row=11, column=1, ipadx="100")
    InvestmentGains_field.grid(row=12, column=1, ipadx="100")
    InvestmentLosses_field.grid(row=13, column=1, ipadx="100")
    WeeklyWorkHours_field.grid(row=14, column=1, ipadx="100")
    CountryOfOrigin_field.grid(row=15, column=1, ipadx="100")
    MonthlyIncome_field.grid(row=16, column=1, ipadx="100")

    # create a Submit Button and place into the root window
    submit = Button(root, text="Send", fg="Black",
                    bg="Red", command=insert)

    submit.grid(row=17, column=1)

    # start the GUI
    root.mainloop()
