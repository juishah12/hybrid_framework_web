from utility import read_utility


test_invalid_login_data = [
    ("Ram@yopmail.com", "Puri", "Invalid username or password. Please try again!"),
    ("Sita@yopmail.com", "Raman", "Invalid username or password. Please try again!"),
    ("Lakshman@yopmail.com", "Puri", "Invalid username or password. Please try again!")
]
test_blank_login_data = [
    ("", "", "This field is required."),
]

test_livedemo_data = read_utility.get_sheet_as_list("../test_data/live_demo.xlsx",
                                                                "Sheet1")
test_trial_data=read_utility.get_csv_as_list("../test_data/Trial.csv")
