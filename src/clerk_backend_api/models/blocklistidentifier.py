"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from enum import Enum
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class BlocklistIdentifierObject(str, Enum):
    r"""String representing the object's type. Objects of the same type share the same value.

    """
    BLOCKLIST_IDENTIFIER = "blocklist_identifier"


class BlocklistIdentifierIdentifierType(str, Enum):
    EMAIL_ADDRESS = "email_address"
    PHONE_NUMBER = "phone_number"
    WEB3_WALLET = "web3_wallet"


class BlocklistIdentifierTypedDict(TypedDict):
    object: NotRequired[BlocklistIdentifierObject]
    r"""String representing the object's type. Objects of the same type share the same value.

    """
    id: NotRequired[str]
    identifier: NotRequired[str]
    r"""An email address, email domain, phone number or web3 wallet.

    """
    identifier_type: NotRequired[BlocklistIdentifierIdentifierType]
    instance_id: NotRequired[str]
    created_at: NotRequired[int]
    r"""Unix timestamp of creation

    """
    updated_at: NotRequired[int]
    r"""Unix timestamp of last update.

    """
    

class BlocklistIdentifier(BaseModel):
    object: Optional[BlocklistIdentifierObject] = None
    r"""String representing the object's type. Objects of the same type share the same value.

    """
    id: Optional[str] = None
    identifier: Optional[str] = None
    r"""An email address, email domain, phone number or web3 wallet.

    """
    identifier_type: Optional[BlocklistIdentifierIdentifierType] = None
    instance_id: Optional[str] = None
    created_at: Optional[int] = None
    r"""Unix timestamp of creation

    """
    updated_at: Optional[int] = None
    r"""Unix timestamp of last update.

    """
    
