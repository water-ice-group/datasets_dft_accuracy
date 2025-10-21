"""
The QCML dataset associated wiht paper
Ganscha et al., Sci Data 12, 406 (2025). https://doi.org/10.1038/s41597-025-04720-7

can be downloaded from Google Cloud gs://qcml-datasets/tfds/
For details on downloading: https://cloud.google.com/storage/docs/downloading-objects
"""


import tensorflow as tf
import tensorflow_datasets as tfds
from ase import units
import numpy as np
import os
from tqdm import tqdm


LOCAL_DATA_DIR = 'qcml'
FORCES_TO_EV_A = units.Hartree / units.Bohr

# Note the read config to keep the same record order in both datasets.
read_config = tfds.ReadConfig(interleave_cycle_length=1)


dft_force_field = iter(tfds.load(
    'dft_force_field',
    split='full',
    data_dir=LOCAL_DATA_DIR,
    read_config=read_config,
))

net_forces = []
net_forces_per_atom = []

for item in tqdm(dft_force_field):
    forces = item['pbe0_forces'].numpy() * FORCES_TO_EV_A
    natoms = forces.shape[0]
    net_forces.append(np.linalg.norm(np.sum(forces, axis=0)))
    net_forces_per_atom.append(np.linalg.norm(np.sum(forces, axis=0)) / natoms)

np.save('net_forces.npy', net_forces)
np.save('net_forces_per_atom.npy', net_forces_per_atom)