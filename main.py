from return_line_with_shifted_time import return_line_with_shifted_time
import datetime as dt

# file_path = "./art.sh"
file_path = input("Give a path to art.sh:")

# Default output start on 2020-04-12 ;P
days_shift = dt.timedelta(days=int(input("How many weeks you want to shift: ")*7)) # 67

if __name__ == "__main__":
    with open(file_path, 'r', encoding='utf-8') as file:
        with open('./modified-art.sh', 'w') as modified_file:
            for line in file:
                line = return_line_with_shifted_time(line, days_shift)
                modified_file.write(line)
