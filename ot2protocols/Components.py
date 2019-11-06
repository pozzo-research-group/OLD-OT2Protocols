#Class: Components
#Purpose:
class Components:
    def __init__(self, name = 'name', molecular_weight = []):
        self.name = name
        self.molecular_weight = molecular_weight



#Template
# self = Components(
#     name = '',
#     molecular_weight =
# )


oleic_acid = Components("oleic_acid", 282.47)
ethanol = Components("ethanol", 46.07)
dodecanoic_acid = Components("dodecanoic_acid", 200.32)
octanoic_acid = Components("octanoic_acid", 144.21)
geranic_acid = Components("geranic_acid", 168.23)
candelilla_wax = Components("candelilla_wax")
light_mineral_oil = Components("light_mineral_oil", 425.363)
heavy_mineral_oil = Components("heavy_mineral_oil", 452.363)
