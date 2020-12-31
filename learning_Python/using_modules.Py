#testing
from Classes import Router,Switch
#
router1 = Router('iosV','15.6.7','10.10.10.1')          # Hier wordt router1 echt gedefinieerd, eigenlijk wordt gebruik gemaakt van template Router
router2 = Router('isr4221', '16.9.5', '10.10.10.5')
switch1 = Switch('Cat9300','16.9.5','10.10.10.8')
#
#
print('Router1\n', router1.getdesc(), '\n', sep ='')
print('Router2\n', router2.getdesc(), '\n', sep ='')
print('Switch1\n', switch1.getdesc(), '\n', sep = '')
