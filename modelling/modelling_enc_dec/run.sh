#!/bin/bash

python run_summarization.py \
    --model_name_or_path razent/SciFive-base-Pubmed \
    --do_train \
    --do_eval \
    --train_file data/train.json \
    --validation_file data/val.json \
    --test_file data/test.json \
    --text_column source \
    --summary_column target \
    --source_prefix "Create a graph from the listed entities and text: " \
    --output_dir outputs/t5_large_WQ \
    --per_device_train_batch_size=4 \
    --per_device_eval_batch_size=4 \
    --predict_with_generate