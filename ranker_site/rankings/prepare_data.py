#!/usr/bin/env python3
import argparse
import os
import sys

import django
from datasets import load_dataset

current_path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.dirname(current_path)
sys.path.append(parent_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ranker_site.settings")
django.setup()
from rankings.models import Task

parser = argparse.ArgumentParser()

parser.add_argument("--seed", default=69, type=int, help="Random seed.")
parser.add_argument("--dataset", default="glue;ax", type=str, help="Dataset to use.")


def preprocess_text(text):
    if len(text) < 30:
        return False, ""
    elif "= =" in text:
        return False, ""
    return True, text.lower()


def add_tasks_to_database(dataset):
    i = 1
    for example in dataset:
        if i > 3:
            break
        good, content = preprocess_text(example['text'])
        if not good:
            continue
        task = Task(content=content)
        task.save()
        i += 1


def main(args: argparse.Namespace):
    if args.dataset.startswith("glue"):
        ds_name, ds_subset = args.dataset.split(";")
        dataset = load_dataset(ds_name, ds_subset, split="all")
        dataset = dataset.rename_column("premise", "text")
    else:
        raise ValueError("The provided dataset \"{args.dataset}\" is not supported.")

    dataset = dataset.shuffle(seed=args.seed)

    add_tasks_to_database(dataset)


if __name__ == "__main__":
    args = parser.parse_args([] if "__file__" not in globals() else None)
    main(args)
