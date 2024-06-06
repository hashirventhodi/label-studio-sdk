# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import pydantic_v1
from ..core.request_options import RequestOptions
from ..types.webhook import Webhook
from ..types.webhook_serializer_for_update import WebhookSerializerForUpdate
from .types.webhooks_update_request_actions_item import WebhooksUpdateRequestActionsItem

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class WebhooksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, *, project: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Webhook]:
        """
        List all webhooks set up for your organization.

        Webhooks in Label Studio let you set up integrations that subscribe to certain events that occur inside Label Studio. When an event is triggered, Label Studio sends an HTTP POST request to the configured webhook URL.

        For more information, see [Set up webhooks in Label Studio](https://labelstud.io/guide/webhooks).

        Parameters
        ----------
        project : typing.Optional[str]
            Project ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Webhook]


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/webhooks/", method="GET", params={"project": project}, request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[Webhook], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(self, *, request: Webhook, request_options: typing.Optional[RequestOptions] = None) -> Webhook:
        """
        Create a webhook.
        Label Studio provides several out-of-the box webhook events, which you can find listed here: [Available Label Studio webhooks](https://labelstud.io/guide/webhooks#Available-Label-Studio-webhooks).

        If you want to create your own custom webhook, refer to [Create custom events for webhooks in Label Studio](https://labelstud.io/guide/webhook_create).

        <Note>Label Studio makes two main types of events available to integrate with webhooks: project-level task events and organization events. If you want to use organization-level webhook events, you will need to set `LABEL_STUDIO_ALLOW_ORGANIZATION_WEBHOOKS=true`. </Note>

        Parameters
        ----------
        request : Webhook

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Webhook


        Examples
        --------
        from label_studio_sdk import Webhook
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.create(
            request=Webhook(
                url="url",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/webhooks/", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(Webhook, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def info(
        self,
        *,
        organization_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Get descriptions of all available webhook actions to set up webhooks. For more information, see the [Webhook event reference](https://labelstud.io/guide/webhook_reference).

        Parameters
        ----------
        organization_only : typing.Optional[bool]
            organization-only or not

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.info()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/webhooks/info/",
            method="GET",
            params={"organization-only": organization_only},
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Webhook:
        """
        Get information about a specific webhook. You will need to provide the webhook ID. You can get this from [List all webhooks](list).

        For more information about webhooks, see [Set up webhooks in Label Studio](https://labelstud.io/guide/webhooks) and the [Webhook event reference](https://labelstud.io/guide/webhook_reference).

        Parameters
        ----------
        id : int
            A unique integer value identifying this webhook.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Webhook


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.get(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/webhooks/{jsonable_encoder(id)}/", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(Webhook, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a webhook. You will need to provide the webhook ID. You can get this from [List all webhooks](list).

        For more information about webhooks, see [Set up webhooks in Label Studio](https://labelstud.io/guide/webhooks) and the [Webhook event reference](https://labelstud.io/guide/webhook_reference).

        Parameters
        ----------
        id : int
            A unique integer value identifying this webhook.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.delete(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/webhooks/{jsonable_encoder(id)}/", method="DELETE", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        id: int,
        *,
        url: str,
        request: WebhookSerializerForUpdate,
        send_payload: typing.Optional[bool] = None,
        send_for_all_actions: typing.Optional[bool] = None,
        headers: typing.Optional[str] = None,
        is_active: typing.Optional[bool] = None,
        actions: typing.Optional[
            typing.Union[WebhooksUpdateRequestActionsItem, typing.Sequence[WebhooksUpdateRequestActionsItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhookSerializerForUpdate:
        """
        Update a webhook. You will need to provide the webhook ID. You can get this from [List all webhooks](list).

        For more information about webhooks, see [Set up webhooks in Label Studio](https://labelstud.io/guide/webhooks) and the [Webhook event reference](https://labelstud.io/guide/webhook_reference).

        Parameters
        ----------
        id : int
            A unique integer value identifying this webhook.

        url : str
            URL of webhook

        request : WebhookSerializerForUpdate

        send_payload : typing.Optional[bool]
            If value is False send only action

        send_for_all_actions : typing.Optional[bool]
            If value is False - used only for actions from WebhookAction

        headers : typing.Optional[str]
            Key Value Json of headers

        is_active : typing.Optional[bool]
            If value is False the webhook is disabled

        actions : typing.Optional[typing.Union[WebhooksUpdateRequestActionsItem, typing.Sequence[WebhooksUpdateRequestActionsItem]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookSerializerForUpdate


        Examples
        --------
        from label_studio_sdk import WebhookSerializerForUpdate
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.update(
            id=1,
            url="url",
            request=WebhookSerializerForUpdate(
                url="url",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/webhooks/{jsonable_encoder(id)}/",
            method="PATCH",
            params={
                "url": url,
                "send_payload": send_payload,
                "send_for_all_actions": send_for_all_actions,
                "headers": headers,
                "is_active": is_active,
                "actions": actions,
            },
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(WebhookSerializerForUpdate, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncWebhooksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, *, project: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Webhook]:
        """
        List all webhooks set up for your organization.

        Webhooks in Label Studio let you set up integrations that subscribe to certain events that occur inside Label Studio. When an event is triggered, Label Studio sends an HTTP POST request to the configured webhook URL.

        For more information, see [Set up webhooks in Label Studio](https://labelstud.io/guide/webhooks).

        Parameters
        ----------
        project : typing.Optional[str]
            Project ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Webhook]


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.webhooks.list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/webhooks/", method="GET", params={"project": project}, request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[Webhook], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(self, *, request: Webhook, request_options: typing.Optional[RequestOptions] = None) -> Webhook:
        """
        Create a webhook.
        Label Studio provides several out-of-the box webhook events, which you can find listed here: [Available Label Studio webhooks](https://labelstud.io/guide/webhooks#Available-Label-Studio-webhooks).

        If you want to create your own custom webhook, refer to [Create custom events for webhooks in Label Studio](https://labelstud.io/guide/webhook_create).

        <Note>Label Studio makes two main types of events available to integrate with webhooks: project-level task events and organization events. If you want to use organization-level webhook events, you will need to set `LABEL_STUDIO_ALLOW_ORGANIZATION_WEBHOOKS=true`. </Note>

        Parameters
        ----------
        request : Webhook

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Webhook


        Examples
        --------
        from label_studio_sdk import Webhook
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.webhooks.create(
            request=Webhook(
                url="url",
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/webhooks/", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(Webhook, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def info(
        self,
        *,
        organization_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Get descriptions of all available webhook actions to set up webhooks. For more information, see the [Webhook event reference](https://labelstud.io/guide/webhook_reference).

        Parameters
        ----------
        organization_only : typing.Optional[bool]
            organization-only or not

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.webhooks.info()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/webhooks/info/",
            method="GET",
            params={"organization-only": organization_only},
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Webhook:
        """
        Get information about a specific webhook. You will need to provide the webhook ID. You can get this from [List all webhooks](list).

        For more information about webhooks, see [Set up webhooks in Label Studio](https://labelstud.io/guide/webhooks) and the [Webhook event reference](https://labelstud.io/guide/webhook_reference).

        Parameters
        ----------
        id : int
            A unique integer value identifying this webhook.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Webhook


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.webhooks.get(
            id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/webhooks/{jsonable_encoder(id)}/", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(Webhook, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a webhook. You will need to provide the webhook ID. You can get this from [List all webhooks](list).

        For more information about webhooks, see [Set up webhooks in Label Studio](https://labelstud.io/guide/webhooks) and the [Webhook event reference](https://labelstud.io/guide/webhook_reference).

        Parameters
        ----------
        id : int
            A unique integer value identifying this webhook.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.webhooks.delete(
            id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/webhooks/{jsonable_encoder(id)}/", method="DELETE", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        id: int,
        *,
        url: str,
        request: WebhookSerializerForUpdate,
        send_payload: typing.Optional[bool] = None,
        send_for_all_actions: typing.Optional[bool] = None,
        headers: typing.Optional[str] = None,
        is_active: typing.Optional[bool] = None,
        actions: typing.Optional[
            typing.Union[WebhooksUpdateRequestActionsItem, typing.Sequence[WebhooksUpdateRequestActionsItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhookSerializerForUpdate:
        """
        Update a webhook. You will need to provide the webhook ID. You can get this from [List all webhooks](list).

        For more information about webhooks, see [Set up webhooks in Label Studio](https://labelstud.io/guide/webhooks) and the [Webhook event reference](https://labelstud.io/guide/webhook_reference).

        Parameters
        ----------
        id : int
            A unique integer value identifying this webhook.

        url : str
            URL of webhook

        request : WebhookSerializerForUpdate

        send_payload : typing.Optional[bool]
            If value is False send only action

        send_for_all_actions : typing.Optional[bool]
            If value is False - used only for actions from WebhookAction

        headers : typing.Optional[str]
            Key Value Json of headers

        is_active : typing.Optional[bool]
            If value is False the webhook is disabled

        actions : typing.Optional[typing.Union[WebhooksUpdateRequestActionsItem, typing.Sequence[WebhooksUpdateRequestActionsItem]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookSerializerForUpdate


        Examples
        --------
        from label_studio_sdk import WebhookSerializerForUpdate
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.webhooks.update(
            id=1,
            url="url",
            request=WebhookSerializerForUpdate(
                url="url",
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/webhooks/{jsonable_encoder(id)}/",
            method="PATCH",
            params={
                "url": url,
                "send_payload": send_payload,
                "send_for_all_actions": send_for_all_actions,
                "headers": headers,
                "is_active": is_active,
                "actions": actions,
            },
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(WebhookSerializerForUpdate, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
