"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from enum import Enum
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class OrganizationInvitationObject(str, Enum):
    r"""String representing the object's type. Objects of the same type share the same value.

    """
    ORGANIZATION_INVITATION = "organization_invitation"


class OrganizationInvitationPublicMetadataTypedDict(TypedDict):
    pass
    

class OrganizationInvitationPublicMetadata(BaseModel):
    pass
    

class OrganizationInvitationPrivateMetadataTypedDict(TypedDict):
    pass
    

class OrganizationInvitationPrivateMetadata(BaseModel):
    pass
    

class OrganizationInvitationTypedDict(TypedDict):
    r"""An organization invitation"""
    
    id: NotRequired[str]
    object: NotRequired[OrganizationInvitationObject]
    r"""String representing the object's type. Objects of the same type share the same value.

    """
    email_address: NotRequired[str]
    role: NotRequired[str]
    organization_id: NotRequired[str]
    status: NotRequired[str]
    public_metadata: NotRequired[OrganizationInvitationPublicMetadataTypedDict]
    private_metadata: NotRequired[OrganizationInvitationPrivateMetadataTypedDict]
    created_at: NotRequired[int]
    r"""Unix timestamp of creation."""
    updated_at: NotRequired[int]
    r"""Unix timestamp of last update."""
    

class OrganizationInvitation(BaseModel):
    r"""An organization invitation"""
    
    id: Optional[str] = None
    object: Optional[OrganizationInvitationObject] = None
    r"""String representing the object's type. Objects of the same type share the same value.

    """
    email_address: Optional[str] = None
    role: Optional[str] = None
    organization_id: Optional[str] = None
    status: Optional[str] = None
    public_metadata: Optional[OrganizationInvitationPublicMetadata] = None
    private_metadata: Optional[OrganizationInvitationPrivateMetadata] = None
    created_at: Optional[int] = None
    r"""Unix timestamp of creation."""
    updated_at: Optional[int] = None
    r"""Unix timestamp of last update."""
    
