# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pydantic_utilities import pydantic_v1
from ...core.request_options import RequestOptions
from ...types.prompt_version import PromptVersion
from ...types.prompt_version_created_by import PromptVersionCreatedBy
from ...types.prompt_version_organization import PromptVersionOrganization
from ...types.prompt_version_provider import PromptVersionProvider
from ...types.refined_prompt_response import RefinedPromptResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class VersionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[PromptVersion]:
        """
        Get a list of prompt versions.

        Parameters
        ----------
        id : int
            Prompt ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PromptVersion]


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.prompts.versions.list(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/prompts/{jsonable_encoder(id)}/versions", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(typing.List[PromptVersion], _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        id: int,
        *,
        title: typing.Optional[str] = OMIT,
        parent_model: typing.Optional[int] = OMIT,
        model_provider_connection: typing.Optional[int] = OMIT,
        prompt: typing.Optional[str] = OMIT,
        provider: typing.Optional[PromptVersionProvider] = OMIT,
        provider_model_id: typing.Optional[str] = OMIT,
        created_by: typing.Optional[PromptVersionCreatedBy] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        organization: typing.Optional[PromptVersionOrganization] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PromptVersion:
        """
        Create a new version of a prompt.

        Parameters
        ----------
        id : int
            Prompt ID

        title : typing.Optional[str]

        parent_model : typing.Optional[int]

        model_provider_connection : typing.Optional[int]

        prompt : typing.Optional[str]

        provider : typing.Optional[PromptVersionProvider]

        provider_model_id : typing.Optional[str]

        created_by : typing.Optional[PromptVersionCreatedBy]

        created_at : typing.Optional[dt.datetime]

        updated_at : typing.Optional[dt.datetime]

        organization : typing.Optional[PromptVersionOrganization]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PromptVersion


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.prompts.versions.create(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/prompts/{jsonable_encoder(id)}/versions",
            method="POST",
            json={
                "title": title,
                "parent_model": parent_model,
                "model_provider_connection": model_provider_connection,
                "prompt": prompt,
                "provider": provider,
                "provider_model_id": provider_model_id,
                "created_by": created_by,
                "created_at": created_at,
                "updated_at": updated_at,
                "organization": organization,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(PromptVersion, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(
        self, id: int, version_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PromptVersion:
        """
        Get a prompt version by ID.

        Parameters
        ----------
        id : int
            Prompt ID

        version_id : int
            Prompt Version ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PromptVersion


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.prompts.versions.get(
            id=1,
            version_id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/prompts/{jsonable_encoder(id)}/versions/{jsonable_encoder(version_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(PromptVersion, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, id: int, version_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a prompt version by ID.

        Parameters
        ----------
        id : int
            Prompt ID

        version_id : int
            Prompt Version ID

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
        client.prompts.versions.delete(
            id=1,
            version_id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/prompts/{jsonable_encoder(id)}/versions/{jsonable_encoder(version_id)}",
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
        id: int,
        version_id: int,
        *,
        title: typing.Optional[str] = OMIT,
        parent_model: typing.Optional[int] = OMIT,
        model_provider_connection: typing.Optional[int] = OMIT,
        prompt: typing.Optional[str] = OMIT,
        provider: typing.Optional[PromptVersionProvider] = OMIT,
        provider_model_id: typing.Optional[str] = OMIT,
        created_by: typing.Optional[PromptVersionCreatedBy] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        organization: typing.Optional[PromptVersionOrganization] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PromptVersion:
        """
        Update a prompt version by ID.

        Parameters
        ----------
        id : int
            Prompt ID

        version_id : int
            Prompt Version ID

        title : typing.Optional[str]

        parent_model : typing.Optional[int]

        model_provider_connection : typing.Optional[int]

        prompt : typing.Optional[str]

        provider : typing.Optional[PromptVersionProvider]

        provider_model_id : typing.Optional[str]

        created_by : typing.Optional[PromptVersionCreatedBy]

        created_at : typing.Optional[dt.datetime]

        updated_at : typing.Optional[dt.datetime]

        organization : typing.Optional[PromptVersionOrganization]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PromptVersion


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.prompts.versions.update(
            id=1,
            version_id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/prompts/{jsonable_encoder(id)}/versions/{jsonable_encoder(version_id)}",
            method="PATCH",
            json={
                "title": title,
                "parent_model": parent_model,
                "model_provider_connection": model_provider_connection,
                "prompt": prompt,
                "provider": provider,
                "provider_model_id": provider_model_id,
                "created_by": created_by,
                "created_at": created_at,
                "updated_at": updated_at,
                "organization": organization,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(PromptVersion, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def refine_prompt(
        self,
        prompt_id: int,
        version_id: int,
        *,
        teacher_model_provider_connection_id: typing.Optional[int] = OMIT,
        teacher_model_name: typing.Optional[str] = OMIT,
        project_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RefinedPromptResponse:
        """
        Refine a prompt version using a teacher model and save the refined prompt as a new version.

        Parameters
        ----------
        prompt_id : int
            Prompt ID

        version_id : int
            Base Prompt Version ID

        teacher_model_provider_connection_id : typing.Optional[int]
            Model Provider Connection ID to use to refine the prompt

        teacher_model_name : typing.Optional[str]
            Name of the model to use to refine the prompt

        project_id : typing.Optional[int]
            Project ID to target the refined prompt for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RefinedPromptResponse


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.prompts.versions.refine_prompt(
            prompt_id=1,
            version_id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/prompts/{jsonable_encoder(prompt_id)}/versions/{jsonable_encoder(version_id)}/refine",
            method="POST",
            json={
                "teacher_model_provider_connection_id": teacher_model_provider_connection_id,
                "teacher_model_name": teacher_model_name,
                "project_id": project_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(RefinedPromptResponse, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncVersionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PromptVersion]:
        """
        Get a list of prompt versions.

        Parameters
        ----------
        id : int
            Prompt ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PromptVersion]


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.prompts.versions.list(
            id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/prompts/{jsonable_encoder(id)}/versions", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(typing.List[PromptVersion], _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        id: int,
        *,
        title: typing.Optional[str] = OMIT,
        parent_model: typing.Optional[int] = OMIT,
        model_provider_connection: typing.Optional[int] = OMIT,
        prompt: typing.Optional[str] = OMIT,
        provider: typing.Optional[PromptVersionProvider] = OMIT,
        provider_model_id: typing.Optional[str] = OMIT,
        created_by: typing.Optional[PromptVersionCreatedBy] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        organization: typing.Optional[PromptVersionOrganization] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PromptVersion:
        """
        Create a new version of a prompt.

        Parameters
        ----------
        id : int
            Prompt ID

        title : typing.Optional[str]

        parent_model : typing.Optional[int]

        model_provider_connection : typing.Optional[int]

        prompt : typing.Optional[str]

        provider : typing.Optional[PromptVersionProvider]

        provider_model_id : typing.Optional[str]

        created_by : typing.Optional[PromptVersionCreatedBy]

        created_at : typing.Optional[dt.datetime]

        updated_at : typing.Optional[dt.datetime]

        organization : typing.Optional[PromptVersionOrganization]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PromptVersion


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.prompts.versions.create(
            id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/prompts/{jsonable_encoder(id)}/versions",
            method="POST",
            json={
                "title": title,
                "parent_model": parent_model,
                "model_provider_connection": model_provider_connection,
                "prompt": prompt,
                "provider": provider,
                "provider_model_id": provider_model_id,
                "created_by": created_by,
                "created_at": created_at,
                "updated_at": updated_at,
                "organization": organization,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(PromptVersion, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self, id: int, version_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PromptVersion:
        """
        Get a prompt version by ID.

        Parameters
        ----------
        id : int
            Prompt ID

        version_id : int
            Prompt Version ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PromptVersion


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.prompts.versions.get(
            id=1,
            version_id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/prompts/{jsonable_encoder(id)}/versions/{jsonable_encoder(version_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(PromptVersion, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(
        self, id: int, version_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a prompt version by ID.

        Parameters
        ----------
        id : int
            Prompt ID

        version_id : int
            Prompt Version ID

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
        await client.prompts.versions.delete(
            id=1,
            version_id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/prompts/{jsonable_encoder(id)}/versions/{jsonable_encoder(version_id)}",
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
        id: int,
        version_id: int,
        *,
        title: typing.Optional[str] = OMIT,
        parent_model: typing.Optional[int] = OMIT,
        model_provider_connection: typing.Optional[int] = OMIT,
        prompt: typing.Optional[str] = OMIT,
        provider: typing.Optional[PromptVersionProvider] = OMIT,
        provider_model_id: typing.Optional[str] = OMIT,
        created_by: typing.Optional[PromptVersionCreatedBy] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        organization: typing.Optional[PromptVersionOrganization] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PromptVersion:
        """
        Update a prompt version by ID.

        Parameters
        ----------
        id : int
            Prompt ID

        version_id : int
            Prompt Version ID

        title : typing.Optional[str]

        parent_model : typing.Optional[int]

        model_provider_connection : typing.Optional[int]

        prompt : typing.Optional[str]

        provider : typing.Optional[PromptVersionProvider]

        provider_model_id : typing.Optional[str]

        created_by : typing.Optional[PromptVersionCreatedBy]

        created_at : typing.Optional[dt.datetime]

        updated_at : typing.Optional[dt.datetime]

        organization : typing.Optional[PromptVersionOrganization]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PromptVersion


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.prompts.versions.update(
            id=1,
            version_id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/prompts/{jsonable_encoder(id)}/versions/{jsonable_encoder(version_id)}",
            method="PATCH",
            json={
                "title": title,
                "parent_model": parent_model,
                "model_provider_connection": model_provider_connection,
                "prompt": prompt,
                "provider": provider,
                "provider_model_id": provider_model_id,
                "created_by": created_by,
                "created_at": created_at,
                "updated_at": updated_at,
                "organization": organization,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(PromptVersion, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def refine_prompt(
        self,
        prompt_id: int,
        version_id: int,
        *,
        teacher_model_provider_connection_id: typing.Optional[int] = OMIT,
        teacher_model_name: typing.Optional[str] = OMIT,
        project_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RefinedPromptResponse:
        """
        Refine a prompt version using a teacher model and save the refined prompt as a new version.

        Parameters
        ----------
        prompt_id : int
            Prompt ID

        version_id : int
            Base Prompt Version ID

        teacher_model_provider_connection_id : typing.Optional[int]
            Model Provider Connection ID to use to refine the prompt

        teacher_model_name : typing.Optional[str]
            Name of the model to use to refine the prompt

        project_id : typing.Optional[int]
            Project ID to target the refined prompt for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RefinedPromptResponse


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.prompts.versions.refine_prompt(
            prompt_id=1,
            version_id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/prompts/{jsonable_encoder(prompt_id)}/versions/{jsonable_encoder(version_id)}/refine",
            method="POST",
            json={
                "teacher_model_provider_connection_id": teacher_model_provider_connection_id,
                "teacher_model_name": teacher_model_name,
                "project_id": project_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(RefinedPromptResponse, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
