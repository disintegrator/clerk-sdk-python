"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from clerk_backend_api.utils import FieldMetadata, QueryParamMetadata
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GetUsersCountRequestTypedDict(TypedDict):
    email_address: NotRequired[List[str]]
    r"""Counts users with the specified email addresses.
    Accepts up to 100 email addresses.
    Any email addresses not found are ignored.
    """
    phone_number: NotRequired[List[str]]
    r"""Counts users with the specified phone numbers.
    Accepts up to 100 phone numbers.
    Any phone numbers not found are ignored.
    """
    external_id: NotRequired[List[str]]
    r"""Counts users with the specified external ids.
    Accepts up to 100 external ids.
    Any external ids not found are ignored.
    """
    username: NotRequired[List[str]]
    r"""Counts users with the specified usernames.
    Accepts up to 100 usernames.
    Any usernames not found are ignored.
    """
    web3_wallet: NotRequired[List[str]]
    r"""Counts users with the specified web3 wallet addresses.
    Accepts up to 100 web3 wallet addresses.
    Any web3 wallet addressed not found are ignored.
    """
    user_id: NotRequired[List[str]]
    r"""Counts users with the user ids specified.
    Accepts up to 100 user ids.
    Any user ids not found are ignored.
    """
    query: NotRequired[str]
    r"""Counts users that match the given query.
    For possible matches, we check the email addresses, phone numbers, usernames, web3 wallets, user ids, first and last names.
    The query value doesn't need to match the exact value you are looking for, it is capable of partial matches as well.
    """
    

class GetUsersCountRequest(BaseModel):
    email_address: Annotated[Optional[List[str]], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    r"""Counts users with the specified email addresses.
    Accepts up to 100 email addresses.
    Any email addresses not found are ignored.
    """
    phone_number: Annotated[Optional[List[str]], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    r"""Counts users with the specified phone numbers.
    Accepts up to 100 phone numbers.
    Any phone numbers not found are ignored.
    """
    external_id: Annotated[Optional[List[str]], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    r"""Counts users with the specified external ids.
    Accepts up to 100 external ids.
    Any external ids not found are ignored.
    """
    username: Annotated[Optional[List[str]], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    r"""Counts users with the specified usernames.
    Accepts up to 100 usernames.
    Any usernames not found are ignored.
    """
    web3_wallet: Annotated[Optional[List[str]], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    r"""Counts users with the specified web3 wallet addresses.
    Accepts up to 100 web3 wallet addresses.
    Any web3 wallet addressed not found are ignored.
    """
    user_id: Annotated[Optional[List[str]], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    r"""Counts users with the user ids specified.
    Accepts up to 100 user ids.
    Any user ids not found are ignored.
    """
    query: Annotated[Optional[str], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    r"""Counts users that match the given query.
    For possible matches, we check the email addresses, phone numbers, usernames, web3 wallets, user ids, first and last names.
    The query value doesn't need to match the exact value you are looking for, it is capable of partial matches as well.
    """
    