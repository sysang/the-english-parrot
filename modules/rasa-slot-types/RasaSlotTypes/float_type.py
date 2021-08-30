import logging
from rasa.shared.core.slots import Slot


class FloatType(Slot):

    def feature_dimensionality(self):
        return 1

    def as_feature(self):

        if not self.value:
            return 0

        return float(self.value)
