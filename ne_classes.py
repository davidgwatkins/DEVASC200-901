class Router:
    '''Router Class'''
    def __init__(self, model, swversion, ip_addr):
        '''Initialize values'''
        self.model = model
        self.swversion = swversion
        self.ip_addr = ip_addr
    
    def getdesc(self):
        '''Return a formatted description of the router'''
        desc = f'Router Model:              {self.model}\n'\
               f'Software Version:          {self.swversion}\n'\
               f'Router Management Address: {self.ip_addr}'
        return desc

class Switch(Router):
    def getdesc(self):
        '''Return a formatted description of the switch'''
        desc = f'Switch Model:              {self.model}\n'\
               f'Software Version:          {self.swversion}\n'\
               f'Switch Management Address: {self.ip_addr}'
        return desc    