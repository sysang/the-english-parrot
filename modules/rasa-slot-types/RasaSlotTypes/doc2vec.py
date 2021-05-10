import os

import numpy as np
from rasa.shared.core.slots import Slot
from gensim.models.doc2vec import Doc2Vec
from gensim.models.callbacks import CallbackAny2Vec

import logging
logger = logging.getLogger(__name__)


logger.info('Loading doc2vec model...')
model_file = os.path.join(os.path.dirname(__file__), 'models/mc_d15_n67_w5_mc99_s00005_ech05_mal0002x25_blogwikgutimdb.bin')
logger.info(model_file)
model = Doc2Vec.load(model_file)
logger.info('...completed loading doc2vec model.')

caches = dict()


def transform_to_vector(sentence):
    if sentence not in caches:
        tokens = sentence.split(' ')
        result = model.infer_vector(tokens)
        caches[sentence] = result.tolist()

    return caches.get(sentence)


class WordVector(Slot):

    def feature_dimensionality(self):
        return 15

    def as_feature(self):
        dim = self.feature_dimensionality()
        r = [0.0] * dim

        if not self.value:
            return r

        r = transform_to_vector(self.value)

        return r
