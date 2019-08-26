import sys

def csv_to_db():
    f = open("pharmacies.csv", "r")
    all_lines = f.readlines()
    f.close()
    all_lines = all_lines[1:len(all_lines)-1] #skip the first line
    for line in all_lines:
        comma_separated_line = line.split(',')
        print("pharmacy name:" + comma_separated_line[0])
        print("address: " + comma_separated_line[1])
        print("zip code: " + comma_separated_line[4])

if __name__ == "__main__":
    csv_to_db()