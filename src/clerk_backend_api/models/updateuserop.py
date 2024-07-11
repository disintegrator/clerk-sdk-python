"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel, Nullable
from clerk_backend_api.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from enum import Enum
from pydantic import model_serializer
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class UpdateUserPasswordHasher(str, Enum):
    r"""The hashing algorithm that was used to generate the password digest.
    The algorithms we support at the moment are [bcrypt](https://en.wikipedia.org/wiki/Bcrypt), [bcrypt_sha256_django](https://docs.djangoproject.com/en/4.0/topics/auth/passwords/),
    [md5](https://en.wikipedia.org/wiki/MD5), pbkdf2_sha256, pbkdf2_sha512, [pbkdf2_sha256_django](https://docs.djangoproject.com/en/4.0/topics/auth/passwords/),
    [phpass](https://www.openwall.com/phpass/), [scrypt_firebase](https://firebaseopensource.com/projects/firebase/scrypt/),
    [sha256](https://en.wikipedia.org/wiki/SHA-2), [scrypt_werkzeug](https://werkzeug.palletsprojects.com/en/3.0.x/utils/#werkzeug.security.generate_password_hash)
    and the [argon2](https://argon2.online/) variants argon2i and argon2id.

    If you need support for any particular hashing algorithm, [please let us know](https://clerk.com/support).

    Note: for password hashers considered insecure (at this moment MD5 and SHA256), the corresponding user password hashes will be transparently migrated to Bcrypt (a secure hasher) upon the user's first successful password sign in.
    Insecure schemes are marked with `(insecure)` in the list below.

    Each of the supported hashers expects the incoming digest to be in a particular format. Specifically:

    **bcrypt:** The digest should be of the following form:

    `$<algorithm version>$<cost>$<salt & hash>`

    **bcrypt_sha256_django:** This is the Django-specific variant of Bcrypt, using SHA256 hashing function. The format should be as follows (as exported from Django):

    `bcrypt_sha256$$<algorithm version>$<cost>$<salt & hash>`

    **md5** (insecure): The digest should follow the regular form e.g.:

    `5f4dcc3b5aa765d61d8327deb882cf99`

    **pbkdf2_sha256:** This is the PBKDF2 algorithm using the SHA256 hashing function. The format should be as follows:

    `pbkdf2_sha256$<iterations>$<salt>$<hash>`

    Note: Both the salt and the hash are expected to be base64-encoded.

    **pbkdf2_sha512:** This is the PBKDF2 algorithm using the SHA512 hashing function. The format should be as follows:

    `pbkdf2_sha512$<iterations>$<salt>$<hash>`

    _iterations:_ The number of iterations used. Must be an integer less than 420000.
    _salt:_ The salt used when generating the hash. Must be less than bytes.
    _hash:_ The hex-encoded hash. Must have been generated with a key length less than 1024 bytes.

    **pbkdf2_sha256_django:** This is the Django-specific variant of PBKDF2 and the digest should have the following format (as exported from Django):

    `pbkdf2_sha256$<iterations>$<salt>$<hash>`

    Note: The salt is expected to be un-encoded, the hash is expected base64-encoded.

    **pbkdf2_sha1:** This is similar to pkbdf2_sha256_django, but with two differences:
    1. uses sha1 instead of sha256
    2. accepts the hash as a hex-encoded string

    The format is the following:

    `pbkdf2_sha1$<iterations>$<salt>$<hash-as-hex-string>`

    **phpass:** Portable public domain password hashing framework for use in PHP applications. Digests hashed with phpass have the following sections:

    The format is the following:

    `$P$<rounds><salt><encoded-checksum>`

    - $P$ is the prefix used to identify phpass hashes.
    - rounds is a single character encoding a 6-bit integer representing the number of rounds used.
    - salt is eight characters drawn from [./0-9A-Za-z], providing a 48-bit salt.
    - checksum is 22 characters drawn from the same set, encoding the 128-bit checksum with MD5.

    **scrypt_firebase:** The Firebase-specific variant of scrypt.
    The value is expected to have 6 segments separated by the $ character and include the following information:

    _hash:_ The actual Base64 hash. This can be retrieved when exporting the user from Firebase.
    _salt:_ The salt used to generate the above hash. Again, this is given when exporting the user.
    _signer key:_ The base64 encoded signer key.
    _salt separator:_ The base64 encoded salt separator.
    _rounds:_ The number of rounds the algorithm needs to run.
    _memory cost:_ The cost of the algorithm run

    The first 2 (hash and salt) are per user and can be retrieved when exporting the user from Firebase.
    The other 4 values (signer key, salt separator, rounds and memory cost) are project-wide settings and can be retrieved from the project's password hash parameters.

    Once you have all these, you can combine it in the following format and send this as the digest in order for Clerk to accept it:

    `<hash>$<salt>$<signer key>$<salt separator>$<rounds>$<memory cost>`

    **scrypt_werkzeug:** The Werkzeug-specific variant of scrypt.

    The value is expected to have 3 segments separated by the $ character and include the following information:

    _algorithm args:_ The algorithm used to generate the hash.
    _salt:_ The salt used to generate the above hash.
    _hash:_ The actual Base64 hash.

    The algorithm args are the parameters used to generate the hash and are included in the digest.

    **argon2i:** Algorithms in the argon2 family generate digests that encode the following information:

    _version (v):_ The argon version, version 19 is assumed
    _memory (m):_ The memory used by the algorithm (in kibibytes)
    _iterations (t):_ The number of iterations to perform
    _parallelism (p):_ The number of threads to use

    Parts are demarcated by the `$` character, with the first part identifying the algorithm variant.
    The middle part is a comma-separated list of the encoding options (memory, iterations, parallelism).
    The final part is the actual digest.

    `$argon2i$v=19$m=4096,t=3,p=1$4t6CL3P7YiHBtwESXawI8Hm20zJj4cs7/4/G3c187e0$m7RQFczcKr5bIR0IIxbpO2P0tyrLjf3eUW3M3QSwnLc`

    **argon2id:** See the previous algorithm for an explanation of the formatting.

    For the argon2id case, the value of the algorithm in the first part of the digest is `argon2id`:

    `$argon2id$v=19$m=64,t=4,p=8$Z2liZXJyaXNo$iGXEpMBTDYQ8G/71tF0qGjxRHEmR3gpGULcE93zUJVU`

    **sha256** (insecure): The digest should be a 64-length hex string, e.g.:

    `9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08`
    """
    ARGON2I = "argon2i"
    ARGON2ID = "argon2id"
    BCRYPT = "bcrypt"
    BCRYPT_SHA256_DJANGO = "bcrypt_sha256_django"
    MD5 = "md5"
    PBKDF2_SHA256 = "pbkdf2_sha256"
    PBKDF2_SHA512 = "pbkdf2_sha512"
    PBKDF2_SHA256_DJANGO = "pbkdf2_sha256_django"
    PBKDF2_SHA1 = "pbkdf2_sha1"
    PHPASS = "phpass"
    SCRYPT_FIREBASE = "scrypt_firebase"
    SCRYPT_WERKZEUG = "scrypt_werkzeug"
    SHA256 = "sha256"


class UpdateUserPublicMetadataTypedDict(TypedDict):
    r"""Metadata saved on the user, that is visible to both your Frontend and Backend APIs"""
    
    

class UpdateUserPublicMetadata(BaseModel):
    r"""Metadata saved on the user, that is visible to both your Frontend and Backend APIs"""
    
    

class UpdateUserPrivateMetadataTypedDict(TypedDict):
    r"""Metadata saved on the user, that is only visible to your Backend API"""
    
    

class UpdateUserPrivateMetadata(BaseModel):
    r"""Metadata saved on the user, that is only visible to your Backend API"""
    
    

class UpdateUserUnsafeMetadataTypedDict(TypedDict):
    r"""Metadata saved on the user, that can be updated from both the Frontend and Backend APIs.
    Note: Since this data can be modified from the frontend, it is not guaranteed to be safe.
    """
    
    

class UpdateUserUnsafeMetadata(BaseModel):
    r"""Metadata saved on the user, that can be updated from both the Frontend and Backend APIs.
    Note: Since this data can be modified from the frontend, it is not guaranteed to be safe.
    """
    
    

class UpdateUserRequestBodyTypedDict(TypedDict):
    external_id: NotRequired[Nullable[str]]
    r"""The ID of the user as used in your external systems or your previous authentication solution.
    Must be unique across your instance.
    """
    first_name: NotRequired[Nullable[str]]
    r"""The first name to assign to the user"""
    last_name: NotRequired[Nullable[str]]
    r"""The last name to assign to the user"""
    primary_email_address_id: NotRequired[str]
    r"""The ID of the email address to set as primary.
    It must be verified, and present on the current user.
    """
    notify_primary_email_address_changed: NotRequired[bool]
    r"""If set to `true`, the user will be notified that their primary email address has changed.
    By default, no notification is sent.
    """
    primary_phone_number_id: NotRequired[str]
    r"""The ID of the phone number to set as primary.
    It must be verified, and present on the current user.
    """
    primary_web3_wallet_id: NotRequired[str]
    r"""The ID of the web3 wallets to set as primary.
    It must be verified, and present on the current user.
    """
    username: NotRequired[Nullable[str]]
    r"""The username to give to the user.
    It must be unique across your instance.
    """
    profile_image_id: NotRequired[Nullable[str]]
    r"""The ID of the image to set as the user's profile image"""
    password: NotRequired[Nullable[str]]
    r"""The plaintext password to give the user.
    Must be at least 8 characters long, and can not be in any list of hacked passwords.
    """
    password_digest: NotRequired[str]
    r"""In case you already have the password digests and not the passwords, you can use them for the newly created user via this property.
    The digests should be generated with one of the supported algorithms.
    The hashing algorithm can be specified using the `password_hasher` property.
    """
    password_hasher: NotRequired[UpdateUserPasswordHasher]
    r"""The hashing algorithm that was used to generate the password digest.
    The algorithms we support at the moment are [bcrypt](https://en.wikipedia.org/wiki/Bcrypt), [bcrypt_sha256_django](https://docs.djangoproject.com/en/4.0/topics/auth/passwords/),
    [md5](https://en.wikipedia.org/wiki/MD5), pbkdf2_sha256, pbkdf2_sha512, [pbkdf2_sha256_django](https://docs.djangoproject.com/en/4.0/topics/auth/passwords/),
    [phpass](https://www.openwall.com/phpass/), [scrypt_firebase](https://firebaseopensource.com/projects/firebase/scrypt/),
    [sha256](https://en.wikipedia.org/wiki/SHA-2), [scrypt_werkzeug](https://werkzeug.palletsprojects.com/en/3.0.x/utils/#werkzeug.security.generate_password_hash)
    and the [argon2](https://argon2.online/) variants argon2i and argon2id.

    If you need support for any particular hashing algorithm, [please let us know](https://clerk.com/support).

    Note: for password hashers considered insecure (at this moment MD5 and SHA256), the corresponding user password hashes will be transparently migrated to Bcrypt (a secure hasher) upon the user's first successful password sign in.
    Insecure schemes are marked with `(insecure)` in the list below.

    Each of the supported hashers expects the incoming digest to be in a particular format. Specifically:

    **bcrypt:** The digest should be of the following form:

    `$<algorithm version>$<cost>$<salt & hash>`

    **bcrypt_sha256_django:** This is the Django-specific variant of Bcrypt, using SHA256 hashing function. The format should be as follows (as exported from Django):

    `bcrypt_sha256$$<algorithm version>$<cost>$<salt & hash>`

    **md5** (insecure): The digest should follow the regular form e.g.:

    `5f4dcc3b5aa765d61d8327deb882cf99`

    **pbkdf2_sha256:** This is the PBKDF2 algorithm using the SHA256 hashing function. The format should be as follows:

    `pbkdf2_sha256$<iterations>$<salt>$<hash>`

    Note: Both the salt and the hash are expected to be base64-encoded.

    **pbkdf2_sha512:** This is the PBKDF2 algorithm using the SHA512 hashing function. The format should be as follows:

    `pbkdf2_sha512$<iterations>$<salt>$<hash>`

    _iterations:_ The number of iterations used. Must be an integer less than 420000.
    _salt:_ The salt used when generating the hash. Must be less than bytes.
    _hash:_ The hex-encoded hash. Must have been generated with a key length less than 1024 bytes.

    **pbkdf2_sha256_django:** This is the Django-specific variant of PBKDF2 and the digest should have the following format (as exported from Django):

    `pbkdf2_sha256$<iterations>$<salt>$<hash>`

    Note: The salt is expected to be un-encoded, the hash is expected base64-encoded.

    **pbkdf2_sha1:** This is similar to pkbdf2_sha256_django, but with two differences:
    1. uses sha1 instead of sha256
    2. accepts the hash as a hex-encoded string

    The format is the following:

    `pbkdf2_sha1$<iterations>$<salt>$<hash-as-hex-string>`

    **phpass:** Portable public domain password hashing framework for use in PHP applications. Digests hashed with phpass have the following sections:

    The format is the following:

    `$P$<rounds><salt><encoded-checksum>`

    - $P$ is the prefix used to identify phpass hashes.
    - rounds is a single character encoding a 6-bit integer representing the number of rounds used.
    - salt is eight characters drawn from [./0-9A-Za-z], providing a 48-bit salt.
    - checksum is 22 characters drawn from the same set, encoding the 128-bit checksum with MD5.

    **scrypt_firebase:** The Firebase-specific variant of scrypt.
    The value is expected to have 6 segments separated by the $ character and include the following information:

    _hash:_ The actual Base64 hash. This can be retrieved when exporting the user from Firebase.
    _salt:_ The salt used to generate the above hash. Again, this is given when exporting the user.
    _signer key:_ The base64 encoded signer key.
    _salt separator:_ The base64 encoded salt separator.
    _rounds:_ The number of rounds the algorithm needs to run.
    _memory cost:_ The cost of the algorithm run

    The first 2 (hash and salt) are per user and can be retrieved when exporting the user from Firebase.
    The other 4 values (signer key, salt separator, rounds and memory cost) are project-wide settings and can be retrieved from the project's password hash parameters.

    Once you have all these, you can combine it in the following format and send this as the digest in order for Clerk to accept it:

    `<hash>$<salt>$<signer key>$<salt separator>$<rounds>$<memory cost>`

    **scrypt_werkzeug:** The Werkzeug-specific variant of scrypt.

    The value is expected to have 3 segments separated by the $ character and include the following information:

    _algorithm args:_ The algorithm used to generate the hash.
    _salt:_ The salt used to generate the above hash.
    _hash:_ The actual Base64 hash.

    The algorithm args are the parameters used to generate the hash and are included in the digest.

    **argon2i:** Algorithms in the argon2 family generate digests that encode the following information:

    _version (v):_ The argon version, version 19 is assumed
    _memory (m):_ The memory used by the algorithm (in kibibytes)
    _iterations (t):_ The number of iterations to perform
    _parallelism (p):_ The number of threads to use

    Parts are demarcated by the `$` character, with the first part identifying the algorithm variant.
    The middle part is a comma-separated list of the encoding options (memory, iterations, parallelism).
    The final part is the actual digest.

    `$argon2i$v=19$m=4096,t=3,p=1$4t6CL3P7YiHBtwESXawI8Hm20zJj4cs7/4/G3c187e0$m7RQFczcKr5bIR0IIxbpO2P0tyrLjf3eUW3M3QSwnLc`

    **argon2id:** See the previous algorithm for an explanation of the formatting.

    For the argon2id case, the value of the algorithm in the first part of the digest is `argon2id`:

    `$argon2id$v=19$m=64,t=4,p=8$Z2liZXJyaXNo$iGXEpMBTDYQ8G/71tF0qGjxRHEmR3gpGULcE93zUJVU`

    **sha256** (insecure): The digest should be a 64-length hex string, e.g.:

    `9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08`
    """
    skip_password_checks: NotRequired[Nullable[bool]]
    r"""Set it to `true` if you're updating the user's password and want to skip any password policy settings check. This parameter can only be used when providing a `password`."""
    sign_out_of_other_sessions: NotRequired[Nullable[bool]]
    r"""Set to `true` to sign out the user from all their active sessions once their password is updated. This parameter can only be used when providing a `password`."""
    totp_secret: NotRequired[str]
    r"""In case TOTP is configured on the instance, you can provide the secret to enable it on the specific user without the need to reset it.
    Please note that currently the supported options are:
    * Period: 30 seconds
    * Code length: 6 digits
    * Algorithm: SHA1
    """
    backup_codes: NotRequired[List[str]]
    r"""If Backup Codes are configured on the instance, you can provide them to enable it on the specific user without the need to reset them.
    You must provide the backup codes in plain format or the corresponding bcrypt digest.
    """
    public_metadata: NotRequired[UpdateUserPublicMetadataTypedDict]
    r"""Metadata saved on the user, that is visible to both your Frontend and Backend APIs"""
    private_metadata: NotRequired[UpdateUserPrivateMetadataTypedDict]
    r"""Metadata saved on the user, that is only visible to your Backend API"""
    unsafe_metadata: NotRequired[UpdateUserUnsafeMetadataTypedDict]
    r"""Metadata saved on the user, that can be updated from both the Frontend and Backend APIs.
    Note: Since this data can be modified from the frontend, it is not guaranteed to be safe.
    """
    delete_self_enabled: NotRequired[Nullable[bool]]
    r"""If true, the user can delete themselves with the Frontend API."""
    create_organization_enabled: NotRequired[Nullable[bool]]
    r"""If true, the user can create organizations with the Frontend API."""
    created_at: NotRequired[str]
    r"""A custom date/time denoting _when_ the user signed up to the application, specified in RFC3339 format (e.g. `2012-10-20T07:15:20.902Z`)."""
    

class UpdateUserRequestBody(BaseModel):
    external_id: Optional[Nullable[str]] = None
    r"""The ID of the user as used in your external systems or your previous authentication solution.
    Must be unique across your instance.
    """
    first_name: Optional[Nullable[str]] = None
    r"""The first name to assign to the user"""
    last_name: Optional[Nullable[str]] = None
    r"""The last name to assign to the user"""
    primary_email_address_id: Optional[str] = None
    r"""The ID of the email address to set as primary.
    It must be verified, and present on the current user.
    """
    notify_primary_email_address_changed: Optional[bool] = False
    r"""If set to `true`, the user will be notified that their primary email address has changed.
    By default, no notification is sent.
    """
    primary_phone_number_id: Optional[str] = None
    r"""The ID of the phone number to set as primary.
    It must be verified, and present on the current user.
    """
    primary_web3_wallet_id: Optional[str] = None
    r"""The ID of the web3 wallets to set as primary.
    It must be verified, and present on the current user.
    """
    username: Optional[Nullable[str]] = None
    r"""The username to give to the user.
    It must be unique across your instance.
    """
    profile_image_id: Optional[Nullable[str]] = None
    r"""The ID of the image to set as the user's profile image"""
    password: Optional[Nullable[str]] = None
    r"""The plaintext password to give the user.
    Must be at least 8 characters long, and can not be in any list of hacked passwords.
    """
    password_digest: Optional[str] = None
    r"""In case you already have the password digests and not the passwords, you can use them for the newly created user via this property.
    The digests should be generated with one of the supported algorithms.
    The hashing algorithm can be specified using the `password_hasher` property.
    """
    password_hasher: Optional[UpdateUserPasswordHasher] = None
    r"""The hashing algorithm that was used to generate the password digest.
    The algorithms we support at the moment are [bcrypt](https://en.wikipedia.org/wiki/Bcrypt), [bcrypt_sha256_django](https://docs.djangoproject.com/en/4.0/topics/auth/passwords/),
    [md5](https://en.wikipedia.org/wiki/MD5), pbkdf2_sha256, pbkdf2_sha512, [pbkdf2_sha256_django](https://docs.djangoproject.com/en/4.0/topics/auth/passwords/),
    [phpass](https://www.openwall.com/phpass/), [scrypt_firebase](https://firebaseopensource.com/projects/firebase/scrypt/),
    [sha256](https://en.wikipedia.org/wiki/SHA-2), [scrypt_werkzeug](https://werkzeug.palletsprojects.com/en/3.0.x/utils/#werkzeug.security.generate_password_hash)
    and the [argon2](https://argon2.online/) variants argon2i and argon2id.

    If you need support for any particular hashing algorithm, [please let us know](https://clerk.com/support).

    Note: for password hashers considered insecure (at this moment MD5 and SHA256), the corresponding user password hashes will be transparently migrated to Bcrypt (a secure hasher) upon the user's first successful password sign in.
    Insecure schemes are marked with `(insecure)` in the list below.

    Each of the supported hashers expects the incoming digest to be in a particular format. Specifically:

    **bcrypt:** The digest should be of the following form:

    `$<algorithm version>$<cost>$<salt & hash>`

    **bcrypt_sha256_django:** This is the Django-specific variant of Bcrypt, using SHA256 hashing function. The format should be as follows (as exported from Django):

    `bcrypt_sha256$$<algorithm version>$<cost>$<salt & hash>`

    **md5** (insecure): The digest should follow the regular form e.g.:

    `5f4dcc3b5aa765d61d8327deb882cf99`

    **pbkdf2_sha256:** This is the PBKDF2 algorithm using the SHA256 hashing function. The format should be as follows:

    `pbkdf2_sha256$<iterations>$<salt>$<hash>`

    Note: Both the salt and the hash are expected to be base64-encoded.

    **pbkdf2_sha512:** This is the PBKDF2 algorithm using the SHA512 hashing function. The format should be as follows:

    `pbkdf2_sha512$<iterations>$<salt>$<hash>`

    _iterations:_ The number of iterations used. Must be an integer less than 420000.
    _salt:_ The salt used when generating the hash. Must be less than bytes.
    _hash:_ The hex-encoded hash. Must have been generated with a key length less than 1024 bytes.

    **pbkdf2_sha256_django:** This is the Django-specific variant of PBKDF2 and the digest should have the following format (as exported from Django):

    `pbkdf2_sha256$<iterations>$<salt>$<hash>`

    Note: The salt is expected to be un-encoded, the hash is expected base64-encoded.

    **pbkdf2_sha1:** This is similar to pkbdf2_sha256_django, but with two differences:
    1. uses sha1 instead of sha256
    2. accepts the hash as a hex-encoded string

    The format is the following:

    `pbkdf2_sha1$<iterations>$<salt>$<hash-as-hex-string>`

    **phpass:** Portable public domain password hashing framework for use in PHP applications. Digests hashed with phpass have the following sections:

    The format is the following:

    `$P$<rounds><salt><encoded-checksum>`

    - $P$ is the prefix used to identify phpass hashes.
    - rounds is a single character encoding a 6-bit integer representing the number of rounds used.
    - salt is eight characters drawn from [./0-9A-Za-z], providing a 48-bit salt.
    - checksum is 22 characters drawn from the same set, encoding the 128-bit checksum with MD5.

    **scrypt_firebase:** The Firebase-specific variant of scrypt.
    The value is expected to have 6 segments separated by the $ character and include the following information:

    _hash:_ The actual Base64 hash. This can be retrieved when exporting the user from Firebase.
    _salt:_ The salt used to generate the above hash. Again, this is given when exporting the user.
    _signer key:_ The base64 encoded signer key.
    _salt separator:_ The base64 encoded salt separator.
    _rounds:_ The number of rounds the algorithm needs to run.
    _memory cost:_ The cost of the algorithm run

    The first 2 (hash and salt) are per user and can be retrieved when exporting the user from Firebase.
    The other 4 values (signer key, salt separator, rounds and memory cost) are project-wide settings and can be retrieved from the project's password hash parameters.

    Once you have all these, you can combine it in the following format and send this as the digest in order for Clerk to accept it:

    `<hash>$<salt>$<signer key>$<salt separator>$<rounds>$<memory cost>`

    **scrypt_werkzeug:** The Werkzeug-specific variant of scrypt.

    The value is expected to have 3 segments separated by the $ character and include the following information:

    _algorithm args:_ The algorithm used to generate the hash.
    _salt:_ The salt used to generate the above hash.
    _hash:_ The actual Base64 hash.

    The algorithm args are the parameters used to generate the hash and are included in the digest.

    **argon2i:** Algorithms in the argon2 family generate digests that encode the following information:

    _version (v):_ The argon version, version 19 is assumed
    _memory (m):_ The memory used by the algorithm (in kibibytes)
    _iterations (t):_ The number of iterations to perform
    _parallelism (p):_ The number of threads to use

    Parts are demarcated by the `$` character, with the first part identifying the algorithm variant.
    The middle part is a comma-separated list of the encoding options (memory, iterations, parallelism).
    The final part is the actual digest.

    `$argon2i$v=19$m=4096,t=3,p=1$4t6CL3P7YiHBtwESXawI8Hm20zJj4cs7/4/G3c187e0$m7RQFczcKr5bIR0IIxbpO2P0tyrLjf3eUW3M3QSwnLc`

    **argon2id:** See the previous algorithm for an explanation of the formatting.

    For the argon2id case, the value of the algorithm in the first part of the digest is `argon2id`:

    `$argon2id$v=19$m=64,t=4,p=8$Z2liZXJyaXNo$iGXEpMBTDYQ8G/71tF0qGjxRHEmR3gpGULcE93zUJVU`

    **sha256** (insecure): The digest should be a 64-length hex string, e.g.:

    `9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08`
    """
    skip_password_checks: Optional[Nullable[bool]] = None
    r"""Set it to `true` if you're updating the user's password and want to skip any password policy settings check. This parameter can only be used when providing a `password`."""
    sign_out_of_other_sessions: Optional[Nullable[bool]] = None
    r"""Set to `true` to sign out the user from all their active sessions once their password is updated. This parameter can only be used when providing a `password`."""
    totp_secret: Optional[str] = None
    r"""In case TOTP is configured on the instance, you can provide the secret to enable it on the specific user without the need to reset it.
    Please note that currently the supported options are:
    * Period: 30 seconds
    * Code length: 6 digits
    * Algorithm: SHA1
    """
    backup_codes: Optional[List[str]] = None
    r"""If Backup Codes are configured on the instance, you can provide them to enable it on the specific user without the need to reset them.
    You must provide the backup codes in plain format or the corresponding bcrypt digest.
    """
    public_metadata: Optional[UpdateUserPublicMetadata] = None
    r"""Metadata saved on the user, that is visible to both your Frontend and Backend APIs"""
    private_metadata: Optional[UpdateUserPrivateMetadata] = None
    r"""Metadata saved on the user, that is only visible to your Backend API"""
    unsafe_metadata: Optional[UpdateUserUnsafeMetadata] = None
    r"""Metadata saved on the user, that can be updated from both the Frontend and Backend APIs.
    Note: Since this data can be modified from the frontend, it is not guaranteed to be safe.
    """
    delete_self_enabled: Optional[Nullable[bool]] = None
    r"""If true, the user can delete themselves with the Frontend API."""
    create_organization_enabled: Optional[Nullable[bool]] = None
    r"""If true, the user can create organizations with the Frontend API."""
    created_at: Optional[str] = None
    r"""A custom date/time denoting _when_ the user signed up to the application, specified in RFC3339 format (e.g. `2012-10-20T07:15:20.902Z`)."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["external_id", "first_name", "last_name", "primary_email_address_id", "notify_primary_email_address_changed", "primary_phone_number_id", "primary_web3_wallet_id", "username", "profile_image_id", "password", "password_digest", "password_hasher", "skip_password_checks", "sign_out_of_other_sessions", "totp_secret", "backup_codes", "public_metadata", "private_metadata", "unsafe_metadata", "delete_self_enabled", "create_organization_enabled", "created_at"]
        nullable_fields = ["external_id", "first_name", "last_name", "username", "profile_image_id", "password", "skip_password_checks", "sign_out_of_other_sessions", "delete_self_enabled", "create_organization_enabled"]
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
        

class UpdateUserRequestTypedDict(TypedDict):
    user_id: str
    r"""The ID of the user to update"""
    request_body: UpdateUserRequestBodyTypedDict
    

class UpdateUserRequest(BaseModel):
    user_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The ID of the user to update"""
    request_body: Annotated[UpdateUserRequestBody, FieldMetadata(request=RequestMetadata(media_type="application/json"))]
    
