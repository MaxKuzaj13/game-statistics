file_name = 'game_stat.txt'
year = 2014

def rows_spliten_by_enter(file_name):
    lines = read_file(file_name)
    split_by_enter = lines.split('\n')
    return split_by_enter

# Report functions
def count_games(file_name):
    split_by_enter = rows_spliten_by_enter(file_name)
    # remove last line becouse it not contain any text
    last_line_without_text = -1
    number_of_lines = split_by_enter[:last_line_without_text]
    return len(number_of_lines)


def decide(file_name, year):
    boolen_value = False
    rows = rows_spliten_by_enter(file_name)
    for row in rows:
        #print(row.split('\t'))
        if str(year) in row.split('\t'):
            boolen_value = True
    print(boolen_value)
    return boolen_value


def get_latest(file_name):
    pass


def count_by_genre(file_name, genre):
    pass


def get_line_number_by_title(file_name, title):
    pass



def read_file(file_name):
    with open(file_name, 'r') as reader:
        # Read & print the first 5 characters of the line 5 times
        #print(reader.read())
        lines = reader.read()
        #print(lines)
    return lines


def main():
    count_games(file_name)
    decide(file_name, year)



if __name__ == "__main__":
    main()