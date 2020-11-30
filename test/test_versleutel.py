import unittest
import src.geheim_schrift_functies

def test_versleutel():
    event = {
        "zin": "Geheime boodschap",
        "sleutel": "sleutel"
    }

    result = src.geheim_schrift_functies.versleutel(event, None)
    assert result['body'] == '{"versleuteld": "YplyBqprmsIwwnzlt"}'

def test_ontsleutel():
    event = {
        "zin": "YplyBqprmsIwwnzlt",
        "sleutel": "sleutel"
    }

    result = src.geheim_schrift_functies.versleutel(event, None)
    assert result['body'] == '{"versleuteld": "Geheime boodschap"}'


if __name__ == "__main__":
    test_versleutel()