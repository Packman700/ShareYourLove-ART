import re
import datetime as dt

def return_line_with_shifted_time(line, days_shift):
    RE_EXP = re.compile('[0-9]{4}-[0-9]{2}-[0-9]{2}')
    if re.search(RE_EXP, line):
        date = re.findall(RE_EXP, line)[0]
        date = dt.date.fromisoformat(date)  # String to datatime object
        date = (date - days_shift).strftime("%Y-%m-%d")  # Add shift and convert to string
        line = re.sub(RE_EXP, date, line)
    return line