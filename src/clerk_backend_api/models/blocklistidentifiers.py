"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from .blocklistidentifier import BlocklistIdentifier, BlocklistIdentifierTypedDict
from clerk_backend_api.types import BaseModel
from typing import List, TypedDict


class BlocklistIdentifiersTypedDict(TypedDict):
    data: List[BlocklistIdentifierTypedDict]
    total_count: int
    r"""Total number of blocklist identifiers

    """
    

class BlocklistIdentifiers(BaseModel):
    data: List[BlocklistIdentifier]
    total_count: int
    r"""Total number of blocklist identifiers

    """
    
