from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_contract
from brownie import network, AdvancedCollectible
import pytest
import time 
from scripts.advanced_collectible.deploy_and_create import deploy_and_create


def test_can_create_advanced_collectible_integration():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    
    advanced_collectible, creation_transaction = deploy_and_create()
    time.sleep(60)

    assert advanced_collectible.tokenCounter() == 1
    