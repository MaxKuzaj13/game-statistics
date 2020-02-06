NAME_GAME_INDEX = 0
INDEX_VALUE_NUMBER_PLAYER = 1
INDEX_GAME_REVIEW = 2

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
        if str(year) in row.split('\t'):
            boolen_value = True
    return boolen_value


def is_longer(temp_year, last_year_production_game):
    if temp_year > last_year_production_game:
        last_year_production_game = temp_year
    return last_year_production_game


def checking_name_lates_game(last_year_production_game, rows):
    last_game_list = []
    for row in rows:
        list_row = row.split('\t')
        if str(last_year_production_game) in list_row:
            last_game_list.append(list_row[NAME_GAME_INDEX])
    first_row = 0
    return last_game_list[first_row]


def get_latest(file_name):
    last_year_production_game = 0
    rows = rows_spliten_by_enter(file_name)
    for row in rows:
        for col in row.split('\t'):
            # if string have length 4 letters
            if len(col) == 4:
                try:
                    temp_year = int(col)
                except:
                    pass
                last_year_production_game = is_longer(temp_year, last_year_production_game)
    last_game = checking_name_lates_game(last_year_production_game, rows)
    return last_game


def count_by_genre(file_name, genre):
    count_genre = 0
    rows = rows_spliten_by_enter(file_name)
    for row in rows:
        if genre in row.split('\t'):
            count_genre += 1
    return count_genre


def get_line_number_by_title(file_name, title):
    count_rows = 0
    rows = rows_spliten_by_enter(file_name)
    split_by_enter = rows_spliten_by_enter(file_name)
    this_row = "Non-existing game"
    for row in rows:
        count_rows += 1
        if title in row.split('\t'):
            this_row = count_rows
            break
        elif count_rows == len(split_by_enter):
            raise ValueError("Non-existing game")

    return this_row


def read_file(file_name):
    with open(file_name, 'r') as reader:
        # Read & print the first 5 characters of the line 5 times
        lines = reader.read()
    return lines


def sort_abc(file_name):
    unsorted_names = []
    lines = read_file(file_name)
    for row in lines:
        for col in row.split('\t'):
            unsorted_names.append(col[NAME_GAME_INDEX])
    for element in range(len(unsorted_names)):
        sorted_names = ''
        #if
    return sorted_names


def get_genres(file_name):
    pass


def when_was_top_sold_fps(file_name):
    pass


def max_value_players_def(file_name):
    max_value_players = 0
    rows = rows_spliten_by_enter(file_name)
    for row in rows:
        row_spliten = row.split("\t")
        try:
            if float(row_spliten[INDEX_VALUE_NUMBER_PLAYER]) > max_value_players:
                max_value_players = float(row_spliten[INDEX_VALUE_NUMBER_PLAYER])
        except:
            pass
    return max_value_players


# cześć 2
def get_most_played(file_name):
    rows = rows_spliten_by_enter(file_name)
    game_max_players = ''
    max_value_players = max_value_players_def(file_name)
    for row in rows:
        row_spliten = row.split("\t")
        try:
            if float(row_spliten[INDEX_VALUE_NUMBER_PLAYER]) == max_value_players:
                game_max_players = row_spliten[NAME_GAME_INDEX]
                break
        except:
            pass
    return game_max_players


def list_number_sold_games(file_name):
    list_sold = []
    rows = rows_spliten_by_enter(file_name)
    for row in rows:
        row_spliten = row.split("\t")
        try:
            list_sold.append(float(row_spliten[INDEX_VALUE_NUMBER_PLAYER]))
        except:
            # print(row)
            pass
    return list_sold


def sum_sold(file_name):
    list_sold = list_number_sold_games(file_name)
    sum_sold_values = sum(list_sold)
    return sum_sold_values


def get_selling_avg(file_name):
    list_sold = list_number_sold_games(file_name)
    avrage_sold = sum(list_sold)/len(list_sold)
    return avrage_sold


def list_game_name(file_name):
    list_game_title = []
    rows = rows_spliten_by_enter(file_name)
    for row in rows:
        row_spliten = row.split("\t")
        try:
            list_game_title.append(row_spliten[NAME_GAME_INDEX])
        except:
            pass
    return list_game_title


def max_len_game_name(lista_game_title):
    temp_list_lenght = []
    for game in lista_game_title:
        temp_list_lenght.append(len(game))
    return temp_list_lenght


def count_longest_title(file_name):
    lista_game_title = list_game_name(file_name)
    # temp_list_lenght = max_len_game_name(lista_game_title)
    # temp_max_value = max(temp_list_lenght)
    longest_title = len(max(lista_game_title, key=len))
    return longest_title


def get_list_date(file_name):
    list_game_date_review = []
    rows = rows_spliten_by_enter(file_name)
    for row in rows:
        row_spliten = row.split("\t")
        try:
            list_game_date_review.append(int(row_spliten[INDEX_GAME_REVIEW]))
        except:
            pass
    return list_game_date_review


def get_date_avg(file_name):
    list_game_date_review = get_list_date(file_name)
    avrage_date = sum(list_game_date_review)/len(list_game_date_review)

    if avrage_date != int(avrage_date):
        avrage_date = int(avrage_date + 1)
    else:
        avrage_date = int(avrage_date)
    return avrage_date


def get_game(file_name, title):
    rows = rows_spliten_by_enter(file_name)
    for row in rows:
        row_spliten = row.split("\t")
        if title in row_spliten:
            break
    return row_spliten



def main():
    file_name = 'game_stat.txt'
    year = 2014
    genre = "First-person shooter"
    title = "Counter-Strike"
    # czy tego nie usunąć?
    count_games(file_name)
    decide(file_name, year)
    get_latest(file_name)
    count_by_genre(file_name, genre)
    get_line_number_by_title(file_name, title)
    get_most_played(file_name)
    sum_sold(file_name)
    get_selling_avg(file_name)
    count_longest_title(file_name)
    get_date_avg(file_name)
    get_game(file_name, title)

if __name__ == "__main__":
    main()


