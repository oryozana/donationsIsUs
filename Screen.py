# # import openpyxl and tkinter modules
# from tkinter import *
#
#
# # globally declare wb and sheet variable
#
# # create the sheet object
#
#
# # Function to set focus (cursor)
# def focus1(event):
#     # id: The citizen id
#     id_field.focus_set()
#
#
# # Function to set focus
# def focus2(event):
#     # Age: The citizen age
#     age_field.focus_set()
#
#
# # Function to set focus
# def focus3(event):
#     # Working condition: The citizen working condition (Private / StateGovernment / SelfEmployedNotIncluded etc...)
#     WorkCond_field.focus_set()
#
#
# # Function to set focus
# def focus4(event):
#     # set focus on the contact_no_field box
#     FinalWeight_field.focus_set()
#
#
# # Function to set focus
# def focus5(event):
#     # Education: Where the citizen learning right now
#     educ_field.focus_set()
#
#
# # Function to set focus
# def focus6(event):
#     # YearsOfEducation: How many years of education the citizen have
#     YearsOfEducation_field.focus_set()
#
#
# def focus7(event):
#     # MaritalStatus: The citizen relationship status
#     MaritalStatus_field.focus_set()
#
#
# def focus8(event):
#     # Occupation: The citizen job
#     Occupation_field.focus_set()
#
#
# def focus9(event):
#     # Relationship: The citizen family relationship
#     Relationship_field.focus_set()
#
#
# def focus10(event):
#     # Ethnicity: The citizen race
#     Ethnicity_field.focus_set()
#
#
# def focus11(event):
#     # Gender: the citizen gender
#     Gender_field.focus_set()
#
#
# def focus12(event):
#     # InvestmentGains: The citizen gains from investments
#     InvestmentGains_field.focus_set()
#
#
# def focus13(event):
#     # InvestmentLosses: The citizen losses from investments
#     InvestmentLosses_field.focus_set()
#
#
# def focus14(event):
#     # WeeklyWorkHours: The citizen weekly work hours
#     WeeklyWorkHours_field.focus_set()
#
#
# def focus15(event):
#     # CountryOfOrigin: Where the citizen is born
#     CountryOfOrigin_field.focus_set()
#
#
# def focus16(event):
#     # MonthlyIncome: Does the citizen have monthly income or not
#     MonthlyIncome_field.focus_set()
#
#
# # Function for clearing the
# # contents of text entry boxes
# def clear():
#     # clear the content of text entry box
#     id_field.delete(0, END)
#     age_field.delete(0, END)
#     WorkCond_field.delete(0, END)
#     FinalWeight_field.delete(0, END)
#     educ_field.delete(0, END)
#     YearsOfEducation.delete(0, END)
#     MaritalStatus_field.delete(0, END)
#     Occupation_field.delete(0, END)
#     Relationship_field.delete(0, END)
#     Ethnicity_field.delete(0, END)
#     Gender_field.delete(0, END)
#     InvestmentGains_field.delete(0, END)
#     InvestmentLosses_field.delete(0, END)
#     WeeklyWorkHours_field.delete(0, END)
#     CountryOfOrigin_field.delete(0, END)
#     MonthlyIncome_field.delete(0, END)
#
#     # MonthlyIncome_field
#     # CountryOfOrigin_field
#     # WeeklyWorkHours_field
#     # InvestmentLosses_field
#     # InvestmentGains_field
#     # Gender_field
#     # Ethnicity_field
#     # Relationship_field
#     # Occupation_field
#     # MaritalStatus_field
#     # YearsOfEducation_field
#     # educ_field
#     # FinalWeight_field
#     # WorkCond_field
#     # age_field
#     # id_field
#
#
# # Function to take data from GUI
#
# def check_if_input_empty():
#     return (MonthlyIncome_field.get() == "" or
#             CountryOfOrigin_field.get() == "" or
#             WeeklyWorkHours_field.get() == "" or
#             InvestmentLosses_field.get() == "" or
#             InvestmentGains_field.get() == "" or
#             Gender_field.get() == "" or
#             Ethnicity_field.get() == "" or
#             Relationship_field.get() == "" or
#             Occupation_field.get() == "" or
#             MaritalStatus_field.get() == "" or
#             YearsOfEducation_field.get() == "" or
#             educ_field.get() == "" or
#             FinalWeight_field.get() == "" or
#             WorkCond_field.get() == "" or
#             age_field.get() == "")
#
# def insert():
#     # if user not fill any entry
#     # then print "empty input"
#     if check_if_input_empty():
#
#         print("empty input")
#
#     else:
#
#         # assigning the max row and max column
#         # value upto which data is written
#         # in an excel sheet to the variable
#         current_row = sheet.max_row
#         current_column = sheet.max_column
#
#         # get method returns current text
#         # as string which we write into
#         # excel spreadsheet at particular location
#         sheet.cell(row=current_row + 1, column=1).value = name_field.get()
#         sheet.cell(row=current_row + 1, column=2).value = course_field.get()
#         sheet.cell(row=current_row + 1, column=3).value = sem_field.get()
#         sheet.cell(row=current_row + 1, column=4).value = form_no_field.get()
#         sheet.cell(row=current_row + 1, column=5).value = contact_no_field.get()
#         sheet.cell(row=current_row + 1, column=6).value = email_id_field.get()
#         sheet.cell(row=current_row + 1, column=7).value = address_field.get()
#
#         # save the file
#         wb.save('C:\\Users\\Admin\\Desktop\\excel.xlsx')
#
#         # set focus on the name_field box
#         name_field.focus_set()
#
#         # call the clear() function
#         clear()
#
#
# # Driver code
# if __name__ == "__main__":
#     # create a GUI window
#     root = Tk()
#
#
#
#     # set the background colour of GUI window
#     root.configure(background='light green')
#
#     # set the title of GUI window
#     root.title("registration form")
#
#     # set the configuration of GUI window
#     root.geometry("500x400")
#
#     # create a Form label
#     heading = Label(root, text="Form", bg="light green")
#
#     # create a Name label
#     id = Label(root, text="id", bg="light green")
#
#     age = Label(root, text="age", bg="light green")
#
#
#     # create a Course label
#     WorkCond = Label(root, text="WorkCond", bg="light green")
#
#     MaritalStatus = Label(root, text="MaritalStatus", bg="light green")
#
#     # create a Semester label
#     FinalWeight = Label(root, text="FinalWeight", bg="light green")
#
#
#     # create a Form No. label
#     educ = Label(root, text="educ", bg="light green")
#
#     # create a Contact No. label
#     YearsOfEducation = Label(root, text="YearsOfEducation", bg="light green")
#
#
#     # create a Email id label
#     Occupation = Label(root, text="Occupation", bg="light green")
#
#
#     # create a address label
#     Relationship = Label(root, text="Relationship", bg="light green")
#
#
#     Ethnicity = Label(root, text="Ethnicity", bg="light green")
#
#     Gender = Label(root, text="Gender", bg="light green")
#
#
#     InvestmentGains = Label(root, text="InvestmentGains", bg="light green")
#
#
#     InvestmentLosses = Label(root, text="InvestmentLosses", bg="light green")
#
#     WeeklyWorkHours = Label(root, text="WeeklyWorkHours", bg="light green")
#
#
#     CountryOfOrigin = Label(root, text="CountryOfOrigin", bg="light green")
#
#
#     MonthlyIncome = Label(root, text="MonthlyIncome", bg="light green")
#
#
#
#
#     # grid method is used for placing
#     # the widgets at respective positions
#     # in table like structure .
#     heading.grid(row=0, column=1)
#     id.grid(row=1, column=0)
#     age.grid(row=2, column=0)
#     WorkCond.grid(row=3, column=0)
#     FinalWeight.grid(row=4, column=0)
#     educ.grid(row=5, column=0)
#     YearsOfEducation.grid(row=6, column=0)
#     MaritalStatus.grid(row=7, column=0)
#     Occupation.grid(row=8, column=0)
#     Relationship.grid(row=9, column=0)
#     Ethnicity.grid(row=10, column=0)
#     Gender.grid(row=11, column=0)
#     InvestmentGains.grid(row=12, column=0)
#     InvestmentLosses.grid(row=13, column=0)
#     WeeklyWorkHours.grid(row=14, column=0)
#     CountryOfOrigin.grid(row=15, column=0)
#     MonthlyIncome.grid(row=16, column=0)
#
#     # MonthlyIncome
#     # CountryOfOrigin
#     # WeeklyWorkHours
#     # InvestmentLosses
#     # InvestmentGains
#     # Gender
#     # Ethnicity
#     # Relationship
#     # Occupation
#     # YearsOfEducation
#     # educ
#     # FinalWeight
#     # WorkCond
#     # age
#     # id
#
#
#     # create a text entry box
#     # for typing the information
#     id_field = Entry(root)
#     age_field = Entry(root)
#     WorkCond_field = Entry(root)
#
#     FinalWeight_field = Entry(root)
#     educ_field = Entry(root)
#
#     YearsOfEducation_field = Entry(root)
#
#     MaritalStatus_field = Entry(root)
#
#     Occupation_field = Entry(root)
#     Relationship_field = Entry(root)
#     Ethnicity_field = Entry(root)
#     Gender_field = Entry(root)
#     InvestmentGains_field = Entry(root)
#     InvestmentLosses_field = Entry(root)
#     WeeklyWorkHours_field = Entry(root)
#     CountryOfOrigin_field = Entry(root)
#     MonthlyIncome_field = Entry(root)
#     course_field = Entry(root)
#
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#
#
#
#
#     id_field.bind("<Return>", focus1)
#
#     # whenever the enter key is pressed
#     # then call the focus2 function
#     age_field.bind("<Return>", focus2)
#
#     # whenever the enter key is pressed
#     # then call the focus3 function
#     WorkCond_field.bind("<Return>", focus3)
#
#     # whenever the enter key is pressed
#     # then call the focus4 function
#     FinalWeight_field.bind("<Return>", focus4)
#
#     # whenever the enter key is pressed
#     # then call the focus5 function
#     educ_field.bind("<Return>", focus5)
#
#     # whenever the enter key is pressed
#     # then call the focus6 function
#     YearsOfEducation_field.bind("<Return>", focus6)
#
#     MaritalStatus_field.bind("<Return>", focus7)
#
#     Occupation_field.bind("<Return>", focus8)
#
#     Relationship_field.bind("<Return>", focus9)
#
#     Ethnicity_field.bind("<Return>", focus10)
#
#     Gender_field.bind("<Return>", focus11)
#     InvestmentGains_field.bind("<Return>", focus12)
#
#     InvestmentLosses_field.bind("<Return>", focus13)
#
#     WeeklyWorkHours_field.bind("<Return>", focus14)
#
#     CountryOfOrigin_field.bind("<Return>", focus15)
#
#     MonthlyIncome_field.bind("<Return>", focus16)
#
#
#     # grid method is used for placing
#     # the widgets at respective positions
#     # in table like structure .
#     id_field.grid(row=1, column=1, ipadx="100")
#     course_field.grid(row=2, column=1, ipadx="100")
#     WorkCond_field.grid(row=3, column=1, ipadx="100")
#
#     FinalWeight_field.grid(row=4, column=1, ipadx="100")
#
#     educ_field.grid(row=5, column=1, ipadx="100")
#
#     YearsOfEducation_field.grid(row=6, column=1, ipadx="100")
#
#     MaritalStatus_field.grid(row=7, column=1, ipadx="100")
#
#     Occupation_field.grid(row=8, column=1, ipadx="100")
#
#     Relationship_field.grid(row=9, column=1, ipadx="100")
#     Ethnicity_field.grid(row=10, column=1, ipadx="100")
#     Gender_field.grid(row=11, column=1, ipadx="100")
#     InvestmentGains_field.grid(row=12, column=1, ipadx="100")
#     InvestmentLosses_field.grid(row=13, column=1, ipadx="100")
#     WeeklyWorkHours_field.grid(row=14, column=1, ipadx="100")
#     CountryOfOrigin_field.grid(row=15, column=1, ipadx="100")
#     MonthlyIncome_field.grid(row=16, column=1, ipadx="100")
#
#
#     # create a Submit Button and place into the root window
#     submit = Button(root, text="Send", fg="Black",
#                     bg="Red", command=insert)
#     submit.grid(row=17, column=1)
#
#     # start the GUI
#     root.mainloop()
