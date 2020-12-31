class Router:                                           #Definitie van de class (het object Router)
    '''Router Class'''                                  #docstring die de class beschrijft
    def __init__(self, model, swversion, ip_address):   #special function __init__ wordt gebruikt voor setup van de class
                                                        # dubbele underscore wordt ook: 'dunder' genoemd of 'magic methods'
                                                        # funcions binnen een class heten 'methods'
        '''initialize models'''
        self.model = model                              # To store attributes, map the name self
        self.swversion = swversion                      # values you pass to it become variables inside the object
        self.ip_address = ip_address

    def getdesc(self):
        '''return a formatted description of the router'''
        desc = f'Router model             :{self.model}\n'\
               f'Software swversion       :{self.swversion}\n'\
               f'Router Management Address:{self.ip_address}\n'
        return desc
#
class Switch(Router):
    def getdesc(self):
        '''return a formatted description of the switch'''
        desc = f'Switch model             :{self.model}\n'\
               f'Software swversion       :{self.swversion}\n'\
               f'Switch Management Address:{self.ip_address}\n'
        return desc

#router1 = Router('iosV','15.6.7','10.10.10.1')          # Hier wordt router1 echt gedefinieerd, eigenlijk wordt gebruik gemaakt van template Router
#router2 = Router('isr4221', '16.9.5', '10.10.10.5')
#switch1 = Switch('Cat9300','16.9.5','10.10.10.8')

#print(router1.model)
#router1.desc = 'virtual router'                         # achteraf toevoegen aan template mag ook...
#print(f'Router description: {router1.desc}')

#print('Router1\n', router1.getdesc(), '\n', sep ='')
#print('Router2\n', router2.getdesc(), '\n', sep ='')
#print('Switch1\n', switch1.getdesc(), '\n', sep = '')
