import logging
from rasa.shared.core.slots import Slot

class SemanticValueEncoder(Slot):

    def as_feature(self):
        dim = self.feature_dimensionality()
        features = [0.0] * dim

        if not self.value:
            return features

        axes = self.axes()
        axis_order = axes.get(self.value, None)
        if not axis_order:
            return features


        influence = self.feature_influence()
        starting = axis_order * influence
        for num in range(influence):
            features[starting + num] = 1.0

        return features

    def feature_dimensionality(self):
        axes = self.axes()
        influence = self.feature_influence()

        return len(axes.keys()) * influence


class SemanticAxisX4(SemanticValueEncoder):

    def axes(self):
        return {
            "materialpr": 0,
            "actor": 1,
            "goal": 2,
            "scope": 3,
            "beneficiary": 4,
            "attributivepr": 5,
            "carrier": 6,
            "attribute": 7,
            "identifyingpr": 8,
            "identified": 9,
            "identifier": 10,
            "mentalpr": 11,
            "senser": 12,
            "phenomenon": 13,
            "behaviouralpr": 14,
            "behaver": 15,
            "verbalpr": 16,
            "sayer": 17,
            "reciver": 18,
            "verbiage": 19,
            "existantialpr": 20,
            "existent": 21,
            "nominalgrp": 22,
            "adjectivegrp": 23,
            "prepositionallocation": 24,
        }

    def feature_influence(self):
        return 4


class SemanticIntentionX4(SemanticValueEncoder):

    def axes(self):
        return {
            "nonexclamation__negative__attributivepr": 0,
            "nonexclamation__positive__materialpr": 1,
            "nonexclamation__negative__materialpr": 2,
            "nonexclamation__positive__identifyingpr": 3,
            "nonexclamation__negative__identifyingpr": 4,
            "nonexclamation__positive__attributivepr": 5,
            "nonexclamation__positive__mentalpr": 6,
            "nonexclamation__negative__mentalpr": 7,
            "affirmative__nominalgroup": 8,
            "negative__nominalgroup": 9,
            "affirmative__adjectivegroup": 10,
            "negative__adjectivegroup": 11,
            "affirmative__prepositionalphrase__location": 12,
            "negative__shortanswer": 13,
            "affirmative__shortanswer": 14,
        }

    def feature_influence(self):
        return 4
