#!/bin/bash

python run_classification.py \
    --model_name_or_path microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext \
    --do_train \
    --do_eval \
    --train_file data/train_v2.json \
    --validation_file data/val_v2.json \
    --test_file data/test_v2.json \
    --text_column_name feature \
    --label_column_name target \
    --output_dir outputs/model_v1 \
    --metric_name f1 \
    --max_seq_length 512 \
    --per_device_train_batch_size 32 \
    --num_train_epochs 15 \

