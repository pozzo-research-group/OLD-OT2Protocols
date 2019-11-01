from opentrons import labware, instruments, robot
robot.reset()
robot.home()

#load labware
tiprack_1000 = labware.load("tiprack-1000ul", '1')
Stock1 = labware.load("vial-20ml", '2')
vials = labware.load("vial-20ml", '3') #More scintillation vials
trash = robot.fixed_trash

P1000 = instruments.P1000_Single(
    mount = 'right',
    tip_racks = [tiprack_1000],
    trash_container = trash
)

robot.home()

P1000.pick_up_tip()

speeds = [.2,.4,.6,.8,1]
pipette_amount = [600]
P1000.aspirate(Stock1('A1'))
P1000.dispense(Stock1('A1'))
P1000.aspirate(Stock1('A1'))
P1000.dispense(Stock1('A1'))

for counter, speed in enumerate(speeds, 0):
    # distribution of the same amount at various speeds
    P1000.distribute(
        pipette_amount,
        Stock1('A1'),
        vials(counter),
        rate = speed,
        new_tip = "never")
    P1000.blow_out()
    #print(pipette_amount, rate)

P1000.drop_tip()
