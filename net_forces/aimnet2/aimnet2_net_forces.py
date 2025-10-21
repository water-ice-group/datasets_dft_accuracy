"""
The wB97M dataset used to train the AIMNet2 potential from the paper
Anstine et al., Chem. Sci., 2025,16, 10228-10244, https://doi.org/10.1039/D4SC08572H

is available to download from
https://kilthub.cmu.edu/articles/dataset/Training_datasets_for_AIMNet2_machine-learned_neural_network_potential/27629937/2
"""


import numpy as np
import h5py
from matplotlib import pyplot as plt
from tqdm import tqdm
from ase import units


DB_FNAME = 'aimnet2_wb97m.h5'


net_forces = []
net_forces_per_atom = []


with h5py.File(DB_FNAME, 'r') as f:
    for natoms in f.keys():
        for forces in tqdm(f[natoms]['forces']):
            num_atoms = forces.shape[0]
            net_force = np.linalg.norm(np.sum(forces, axis=0))
            net_forces.append(net_force)
            net_forces_per_atom.append(net_force / num_atoms)


np.save('net_forces.npy', net_forces)
np.save('net_forces_per_atom.npy', net_forces_per_atom)