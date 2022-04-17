from random import randint


def _training_model_a():
    return 9


def _training_model_b():
    return 3


def _training_model_c():
    return 5


def _choose_best_model(task_instance):
    # pull the accuracies gotten from traing the models from airflows db using their task ids
    accuracies = task_instance.xcom_pull(task_ids=[
        "training model a",
        "training model b",
        "training model c"
    ])
    
    best_accuracy = max(accuracies)
    
    if best_accuracy > 8:
        return 'accurate'
    return 'inaccurate'
