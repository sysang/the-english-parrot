import logging
from rasa.shared.core.slots import Slot

class Influentialx10(Slot):

    def feature_dimensionality(self):
        return 10

    def as_feature(self):
        dim = self.feature_dimensionality()

        if not self.value:
            return [0.0] * dim

        return [1.0] * dim
