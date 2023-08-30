import pandas as pd

import Consts


def insert_database(id, age, working_condition, final_weight,
                    education, years_of_education, marital_status, occupation, relationship, ethnicity,
                    gender, investment_gains, investment_losses, weekly_work_hours, country_of_origin):
    new_data_line = {"Id": [id], "Age": [age], "WorkingCondition": [working_condition], "FinalWeight": [final_weight],
                     "Education": [education], "YearsOfEducation": [years_of_education],
                     "MaritalStatus": [marital_status],
                     "Occupation": [occupation], "Relationship": [relationship], "Ethnicity": [ethnicity],
                     "Gender": [gender],
                     "InvestmentGains": [investment_gains], "InvestmentLosses": [investment_losses],
                     "WeeklyWorkHours": [weekly_work_hours], "CountryOfOrigin": [country_of_origin]}

    df = pd.DataFrame.from_dict(new_data_line)
    df.to_csv(Consts.TEST_FILE_NAME, index=False, header=True)


def convert_data(data_string):
    list_of_data = data_string.split(",")
    list_of_data[0] = int(list_of_data[0])
    list_of_data[1] = int(list_of_data[1])
    list_of_data[3] = int(list_of_data[3])
    list_of_data[5] = int(list_of_data[5])
    list_of_data[11] = int(list_of_data[11])
    list_of_data[12] = int(list_of_data[12])
    list_of_data[13] = int(list_of_data[13])
    print(type(list_of_data))
    return list_of_data



str1 = "18079,61,Private,119684,ProfessionalSchool,15,MarriedCivilianSpouse,ProfessionalSpecialty,Husband,White,Male,15024,0,20,United-States"
data = convert_data(str1)


