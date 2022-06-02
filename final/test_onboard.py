from checker import onboard


def test_onboard():
    assert(onboard(1, 1))
    assert(onboard(0, 0))
    assert(not onboard(9, 9))
