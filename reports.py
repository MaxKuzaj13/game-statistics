file_name = 'game_stat.txt'
year = 2014
name_of_game = 0
genre = "First-person shooter"
title = "Counter-Strike"

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
        # print(row.split('\t'))
        if str(year) in row.split('\t'):
            boolen_value = True
    return boolen_value


def is_longer(temp_year, last_year_production_game):
    if temp_year > last_year_production_game:
        last_year_production_game = temp_year
    return last_year_production_game


def checking_name_lates_game(last_year_production_game, rows, name_of_game):
    last_game_list = []
    for row in rows:
        list_row = row.split('\t')
        if str(last_year_production_game) in list_row:
            last_game_list.append(list_row[name_of_game])
    first_row = 0
    # print(last_game_list[first_row])
    return last_game_list[first_row]


def get_latest(file_name):
    last_year_production_game = 0
    rows = rows_spliten_by_enter(file_name)
    for row in rows:
        # print('huj')
        for col in row.split('\t'):
            # if string have length 4 letters
            if len(col) == 4:
                try:
                    temp_year = int(col)
                except:
                    pass
                last_year_production_game = is_longer(temp_year, last_year_production_game)
    last_game = checking_name_lates_game(last_year_production_game, rows, name_of_game)
    return last_game


def count_by_genre(file_name, genre):
    count_genre = 0
    rows = rows_spliten_by_enter(file_name)
    for row in rows:
        if genre in row.split('\t'):
            count_genre += 1
    print(count_genre)
    return count_genre



def get_line_number_by_title(file_name, title):
    count_rows = 0
    rows = rows_spliten_by_enter(file_name)
    for row in rows:
        count_rows += 1
        if title in row.split('\t'):
            this_row = count_rows
    #print(this_row)
    return this_row


def read_file(file_name):
    with open(file_name, 'r') as reader:
        # Read & print the first 5 characters of the line 5 times
        #print(reader.read())
        lines = reader.read()
        #print(lines)
    return lines


def main():
    # czy tego nie usunąć?
    count_games(file_name)
    decide(file_name, year)
    get_latest(file_name)
    count_by_genre(file_name, genre)
    get_line_number_by_title(file_name, title)


if __name__ == "__main__":
    main()