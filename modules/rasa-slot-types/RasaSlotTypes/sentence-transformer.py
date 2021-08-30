import os

from rasa.shared.core.slots import Slot
from sentence_transformers import SentenceTransformer

import logging
logger = logging.getLogger(__name__)

from lru import LRU

MODEL_NAME = 'paraphrase-MiniLM-L6-v2'


class Model():
    __instance = None

    @staticmethod
    def getInstance():
        if Model.__instance is None:
            Model()
        return Model.__instance

    def __init__(self):

        if Model.__instance is not None:
            raise Exception("This class is a singleton! Use Model.getInstance() instead.")
        else:
            self.model = SentenceTransformer(MODEL_NAME)
            logger.info(f"Loaded Sentence Transformer pre-trained model {MODEL_NAME}")

            self.caches = LRU(100)

            Model.__instance = self

    def infer_sentence_vector(self, sentence):
        key = "".join((sentence.split()))
        if key not in self.caches:
            result = self.model.infer_vector(sentence)
            self.caches[key] = result.tolist()

        return self.caches.get(key)


class EmbeddedSentence(Slot):
    def __init__(self, *args, **kwargs):
        super(WordVector, self).__init__(*args, **kwargs)
        self.model = Model.getInstance()

    def feature_dimensionality(self):
        return 384

    def as_feature(self):
        dim = self.feature_dimensionality()
        r = [0.0] * dim

        if not self.value:
            return r

        r = self.model.infer_sentence_vector(self.value)

        return r
