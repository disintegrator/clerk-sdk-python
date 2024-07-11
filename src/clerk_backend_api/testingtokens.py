"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .basesdk import BaseSDK
from clerk_backend_api import models
from clerk_backend_api._hooks import HookContext
from clerk_backend_api.types import Nullable, UNSET
import clerk_backend_api.utils as utils
from typing import Optional

class TestingTokens(BaseSDK):
    
    
    def create(
        self, *,
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.TestingToken:
        r"""Retrieve a new testing token

        Retrieve a new testing token. Only available for development instances.

        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_config is None:
            timeout_config = self.sdk_configuration.timeout_config
        
        if server_url is not None:
            base_url = server_url
        req = self.build_request(
            method="POST",
            path="/testing_tokens",
            base_url=base_url,
            url_variables=url_variables,
            request=None,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_config=timeout_config,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="CreateTestingToken", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["400","4XX","5XX"],
            retry_config=retry_config
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.TestingToken])
        if utils.match_response(http_res, ["400","4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    async def create_async(
        self, *,
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.TestingToken:
        r"""Retrieve a new testing token

        Retrieve a new testing token. Only available for development instances.

        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_config is None:
            timeout_config = self.sdk_configuration.timeout_config
        
        if server_url is not None:
            base_url = server_url
        req = self.build_request(
            method="POST",
            path="/testing_tokens",
            base_url=base_url,
            url_variables=url_variables,
            request=None,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_config=timeout_config,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="CreateTestingToken", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["400","4XX","5XX"],
            retry_config=retry_config
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.TestingToken])
        if utils.match_response(http_res, ["400","4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
