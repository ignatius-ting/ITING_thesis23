# Bridging the Semantic Gap: A Novel Biomedical Graph-Text Dataset and Its applications

The final graph-text dataset can be found in **graph_text_dataset.csv** in the home directory.
The all unique relations can be found in **relations.txt** in the home directory.

The analysis folder contains notebooks used for processing data and retrieval pipelines.


The main filtering and consolidation of UMLS data can be found in the **analysis/exploration.ipynb** notebook. 

The pipeline to connect to PubMed can be found in the **connect_pubmed.ipynb** notebook, and has been packaged into a functionalised script in the **utils.py** file for easy imports.

The **trim_word_len.ipynb** notebook is where we trim down our RDF triples based on several heuristics

**split_and_format_feature.ipynb** is for formatting of features and ground-truth labels to satisfy the various tasks and model architectures.

