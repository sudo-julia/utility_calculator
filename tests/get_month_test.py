# -*- coding: utf-8 -*-
from io import StringIO
import pytest
from utility_calculator.misc import get_month


def test_get_month_correct(monkeypatch):
    monkeypatch.setattr("sys.stdin", StringIO("2021-07\n"))
    assert get_month() == "2021-07"


def test_get_month_incorrect(monkeypatch):
    with pytest.raises(EOFError):
        monkeypatch.setattr("sys.stdin", StringIO("2020-13\n"))
        get_month()

    with pytest.raises(EOFError):
        monkeypatch.setattr("sys.stdin", StringIO("2020-011\n"))
        get_month()
