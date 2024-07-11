"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel, Nullable
from enum import Enum
from pydantic import model_serializer
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class SignUpObject(str, Enum):
    SIGN_UP_ATTEMPT = "sign_up_attempt"


class SignUpStatus(str, Enum):
    MISSING_REQUIREMENTS = "missing_requirements"
    COMPLETE = "complete"
    ABANDONED = "abandoned"


class VerificationsTypedDict(TypedDict):
    pass
    

class Verifications(BaseModel):
    pass
    

class SignUpUnsafeMetadataTypedDict(TypedDict):
    pass
    

class SignUpUnsafeMetadata(BaseModel):
    pass
    

class SignUpPublicMetadataTypedDict(TypedDict):
    pass
    

class SignUpPublicMetadata(BaseModel):
    pass
    

class ExternalAccountTypedDict(TypedDict):
    pass
    

class ExternalAccount(BaseModel):
    pass
    

class SignUpTypedDict(TypedDict):
    object: SignUpObject
    id: str
    status: SignUpStatus
    password_enabled: bool
    custom_action: bool
    abandon_at: int
    required_fields: NotRequired[List[str]]
    optional_fields: NotRequired[List[str]]
    missing_fields: NotRequired[List[str]]
    unverified_fields: NotRequired[List[str]]
    verifications: NotRequired[VerificationsTypedDict]
    username: NotRequired[Nullable[str]]
    email_address: NotRequired[Nullable[str]]
    phone_number: NotRequired[Nullable[str]]
    web3_wallet: NotRequired[Nullable[str]]
    first_name: NotRequired[Nullable[str]]
    last_name: NotRequired[Nullable[str]]
    unsafe_metadata: NotRequired[SignUpUnsafeMetadataTypedDict]
    public_metadata: NotRequired[SignUpPublicMetadataTypedDict]
    external_id: NotRequired[Nullable[str]]
    created_session_id: NotRequired[Nullable[str]]
    created_user_id: NotRequired[Nullable[str]]
    external_account: NotRequired[ExternalAccountTypedDict]
    

class SignUp(BaseModel):
    object: SignUpObject
    id: str
    status: SignUpStatus
    password_enabled: bool
    custom_action: bool
    abandon_at: int
    required_fields: Optional[List[str]] = None
    optional_fields: Optional[List[str]] = None
    missing_fields: Optional[List[str]] = None
    unverified_fields: Optional[List[str]] = None
    verifications: Optional[Verifications] = None
    username: Optional[Nullable[str]] = None
    email_address: Optional[Nullable[str]] = None
    phone_number: Optional[Nullable[str]] = None
    web3_wallet: Optional[Nullable[str]] = None
    first_name: Optional[Nullable[str]] = None
    last_name: Optional[Nullable[str]] = None
    unsafe_metadata: Optional[SignUpUnsafeMetadata] = None
    public_metadata: Optional[SignUpPublicMetadata] = None
    external_id: Optional[Nullable[str]] = None
    created_session_id: Optional[Nullable[str]] = None
    created_user_id: Optional[Nullable[str]] = None
    external_account: Optional[ExternalAccount] = None
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["required_fields", "optional_fields", "missing_fields", "unverified_fields", "verifications", "username", "email_address", "phone_number", "web3_wallet", "first_name", "last_name", "unsafe_metadata", "public_metadata", "external_id", "created_session_id", "created_user_id", "external_account"]
        nullable_fields = ["username", "email_address", "phone_number", "web3_wallet", "first_name", "last_name", "external_id", "created_session_id", "created_user_id"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            if val is not None:
                m[k] = val
            elif not k in optional_fields or (
                    k in optional_fields
                    and k in nullable_fields
                    and (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member
                ):
                m[k] = val

        return m
        
