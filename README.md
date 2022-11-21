
# Competitive StarCraft Multi-Agent Challenge

Competitive SMAC is the extension of [SMAC](https://github.com/oxwhirl/smac) which allows to control 2 teams of the SC2 map.

It has been implemented for our paper entitled [Value-based CTDE Methods in Symmetric Two-team Markov Game: from Cooperation to Team Competition](TDB).

We also developed the corresponding [competitive pymarl](https://github.com/paleroy/competPymarl) framework to train both teams.

# Code Example
Example on how using the code is provided [here](smac/examples/random_agents_compet.py).

# Installation

## Installing competitive SMAC

Like SMAC, you can install competitive SMAC by using the following command:

```shell
$ pip install git+https://github.com/paleroy/competSmac.git
```

Alternatively, you can clone the SMAC repository and then install `smac` with its dependencies:

```shell
$ git clone https://github.com/paleroy/competSmac.git
$ pip install smac/
```

You may also need to upgrade pip: `pip install --upgrade pip` for the install to work.

## Installing StarCraft II
The installation procedure is the same as the one of [SMAC](https://github.com/oxwhirl/smac/#installing-starcraft-ii).

Note that for the paper experiments, we used the version of  4.6.2 StarCraft II for Linux.

### List the maps

We 

To see the list of SMAC maps, together with the number of ally and enemy units and episode limit, run:

```shell
$ python -m smac.bin.map_list 
```

# Citing competitive SMAC 

If you use QVMix implementation in your own work, please cite our paper: [Value-based CTDE Methods in Symmetric Two-team Markov Game: from Cooperation to Team Competition](TDB).

```tex
@inproceedings{leroy2022twoteam,
title={Value-based {CTDE} Methods in Symmetric Two-team Markov Game: from Cooperation to Team Competition},
author={Leroy, Pascal and Pisane, Jonathan and Ernst, Damien},
booktitle={Deep Reinforcement Learning Workshop NeurIPS 2022},
year={2022}
}
```
