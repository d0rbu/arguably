"""Test cases for list and tuple default values"""
import sys
from io import StringIO

import arguably
from . import get_and_clear_io, run_cli_and_manual


def test_list_with_default(iobuf: StringIO) -> None:
    """Test that list with default value is respected"""
    @arguably.command
    def main(*, samples: list[int] = [2, 3, 5]):
        iobuf.write(f"samples={samples}\n")
    
    argv = []
    args = []
    kwargs = dict(samples=[2, 3, 5])
    
    cli, manual = run_cli_and_manual(iobuf, main, argv, args, kwargs)
    
    assert "samples=[2, 3, 5]" in cli
    assert cli == manual


def test_tuple_with_default(iobuf: StringIO) -> None:
    """Test that tuple with default value is respected"""
    @arguably.command
    def main(*, samples: tuple[int, ...] = (2, 3)):
        iobuf.write(f"samples={samples}\n")
    
    argv = []
    args = []
    kwargs = dict(samples=(2, 3))
    
    cli, manual = run_cli_and_manual(iobuf, main, argv, args, kwargs)
    
    assert "samples=(2, 3)" in cli
    assert cli == manual


def test_fixed_tuple_with_default(iobuf: StringIO) -> None:
    """Test that fixed-size tuple with default value is respected"""
    @arguably.command
    def main(*, coords: tuple[int, int] = (10, 20)):
        iobuf.write(f"coords={coords}\n")
    
    argv = []
    args = []
    kwargs = dict(coords=(10, 20))
    
    cli, manual = run_cli_and_manual(iobuf, main, argv, args, kwargs)
    
    assert "coords=(10, 20)" in cli
    assert cli == manual


def test_list_with_default_overridden(iobuf: StringIO) -> None:
    """Test that list with default value can be overridden"""
    @arguably.command
    def main(*, samples: list[int] = [2, 3, 5]):
        iobuf.write(f"samples={samples}\n")
    
    argv = ["--samples", "7,11"]
    args = []
    kwargs = dict(samples=[7, 11])
    
    cli, manual = run_cli_and_manual(iobuf, main, argv, args, kwargs)
    
    assert "samples=[7, 11]" in cli
    assert cli == manual


def test_tuple_with_default_overridden(iobuf: StringIO) -> None:
    """Test that tuple with default value can be overridden"""
    @arguably.command
    def main(*, samples: tuple[int, ...] = (2, 3)):
        iobuf.write(f"samples={samples}\n")
    
    argv = ["--samples", "7,11"]
    args = []
    kwargs = dict(samples=(7, 11))
    
    cli, manual = run_cli_and_manual(iobuf, main, argv, args, kwargs)
    
    assert "samples=(7, 11)" in cli
    assert cli == manual


def test_list_without_default(iobuf: StringIO) -> None:
    """Test that list without default value uses empty list"""
    @arguably.command
    def main(*, samples: list[int] = []):
        iobuf.write(f"samples={samples}\n")
    
    argv = []
    args = []
    kwargs = dict(samples=[])
    
    cli, manual = run_cli_and_manual(iobuf, main, argv, args, kwargs)
    
    assert "samples=[]" in cli
    assert cli == manual


def test_tuple_without_default(iobuf: StringIO) -> None:
    """Test that tuple without default value uses empty tuple"""
    @arguably.command
    def main(*, samples: tuple[int, ...] = ()):
        iobuf.write(f"samples={samples}\n")
    
    argv = []
    args = []
    kwargs = dict(samples=())
    
    cli, manual = run_cli_and_manual(iobuf, main, argv, args, kwargs)
    
    assert "samples=()" in cli
    assert cli == manual


def test_list_positional_with_default(iobuf: StringIO) -> None:
    """Test that positional list with default value is respected"""
    @arguably.command
    def main(samples: list[int] = [2, 3, 5]):
        iobuf.write(f"samples={samples}\n")
    
    argv = []
    args = [[2, 3, 5]]
    kwargs = dict()
    
    cli, manual = run_cli_and_manual(iobuf, main, argv, args, kwargs)
    
    assert "samples=[2, 3, 5]" in cli
    assert cli == manual


def test_tuple_positional_with_default(iobuf: StringIO) -> None:
    """Test that positional tuple with default value is respected"""
    @arguably.command
    def main(samples: tuple[int, ...] = (2, 3)):
        iobuf.write(f"samples={samples}\n")
    
    argv = []
    args = [(2, 3)]
    kwargs = dict()
    
    cli, manual = run_cli_and_manual(iobuf, main, argv, args, kwargs)
    
    assert "samples=(2, 3)" in cli
    assert cli == manual
