#!/usr/bin/env python3
import argparse
import os
import sys

import django
from datasets import load_dataset
from mosestokenizer import MosesTokenizer

current_path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.dirname(current_path)
sys.path.append(parent_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ranker_site.settings")
django.setup()
from rankings.models import Task, Assignment

parser = argparse.ArgumentParser()

parser.add_argument("--seed", default=69, type=int, help="Random seed.")
parser.add_argument("--dataset", default="glue;ax", type=str, help="Dataset to use.")
parser.add_argument("--num_samples", default=3, type=int, help="Number of tasks to create.")


def preprocess_text(text, tokenizer=None):
    if len(text) < 30:  # filter too long texts
        return False, ""
    elif "= =" in text:  # wikitext - filter headings
        return False, ""
    if tokenizer:
        tokenized = " ".join(tokenizer(text))
        text = tokenized.replace("&apos;", "'")
    return True, text


def add_tasks_to_database(dataset, num_samples=float('inf')):
    i = 1
    tokenizer = MosesTokenizer('en')
    for example in dataset:
        if i > num_samples:
            break
        good, content = preprocess_text(example['text'], tokenizer)
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

    add_tasks_to_database(dataset, args.num_samples)
    # add_assignments_for_user(1)


if __name__ == "__main__":
    args = parser.parse_args([] if "__file__" not in globals() else None)
    main(args)
    # username_to_find = 'adas'
    #
    # try:
    #     user = User.objects.get(username=username_to_find)
    #     user_id = user.id
    #     print(f"The user_id for '{username_to_find}' is {user_id}.")
    # except User.DoesNotExist:
    #     print(f"User '{username_to_find}' does not exist.")
