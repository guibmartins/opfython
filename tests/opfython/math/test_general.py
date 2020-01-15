import pytest

from opfython.math import general


def test_confusion_matrix():
    labels = [1, 1, 2, 2]
    preds = [1, 1, 2, 2]

    c_matrix = general.confusion_matrix(labels, preds)

    assert c_matrix.shape == (2, 2)


def test_normalize():
    array = [1, 1, 1, 2]

    norm_array = general.normalize(array)

    assert norm_array[3] == 1.7320508075688774


def test_opf_accuracy():
    labels = [1, 1, 2, 2]
    preds = [1, 1, 1, 1]

    acc = general.opf_accuracy(labels, preds)

    assert acc == 0.5


def test_opf_accuracy_per_label():
    labels = [1, 1, 2, 2]
    preds = [1, 1, 1, 1]

    acc_per_label = general.opf_accuracy_per_label(labels, preds)

    assert acc_per_label.shape == (2,)


def test_purity():
    labels = [1, 1, 2, 2]
    preds = [1, 1, 2, 2]

    purity = general.purity(labels, preds)

    assert purity == 1
