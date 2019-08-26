import csv
from app import db
from app.models import Pharmacy

def csv_to_db():
    with open('pharmacies.csv', 'r') as csv_file:
        pharmacy_records = csv.reader(csv_file)
        for row in pharmacy_records:
            print("pharmacy_name=" + row[0] + \
                " address=" + row[1] + \
                " city=" + row[2] + \
                " state=" + row[3] + \
                " zip=" + row[4] + \
                " latitude=" + row[5] + \
                " longitude=" + row[6])


    # f = open("pharmacies.csv", "r")
    # all_lines = f.readlines()
    # f.close()
    # all_lines = all_lines[1:len(all_lines)-1] #skip the first line
    # for line in all_lines:
    #     #format: pharmacy name, address, city, state, zip, latitude, longitude
    #     line = line.replace('\n"', '')
    #     row = line.split(',')
    #     print("pharmacy_name=" + row[0] + \
    #             " address=" + row[1] + \
    #             " city=" + row[2] + \
    #             " state=" + row[3] + \
    #             " zip=" + row[4] + \
    #             " latitude=" + row[5] + \
    #             " longitude=" + row[6])

    #     new_pharmacy = Pharmacy(pharmacy_name=row[0], \
    #                             address=row[1], \
    #                             city=row[2], \
    #                             state=row[3], \
    #                             zip=row[4], \
    #                             latitude=row[5], \
    #                             longitude=row[6])
    #     db.session.add(new_pharmacy)
    # db.session.commit()

if __name__ == "__main__":
    csv_to_db()