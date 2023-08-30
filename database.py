import pandas as pd


def insert_database(Id, Age, Working_condition, FinalWeight,
                    Education, YearsOfEducation, MaritalStatus, Occupation, Relationship, Gender,
                    InvestmentGains, InvestmentLosses, WeeklyWorkHours, CountryOfOrigin):
    new_data_line = {"Id": Id, "Age": Age, "Working_condition": Working_condition, "FinalWeight": FinalWeight,
                     "Education": Education, "YearsOfEducation": YearsOfEducation, "MaritalStatus": MaritalStatus,
                     "Occupation": Occupation, "Relationship": Relationship, "Gender": Gender,
                     "InvestmentGains": InvestmentGains,
                     "InvestmentLosses": InvestmentLosses, "WeeklyWorkHours": WeeklyWorkHours,
                     "CountryOfOrigin": CountryOfOrigin}
    df = pd.read_csv("test_data.csv")
    df.append(new_data_line)
    df.to_csv("test_data.csv")
