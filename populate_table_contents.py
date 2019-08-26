import csv
from app import db
from app.models import Pharmacy

def csv_to_db():
    with open('pharmacies.csv', 'r') as csv_file:
        pharmacy_records = csv.reader(csv_file)
        first_line = True
        display_csv_lines = False
        for row in pharmacy_records:
            if first_line:
                first_line = False
                continue

            # CSV format: pharmacy name, address, city, state, zip, latitude, longitude
            
            if display_csv_lines:
                print("pharmacy_name=" + row[0] + \
                    " address=" + row[1] + \
                    " city=" + row[2] + \
                    " state=" + row[3] + \
                    " zip=" + row[4] + \
                    " latitude=" + row[5] + \
                    " longitude=" + row[6])

            new_pharmacy = Pharmacy(pharmacy_name=row[0], \
                                    address=row[1], \
                                    city=row[2], \
                                    state=row[3], \
                                    zip=row[4], \
                                    latitude=row[5], \
                                    longitude=row[6])
            db.session.add(new_pharmacy)
    db.session.commit()

if __name__ == "__main__":
    csv_to_db()