""" 
The ANI-1xBB dataset associated with Zhang et al., J. Chem. Theory Comput. 2025, 21, 9, 4365–4374, https://doi.org/10.1021/acs.jctc.5c00347,
can be downloaded from https://kilthub.cmu.edu/articles/dataset/ANI-1xBB_dataset/28405316
"""


import numpy as np
import h5py
from matplotlib import pyplot as plt
from tqdm import tqdm
from ase import units
import glob


DB_FNAMES = sorted(glob.glob('bond_breaking_4el/*'))
FORCES_TO_EV_A = units.Hartree / units.Angstrom


def get_force_statistics(forces_key):
    net_forces = []
    net_forces_per_atom = []

    for fname in DB_FNAMES:
        data = np.load(fname)
        forces = data[forces_key]
        num_atoms = forces.shape[1]
        net_forces_block = np.linalg.norm(np.sum(forces, axis=1), axis=1) * FORCES_TO_EV_A
        net_forces += net_forces_block.tolist()
        net_forces_per_atom += (net_forces_block / num_atoms).tolist()

    np.save('net_forces.npy', net_forces)
    np.save('net_forces_per_atom.npy', net_forces_per_atom)


if __name__ == "__main__":
    get_force_statistics(forces_key='b973c_etemp5000.forces')