# EmailAddresses
(*email_addresses*)

### Available Operations

* [create](#create) - Create an email address
* [get](#get) - Retrieve an email address
* [delete](#delete) - Delete an email address
* [update](#update) - Update an email address

## create

Create a new email address

### Example Usage

```python
from clerk import Clerk
import os

s = Clerk(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.email_addresses.create(user_id="user_12345", email_address="example@clerk.com", verified=False, primary=True)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                | Example                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `user_id`                                                                                                                  | *Optional[str]*                                                                                                            | :heavy_minus_sign:                                                                                                         | The ID representing the user                                                                                               | user_12345                                                                                                                 |
| `email_address`                                                                                                            | *Optional[str]*                                                                                                            | :heavy_minus_sign:                                                                                                         | The new email address. Must adhere to the RFC 5322 specification for email address format.                                 | example@clerk.com                                                                                                          |
| `verified`                                                                                                                 | *Optional[Nullable[bool]]*                                                                                                 | :heavy_minus_sign:                                                                                                         | When created, the email address will be marked as verified.                                                                | false                                                                                                                      |
| `primary`                                                                                                                  | *Optional[Nullable[bool]]*                                                                                                 | :heavy_minus_sign:                                                                                                         | Create this email address as the primary email address for the user.<br/>Default: false, unless it is the first email address. | true                                                                                                                       |
| `retries`                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                           | :heavy_minus_sign:                                                                                                         | Configuration to override the default retry behavior of the client.                                                        |                                                                                                                            |


### Response

**[models.EmailAddress](../../models/emailaddress.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.ClerkErrors  | 400,401,403,404,422 | application/json    |
| models.SDKError     | 4xx-5xx             | */*                 |

## get

Returns the details of an email address.

### Example Usage

```python
from clerk import Clerk
import os

s = Clerk(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.email_addresses.get(email_address_id="email_address_id_example")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `email_address_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The ID of the email address to retrieve                             | email_address_id_example                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.EmailAddress](../../models/emailaddress.md)**
### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,401,403,404    | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |

## delete

Delete the email address with the given ID

### Example Usage

```python
from clerk import Clerk
import os

s = Clerk(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.email_addresses.delete(email_address_id="email_address_id_example")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `email_address_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The ID of the email address to delete                               | email_address_id_example                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.DeletedObject](../../models/deletedobject.md)**
### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,401,403,404    | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |

## update

Updates an email address.

### Example Usage

```python
from clerk import Clerk
import os

s = Clerk(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.email_addresses.update(email_address_id="email_address_id_example", verified=False, primary=True)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `email_address_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The ID of the email address to update                               | email_address_id_example                                            |
| `verified`                                                          | *Optional[Nullable[bool]]*                                          | :heavy_minus_sign:                                                  | The email address will be marked as verified.                       | false                                                               |
| `primary`                                                           | *Optional[Nullable[bool]]*                                          | :heavy_minus_sign:                                                  | Set this email address as the primary email address for the user.   | true                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.EmailAddress](../../models/emailaddress.md)**
### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,401,403,404    | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |