# python csv2json_restaurant.py <restaurants.csv> <inspections.csv>
#
# *ATTENTION*
# 1) l ordre dans le user type cassandra doit "coller" à l ordre dans l objet JSON, non granti par le dict python
# 2) l'algo est tres tres criticable, temps d execution ~10h..............

import csv
import json
import sys
import time

number_args = len(sys.argv)
if number_args != 3 :
    print("Error in in arguments !")
    exit(1)

try:
    resto_file = open(sys.argv[1], 'r')
    jsonfile = open('restaurants_inspections.json', 'w')
    resto_fieldnames = ("id", "Name", "borough", "BuildingNum", "Street", "ZipCode","Phone","CuisineType" )
    resto_reader = csv.DictReader(resto_file, resto_fieldnames)
    inspection_fieldnames = ( "idrestau", "date", "ViolationCode", "ViolationDescription", "CriticalFlag", "Score", "GRADE")
    for resto_row in resto_reader :
        inspection_file = open(sys.argv[2], 'r')
        inspection_reader = csv.DictReader(inspection_file, inspection_fieldnames)
        inspections_dict = {}
        #generer les inspections correspondantes au restau
        for inspection_row in inspection_reader :
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
