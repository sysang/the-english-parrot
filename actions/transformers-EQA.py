from transformers import pipeline

nlp = pipeline("question-answering")

#context = " Extractive Question Answering is the task of extracting an answer from a text given a question. An example of a question answering dataset is the SQuAD dataset, which is entirely based on that task. If you would like to fine-tune a model on a SQuAD task, you may leverage the examples/question-answering/run_squad.py script. "
context = "Carlos buys a new car. It's a very expensive car. It's a huge, blue, fast car. While driving down the street, Carlos sees a girl on a bicycle.  \
        She has long blond hair and is beautiful. "

result = nlp(question="What is extractive question answering?", context=context)
print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")
