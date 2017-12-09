# csv..py <restaurants.csv> <inspections.csv>
import csv
import json
import sys
import time

number_args = len(sys.argv)
if number_args != 3 :
    print("Error in in arguments !")
    exit(1)
# print ('Number of arguments:', len(sys.argv), 'arguments.')
# i= 0
# while i <  len(sys.argv) :
#     print ( str(i) + " " + sys.argv[i])
#     i=i+1
# print ('Argument List:', str(sys.argv))
# exit(0)

try:
    resto_file = open(sys.argv[1], 'r')
    jsonfile = open('restaurants_inspections.json', 'w')
    resto_fieldnames = ("id", "Name", "borough", "BuildingNum", "Street", "ZipCode","Phone","CuisineType" )
    resto_reader = csv.DictReader(resto_file, resto_fieldnames)
    inspection_fieldnames = ( "idrestau", "date", "ViolationCode", "ViolationDescription", "CriticalFlag", "Score", "GRADE")
    j = 0
    for resto_row in resto_reader :
        inspection_file = open(sys.argv[2], 'r')
        inspection_reader = csv.DictReader(inspection_file, inspection_fieldnames)
        inspections_dict = {}
        #generer les inspections correspondantes au restau
        for inspection_row in inspection_reader :
            ##print( "idrestau <" + inspection_row["idrestau"] +  "> id <" + resto_row["id"] +">" )
            ##time.sleep(1)
            if inspection_row["idrestau"] == resto_row["id"] :
                # nettoyer l inspection
                inspection_row_tmp = inspection_row
                date = inspection_row_tmp.pop("date")
                del inspection_row_tmp["idrestau"]
                # generer une inspection
                inspections_dict[date]=inspection_row_tmp
        #inserer le dict inspections dans la map
        resto_row["inspections"] = inspections_dict
        json.dump(resto_row, jsonfile)
        jsonfile.write('\n')
        inspection_file.close()
    resto_file.close()
    jsonfile.close()
except ValueError:
    print("Excepiton !" + ValueError)
