def choose_pipette(volume):
    """
    This function decides which pipette to use based on the volume given.
    For this function to work, you have to have P50, P300 defined before
    hand, outside this function.
    """
    values = volume
    if values == float(0):                                  # If volume is 0, well is skipped
        pass
    elif values < float(30):                                # If volume below 30uL, P50 used not P300. Greater than 30uL P300 is used.
        instrument = P50
    else:
        instrument = P300
    return instrument

def destination_well_plate(i, well_plate_list):
    """
    This function checks if you've filled the current well plate and need
    to move to the next one. Function is written to work with 96 well plate.
    For the function to work, i is the count of all the trials.
    """
    try:
        well_number = i // 96
        well_plate = well_plate_list[well_number]
    except ValueError:
          print("You ran out of space in the well plate. You either need to add new\
          well plates, or continue new experiment from where you stopped.")
    return well_plate

def transfer_list_of_volumes(source, starting_well_plate,starting_well_number, volume_list):
    P300list = [source]
    P50list  = [source]
    P300.pick_up_tip()                                          # Picks up pipette tip for both P50 and P300 to allow to alternate
    P50.pick_up_tip()
    for well_counter, values in enumerate(volume_list):
        pipette = choose_pipette(values)
        pipette.transfer(values, stock[source], starting_well_plate(starting_well_number+well_counter).top(0.5), new_tip='never')
        #pipette.touch_tip(starting_well_plate(starting_well_number+well_counter).top(0.5))         # Touches tip to remove any droplets
        pipette.blow_out(starting_well_plate(starting_well_number+well_counter).top(0.5))
    P300.drop_tip()
    P50.drop_tip()
    return len(volume_list)

def main(reagent_pos, reagent_volume, well_plate_list, starting_position):
    i = starting_position
    total_number_of_wells_needed = len(reagent_pos)*len(reagent_volume)
    available_wells = (len(well_plate_list)+1)*96 - i - 1
    if total_number_of_wells_needed > available_wells:
        print("Total number of empty wells needed for carrying out the experiment is {},\
        greater than the available empty wells {}.".format(total_number_of_wells_needed, available_wells))
        print("Either add empty wells or remove some of the combinations out from reagent_pos")
    else:
        for j in range(len(reagent_pos)):
            Q = reagent_pos[j][0]
            H = reagent_pos[j][1]
            starting_well_plate = destination_well_plate(i, well_plate_list)
            starting_well_number = i % 96
            # need another number to go from target well in to ending
            transfer_list_of_volumes(Q, starting_well_plate,starting_well_number, reagent_volume[0])
            moves = transfer_list_of_volumes(H, starting_well_plate,starting_well_number, reagent_volume[1])
            i += moves
    return

#Import Dependencies
from opentrons import labware, instruments, robot
import numpy as np
################################################################################
#Importing labware
tiprack_300 = labware.load("opentrons-tiprack-300ul", '10') # 300ul tips can be used for P300 and P50 pipettes
tiprack_300_2 = labware.load("opentrons-tiprack-300ul", '11') # Second tiprack
stock = labware.load("trough-12row", '7' ) # 12 well resovoir for stocks
A_96_well= labware.load("96-flat", '8') # Using 4, 96 wellplates labeled A-D
B_96_well= labware.load("96-flat", '9')
C_96_well= labware.load("96-flat", '5')
D_96_well= labware.load("96-flat", '6')
trash = robot.fixed_trash
################################################################################
#Importing pipettes
P300 = instruments.P300_Single(
    mount='left',
    tip_racks=[tiprack_300],
    trash_container=trash
) # Volume range = 30-300uL

P50 = instruments.P50_Single(
    mount='right',
    tip_racks=[tiprack_300_2],
    trash_container=trash
) # Volume range = 5-50uL

################################################################################
#Input volumes to pipette in uL. first list is for QAS and second is for HBD
volumes = [[7.5,15.0,30.000000000000004,45.00000000000001,51.00000000000001,60.0,
75.0,81.0,90.0,99.0,105.0,119.99999999999856,135.0,150.0,165.0,180.0,195.0,
210.0,225.0,240.00000000000003,255.00000005698485,270.0,285.0,292.5],[292.5,
285.0,270.0,254.99999999999997,248.99999999999997,240.0,225.00000000000003,
219.0,210.0,201.0,195.0,180.00000000000142,165.0,150.0,135.0,120.0,105.0,90.0,
75.0,60.0,44.99999994301515,30.0,15.000000000000002,7.500000000000001]]

#Define mixtures to create. A1-A8 are positions on 12 row trough where the stocks are located.
mixtures = np.array([['A1', 'A5'], ['A1', 'A6'], ['A1', 'A7'],['A1', 'A8'], ['A2', 'A5']])

robot.home()

main(mixtures, volumes, [A_96_well, B_96_well, C_96_well, D_96_well], 0)
