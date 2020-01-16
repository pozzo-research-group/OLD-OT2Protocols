class OuzoSample:
    '''
    Create ouzo sample with colloidal stabilizer in Aq. phase:
    organic solvent, organic solvent + hydrophobe/oil, 
    water, water + colloidal stabilizer 
    
    components_dict - dictionary pointing to Component objects with context specific roles
    e.g. {'hydrophobe':Component, 'organic_solvent':Component, 'water':Component, 'stabilizer1':Component}
    
    wt_f_dict - dictionary which ties components to their respective weight fractions:
    e.g. {'hydrophobe':float, 'organic_solvent':float...'water':None}
    
    '''
    def __init__(self, mass = None, components_dict ={}, wt_f_dict ={}, density = None, stock_dict ={}):
        self.hydrophobe = components_dict['hydrophobe']
        self.organic_solvent = components_dict['organic_solvent']
        self.stabilizer1 = components_dict['stabilizer1']
        self.water = components_dict['water']
        
        self.hydrophobe_wtf = wt_f_dict['hydrophobe']
        self.organic_solvent_wtf = wt_f_dict['organic_solvent']
        self.stabilizer1_wtf = wt_f_dict['stabilizer1']
        self.water_wtf = wt_f_dict['water']
        
        self.hydrophobe_stock =stock_dict['hydrophobe'] 
        self.organic_solvent_stock =stock_dict['organic_solvent'] 
        self.stabilizer1_stock =stock_dict['stabilizer1'] 
        self.water_stock =stock_dict['water'] 
        if stabilizer1_stock.solvent1 = self.organic_solvent:
            source_organic()

        self.mass = mass
        self.hydrophobe_mass = mass * self.hydrophobe_wtf
        self.organic_solvent_mass = mass * self.organic_solvent_wthydrophobe_wtf
        self.stabilizer1_mass = mass * self.stabilizer1_wthydrophobe_wtf
        self.water_mass = mass * self.water_wthydrophobe_wtf
    
    def source_organic(self)
        self.hydrophobe_stock_mass = self.hydrophobe_mass/self.hydrophobe_stock.componentA_wtf 
        self.additional_organic_solvent_mass = self.organic_solvent_mass-(self.hydrophobe_stock_mass-self.hydrophobe_mass)

    def source_aq(self, parameter_list):
        pass



                