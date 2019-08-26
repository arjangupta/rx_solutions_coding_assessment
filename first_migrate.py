import sys
from app import db
from app.models import Pharmacy

def csv_to_db():
    f = open("pharmacies.csv", "r")
    all_lines = f.readlines()
    f.close()
    all_lines = all_lines[1:len(all_lines)-1] #skip the first line
    for line in all_lines:
        #format: pharmacy name, address, city, state, zip, latitude, longitude
        comma_separated_line = line.split(',')
        print(pharmacy_name=comma_separated_line[0], \
                address=comma_separated_line[1], \
                city=comma_separated_line[2], \
                state=comma_separated_line[3], \
                zip=comma_separated_line[4], \
                latitude=comma_separated_line[5], \
                longitude=comma_separated_line[6]))

    #     new_pharmacy = Pharmacy(pharmacy_name=comma_separated_line[0], \
    #                             address=comma_separated_line[1], \
    #                             city=comma_separated_line[2], \
    #                             state=comma_separated_line[3], \
    #                             zip=comma_separated_line[4], \
    #                             latitude=comma_separated_line[5], \
    #                             longitude=comma_separated_line[6])
    #     db.session.add(new_pharmacy)
    # db.session.commit()

if __name__ == "__main__":
    csv_to_db()