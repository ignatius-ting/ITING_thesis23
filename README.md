# Bridging the Semantic Gap: A Novel Biomedical Graph-Text Dataset and Its applications

The final graph-text dataset can be found at https://drive.google.com/drive/folders/1evMLHJSX2DOUNTrhCwtwq3mQMQpu5h4q?usp=share_link

- The all unique relations can be found in **relations.txt** in the home directory.
- The analysis folder contains notebooks used for processing data and retrieval pipelines.
- The main filtering and consolidation of UMLS data can be found in the **analysis/exploration.ipynb** notebook. 
- The pipeline to connect to PubMed can be found in the **connect_pubmed.ipynb** notebook, and has been packaged into a functionalised script in the **utils.py** file for easy imports.
- The **trim_word_len.ipynb** notebook is where we trim down our RDF triples based on several heuristics
- The notebook **split_and_format_feature.ipynb** is for formatting of features and ground-truth labels to satisfy the various tasks and model architectures.

- The modelling sub-directory contains HuggingFace helper scripts as well as config files used to train models on the M3 platform.

Knowledge graphs (KGs) have proven to be particularly relevant for NLP as a representation
of semantic relations between entities. As a result, there is an entire taxonomy of NLP tasks
related to KGs. In the general domain, there
exists several benchmark datasets composed of
parallel graph-text pairs that form the basis for
one of these tasks in graph-to-text (G2T) generation. Notably, such a resource is absent in
the biomedical domain, despite having several
large-scale KGs available for use. To address
this shortcoming, we develop a pipeline to retrieve graph-text data specific to the biomedical domain. Our dataset provides a unique
and controlled distribution of semantic types
of entities and relations, covering 184 relation
types and 15 semantic types. In addition to
this, we explore the tasks of G2T and relation
extraction by using a diverse set of pre-trained
language models (PLMs) fine-tuned on our curated data. Our experiments demonstrate the
models to be very effective at relation extraction, even when given complex entity and text
sets. However, their performance in text generation for the G2T task is notably hindered by the
inherent challenges associated with obtaining
concise text labels. This challenge is particularly pronounced in the biomedical domain,
given the extensive terminology, complex relations, and intricate experimental setups that
characterise it.
