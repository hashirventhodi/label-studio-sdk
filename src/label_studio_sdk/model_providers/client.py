# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.model_provider_connection import ModelProviderConnection
from ..core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.model_provider_connection_provider import ModelProviderConnectionProvider
from ..types.model_provider_connection_scope import ModelProviderConnectionScope
from ..types.model_provider_connection_organization import ModelProviderConnectionOrganization
from ..types.model_provider_connection_created_by import ModelProviderConnectionCreatedBy
import datetime as dt
from ..types.model_provider_connection_budget_reset_period import ModelProviderConnectionBudgetResetPeriod
from ..core.serialization import convert_and_respect_annotation_metadata
from ..core.jsonable_encoder import jsonable_encoder
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ModelProvidersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[ModelProviderConnection]:
        """
        Get all model provider connections created by the user in the current organization.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ModelProviderConnection]


        Examples
        --------
        from label_studio_sdk import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.model_providers.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/model-provider-connections/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[ModelProviderConnection],
                    parse_obj_as(
                        type_=typing.List[ModelProviderConnection],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        provider: ModelProviderConnectionProvider,
        api_key: typing.Optional[str] = OMIT,
        deployment_name: typing.Optional[str] = OMIT,
        endpoint: typing.Optional[str] = OMIT,
        scope: typing.Optional[ModelProviderConnectionScope] = OMIT,
        organization: typing.Optional[ModelProviderConnectionOrganization] = OMIT,
        created_by: typing.Optional[ModelProviderConnectionCreatedBy] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        is_internal: typing.Optional[bool] = OMIT,
        budget_limit: typing.Optional[float] = OMIT,
        budget_last_reset_date: typing.Optional[dt.datetime] = OMIT,
        budget_reset_period: typing.Optional[ModelProviderConnectionBudgetResetPeriod] = OMIT,
        budget_total_spent: typing.Optional[float] = OMIT,
        budget_alert_threshold: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModelProviderConnection:
        """
        Create a new model provider connection.

        Parameters
        ----------
        provider : ModelProviderConnectionProvider

        api_key : typing.Optional[str]

        deployment_name : typing.Optional[str]

        endpoint : typing.Optional[str]

        scope : typing.Optional[ModelProviderConnectionScope]

        organization : typing.Optional[ModelProviderConnectionOrganization]

        created_by : typing.Optional[ModelProviderConnectionCreatedBy]

        created_at : typing.Optional[dt.datetime]

        updated_at : typing.Optional[dt.datetime]

        is_internal : typing.Optional[bool]
            Whether the model provider connection is internal, not visible to the user.

        budget_limit : typing.Optional[float]
            Budget limit for the model provider connection (null if unlimited)

        budget_last_reset_date : typing.Optional[dt.datetime]
            Date and time the budget was last reset

        budget_reset_period : typing.Optional[ModelProviderConnectionBudgetResetPeriod]
            Budget reset period for the model provider connection (null if not reset)

        budget_total_spent : typing.Optional[float]
            Tracked total budget spent for the given provider connection within the current budget period

        budget_alert_threshold : typing.Optional[float]
            Budget alert threshold for the given provider connection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelProviderConnection


        Examples
        --------
        from label_studio_sdk import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.model_providers.create(
            provider="OpenAI",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/model-provider-connections/",
            method="POST",
            json={
                "provider": provider,
                "api_key": api_key,
                "deployment_name": deployment_name,
                "endpoint": endpoint,
                "scope": scope,
                "organization": convert_and_respect_annotation_metadata(
                    object_=organization, annotation=ModelProviderConnectionOrganization, direction="write"
                ),
                "created_by": convert_and_respect_annotation_metadata(
                    object_=created_by, annotation=ModelProviderConnectionCreatedBy, direction="write"
                ),
                "created_at": created_at,
                "updated_at": updated_at,
                "is_internal": is_internal,
                "budget_limit": budget_limit,
                "budget_last_reset_date": budget_last_reset_date,
                "budget_reset_period": budget_reset_period,
                "budget_total_spent": budget_total_spent,
                "budget_alert_threshold": budget_alert_threshold,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ModelProviderConnection,
                    parse_obj_as(
                        type_=ModelProviderConnection,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, pk: int, *, request_options: typing.Optional[RequestOptions] = None) -> ModelProviderConnection:
        """
        Get a model provider connection by ID.

        Parameters
        ----------
        pk : int
            Model Provider Connection ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelProviderConnection


        Examples
        --------
        from label_studio_sdk import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.model_providers.get(
            pk=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/model-provider-connections/{jsonable_encoder(pk)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ModelProviderConnection,
                    parse_obj_as(
                        type_=ModelProviderConnection,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, pk: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a model provider connection by ID.

        Parameters
        ----------
        pk : int
            Model Provider Connection ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from label_studio_sdk import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.model_providers.delete(
            pk=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/model-provider-connections/{jsonable_encoder(pk)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        pk: int,
        *,
        provider: ModelProviderConnectionProvider,
        api_key: typing.Optional[str] = OMIT,
        deployment_name: typing.Optional[str] = OMIT,
        endpoint: typing.Optional[str] = OMIT,
        scope: typing.Optional[ModelProviderConnectionScope] = OMIT,
        organization: typing.Optional[ModelProviderConnectionOrganization] = OMIT,
        created_by: typing.Optional[ModelProviderConnectionCreatedBy] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        is_internal: typing.Optional[bool] = OMIT,
        budget_limit: typing.Optional[float] = OMIT,
        budget_last_reset_date: typing.Optional[dt.datetime] = OMIT,
        budget_reset_period: typing.Optional[ModelProviderConnectionBudgetResetPeriod] = OMIT,
        budget_total_spent: typing.Optional[float] = OMIT,
        budget_alert_threshold: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModelProviderConnection:
        """
        Update a model provider connection by ID.

        Parameters
        ----------
        pk : int
            Model Provider Connection ID

        provider : ModelProviderConnectionProvider

        api_key : typing.Optional[str]

        deployment_name : typing.Optional[str]

        endpoint : typing.Optional[str]

        scope : typing.Optional[ModelProviderConnectionScope]

        organization : typing.Optional[ModelProviderConnectionOrganization]

        created_by : typing.Optional[ModelProviderConnectionCreatedBy]

        created_at : typing.Optional[dt.datetime]

        updated_at : typing.Optional[dt.datetime]

        is_internal : typing.Optional[bool]
            Whether the model provider connection is internal, not visible to the user.

        budget_limit : typing.Optional[float]
            Budget limit for the model provider connection (null if unlimited)

        budget_last_reset_date : typing.Optional[dt.datetime]
            Date and time the budget was last reset

        budget_reset_period : typing.Optional[ModelProviderConnectionBudgetResetPeriod]
            Budget reset period for the model provider connection (null if not reset)

        budget_total_spent : typing.Optional[float]
            Tracked total budget spent for the given provider connection within the current budget period

        budget_alert_threshold : typing.Optional[float]
            Budget alert threshold for the given provider connection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelProviderConnection


        Examples
        --------
        from label_studio_sdk import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.model_providers.update(
            pk=1,
            provider="OpenAI",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/model-provider-connections/{jsonable_encoder(pk)}",
            method="PATCH",
            json={
                "provider": provider,
                "api_key": api_key,
                "deployment_name": deployment_name,
                "endpoint": endpoint,
                "scope": scope,
                "organization": convert_and_respect_annotation_metadata(
                    object_=organization, annotation=ModelProviderConnectionOrganization, direction="write"
                ),
                "created_by": convert_and_respect_annotation_metadata(
                    object_=created_by, annotation=ModelProviderConnectionCreatedBy, direction="write"
                ),
                "created_at": created_at,
                "updated_at": updated_at,
                "is_internal": is_internal,
                "budget_limit": budget_limit,
                "budget_last_reset_date": budget_last_reset_date,
                "budget_reset_period": budget_reset_period,
                "budget_total_spent": budget_total_spent,
                "budget_alert_threshold": budget_alert_threshold,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ModelProviderConnection,
                    parse_obj_as(
                        type_=ModelProviderConnection,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncModelProvidersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ModelProviderConnection]:
        """
        Get all model provider connections created by the user in the current organization.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ModelProviderConnection]


        Examples
        --------
        import asyncio

        from label_studio_sdk import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.model_providers.list()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/model-provider-connections/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[ModelProviderConnection],
                    parse_obj_as(
                        type_=typing.List[ModelProviderConnection],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        provider: ModelProviderConnectionProvider,
        api_key: typing.Optional[str] = OMIT,
        deployment_name: typing.Optional[str] = OMIT,
        endpoint: typing.Optional[str] = OMIT,
        scope: typing.Optional[ModelProviderConnectionScope] = OMIT,
        organization: typing.Optional[ModelProviderConnectionOrganization] = OMIT,
        created_by: typing.Optional[ModelProviderConnectionCreatedBy] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        is_internal: typing.Optional[bool] = OMIT,
        budget_limit: typing.Optional[float] = OMIT,
        budget_last_reset_date: typing.Optional[dt.datetime] = OMIT,
        budget_reset_period: typing.Optional[ModelProviderConnectionBudgetResetPeriod] = OMIT,
        budget_total_spent: typing.Optional[float] = OMIT,
        budget_alert_threshold: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModelProviderConnection:
        """
        Create a new model provider connection.

        Parameters
        ----------
        provider : ModelProviderConnectionProvider

        api_key : typing.Optional[str]

        deployment_name : typing.Optional[str]

        endpoint : typing.Optional[str]

        scope : typing.Optional[ModelProviderConnectionScope]

        organization : typing.Optional[ModelProviderConnectionOrganization]

        created_by : typing.Optional[ModelProviderConnectionCreatedBy]

        created_at : typing.Optional[dt.datetime]

        updated_at : typing.Optional[dt.datetime]

        is_internal : typing.Optional[bool]
            Whether the model provider connection is internal, not visible to the user.

        budget_limit : typing.Optional[float]
            Budget limit for the model provider connection (null if unlimited)

        budget_last_reset_date : typing.Optional[dt.datetime]
            Date and time the budget was last reset

        budget_reset_period : typing.Optional[ModelProviderConnectionBudgetResetPeriod]
            Budget reset period for the model provider connection (null if not reset)

        budget_total_spent : typing.Optional[float]
            Tracked total budget spent for the given provider connection within the current budget period

        budget_alert_threshold : typing.Optional[float]
            Budget alert threshold for the given provider connection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelProviderConnection


        Examples
        --------
        import asyncio

        from label_studio_sdk import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.model_providers.create(
                provider="OpenAI",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/model-provider-connections/",
            method="POST",
            json={
                "provider": provider,
                "api_key": api_key,
                "deployment_name": deployment_name,
                "endpoint": endpoint,
                "scope": scope,
                "organization": convert_and_respect_annotation_metadata(
                    object_=organization, annotation=ModelProviderConnectionOrganization, direction="write"
                ),
                "created_by": convert_and_respect_annotation_metadata(
                    object_=created_by, annotation=ModelProviderConnectionCreatedBy, direction="write"
                ),
                "created_at": created_at,
                "updated_at": updated_at,
                "is_internal": is_internal,
                "budget_limit": budget_limit,
                "budget_last_reset_date": budget_last_reset_date,
                "budget_reset_period": budget_reset_period,
                "budget_total_spent": budget_total_spent,
                "budget_alert_threshold": budget_alert_threshold,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ModelProviderConnection,
                    parse_obj_as(
                        type_=ModelProviderConnection,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, pk: int, *, request_options: typing.Optional[RequestOptions] = None) -> ModelProviderConnection:
        """
        Get a model provider connection by ID.

        Parameters
        ----------
        pk : int
            Model Provider Connection ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelProviderConnection


        Examples
        --------
        import asyncio

        from label_studio_sdk import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.model_providers.get(
                pk=1,
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/model-provider-connections/{jsonable_encoder(pk)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ModelProviderConnection,
                    parse_obj_as(
                        type_=ModelProviderConnection,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, pk: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a model provider connection by ID.

        Parameters
        ----------
        pk : int
            Model Provider Connection ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from label_studio_sdk import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.model_providers.delete(
                pk=1,
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/model-provider-connections/{jsonable_encoder(pk)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        pk: int,
        *,
        provider: ModelProviderConnectionProvider,
        api_key: typing.Optional[str] = OMIT,
        deployment_name: typing.Optional[str] = OMIT,
        endpoint: typing.Optional[str] = OMIT,
        scope: typing.Optional[ModelProviderConnectionScope] = OMIT,
        organization: typing.Optional[ModelProviderConnectionOrganization] = OMIT,
        created_by: typing.Optional[ModelProviderConnectionCreatedBy] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        is_internal: typing.Optional[bool] = OMIT,
        budget_limit: typing.Optional[float] = OMIT,
        budget_last_reset_date: typing.Optional[dt.datetime] = OMIT,
        budget_reset_period: typing.Optional[ModelProviderConnectionBudgetResetPeriod] = OMIT,
        budget_total_spent: typing.Optional[float] = OMIT,
        budget_alert_threshold: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModelProviderConnection:
        """
        Update a model provider connection by ID.

        Parameters
        ----------
        pk : int
            Model Provider Connection ID

        provider : ModelProviderConnectionProvider

        api_key : typing.Optional[str]

        deployment_name : typing.Optional[str]

        endpoint : typing.Optional[str]

        scope : typing.Optional[ModelProviderConnectionScope]

        organization : typing.Optional[ModelProviderConnectionOrganization]

        created_by : typing.Optional[ModelProviderConnectionCreatedBy]

        created_at : typing.Optional[dt.datetime]

        updated_at : typing.Optional[dt.datetime]

        is_internal : typing.Optional[bool]
            Whether the model provider connection is internal, not visible to the user.

        budget_limit : typing.Optional[float]
            Budget limit for the model provider connection (null if unlimited)

        budget_last_reset_date : typing.Optional[dt.datetime]
            Date and time the budget was last reset

        budget_reset_period : typing.Optional[ModelProviderConnectionBudgetResetPeriod]
            Budget reset period for the model provider connection (null if not reset)

        budget_total_spent : typing.Optional[float]
            Tracked total budget spent for the given provider connection within the current budget period

        budget_alert_threshold : typing.Optional[float]
            Budget alert threshold for the given provider connection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelProviderConnection


        Examples
        --------
        import asyncio

        from label_studio_sdk import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.model_providers.update(
                pk=1,
                provider="OpenAI",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/model-provider-connections/{jsonable_encoder(pk)}",
            method="PATCH",
            json={
                "provider": provider,
                "api_key": api_key,
                "deployment_name": deployment_name,
                "endpoint": endpoint,
                "scope": scope,
                "organization": convert_and_respect_annotation_metadata(
                    object_=organization, annotation=ModelProviderConnectionOrganization, direction="write"
                ),
                "created_by": convert_and_respect_annotation_metadata(
                    object_=created_by, annotation=ModelProviderConnectionCreatedBy, direction="write"
                ),
                "created_at": created_at,
                "updated_at": updated_at,
                "is_internal": is_internal,
                "budget_limit": budget_limit,
                "budget_last_reset_date": budget_last_reset_date,
                "budget_reset_period": budget_reset_period,
                "budget_total_spent": budget_total_spent,
                "budget_alert_threshold": budget_alert_threshold,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ModelProviderConnection,
                    parse_obj_as(
                        type_=ModelProviderConnection,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
