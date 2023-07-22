#
# Python: 3.11.4
#
# Coder: James Santa

#parent class
class house:
    #Items a home will need
    name = 'No Owner Name Provided'
    roofType = 'Roofing Type Not Provided'
    doorType = 'Door Types Not Provided'
    windowsCount = 0

#child class
class garage(house):
    #Additional items a garage may need
    insulationType = 'Insulation Type Not Provided'
    electrical = 'Electrical Needs Not Provided?'

#child class
class shed(house):
    #Additional items a shed may need
    slab = 'Slab Type Not Provided'
    style = 'Shed Style Not Provided'
    
