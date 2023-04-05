def show_table(teams_list , data):
    row_format = "{:>15}" * (len(teams_list) + 1)
    print(row_format.format("", *teams_list))
    for team, row in zip(teams_list, data):
        print(row_format.format("", *row))
