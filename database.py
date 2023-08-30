import pandas as pd

import Consts


def insert_database(Id, Age, Working_condition, FinalWeight,
                    Education, YearsOfEducation, MaritalStatus, Occupation, Relationship, Ethnicity,
                    Gender, InvestmentGains, InvestmentLosses, WeeklyWorkHours, CountryOfOrigin):
    new_data_line = {"Id": [Id], "Age": [Age], "WorkingCondition": [Working_condition], "FinalWeight": [FinalWeight],
                     "Education": [Education], "YearsOfEducation": [YearsOfEducation], "MaritalStatus": [MaritalStatus],
                     "Occupation": [Occupation], "Relationship": [Relationship], "Ethnicity": [Ethnicity],
                     "Gender": [Gender],
                     "InvestmentGains": [InvestmentGains], "InvestmentLosses": [InvestmentLosses],
                     "WeeklyWorkHours": [WeeklyWorkHours], "CountryOfOrigin": [CountryOfOrigin]}
    print(new_data_line)
    df = pd.DataFrame.from_dict(new_data_line)
    df.to_csv(Consts.TEST_FILE_NAME, index=False, header=True)


insert_database(5355, 42, "SelfEmployedIncluded", 78765, "College", 10, "Divorced", "ExecutiveManagerial", "Unmarried",
                "White", "Male", 0, 0, 90, "United-States"
                )
