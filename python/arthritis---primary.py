# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"46622.0","system":"readv2"},{"code":"71083.0","system":"readv2"},{"code":"94854.0","system":"readv2"},{"code":"36276.0","system":"readv2"},{"code":"31360.0","system":"readv2"},{"code":"12575.0","system":"readv2"},{"code":"21533.0","system":"readv2"},{"code":"42405.0","system":"readv2"},{"code":"27557.0","system":"readv2"},{"code":"4186.0","system":"readv2"},{"code":"50644.0","system":"readv2"},{"code":"31181.0","system":"readv2"},{"code":"47831.0","system":"readv2"},{"code":"28456.0","system":"readv2"},{"code":"7196.0","system":"readv2"},{"code":"M08","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('juvenile-arthritis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["arthritis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["arthritis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["arthritis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
