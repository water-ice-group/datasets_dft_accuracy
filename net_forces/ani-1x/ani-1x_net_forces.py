"""
The ANI-1x dataset (wB97x / 6-31G* and def2-TZVPP versions) associated with paper
Smith et al., Sci Data 7, 134 (2020). https://doi.org/10.1038/s41597-020-0473-z,

is available to download from https://doi.org/10.6084/m9.figshare.c.4712477
"""


import numpy as np
import h5py
from matplotlib import pyplot as plt
from tqdm import tqdm
from ase import units


DB_FNAME = './ANI-1x.h5'
FORCES_TO_EV_A = units.Hartree / units.Angstrom


def get_force_statistics(forces_key, output_prefix):
    f = h5py.File(DB_FNAME, 'r')

    net_forces = []
    net_forces_per_atom = []

    for formula in tqdm(f):
        for forces in f[formula][forces_key]:
            if np.all(~np.isnan(forces)):
                natoms = forces.shape[0]
                net_forces.append(np.linalg.norm(np.sum(forces*FORCES_TO_EV_A, axis=0)))
                net_forces_per_atom.append(np.linalg.norm(np.sum(forces*FORCES_TO_EV_A, axis=0)) / natoms)


    np.save(f'{output_prefix}net_forces.npy', net_forces)
    np.save(f'{output_prefix}net_forces_per_atom.npy', net_forces_per_atom)


if __name__ == "__main__":
    get_force_statistics(forces_key='wb97x_dz.forces', output_prefix='wb97x_dz')
    get_force_statistics(forces_key='wb97x_tz.forces', output_prefix='wb97x_tz')