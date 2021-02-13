import os
from brownie import accounts,network,SIGHBoosters,SIGHBoostersSale


def main():
    return deploySIGHBoosterContracts()


def deploySIGHBoosterContracts():
    if network.show_active() == 'mainnet-fork' or  network.show_active()== 'development':
        return deployScript(accounts[0])
    elif network.show_active() == 'live':
        ac = accounts.add(os.getenv('PRIVATE_KEY'))
        return deployScript(ac)

def deployScript(a1):
    boosters = SIGHBoosters.deploy('SIGH BOOSTERS', 'SBT', {'from': a1})                              # GAS FEE = $541.8
    boosterSales = SIGHBoostersSale.deploy(boosters.address, {'from':a1})                             # GAS FEE = $301.8
    boosterSales.updateAcceptedToken('0x6b175474e89094c44da98b954eedeac495271d0f', {'from':a1})       # GAS FEE = $25
    boosterSales.updateSaleTime(1613268107,{'from':a1})                                               # GAS FEE = $7
    boosters._updateBaseURI('https://slate.textile.io/ipfs/', {'from': a1})                           # GAS FEE = $7

    # ADDING 'SIGH FARMS' Booster Category and creating Boosters
    boosters.addNewBoosterType("SIGH FARMS", 10, 10, 510, {'from': a1})                               # GAS FEE = $23
    boosters.createNewBoosters(boosterSales.address,
                               ['SIGH FARMS', 'SIGH FARMS', 'SIGH FARMS', 'SIGH FARMS', 'SIGH FARMS','SIGH FARMS', 'SIGH FARMS', 'SIGH FARMS', 'SIGH FARMS', 'SIGH FARMS'],
                               ['bafybeiaonlpgtme6zsu7t2iqi5locunybsk2nidaokopdptjplmiicq2cq', 'bafybeiaonlpgtme6zsu7t2iqi5locunybsk2nidaokopdptjplmiicq2cq',
                                'bafybeiaonlpgtme6zsu7t2iqi5locunybsk2nidaokopdptjplmiicq2cq', 'bafybeiaonlpgtme6zsu7t2iqi5locunybsk2nidaokopdptjplmiicq2cq',
                                'bafybeiaonlpgtme6zsu7t2iqi5locunybsk2nidaokopdptjplmiicq2cq','bafybeiaonlpgtme6zsu7t2iqi5locunybsk2nidaokopdptjplmiicq2cq',
                                'bafybeiaonlpgtme6zsu7t2iqi5locunybsk2nidaokopdptjplmiicq2cq','bafybeiaonlpgtme6zsu7t2iqi5locunybsk2nidaokopdptjplmiicq2cq',
                                'bafybeiaonlpgtme6zsu7t2iqi5locunybsk2nidaokopdptjplmiicq2cq','bafybeiaonlpgtme6zsu7t2iqi5locunybsk2nidaokopdptjplmiicq2cq'
                                ],{'from':a1})                                                       # GAS FEE = $557

    # ADDING 'INTELLIGENCE NETWORK' Booster Category and creating Boosters
    boosters.addNewBoosterType("INTELLIGENCE NETWORK", 20, 10, 410, {'from': a1})                    # GAS FEE = $23
    boosters.createNewBoosters(boosterSales.address,
                               ['INTELLIGENCE NETWORK', 'INTELLIGENCE NETWORK', 'INTELLIGENCE NETWORK', 'INTELLIGENCE NETWORK', 'INTELLIGENCE NETWORK',
                                'INTELLIGENCE NETWORK', 'INTELLIGENCE NETWORK', 'INTELLIGENCE NETWORK', 'INTELLIGENCE NETWORK', 'INTELLIGENCE NETWORK'],
                               ['bafybeicukpotncpf7nhxi73trpgvnefkq5oklpkiuj3jwj3fug43yaecaa','bafybeicukpotncpf7nhxi73trpgvnefkq5oklpkiuj3jwj3fug43yaecaa',
                                'bafybeicukpotncpf7nhxi73trpgvnefkq5oklpkiuj3jwj3fug43yaecaa','bafybeicukpotncpf7nhxi73trpgvnefkq5oklpkiuj3jwj3fug43yaecaa',
                                'bafybeicukpotncpf7nhxi73trpgvnefkq5oklpkiuj3jwj3fug43yaecaa','bafybeicukpotncpf7nhxi73trpgvnefkq5oklpkiuj3jwj3fug43yaecaa',
                                'bafybeicukpotncpf7nhxi73trpgvnefkq5oklpkiuj3jwj3fug43yaecaa','bafybeicukpotncpf7nhxi73trpgvnefkq5oklpkiuj3jwj3fug43yaecaa',
                                'bafybeicukpotncpf7nhxi73trpgvnefkq5oklpkiuj3jwj3fug43yaecaa','bafybeicukpotncpf7nhxi73trpgvnefkq5oklpkiuj3jwj3fug43yaecaa'
                                ],{'from':a1})                                                      # GAS FEE = $550

    # ADDING 'RESEARCH LABS IN SPACE' Booster Category and creating Boosters
    boosters.addNewBoosterType("RESEARCH LABS IN SPACE", 30, 10, 310, {'from': a1})                 # GAS FEE = $23
    boosters.createNewBoosters(boosterSales.address,
                               ['RESEARCH LABS IN SPACE', 'RESEARCH LABS IN SPACE', 'RESEARCH LABS IN SPACE', 'RESEARCH LABS IN SPACE', 'RESEARCH LABS IN SPACE',
                                'RESEARCH LABS IN SPACE', 'RESEARCH LABS IN SPACE', 'RESEARCH LABS IN SPACE', 'RESEARCH LABS IN SPACE', 'RESEARCH LABS IN SPACE'],
                               ['bafybeiaogep2eudz7e3lr5vu45m6ymmlptrliub5soe74l7gsycwbou5te','bafybeiaogep2eudz7e3lr5vu45m6ymmlptrliub5soe74l7gsycwbou5te',
                                'bafybeiaogep2eudz7e3lr5vu45m6ymmlptrliub5soe74l7gsycwbou5te','bafybeiaogep2eudz7e3lr5vu45m6ymmlptrliub5soe74l7gsycwbou5te',
                                'bafybeiaogep2eudz7e3lr5vu45m6ymmlptrliub5soe74l7gsycwbou5te','bafybeiaogep2eudz7e3lr5vu45m6ymmlptrliub5soe74l7gsycwbou5te',
                                'bafybeiaogep2eudz7e3lr5vu45m6ymmlptrliub5soe74l7gsycwbou5te','bafybeiaogep2eudz7e3lr5vu45m6ymmlptrliub5soe74l7gsycwbou5te',
                                'bafybeiaogep2eudz7e3lr5vu45m6ymmlptrliub5soe74l7gsycwbou5te','bafybeiaogep2eudz7e3lr5vu45m6ymmlptrliub5soe74l7gsycwbou5te'
                                ],{'from':a1})                                                      # GAS FEE = $550

    # SETTING SALE PRIZES
    boosterSales.updateSalePrice("SIGH FARMS",1000000000000000000000,{'from':a1})                        # $8 gas fee
    boosterSales.updateSalePrice("INTELLIGENCE NETWORK",2500000000000000000000,{'from':a1})               # $8 gas fee
    boosterSales.updateSalePrice("RESEARCH LABS IN SPACE",5000000000000000000000,{'from':a1})            # $8 gas fee


boosters.createNewBoosters(boosterSales.address, ['RESEARCH LABS IN SPACE'], ['bafybeiaogep2eudz7e3lr5vu45m6ymmlptrliub5soe74l7gsycwbou5te'],{'from':a1})

