import os
import re

from gensim.models.doc2vec import Doc2Vec

import logging
logger = logging.getLogger(__name__)


def load_model():
    dirpath = os.path.join(os.path.dirname(__file__), 'models/')

    most_recent = 0
    model_fname = ''
    for entry in os.listdir(dirpath):
        if re.match(r".+\.bin$", entry):
            fname = dirpath + entry
            stat_result = os.stat(fname)
            if stat_result.st_mtime > most_recent:
                most_recent = stat_result.st_mtime
                model_fname = fname

    if model_fname:
        model = Doc2Vec.load(model_fname)
        logger.info('Loaded model: %s' % (str(model)))
        return model
    else:
        raise Exception('There is not binary file to load Doc2vec model.')


if __name__ == '__main__':
    print(load_model())

