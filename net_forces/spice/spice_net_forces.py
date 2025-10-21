"""
Spice-2 dataset SPICE-2.0.1.hdf5 
associated with papers:

Eastman et al., Sci Data 10, 11 (2023) 
DOI: 10.1038/s41597-022-01882-6

Eastman et al.,
Journal of Chemical Theory and Computation 2024 20 (19), 8583-8593
DOI: 10.1021/acs.jctc.4c00794

can be downloaded from https://zenodo.org/records/10975225
"""


import numpy as np
import h5py
from matplotlib import pyplot as plt
from tqdm import tqdm
from ase import units


DB_FNAME = 'SPICE-2.0.1.hdf5'
FORCES_TO_EV_A = units.Hartree / units.Bohr


def get_force_statistics():
    f = h5py.File(DB_FNAME, 'r')

    net_forces = []
    net_forces_per_atom = []
    subsets = []

    for group in tqdm(f):
        for gradient in f[group]['dft_total_gradient']:
            gradient = gradient * FORCES_TO_EV_A
            forces = -gradient
            subsets.append(f[group]['subset'])
            if np.all(~np.isnan(forces)):
                net_forces.append(np.linalg.norm(np.sum(forces, axis=0)))
                net_forces_per_atom.append(np.linalg.norm(np.sum(forces, axis=0)) / forces.shape[0])


    subset_array = np.array(subsets, dtype=object)
    np.save('subsets.npy', subset_array)
    np.save('net_forces.npy', net_forces)
    np.save('net_forces_per_atom.npy', net_forces_per_atom)


if __name__ == "__main__":
    get_force_statistics()