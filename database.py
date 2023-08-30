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


insert_database(25580, 27, "Private", 159623, "College", 10, "MarriedCivilianSpouse", "Sales", "Husband", "White",
                "Male", 0, 0, 40, "United-States")
