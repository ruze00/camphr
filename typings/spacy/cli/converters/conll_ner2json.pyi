"""
This type stub file was generated by pyright.
"""

from typing import Any, Optional

def conll_ner2json(
    input_data,
    n_sents=...,
    seg_sents: bool = ...,
    model: Optional[Any] = ...,
    no_print: bool = ...,
    **kwargs
):
    """
    Convert files in the CoNLL-2003 NER format and similar
    whitespace-separated columns into JSON format for use with train cli.

    The first column is the tokens, the final column is the IOB tags. If an
    additional second column is present, the second column is the tags.

    Sentences are separated with whitespace and documents can be separated
    using the line "-DOCSTART- -X- O O".

    Sample format:

    -DOCSTART- -X- O O

    I O
    like O
    London B-GPE
    and O
    New B-GPE
    York I-GPE
    City I-GPE
    . O

    """
    ...

def segment_sents_and_docs(
    doc, n_sents, doc_delimiter, model: Optional[Any] = ..., msg: Optional[Any] = ...
): ...
def segment_docs(input_data, n_sents, doc_delimiter): ...
def n_sents_info(msg, n_sents): ...
