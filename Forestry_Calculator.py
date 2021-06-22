import csv
import math

plantation = '40'

rows = []

treecounter = 0
h_sum = 0
dbh_sum = 0

a_bark = 0
b_bark = 0
c_bark = 0
a_branches = 0
b_branches = 0
c_branches = 0
a_foliage = 0
b_foliage = 0
c_foliage = 0
a_wood = 0
b_wood = 0
c_wood = 0

#basalarea_sum = 0
#woodbiomass_sum = 0
#barkbiomass_sum = 0
#stembiomass_sum = 0
#foliagebiomass_sum = 0
#branchesbiomass_sum = 0
#crownbiomass_sum = 0
#totalbiomass_sum = 0
#carbonmass_sum = 0
#carbonmassmin_sum = 0
#carbonmassmax_sum = 0
#eco2mass_sum = 0
#eco2massmin_sum = 0
#eco2massmax_sum = 0

def tl_basalarea(dbh):
    basalarea = math.pi * (dbh*0.01/2)**2
#    basalarea_sum += basalarea
    return round(basalarea, 4)

def tl_woodbiomass(h, dbh, a_wood, b_wood, c_wood): #missing error terms

    if a_wood == 'N/A':
        return 'N/A'

    elif h is None:
        woodbiomass = a_wood * dbh**b_wood
#        woodbiomass_sum += woodbiomass
        return round(woodbiomass, 4)
    else:
        woodbiomass = a_wood * (dbh**b_wood) * (h**c_wood)
#        woodbiomass_sum += woodbiomass
        return round(woodbiomass, 4)

def tl_barkbiomass(h, dbh, a_bark, b_bark, c_bark): #missing error terms

    if a_bark == 'N/A':
        return 'N/A'

    elif h is None:
        barkbiomass = a_bark * dbh**b_bark
#        barkbiomass_sum += barkbiomass
        return round(barkbiomass, 4)
    else:
        barkbiomass = a_bark * dbh**b_bark * h**c_bark
#        barkbiomass_sum += barkbiomass
        return round(barkbiomass, 4)

def tl_stembiomass(h, dbh): #missing error terms
    if tl_woodbiomass(h, dbh, a_wood, b_wood, c_wood) == 'N/A' or tl_barkbiomass(h, dbh, a_bark, b_bark, c_bark) == 'N/A':
        return 'N/A'
    else:
        stembiomass = tl_woodbiomass(h, dbh, a_wood, b_wood, c_wood) + tl_barkbiomass(h, dbh, a_bark, b_bark, c_bark)
#    stembiomass_sum += stembiomass
        return round(stembiomass, 4)

def tl_foliagebiomass(h, dbh, a_foliage, b_foliage, c_foliage): #missing error terms

    if a_foliage == 'N/A':
        return 'N/A'

    elif h is None:
        foliagebiomass = a_foliage * dbh**b_foliage
#        foliagebiomass_sum += foliagebiomass
        return round(foliagebiomass, 4)
    else:
        foliagebiomass = a_foliage * dbh**b_foliage * h**c_foliage
#        foliagebiomass_sum += foliagebiomass
        return round(foliagebiomass, 4)

def tl_branchesbiomass(h, dbh, a_branches, b_branches, c_branches): #missing error terms

    if a_branches == 'N/A':
        return 'N/A'

    elif h is None:
        branchesbiomass = a_branches * dbh**b_branches
#        branchesbiomass_sum += branchesbiomass
        return round(branchesbiomass, 4)
    else:
        branchesbiomass = a_branches * dbh**b_branches * h**c_branches
#        branchesbiomass_sum += branchesbiomass
        return round(branchesbiomass, 4)

def tl_crownbiomass(h, dbh): #missing error terms

    if tl_foliagebiomass(h, dbh, a_foliage, b_foliage, c_foliage) == 'N/A' or tl_branchesbiomass(h, dbh, a_branches, b_branches, c_branches) == 'N/A':
        return 'N/A'
    else:
        crownbiomass = tl_foliagebiomass(h, dbh, a_foliage, b_foliage, c_foliage) + tl_branchesbiomass(h, dbh, a_branches, b_branches, c_branches)
#    crownbiomass_sum += crownbiomass
        return round(crownbiomass, 4)

def tl_totalbiomass(h, dbh): #missing error terms

    if tl_woodbiomass(h, dbh, a_wood, b_wood, c_wood) == 'N/A' or tl_barkbiomass(h, dbh, a_bark, b_bark, c_bark) == 'N/A' or tl_foliagebiomass(h, dbh, a_foliage, b_foliage, c_foliage) == 'N/A' or tl_branchesbiomass(h, dbh, a_branches, b_branches, c_branches) == 'N/A':
        return 'N/A'
    else:
        totalbiomass = tl_woodbiomass(h, dbh, a_wood, b_wood, c_wood) + tl_barkbiomass(h, dbh, a_bark, b_bark, c_bark) + tl_foliagebiomass(h, dbh, a_foliage, b_foliage, c_foliage) + tl_branchesbiomass(h, dbh, a_branches, b_branches, c_branches)
#    totalbiomass_sum += totalbiomass
        return round(totalbiomass, 4)

def tl_carbonmass(h, dbh, cperc, compartment):

    if cperc == 'N/A':
        return 'N/A'

    elif compartment == 'wood':
        f = tl_woodbiomass(h, dbh, a_wood, b_wood, c_wood)
    elif compartment == 'bark':
        f = tl_barkbiomass(h, dbh, a_bark, b_bark, c_bark)
    elif compartment == 'stem':
        f = tl_stembiomass(h, dbh)
    elif compartment == 'foliage':
        f = tl_foliagebiomass(h, dbh, a_foliage, b_foliage, c_foliage)
    elif compartment == 'branches':
        f = tl_branchesbiomass(h, dbh, a_branches, b_branches, c_branches)
    elif compartment == 'crown':
        f = tl_crownbiomass(h, dbh)
    elif compartment == 'total':
        f = tl_totalbiomass(h, dbh)

    carbonmass = f * cperc/100
#    carbonmass_sum += carbonmass
    return round(carbonmass, 4)

def tl_carbonmassmin(h, dbh, cperc, cperc_sd, compartment):
    carbonmassmin = tl_carbonmass(h, dbh, cperc, compartment)/c * (c - c_sd)
#    carbonmassmin_sum += carbonmassmin
    return carbonmassmin

def tl_carbonmassmax(h, dbh, cperc, cperc_sd, compartment):
    carbonmassmax = tl_carbonmass(h, dbh, cperc, compartment)/c * (c + c_sd)
#    carbonmassmax_sum += carbonmassmax
    return carbonmassmax

def tl_eco2mass(h, dbh, cperc, compartment):
    eco2mass = tl_carbonmass(h, dbh, cperc, compartment) * 3.67
#    eco2mass_sum += eco2mass
    return eco2mass

def tl_eco2massmin(h, dbh, cperc, cperc_sd, compartment):
    eco2massmin = tl_carbonmassmin(h, dbh, cperc_sd, compartment) * 3.67
#    eco2massmin_sum += eco2massmin
    return eco2massmin

def tl_eco2massmax(h, dbh, cperc, cperc_sd, compartment):
    eco2massmax = tl_carbonmassmax(h, dbh, cperc_sd, compartment) * 3.67
#    eco2massmax_sum += eco2massmax
    return eco2massmax

def tl_volume():
    return Null



def sl_height(h_sum, treecounter):
    height_mean = h_sum/treecounter
    return height_mean

def sl_dbh(dbh_sum, treecounter):
    dbh_mean = dbh_sum/treecounter
    return dbh_mean

def sl_basalarea(basalarea_sum, treecounter):
    basalarea_mean = basalarea_sum/treecounter
    return basalarea_mean

def sl_woodbiomass(woodbiomass_sum):
    woodbiomass = woodbiomass_sum
    return woodbiomass

def sl_barkbiomass(barkbiomass_sum):
    barkbiomass = barkbiomass_sum
    return barkbiomass

def sl_stembiomass(stembiomass_sum):
    stembiomass = stembiomass_sum
    return stembiomass

def sl_foliagebiomass(foliagebiomass_sum):
    foliagebiomass = foliagebiomass_sum
    return foliagebiomass

def sl_branchesbiomass(branchesbiomass_sum):
    branchesbiomass = branchesbiomass_sum
    return branchesbiomass

def sl_crownbiomass(crownbiomass_sum):
    crownbiomass = crownbiomass_sum
    return crownbiomass

def sl_totalbiomass(totalbiomass_sum):
    totalbiomass = totalbiomass_sum
    return totalbiomass

def sl_carbonmass(carbonmass_sum):
    carbonmass = carbonmass_sum
    return carbonmass

def sl_carbonmassmin(carbonmassmin_sum):
    carbonmassmin = carbonmassmin_sum
    return carbonmassmin

def sl_carbonmassmax(carbonmassmax_sum):
    carbonmassmax = carbonmassmax_sum
    return carbonmassmax

def sl_eco2mass(eco2mass_sum):
    eco2mass = eco2mass_sum
    return eco2mass

def sl_eco2massmin(eco2massmin_sum):
    eco2massmin = eco2massmin_sum
    return eco2massmin

def sl_eco2massmax(eco2massmax_sum):
    eco2massmax = eco2massmax_sum
    return eco2massmax

with open('CSV_Files\\Plantation '+ plantation +'.csv', 'r') as csv_data:
    csv_data_reader = csv.reader(csv_data)
#    header = csv_data_reader[0]
#    species_ind = header.index('Species')

    header = next(csv_data_reader)
    horizontal_accuracy_ind = header.index('Horizontal Accuracy (m)')
    latitude_ind = header.index('Latitude')
    longitude_ind = header.index('Longitude')
    date_ind = header.index('CreationDate')
    creator_ind = header.index('Creator')
    edit_ind = header.index('EditDate')
    editor_ind = header.index('Editor')
    species_ind = header.index('English Name')
    height_ind = header.index('Height (m)')
    dbh_ind = header.index('DBH (cm)')
#    defects_ind = header.index('Defects')
    notes_ind = header.index('Notes')
    shape_ind = header.index('Shape *')

    for line in csv_data_reader: #for each tree in the dataset


        horizontal_accuracy = line[horizontal_accuracy_ind]
        latitude = line[latitude_ind]
        longitude = line[longitude_ind]
        date = line[date_ind]
        creator = line[creator_ind]
        edit = line[edit_ind]
        editor = line[editor_ind]
        species = line[species_ind]
        h = float(line[height_ind])
        dbh = float(line[dbh_ind])
        print(treecounter, dbh, h)
#        defects = line[defects_ind]

        if line[notes_ind] == '<Null>':
            notes = '<Null>'
        else:
            notes = line[notes_ind]

        if line[shape_ind] == '<Null>':
            shape = '<Null>'
        else:
            shape = line[shape_ind]

        treecounter += 1
#        h_sum += h
#        dbh_sum += dbh

        print(species)

        if species == 'Norway spruce':
            a_bark = 'N/A'
            b_bark = 'N/A'
            c_bark = 'N/A'
            a_branches = 'N/A'
            b_branches = 'N/A'
            c_branches = 'N/A'
            a_foliage = 'N/A'
            b_foliage = 'N/A'
            c_foliage = 'N/A'
            a_wood = 'N/A'
            b_wood = 'N/A'
            c_wood = 'N/A'
            cperc = 'N/A'
            cperc_sd = 'N/A'
            hperc = 'N/A'
            hperc_sd = 'N/A'

            rows.append([plantation, species, h, dbh, notes, tl_basalarea(dbh), tl_woodbiomass(h, dbh, a_wood, b_wood, c_wood), tl_carbonmass(h, dbh, cperc, 'wood'), tl_barkbiomass(h, dbh, a_bark, b_bark, c_bark), tl_carbonmass(h, dbh, cperc, 'bark'), tl_stembiomass(h, dbh), tl_carbonmass(h, dbh, cperc, 'stem'), tl_foliagebiomass(h, dbh, a_foliage, b_foliage, c_foliage), tl_carbonmass(h, dbh, cperc, 'foliage'), tl_branchesbiomass(h, dbh, a_branches, b_branches, c_branches), tl_carbonmass(h, dbh, cperc, 'branches'), tl_crownbiomass(h, dbh), tl_carbonmass(h, dbh, cperc, 'crown'), tl_totalbiomass(h, dbh), tl_carbonmass(h, dbh, cperc, 'total'), horizontal_accuracy, latitude, longitude, date, creator, edit, editor, shape])
        else:

            if h is None:

                with open('CSV_Files\\Tree-Level allometric equations dbh.csv', 'r') as csv_biomass_dbh:
                    csv_biomass_dbh_reader = csv.reader(csv_biomass_dbh)

                    for line in csv_biomass_dbh_reader: #searching for a and b parameters in dbh-only allometry
                        if line[0] == species and line[2] == 'Bark':
                            a_bark = float(line[4])
                            b_bark = float(line[5])
                        elif line[0] == species and line[2] == 'Branches':
                            a_branches = float(line[4])
                            b_branches = float(line[5])
                        elif line[0] == species and line[2] == 'Foliage':
                            a_foliage = float(line[4])
                            b_foliage = float(line[5])
                        elif line[0] == species and line[2] == 'Wood':
                            a_wood = float(line[4])
                            b_wood = float(line[5])

                with open('CSV_Files\\Tree-level nutrient values.csv', 'r') as csv_nutrient:
                    csv_nutrient_reader = csv.reader(csv_nutrient)

                    for line in csv_nutrient_reader: #searching for carbon and hydrogen values
                        if line[0] == species:
                            c = float(line[3])
                            c_sd = float(line[4])
                            h = float(line[5])
                            h_sd = float(line[6])

                rows.append([plantation, species, h, dbh, notes, tl_basalarea(dbh), tl_woodbiomass(h, dbh, a_wood, b_wood, c_wood), tl_carbonmass(h, dbh, cperc, 'wood'), tl_barkbiomass(h, dbh, a_bark, b_bark, c_bark), tl_carbonmass(h, dbh, cperc, 'bark'), tl_stembiomass(h, dbh), tl_carbonmass(h, dbh, cperc, 'stem'), tl_foliagebiomass(h, dbh, a_foliage, b_foliage, c_foliage), tl_carbonmass(h, dbh, cperc, 'foliage'), tl_branchesbiomass(h, dbh, a_branches, b_branches, c_branches), tl_carbonmass(h, dbh, cperc, 'branches'), tl_crownbiomass(h, dbh), tl_carbonmass(h, dbh, cperc, 'crown'), tl_totalbiomass(h, dbh), tl_carbonmass(h, dbh, cperc, 'total'), horizontal_accuracy, latitude, longitude, date, creator, edit, editor, shape])
            else:

                with open('CSV_Files\\Tree-level allometric equations dbh-height.csv', 'r') as csv_biomass_dbh_h:
                    csv_biomass_dbh_h_reader = csv.reader(csv_biomass_dbh_h)

                    for line in csv_biomass_dbh_h_reader: #searching for a, b and c parameters in dbh-&-h allometry
                        if line[0] == species and line[2] == 'Bark':
                            a_bark = float(line[4])
                            b_bark = float(line[5])
                            c_bark = float(line[6])
                        elif line[0] == species and line[2] == 'Branches':
                            a_branches = float(line[4])
                            b_branches = float(line[5])
                            c_branches = float(line[6])
                        elif line[0] == species and line[2] == 'Foliage':
                            a_foliage = float(line[4])
                            b_foliage = float(line[5])
                            c_foliage = float(line[6])
                        elif line[0] == species and line[2] == 'Wood':
                            a_wood = float(line[4])
                            b_wood = float(line[5])
                            c_wood = float(line[6])

                with open('CSV_Files\\Tree-level nutrient values.csv', 'r') as csv_nutrient:
                    csv_nutrient_reader = csv.reader(csv_nutrient)

                    for line in csv_nutrient_reader: #searching for carbon and hydrogen values
                        if line[0] == species:
                            cperc = float(line[3])
                            cperc_sd = float(line[4])
                            hperc = float(line[5])
                            hperc_sd = float(line[6])

                rows.append([plantation, species, h, dbh, notes, tl_basalarea(dbh), tl_woodbiomass(h, dbh, a_wood, b_wood, c_wood), tl_carbonmass(h, dbh, cperc, 'wood'), tl_barkbiomass(h, dbh, a_bark, b_bark, c_bark), tl_carbonmass(h, dbh, cperc, 'bark'), tl_stembiomass(h, dbh), tl_carbonmass(h, dbh, cperc, 'stem'), tl_foliagebiomass(h, dbh, a_foliage, b_foliage, c_foliage), tl_carbonmass(h, dbh, cperc, 'foliage'), tl_branchesbiomass(h, dbh, a_branches, b_branches, c_branches), tl_carbonmass(h, dbh, cperc, 'branches'), tl_crownbiomass(h, dbh), tl_carbonmass(h, dbh, cperc, 'crown'), tl_totalbiomass(h, dbh), tl_carbonmass(h, dbh, cperc, 'total'), horizontal_accuracy, latitude, longitude, date, creator, edit, editor, shape])
#need to add defects after 'notes'


with open('CSV_Files\\Plantation '+ plantation + ' New.csv', 'w', newline = '') as csv_data_new:
    csv_data_writer = csv.writer(csv_data_new)

    csv_data_writer.writerow(['Plantation', 'Species (English)', 'Height (m)', 'DBH (cm)', 'Notes', 'Basal Area (m2)', 'Wood Biomass (kg)', 'Carbon Mass of Wood (kg)', 'Bark Biomass (kg)', 'Carbon Mass of Bark (kg)', 'Stem Biomass (kg)', 'Carbon Mass of Stem (kg)', 'Foliage Biomass (kg)', 'Carbon Mass of Foliage (kg)', 'Branches Biomass (kg)', 'Carbon Mass of Branches (kg)', 'Crown Biomass (kg)', 'Carbon Mass of Crown (kg)', 'Total Biomass (kg)', 'Carbon Mass of Total (kg)', 'Horizontal Accuracy (m)', 'Latitude', 'Longitude', 'Creation Date', 'Creator', 'Edit Date', 'Editor', 'Shape *'])

    for row in rows:
        csv_data_writer.writerow(row)
