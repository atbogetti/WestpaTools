"""
Unit and regression test for the westpatools package.
"""

# Import package, test suite, and other packages as needed
import wtools
import pytest
import sys

def test_westpatools_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "wtools" in sys.modules
