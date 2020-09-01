import re

import tarfile

from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
from gensim.models.callbacks import CallbackAny2Vec
from gensim.utils import simple_preprocess
from gensim.test.utils import datapath

import pprint
pp = pprint.PrettyPrinter(indent=4)


class EpochLogger(CallbackAny2Vec):
    '''Callback to log information about training'''

    def __init__(self):
        self.epoch = 0

    def on_epoch_begin(self, model):
        print("Epoch #{} start".format(self.epoch))

    def on_epoch_end(self, model):
        print("Epoch #{} end".format(self.epoch))
        self.epoch += 1

class MyCorpus(object):
    def __init__(self, fname):
        self.fname = fname

    def __iter__(self):
        index = 1
        with tarfile.open(self.fname, mode='r:gz') as tar:
            for member in tar.getmembers():
                if re.match(r'aclImdb/(train|test)/(pos|neg|unsup)/\d+_\d+.txt$', member.name):
                    member_bytes = tar.extractfile(member).read()
                    member_text = member_bytes.decode('utf-8', errors='replace')
                    assert member_text.count('\n') == 0
                    yield TaggedDocument(simple_preprocess(member_text), [index])
                    index += 1


def train_model(common_kwargs, corpus_file):
    stream_corpus = MyCorpus(corpus_file)
    corpus = [doc for doc in stream_corpus]
    model = Doc2Vec(**common_kwargs)
    model.build_vocab(corpus)

    model.train(corpus, total_examples=model.corpus_count, epochs=model.epochs)

    return model


def save_model(common_kwargs, corpus_file, dataset_name):
    saved_file = generate_saved_file(common_kwargs, dataset_name)
    model = train_model(common_kwargs, corpus_file)
    model.save(saved_file)


def load_model(common_kwargs, dataset_name):
    saved_file = generate_saved_file(common_kwargs, dataset_name)

    return Doc2Vec.load(saved_file)


def generate_saved_file(common_kwargs, dataset_name):
    common_kwargs['alpha'] *= 100
    format_params = {
            'algorithm': 'pvdm' if common_kwargs['dm'] == 1 else 'pvdbow',
            'params': 'hs{hs}_dmconcat{dm_concat}_vecsz{vector_size}_neg{negative}_win{window}_alpha{alpha:02.0f}_sample{sample}_minc{min_count}'.format(**common_kwargs),
            'dataset': dataset_name
        }

    return 'models/{algorithm}_{params}_{dataset}.bin'.format(**format_params)


common_kwargs = dict(
    dm=1, hs=0, dm_concat=0, vector_size=100, negative=5,
    window=10, alpha=0.05, sample=0, min_count=2,
    workers=12, epochs=20, comment='alpha=0.05',
)
# common_kwargs = dict(
#     dm=1, hs=0, dm_concat=0, vector_size=50, negative=5,
#     window=10, alpha=0.05, sample=0, min_count=3,
#     workers=12, epochs=20, comment='alpha=0.05',
# )
# common_kwargs = dict(
#     dm=1, hs=0, dm_concat=0, vector_size=50, negative=5,
#     window=10, alpha=0.05, sample=0, min_count=0,
#     workers=12, epochs=20, comment='alpha=0.05',
# )


def make_experiment():
    corpus_file = 'corpus/aclImdb_v1.tar.gz'
    dataset_name = 'aclImdb_v1'

    save_model(common_kwargs, corpus_file, dataset_name)


def evaluate_model(target=None, comparison=None):
    dataset_name = 'aclImdb_v1'

    model = load_model(common_kwargs, dataset_name)

    result = model.wv.evaluate_word_pairs(datapath('wordsim353.tsv'))
    pp.pprint(result)

    if target:
        result = model.wv.most_similar(target.split(' '))
        pp.pprint(result)
    if target and comparison:
        result = model.wv.n_similarity(target.split(' '), comparison.split(' '))
        pp.pprint(result)
        result = model.wv.wmdistance(target.split(' '), comparison.split(' '))
        pp.pprint(result)

    return model


if __name__ == "__main__":
    make_experiment()
