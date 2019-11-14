"""
Unit and regression test for the wess package.
"""

# Import package, test suite, and other packages as needed
import wess
import pytest
import sys

def test_wess_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "wess" in sys.modules
