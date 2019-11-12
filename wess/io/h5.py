import h5py
import numpy

def open_h5(file_location = "./west.h5"):
    h5_file = h5py.File(file_location)
    return h5_file
