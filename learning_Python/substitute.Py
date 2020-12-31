# testing functions to recreate perl substitute
#
# voorbeeld: org_string = 'testing'
#            old_part = 'ing'
#            new_part = 'en'
# result wordt dan: 'testen'
#
# deze test is overbodig: mbv string replace kan dit ook...
#
def substitute(org_string,old_part,new_part):
    '''substitute part of string'''
    return org_string.replace(old_part,new_part)

# Main program
my_string = 'testing'
kanweg    = 'ing'
newtekst  = 'en'
my_string = substitute(my_string,kanweg,newtekst)
print (f'Result = {my_string}')
#
