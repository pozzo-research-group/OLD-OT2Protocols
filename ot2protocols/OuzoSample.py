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
    

        self.mass = mass
        self.hydrophobe_mass = mass * self.hydrophobe_wtf
        self.organic_solvent_mass = mass * self.organic_solvent_wtf
        self.stabilizer1_mass = mass * self.stabilizer1_wtf
        self.water_mass = mass * self.water_wtf
        
        #{component, component_mass is mass of component in sample, component_stock points to stock class 
        # object associated with object, component_wtf is the wtf of this component in sample}
        self.hydrophobe_dict = {'component':self.hydrophobe,'component_mass':self.hydrophobe_mass, 
        'component_stock':self.hydrophobe_stock, 'component_wtf':self.hydrophobe_wtf}
        self.organic_solvent_dict = {'component':self.organic_solvent,
        'component_mass':self.organic_solvent_mass, 'component_stock':self.organic_solvent_stock, 'component_wtf':self.organic_solvent_wtf}
        self.stabilizer1_dict = {'component':self.stabilizer1,
        'component_mass':self.stabilizer1_mass, 'component_stock':self.stabilizer1_stock, 'component_wtf':self.stabilizer1_wtf}
        self.water_dict = {'component':self.water,
        'component_mass':self.water_mass, 'component_stock':self.water_stock, 'component_wtf':self.water_wtf}

     
        self.additional_organic_solvent_mass = self.organic_solvent_mass
        if self.hydrophobe_stock.solvent == self.organic_solvent:
            self.source_organic(self.hydrophobe_dict)
        
        self.additional_water_mass = self.water_mass
        if self.stabilizer1.solvent == self.water:
            self.source_aq(self.stabilizer1_dict)
            self.make_prestock(self.stabilizer1_dict)

    def source_aq(self,dict_to_source):
        '''
        Update dictionary that tracks paremeters associated with this component with how much water/aq stock is necessary to make sample, 
        and simultaneously track how this affects solvent volume
        '''
        component_mass = dict_to_source['component_mass']
        component_stock = dict_to_source['component_stock']
        
        total_stock_mass = component_mass/component_stock.componentA_wtf
        solvent_stock_mass = total_stock_mass-component_mass

        dict_to_source['total_stock_mass']=total_stock_mass
        dict_to_source['solvent_stock_mass']=solvent_stock_mass
        self.additional_water_mass -= solvent_stock_mass
        return
    
    def source_organic(self, dict_to_source):
        '''
        Update dictionary that tracks paremeters associated with this component with how much organic stock is necessary to make sample, 
        and simultaneously track how this affects solvent volume
        '''
        component_mass = dict_to_source['component_mass']
        component_stock = dict_to_source['component_stock']
        
        total_stock_mass = component_mass/component_stock.componentA_wtf
        solvent_stock_mass = total_stock_mass-component_mass

        dict_to_source['total_stock_mass']=total_stock_mass
        dict_to_source['solvent_stock_mass']=solvent_stock_mass
        self.additional_organic_solvent_mass -= solvent_stock_mass

        return 


                