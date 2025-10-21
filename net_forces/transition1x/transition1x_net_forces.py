"""
The Transition1x data set from the paper
Schreiner et al., Sci Data 9, 779 (2022). https://doi.org/10.1038/s41597-022-01870-w

can be downloaded from https://figshare.com/articles/dataset/Transition1x/19614657/4?file=36035789
"""


import numpy as np
import h5py
from matplotlib import pyplot as plt
from tqdm import tqdm
from ase import units


DB_FNAME = './Transition1x.h5'


def get_force_statistics():
    f = h5py.File(DB_FNAME, 'r')

    net_forces = []
    net_forces_per_atom = []

    for formula in tqdm(f['data'].keys()):
        for rxn in f['data'][formula].keys():
            for forces in f['data'][formula][rxn]['wB97x_6-31G(d).forces']:
                natoms = forces.shape[0]
                net_forces.append(np.linalg.norm(np.sum(forces, axis=0)))
                net_forces_per_atom.append(np.linalg.norm(np.sum(forces, axis=0)) / natoms)

    np.save('net_forces.npy', net_forces)
    np.save('net_forces_per_atom.npy', net_forces_per_atom)


if __name__ == "__main__":
    get_force_statistics()