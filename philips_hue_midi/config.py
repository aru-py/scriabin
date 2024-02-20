"""
config.py

This file reads and validates the configuration file.
"""

import sys
from dataclasses import dataclass, field
from typing import Any, List

import requests
import toml


def default_bridge_ip():
    """
    Calls discovery.meethue.com to get bridge ip address.
    todo phue library already has method to do this ... use that instead?
    """
    try:
        data = requests.get('https://discovery.meethue.com/').json()
        bridge_ip = data[0]['internalipaddress']
    except Exception:
        raise Exception("Could not get bridge ip dynamically. Try setting it in your config file manually.")
    return bridge_ip


def get_default_palette():
    """
    Returns warm RGB Palette.
    """
    return ["FFD1BB", "FFAB76", "FF8C42", "E76F51", "D84315"]


@dataclass
class Config:
    """
    Configuration schema (used for validation).
    """
    palette: List[str] = field(default_factory=get_default_palette)
    bridge_ip: str = field(default_factory=default_bridge_ip)
    channels: Any = field(default_factory=list)


config_path = sys.argv[1]
with open(config_path, 'r') as f:
    config = Config(**toml.load(f))
