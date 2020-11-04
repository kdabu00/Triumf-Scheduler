import getpass
import os.path
import pandas as pd
from datetime import datetime
import calendar

def main():
    """Main function"""

    # gets the current logged in user's name
    user = getpass.getuser()

    # Grabs filename input from user
    requests_name = ask_file_names()

    # I placed my excel files in C:\Users\USERNAME\Documents. Note: depending on where the file is *change*
    requests_path = os.path.join("C:\\Users", user, "Documents", requests_name)

    # assign the excel data frame to requests variable
    requests = read_file(requests_path)
    isac_requests = get_expirment_from_isac(requests)
    requests_sort_by_tb = sort_by_target_block(isac_requests)
    # Outputs - Will probably be made into a separate function and saved for future use
    print("-" * 100)
    print("OVERVIEW OF REQUEST")
    print("-" * 100)
    print(requests_sort_by_tb)

def read_file(path: str) -> object:
    """Open excel requests, displays contents turns excel file into a data frame: requests"""
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    excel_file = pd.read_excel(path)  # first index: row, second index: column ex. schedule.values[0][0] == 'Date'
    return excel_file

def ask_file_names() -> object:
    """Prompts user for file names for requests and schedules, then returns them"""
    requests_name = input("Input requests file name (Schedule 138 Beam Requests.xlsx): ")
    return requests_name

def get_expirment_from_isac(requests: object):
    """get the data frame which only contain the ISAC experiment"""
    isac_request = requests.loc[(requests['Beam options'] == 'ISAC Target (RIB)')]
    return isac_request
    
def get_required_shifts(requests: object, row_number):
    required_shifts = requests.values[row_number-2][4]    
    return required_shifts 

def get_expirment_number(requests: object, row_number):
    exp_num = requests.values[row_number-2][0]
    return exp_num

def sort_by_target_block(requests: object):
    """group by source then group by target type"""
    requests_sort_by_tb = requests.sort_values(by=['Ion Source', 'Target'])
    return requests_sort_by_tb

def set_ts_tm(requests: object, combo):
    if combo == "w2":
        ts = "West"
        tm = 2
    elif combo == "e2":
        ts = "East"
        tm = 2
    elif combo == "w4":
        ts = "West"
        tm = 4
    elif combo == "e4":
        ts = "East"
        tm = 4
    return ts,tm

def set_date(row_number):
    year_now = datetime.datetime.now().year
    date_list = []
    if row_number == 1 or row_number == 2 or row_number == 3:
        string_2021 = "25/4/2021"
        string_2022 = "25/4/2022"
        string_2023 = "25/4/2023"
        string_2024 = "25/4/2024"
        string_2025 = "25/4/2025"
        string_2026 = "25/4/2026"
        string_2027 = "25/4/2027"
        string_2028 = "25/4/2028"
        string_2029 = "25/4/2029"
        string_2030 = "25/4/2030"
        date_2021 = datetime.strptime(string_2021, "%d/%m/%Y")
        date_2022 = datetime.strptime(string_2022, "%d/%m/%Y")
        date_2023 = datetime.strptime(string_2023, "%d/%m/%Y")
        date_2024 = datetime.strptime(string_2024, "%d/%m/%Y")
        date_2025 = datetime.strptime(string_2025, "%d/%m/%Y")
        date_2026 = datetime.strptime(string_2026, "%d/%m/%Y")
        date_2027 = datetime.strptime(string_2027, "%d/%m/%Y")
        date_2028 = datetime.strptime(string_2028, "%d/%m/%Y")
        date_2029 = datetime.strptime(string_2029, "%d/%m/%Y")
        date_2030 = datetime.strptime(string_2030, "%d/%m/%Y")
        present = datetime.now()
        if present.date() < date_2021():
            date = datetime.datetime(2021, 4, 6)
            date_list.append(date, date, date)
        elif present.date() < date_2022():
            date = datetime.datetime(2022, 4, 5)
            date_list.append(date, date, date)
        elif present.date() < date_2023():
            date = datetime.datetime(2023, 4, 11)
            date_list.append(date, date, date)
        elif present.date() < date_2024():
            date = datetime.datetime(2024, 4, 9)
            date_list.append(date, date, date)
        elif present.date() < date_2025():
            date = datetime.datetime(2025, 4, 8)
            date_list.append(date, date, date)
        elif present.date() < date_2026():
            date = datetime.datetime(2026, 4, 7)
            date_list.append(date, date, date)
        elif present.date() < date_2027():
            date = datetime.datetime(2027, 4, 6)
            date_list.append(date, date, date)
        elif present.date() < date_2028():
            date = datetime.datetime(2028, 4, 11)
            date_list.append(date, date, date)
        elif present.date() < date_2029():
            date = datetime.datetime(2029, 4, 10)
            date_list.append(date, date, date)
        elif present.date() < date_2030():
            date = datetime.datetime(2030, 4, 9)
            date_list.append(date, date, date)
    else:
        previous_date = date_list[row_number-4]
        date = pd.to_datetime(previous_date) + pd.DateOffset(days=1)
        date_list.append(date, date, date)
    return date


def add_shift(row_number):
    df_shift_list = []
    if row_number == 1:
        shift_name = "DAY"
        df_shift_list.append("DAY")
    else:
        if df_shift_list[row_number-2] == "DAY":
            df_shift_list.append("EVE")
            shift_name = "EVE"
        elif df_shift_list[row_number-2] == "EVE":
            df_shift_list.append("OWL")
            shift_name = "EVE"
        elif df_shift_list[row_number-2] == "OWL":
            df_shift_list.append("DAY")
            shift_name = "EVE"
    return shift_name

def create_data_frame():
    pass

def write_to_excel():
    pass

if __name__ == "__main__":
    main()