from RasaSlotTypes import WordVector

import pprint
pp = pprint.PrettyPrinter(indent=4)

v = WordVector('test_slot')
v.value = 'bicycle'

pp.pprint("feature_dimensionality(): {}".format(v.feature_dimensionality()))
pp.pprint("as_feature():")
print(v.as_feature())
print(v.as_feature())
