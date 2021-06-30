import csv
import math

""" TO BE MODIFIED FOR EACH NEW FILE """

#Set your directories
InventoryDirectory = ''
#Setting indexes for values in Inventory. At the moment, it is set up to find the indexes based on their strings.
inv_plantation = ''

TranslationDirectory = 'Tree-level species translations.csv'
#Setting indexes for values in Translation
tra_english_ind = 0
tra_french_ind = 1
tra_latin_ind = 2

AllometryDirectory = 'Tree-level allometric equations dbh-height.csv'
#Setting indexes for values in Allometry
all_species_ind = 0
all_component_ind = 2
all_a_ind = 4
all_b_ind = 5
all_c_ind = 6

NutrientDirectory = 'Tree-level nutrient values.csv'
#Setting indexes for values in Nutrient
nut_species_ind = 0
nut_carbon_ind = 3
nut_carbon_sd_ind = 4
nut_hydrogen_ind = 5
nut_hydrogen_sd_ind = 6

VolumeDirectory = ''
#Setting indexes for values in Volume. TBD.

UpdatedInventoryDirectory = ''

""" DONE MODIFYING """

#Setting null values for the sum of individual parameters to calculate stand-level data
#basalarea_sum = 0
#woodbiomass_sum = 0
#barkbiomass_sum = 0
#stembiomass_sum = 0
#foliagebiomass_sum = 0
#branchesbiomass_sum = 0
#crownbiomass_sum = 0
#totalbiomass_sum = 0
#Add running carbon sum for all biomass components

def f_BasalArea(dbh):
    """Basal area function"""
    args = [dbh]
    if None in args:
        return None
    else:
        dbh_m = dbh*0.01
        basalarea = math.pi * (dbh_m/2)**2
    #    basalarea_sum += basalarea
        return round(basalarea, 4)

def f_WoodBiomass(dbh, h, a_wood, b_wood, c_wood):
    """Wood biomass function"""
    args = [dbh, h, a_wood, b_wood, c_wood]
    if None in args:
        return None
    else:
        woodbiomass = a_wood * (dbh**b_wood) * (h**c_wood)
    #    woodbiomass_sum += woodbiomass
        return round(woodbiomass, 0)

def f_BarkBiomass(dbh, h, a_bark, b_bark, c_bark):
    """Bark biomass function"""
    args = [dbh, h, a_bark, b_bark, c_bark]
    if None in args:
        return None
    else:
        barkbiomass = a_bark * (dbh**b_bark) * (h**c_bark)
    #    barkbiomass_sum += barkbiomass
        return round(barkbiomass, 0)

def f_StemBiomass(dbh, h):
    """Stem biomass function"""
    args = [dbh, h]
    if None in args:
        return None
    else:
        woodbiomass = f_WoodBiomass(dbh, h, a_wood, b_wood, c_wood)
        barkbiomass = f_BarkBiomass(dbh, h, a_bark, b_bark, c_bark)
        if woodbiomass == None or barkbiomass == None:
            return None
        else:
            stembiomass =  woodbiomass + barkbiomass
        #    stembiomass_sum += stembiomass
            return round(stembiomass, 0)

def f_FoliageBiomass(dbh, h, a_foliage, b_foliage, c_foliage): #missing error terms
    """Foliage biomass function"""
    args = [dbh, h, a_foliage, b_foliage, c_foliage]
    if None in args:
        return None
    else:
        foliagebiomass = a_foliage * dbh**b_foliage * h**c_foliage
    #    foliagebiomass_sum += foliagebiomass
        return round(foliagebiomass, 0)

def f_BranchesBiomass(dbh, h, a_branches, b_branches, c_branches): #missing error terms
    """Branches biomass function"""
    args = [dbh, h, a_branches, b_branches, c_branches]
    if None in args:
        return None
    else:
        branchesbiomass = a_branches * dbh**b_branches * h**c_branches
    #    branchesbiomass_sum += branchesbiomass
        return round(branchesbiomass, 0)

def f_CrownBiomass(dbh, h): #missing error terms
    """Crown biomass function"""
    args = [dbh, h]
    if None in args:
        return None
    else:
        foliagebiomass = f_FoliageBiomass(dbh, h, a_foliage, b_foliage, c_foliage)
        branchesbiomass = f_BranchesBiomass(dbh, h, a_branches, b_branches, c_branches)
        if foliagebiomass == None or branchesbiomass == None:
            return None
        else:
            crownbiomass = foliagebiomass + branchesbiomass
        #    crownbiomass_sum += crownbiomass
            return round(crownbiomass, 0)

def f_TotalBiomass(dbh, h): #missing error terms
    """Total biomass function"""
    args = [dbh, h]
    if None in args:
        return None
    else:
        woodbiomass = f_WoodBiomass(dbh, h, a_wood, b_wood, c_wood)
        barkbiomass = f_BarkBiomass(dbh, h, a_bark, b_bark, c_bark)
        foliagebiomass = f_FoliageBiomass(dbh, h, a_foliage, b_foliage, c_foliage)
        branchesbiomass = f_BranchesBiomass(dbh, h, a_branches, b_branches, c_branches)
        if woodbiomass == None or barkbiomass == None or foliagebiomass == None or branchesbiomass == None:
            return None
        else:
            totalbiomass = woodbiomass + barkbiomass + foliagebiomass + branchesbiomass
        #    totalbiomass_sum += totalbiomass
            return round(totalbiomass, 0)

def f_Carbon(dbh, h, carbon, compartment):
    """Carbon mass of biomass pools function"""
    args = [dbh, h, carbon, compartment]
    if None in args:
        return None
    else:
        if compartment == 'wood':
            carbonmass = f_WoodBiomass(dbh, h, a_wood, b_wood, c_wood) * carbon/100
    #        carbonwood_sum += carbonmass
            return round(carbonmass, 0)
        elif compartment == 'bark':
            carbonmass = f_BarkBiomass(dbh, h, a_bark, b_bark, c_bark) * carbon/100
    #        carbonbark_sum += carbonmass
            return round(carbonmass, 0)
        elif compartment == 'stem':
            carbonmass = f_StemBiomass(dbh, h) * carbon/100
    #        carbonstem_sum += carbonmass
            return round(carbonmass, 0)
        elif compartment == 'foliage':
            carbonmass = f_FoliageBiomass(dbh, h, a_foliage, b_foliage, c_foliage) * carbon/100
    #        carbonfoliage_sum += carbonmass
            return round(carbonmass, 0)
        elif compartment == 'branches':
            carbonmass = f_BranchesBiomass(dbh, h, a_branches, b_branches, c_branches) * carbon/100
    #        carbonbranches_sum += carbonmass
            return round(carbonmass, 0)
        elif compartment == 'crown':
            carbonmass = f_CrownBiomass(dbh, h) * carbon/100
    #        carboncrown_sum += carbonmass
            return round(carbonmass, 0)
        elif compartment == 'total':
            carbonmass = f_TotalBiomass(dbh, h) * carbon/100
    #        carbontotal_sum += carbonmass
            return round(carbonmass, 0)

def f_volume(species, dbh,h):
    """Volume of trees"""
    if species == 'White birch':
        volume = (1.2173 - 2.7952299*h + 0.1275970*dbh*h + 0.03278430*(dbh**2)*h) * 0.001
        return round(volume, 2)
    elif species == 'Grey birch':
        volume = (3.345 - 4.814*h + 0.415*dbh*h + 0.02*(dbh**2)*h) * 0.001
        return round(volume, 2)
    elif species == 'Yellow birch':
        volume = (1.4011602 - 0.0509565*(dbh**2) - 1.6089497*h - 0.109785*dbh*h + 0.0381859*(dbh**2)*h) * 0.001
        return round(volume, 2)
    elif species == 'Bitternut hickory':
        volume = (1.4011602 - 0.0509565*(dbh**2) - 1.6089497*h - 0.109785*dbh*h + 0.0381859*(dbh**2)*h)* 0.001
        return round(volume, 2)
    elif species == 'Butternut':
        volume = (1.4011602 - 0.0509565*(dbh**2) - 1.6089497*h - 0.109785*dbh*h + 0.0381859*(dbh**2)*h) * 0.001
        return round(volume, 2)
    elif species == 'White elm':
        volume = (0.7829 + 0.132188*h - 0.271184*dbh*h + 0.0395851*(dbh**2)*h) * 0.001
        return round(volume, 2)
    elif species == 'Black cherry':
        volume = (-1.8224401*h + 0.034424*(dbh**2)*h) * 0.001
        return round(volume, 2)
    elif species == 'Red oak':
        volume = (-7.6298 - 0.0911019*(h**2) + 0.035163*(dbh**2)*h) * 0.001
        return round(volume, 2)
    elif species == 'Red maple':
        volume = (-1.1724901*h - 0.03843*dbh*h + 0.03287*(dbh**2)*h) * 0.001
        return round(volume, 2)
    elif species == 'Sugar maple':
        volume = (7.5092 - 2.3793097*h + 0.0336075*(dbh**2)*h) * 0.001
        return round(volume, 2)
    elif species == 'White ash':
        volume = (6.9773 - 2.3424301*dbh + 0.21663*(dbh**2) - 0.14065*dbh*h + 0.02777*(dbh**2)*h) * 0.001
        return round(volume, 2)
    elif species == 'American beech':
        volume = (-2.5705099*h + 0.0986*dbh*h + 0.03382*(dbh**2)*h) * 0.001
        return round(volume, 2)
    elif species == 'Hop-Hornbeam':
        volume = (0.09197*(dbh**2) - 4.7163801*h + 0.40091*dbh*h + 0.01579*(dbh**2)*h) * 0.001
        return round(volume, 2)
    elif species == 'Largetooth aspen':
        volume = (-1.2628202*h + 0.0318047*(dbh**2)*h) * 0.001
        return round(volume, 2)
    elif species == 'Trembling aspen':
        volume = (-1.5881596*h + 0.0358535*(dbh**2)*h) * 0.001
        return round(volume, 2)
    elif species == 'White pine':
        volume = (-5.1688604*h + 0.489927*dbh*h + 0.0238182*(dbh**2)*h) * 0.001
        return round(volume, 2)
    elif species == 'Eastern hemlock':
        volume = (-3.0448503*h + 0.213098*dbh*h + 0.0272291*(dbh**2)*h) * 0.001
        return round(volume, 2)
    elif species == 'Basswood':
        volume = (-2.1279802*h + 0.0339905*(dbh**2)*h) * 0.001
        return round(volume, 2)
    elif species == 'Norway spruce':
        volume = 0.6715*f_BasalArea(dbh) + 0.3324*f_BasalArea(dbh)*h
        return round(volume, 2)
    elif species == 'Tamarack larch':
        volume = 0.6715*f_BasalArea(dbh) + 0.3324*f_BasalArea(dbh)*h
        return round(volume, 2)
    else:
        volume = None
        return volume

#Making an iterable list of lists to write to
rows = []
treecounter = 0

#Opening the original CSV file
with open(InventoryDirectory, 'r') as inventory:
    inventory_reader = csv.reader(inventory)

    header = next(inventory_reader)

    #Gathering the indexes of each relevant value from the header. Change the strings to those found in your header or place them in comment if not found.
    horizontalaccuracy_ind = header.index('Horizontal Accuracy (m)')
    latitude_ind = header.index('Latitude')
    longitude_ind = header.index('Longitude')
    date_ind = header.index('CreationDate')
    creator_ind = header.index('Creator')
    edit_ind = header.index('EditDate')
    editor_ind = header.index('Editor')
    species_ind = header.index('Species')
    height_ind = header.index('Height (m)')
    dbh_ind = header.index('DBH (cm)')
    defects_ind = header.index('Defects')
    notes_ind = header.index('Notes')
    shape_ind = header.index('Shape *')

    #Starting for loop. Each tree as item in the CSV file.
    for line in inventory_reader:

        treecounter += 1

        #Setting values for each tree at the indexes set above
        horizontalaccuracy = line[horizontalaccuracy_ind]
        latitude = line[latitude_ind]
        longitude = line[longitude_ind]
        date = line[date_ind]
        creator = line[creator_ind]
        edit = line[edit_ind]
        editor = line[editor_ind]
        species = line[species_ind]
        h = float(line[height_ind])
        dbh = float(line[dbh_ind])
        defects = line[defects_ind]
        if defects == '<Null>':
            defects = None
        notes = line[notes_ind]
        if notes == '<Null>':
            notes = None
        shape = line[shape_ind]
        treeid = inv_plantation + str(treecounter).zfill(3)

        #Opening Translation to fetch french and latin values
        with open(TranslationDirectory, 'r') as translation:
            translation_reader = csv.reader(translation)

            #Gathering french and latin values in Translation
            for line in translation_reader:
                if line[tra_english_ind] == species:
                    species_fr = line[tra_french_ind]
                    species_la = line[tra_latin_ind]

        #Opening Allometry to fetch a, b, and c
        with open(AllometryDirectory, 'r') as allometry:
            allometry_reader = csv.reader(allometry)

            #Gathering a, b, and c values in Allometry
            for line in allometry_reader:
                if line[all_species_ind] == species and line[all_component_ind] == 'Bark':
                    if '' in line:
                        a_bark = None
                        b_bark = None
                        c_bark = None
                    else:
                        a_bark = float(line[all_a_ind])
                        b_bark = float(line[all_b_ind])
                        c_bark = float(line[all_c_ind])
                elif line[all_species_ind] == species and line[all_component_ind] == 'Branches':
                    if '' in line:
                        a_branches = None
                        b_branches = None
                        c_branches = None
                    else:
                        a_branches = float(line[all_a_ind])
                        b_branches = float(line[all_b_ind])
                        c_branches = float(line[all_c_ind])
                elif line[all_species_ind] == species and line[all_component_ind] == 'Foliage':
                    if '' in line:
                        a_foliage = None
                        b_foliage = None
                        c_foliage = None
                    else:
                        a_foliage = float(line[all_a_ind])
                        b_foliage = float(line[all_b_ind])
                        c_foliage = float(line[all_c_ind])
                elif line[all_species_ind] == species and line[all_component_ind] == 'Wood':
                    if '' in line:
                        a_wood = None
                        b_wood = None
                        c_wood = None
                    else:
                        a_wood = float(line[all_a_ind])
                        b_wood = float(line[all_b_ind])
                        c_wood = float(line[all_c_ind])

                    #Running biomass functions
                    tl_BasalArea = f_BasalArea(dbh)
                    tl_WoodBiomass = f_WoodBiomass(dbh, h, a_wood, b_wood, c_wood)
                    tl_BarkBiomass = f_BarkBiomass(dbh, h, a_bark, b_bark, c_bark)
                    tl_StemBiomass = f_StemBiomass(dbh, h)
                    tl_FoliageBiomass = f_FoliageBiomass(dbh, h, a_foliage, b_foliage, c_foliage)
                    tl_BranchesBiomass = f_BranchesBiomass(dbh, h, a_branches, b_branches, c_branches)
                    tl_CrownBiomass = f_CrownBiomass(dbh, h)
                    tl_TotalBiomass = f_CrownBiomass(dbh, h)

        #Opening Nutrient to fetch carbon and hydrogen
        with open(NutrientDirectory, 'r') as nutrient:
            nutrient_reader = csv.reader(nutrient)

            #Gathering carbon, carbon_sd, hydrogen, and hydrogen_sd from Nutrient
            for line in nutrient_reader:
                if line[0] == species:
                    if line[nut_carbon_ind] == '':
                        carbon = None
                    else:
                        carbon = float(line[nut_carbon_ind])

                    if line[nut_carbon_sd_ind] == '':
                        carbon_sd = None
                    else:
                        carbon_sd = float(line[nut_carbon_sd_ind])
                    if line[nut_hydrogen_ind] == '':
                        hydrogen = None
                    else:
                        hydrogen = float(line[nut_hydrogen_ind])
                    if line[nut_hydrogen_sd_ind] == '':
                        hydrogen_sd = None
                    else:
                        hydrogen_sd = float(line[nut_hydrogen_sd_ind])

                    #Running carbon and hydrogen functions
                    tl_WoodCarbon = f_Carbon(dbh, h, carbon, 'wood')
                    tl_BarkCarbon = f_Carbon(dbh, h, carbon, 'bark')
                    tl_StemCarbon = f_Carbon(dbh, h, carbon, 'stem')
                    tl_FoliageCarbon = f_Carbon(dbh, h, carbon, 'foliage')
                    tl_BranchesCarbon = f_Carbon(dbh, h, carbon, 'branches')
                    tl_CrownCarbon = f_Carbon(dbh, h, carbon, 'crown')
                    tl_TotalBiomass = f_Carbon(dbh, h, carbon, 'total')

        tl_Volume = f_volume(species, dbh,h)

        #Appending new lines of relevant paramters to rows
        upd_order = [treeid, inv_plantation, species, species_fr, species_la, h, dbh, notes, defects, tl_BasalArea, carbon, tl_WoodBiomass, tl_BarkBiomass, tl_StemBiomass, tl_FoliageBiomass, tl_BranchesBiomass, tl_CrownBiomass, tl_TotalBiomass, tl_Volume, horizontalaccuracy, latitude, longitude, date, creator, edit, editor, shape]
        rows.append(upd_order)
        print(species)

#Opening a new file to write to
with open(UpdatedInventoryDirectory, 'w', newline = '') as updated_inventory:
    updated_inventory_writer = csv.writer(updated_inventory)

    #Making the header
    updated_inventory_writer.writerow(['Tree ID', 'Plantation', 'Species (English)', 'Species (French)', 'Species (Latin)', 'Height (m)', 'DBH (cm)', 'Notes', 'Defects', 'Basal Area (m2)', 'Carbon Content (%)', 'Wood Biomass (kg)', 'Bark Biomass (kg)', 'Stem Biomass (kg)', 'Foliage Biomass (kg)', 'Branches Biomass (kg)', 'Crown Biomass (kg)', 'Total Biomass (kg)', 'Volume (m3)', 'Horizontal Accuracy (m)', 'Latitude', 'Longitude', 'Creation Date', 'Creator', 'Edit Date', 'Editor', 'Shape *'])

    #Writing the updated CSV file
    for row in rows:
        updated_inventory_writer.writerow(row)
