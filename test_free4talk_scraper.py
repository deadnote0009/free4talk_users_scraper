import pytest
import requests

from free4talk_scraper import JsonRequest, ParsedData, SaveAsCsv

_data = 0


def test_JsonRequest():
    global _data
    _data = JsonRequest.get_json_data()
    assert _data
    assert JsonRequest.status == 200


def test_ParsedData():
    parser = ParsedData(_data)
    assert parser._header == ["Name", "Id", "Followers", "following", "friends"]
    lis = list(parser.extracting_data())
    assert len(lis) >= 1


def test_SaveAsCsv():
    ob = SaveAsCsv("test.csv")
    assert ob.file == "test.csv"
    assert ob._status == 200
    assert ob.save()
    assert ob.users >= 1
