from omspy_brokers.alice_blue import *
import pytest
from unittest.mock import patch
import pendulum


@pytest.fixture
def ab():
    with patch("pya3.Aliceblue") as alice:
        broker = AliceBlue(user_id="user_id", api_key="api_key")
        broker.alice = alice
        return broker


def test_ab_authenticate(ab):
    ab.authenticate()
    ab.alice.get_session_id.side_effect = ["session_id"] * 4
    ab.alice.get_session_id.assert_called_once()
    assert ab.authenticate() == "session_id"
    assert ab.alice.get_session_id() == "session_id"
