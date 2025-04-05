import pytest

from unlockdoc.unlockdoc import generate_doc


def test_integrated_test():
    input_file = "test/unlockdoc/example-hlr/.spec"
    output_file = "test/unlockdoc/output/example-hlr.spec"
    generate_doc(input_file, output_file)
