"""
WESS
A python analysis and visualization suite for WESTPA simulations.
"""

# Add imports here
from .io import loadh5
from .timings import walltime, aggtime

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
