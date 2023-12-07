import csv

cars = [["BMW", "M3", "RWD"], ["BMW", "Series 7", "AWD"], ["Mini", "Cooper S", "FWD"]]

with open("csv_to_write.txt", "w") as file:
    writer = csv.writer(file)
    writer.writerows(cars)