# -*- coding: utf-8 -*-
from io import StringIO
import pytest
from utility_calculator.misc import get_float


def test_get_float_correct(monkeypatch):
    monkeypatch.setattr("sys.stdin", StringIO("1.0\n"))
    assert get_float("float: ") == 1.0

    monkeypatch.setattr("sys.stdin", StringIO("0.78\n"))
    assert get_float("float: ") == 0.78


def test_get_float_incorrect(monkeypatch):
    with pytest.raises(EOFError):
        monkeypatch.setattr("sys.stdin", StringIO("FLOAT\n"))
        get_float("float: ")
