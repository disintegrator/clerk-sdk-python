"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from clerk_backend_api.utils import FieldMetadata, PathParamMetadata
from typing import TypedDict
from typing_extensions import Annotated


class DeleteEmailAddressRequestTypedDict(TypedDict):
    email_address_id: str
    r"""The ID of the email address to delete"""
    

class DeleteEmailAddressRequest(BaseModel):
    email_address_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The ID of the email address to delete"""
    
