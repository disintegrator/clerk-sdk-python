"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from clerk_backend_api.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import TypedDict
from typing_extensions import Annotated


class CreateOrganizationMembershipRequestBodyTypedDict(TypedDict):
    user_id: str
    r"""The ID of the user that will be added as a member in the organization."""
    role: str
    r"""The role that the new member will have in the organization."""
    

class CreateOrganizationMembershipRequestBody(BaseModel):
    user_id: str
    r"""The ID of the user that will be added as a member in the organization."""
    role: str
    r"""The role that the new member will have in the organization."""
    

class CreateOrganizationMembershipRequestTypedDict(TypedDict):
    organization_id: str
    r"""The ID of the organization where the new membership will be created"""
    request_body: CreateOrganizationMembershipRequestBodyTypedDict
    

class CreateOrganizationMembershipRequest(BaseModel):
    organization_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The ID of the organization where the new membership will be created"""
    request_body: Annotated[CreateOrganizationMembershipRequestBody, FieldMetadata(request=RequestMetadata(media_type="application/json"))]
    
