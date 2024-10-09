import matplotlib.pyplot as plt
import pytest


def test_subplots_simple():
    fig, ax = plt.subplots()

@pytest.mark.mpl_image_compare()
def test_subplots_with_pytest_mpl():
    fig, ax = plt.subplots()
    return fig