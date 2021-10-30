from brownie import SimpleStorage, accounts, config


def read_contract():
    # -1 returns length -1 to index
    simple_storage = SimpleStorage[-1]
    # ABI - auto populated by brwonie
    # Address - auto populated by brownie
    print(simple_storage.retrieve())


def main():
    read_contract()
