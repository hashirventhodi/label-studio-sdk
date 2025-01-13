# This file was auto-generated by Fern from our API Definition.

from ..core.client_wrapper import SyncClientWrapper
from .azure.client import AzureClient
from .gcs.client import GcsClient
from .local.client import LocalClient
from .redis.client import RedisClient
from .s3.client import S3Client
from .s3s.client import S3SClient
import typing
from ..core.request_options import RequestOptions
from .types.import_storage_list_types_response_item import ImportStorageListTypesResponseItem
from ..core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper
from .azure.client import AsyncAzureClient
from .gcs.client import AsyncGcsClient
from .local.client import AsyncLocalClient
from .redis.client import AsyncRedisClient
from .s3.client import AsyncS3Client
from .s3s.client import AsyncS3SClient


class ImportStorageClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.azure = AzureClient(client_wrapper=self._client_wrapper)
        self.gcs = GcsClient(client_wrapper=self._client_wrapper)
        self.local = LocalClient(client_wrapper=self._client_wrapper)
        self.redis = RedisClient(client_wrapper=self._client_wrapper)
        self.s3 = S3Client(client_wrapper=self._client_wrapper)
        self.s3s = S3SClient(client_wrapper=self._client_wrapper)

    def list_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ImportStorageListTypesResponseItem]:
        """
        Retrieve a list of the import storages types.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ImportStorageListTypesResponseItem]


        Examples
        --------
        from label_studio_sdk import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.import_storage.list_types()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/storages/types",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[ImportStorageListTypesResponseItem],
                    parse_obj_as(
                        type_=typing.List[ImportStorageListTypesResponseItem],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncImportStorageClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.azure = AsyncAzureClient(client_wrapper=self._client_wrapper)
        self.gcs = AsyncGcsClient(client_wrapper=self._client_wrapper)
        self.local = AsyncLocalClient(client_wrapper=self._client_wrapper)
        self.redis = AsyncRedisClient(client_wrapper=self._client_wrapper)
        self.s3 = AsyncS3Client(client_wrapper=self._client_wrapper)
        self.s3s = AsyncS3SClient(client_wrapper=self._client_wrapper)

    async def list_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ImportStorageListTypesResponseItem]:
        """
        Retrieve a list of the import storages types.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ImportStorageListTypesResponseItem]


        Examples
        --------
        import asyncio

        from label_studio_sdk import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.import_storage.list_types()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/storages/types",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[ImportStorageListTypesResponseItem],
                    parse_obj_as(
                        type_=typing.List[ImportStorageListTypesResponseItem],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
