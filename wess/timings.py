import h5py
import numpy

def walltime(h5file):
    wallclocktime = h5file['summary']['walltime']
    print(numpy.sum(wallclocktime),"seconds")

def aggtime(h5file, tau):
    aggregatetime = h5file['summary']['n_particles']
    print(numpy.sum(aggregatetime)*tau,"picoseconds")
