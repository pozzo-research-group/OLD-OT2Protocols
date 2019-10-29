from opentrons import labware, instruments, robot
robot.reset()
robot.home()

trash = robot.fixed_trash
tiprack_1000 = labware.load("tiprack-1000ul", '4')
stock = labware.load("vial-20ml", '2')
vials = labware.load("vial-20ml", '3') #More scintillation vials

P1000 = instruments.P1000_Single(
    mount = 'right',
    tip_racks = [tiprack_1000],
    trash_container = trash
)


speeds = [.2,.4,.6,.8,1]
pipette_amount = [600]

for amount in pipette_amount:
    P1000.aspirate(Stock1(source))
    P1000.dispense(Stock1(source))
    P1000.aspirate(Stock1(source))
    P1000.dispense(Stock1(source))
    for speed in speeds:
        # distribution of the same amount at various speeds
        P1000.distribute(
            amount,
            Stock1(source),
            vials(counter),
            rate = speed,
            new_tip = "never")
        print(pipette_amount, rate)
