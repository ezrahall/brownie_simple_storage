from brownie import SimpleStorage, accounts

EXPECTED_START_VALUE = 0
EXPECTED_UPDATE_VALUE = 15


def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    # Assert
    assert starting_value == EXPECTED_START_VALUE


def test_update_storage():
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    simple_storage.store(EXPECTED_UPDATE_VALUE, {"from": account})
    updated_value = simple_storage.retrieve()
    # Assert
    assert updated_value == EXPECTED_UPDATE_VALUE
