
start_year = 2017
end_year = 2017
start_year = str(start_year) + '01'
end_year = str(end_year) + '13'
print(start_year, type(start_year))
print(end_year, type(end_year))

for index in range(int(start_year), int(end_year)):
    print(int(str(index)[0:4]), str(index)[4:6])