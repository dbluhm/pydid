"""Integration tests using uni-resolver."""

import json
import logging
from pathlib import Path

import pytest

import pydid

DOCS_PATH = Path(__file__).parent / "test_docs.json"
DOCS = json.loads(DOCS_PATH.read_text())
LOGGER = logging.getLogger(__name__)


@pytest.mark.parametrize("doc", DOCS)
def test_sample_doc_deserialization(caplog, doc):
    caplog.set_level(logging.INFO)
    LOGGER.info("Doc\n%s", json.dumps(doc, indent=2))
    pydid.deserialize_document(doc)


@pytest.mark.parametrize("value", DOCS)
def test_strict_doc_deserialization(value):
    doc = pydid.deserialize_document(value)
    if doc.is_nonconformant:
        with pytest.raises(ValueError):
            pydid.deserialize_document(value, strict=True)
    elif doc.is_conformant:
        pydid.deserialize_document(value, strict=True)
