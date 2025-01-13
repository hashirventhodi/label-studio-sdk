# This file was auto-generated by Fern from our API Definition.

import typing
from ...core.client_wrapper import SyncClientWrapper
from ...core.request_options import RequestOptions
from ...types.azure_blob_export_storage import AzureBlobExportStorage
from ...core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from ...core.api_error import ApiError
from .types.azure_create_response import AzureCreateResponse
from ...core.jsonable_encoder import jsonable_encoder
from .types.azure_update_response import AzureUpdateResponse
from ...core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class AzureClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, *, project: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AzureBlobExportStorage]:
        """

        You can connect your Microsoft Azure Blob storage container to Label Studio as a source storage or target storage. Use this API request to get a list of all Azure export (target) storage connections for a specific project.

        The project ID can be found in the URL when viewing the project in Label Studio, or you can retrieve all project IDs using [List all projects](../projects/list).

        For more information about working with external storage, see [Sync data from external storage](https://labelstud.io/guide/storage).

        Parameters
        ----------
        project : typing.Optional[int]
            Project ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AzureBlobExportStorage]


        Examples
        --------
        from label_studio_sdk import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.export_storage.azure.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/storages/export/azure",
            method="GET",
            params={
                "project": project,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[AzureBlobExportStorage],
                    parse_obj_as(
                        type_=typing.List[AzureBlobExportStorage],  # type: ignore
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
        can_delete_objects: typing.Optional[bool] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        project: typing.Optional[int] = OMIT,
        container: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        account_name: typing.Optional[str] = OMIT,
        account_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AzureCreateResponse:
        """

        Create a new target storage connection to Microsoft Azure Blob storage.

        For information about the required fields and prerequisites, see [Microsoft Azure Blob storage](https://labelstud.io/guide/storage#Microsoft-Azure-Blob-storage) in the Label Studio documentation.

        <Tip>After you add the storage, you should validate the connection before attempting to sync your data. Your data will not be exported until you [sync your connection](sync).</Tip>

        Parameters
        ----------
        can_delete_objects : typing.Optional[bool]
            Deletion from storage enabled

        title : typing.Optional[str]
            Storage title

        description : typing.Optional[str]
            Storage description

        project : typing.Optional[int]
            Project ID

        container : typing.Optional[str]
            Azure blob container

        prefix : typing.Optional[str]
            Azure blob prefix name

        account_name : typing.Optional[str]
            Azure Blob account name

        account_key : typing.Optional[str]
            Azure Blob account key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AzureCreateResponse


        Examples
        --------
        from label_studio_sdk import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.export_storage.azure.create()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/storages/export/azure",
            method="POST",
            json={
                "can_delete_objects": can_delete_objects,
                "title": title,
                "description": description,
                "project": project,
                "container": container,
                "prefix": prefix,
                "account_name": account_name,
                "account_key": account_key,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AzureCreateResponse,
                    parse_obj_as(
                        type_=AzureCreateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def validate(
        self,
        *,
        id: typing.Optional[int] = OMIT,
        can_delete_objects: typing.Optional[bool] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        project: typing.Optional[int] = OMIT,
        container: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        account_name: typing.Optional[str] = OMIT,
        account_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """

        Validate a specific Azure export storage connection. This is useful to ensure that the storage configuration settings are correct and operational before attempting to export data.

        Parameters
        ----------
        id : typing.Optional[int]
            Storage ID. If set, storage with specified ID will be updated

        can_delete_objects : typing.Optional[bool]
            Deletion from storage enabled

        title : typing.Optional[str]
            Storage title

        description : typing.Optional[str]
            Storage description

        project : typing.Optional[int]
            Project ID

        container : typing.Optional[str]
            Azure blob container

        prefix : typing.Optional[str]
            Azure blob prefix name

        account_name : typing.Optional[str]
            Azure Blob account name

        account_key : typing.Optional[str]
            Azure Blob account key

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
        client.export_storage.azure.validate()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/storages/export/azure/validate",
            method="POST",
            json={
                "id": id,
                "can_delete_objects": can_delete_objects,
                "title": title,
                "description": description,
                "project": project,
                "container": container,
                "prefix": prefix,
                "account_name": account_name,
                "account_key": account_key,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> AzureBlobExportStorage:
        """

        Get a specific Azure export storage connection. You will need to provide the export storage ID. You can find this using [List export storages](list).

        For more information about working with external storage, see [Sync data from external storage](https://labelstud.io/guide/storage).

        Parameters
        ----------
        id : int
            A unique integer value identifying this azure blob export storage.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AzureBlobExportStorage


        Examples
        --------
        from label_studio_sdk import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.export_storage.azure.get(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/storages/export/azure/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AzureBlobExportStorage,
                    parse_obj_as(
                        type_=AzureBlobExportStorage,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """

        Delete a specific Azure export storage connection. You will need to provide the export storage ID. You can find this using [List export storages](list).

        Deleting an export/target storage connection does not affect tasks with synced data in Label Studio. If you want to remove the tasks that were synced from the external storage, you will need to delete them manually from within the Label Studio UI or use the [Delete tasks](../../tasks/delete-all-tasks) API.

        Parameters
        ----------
        id : int
            A unique integer value identifying this azure blob export storage.

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
        client.export_storage.azure.delete(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/storages/export/azure/{jsonable_encoder(id)}",
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
        *,
        can_delete_objects: typing.Optional[bool] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        project: typing.Optional[int] = OMIT,
        container: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        account_name: typing.Optional[str] = OMIT,
        account_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AzureUpdateResponse:
        """

        Update a specific Azure export storage connection. You will need to provide the export storage ID. You can find this using [List export storages](list).

        For more information about working with external storage, see [Sync data from external storage](https://labelstud.io/guide/storage).

        Parameters
        ----------
        id : int
            A unique integer value identifying this azure blob export storage.

        can_delete_objects : typing.Optional[bool]
            Deletion from storage enabled

        title : typing.Optional[str]
            Storage title

        description : typing.Optional[str]
            Storage description

        project : typing.Optional[int]
            Project ID

        container : typing.Optional[str]
            Azure blob container

        prefix : typing.Optional[str]
            Azure blob prefix name

        account_name : typing.Optional[str]
            Azure Blob account name

        account_key : typing.Optional[str]
            Azure Blob account key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AzureUpdateResponse


        Examples
        --------
        from label_studio_sdk import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.export_storage.azure.update(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/storages/export/azure/{jsonable_encoder(id)}",
            method="PATCH",
            json={
                "can_delete_objects": can_delete_objects,
                "title": title,
                "description": description,
                "project": project,
                "container": container,
                "prefix": prefix,
                "account_name": account_name,
                "account_key": account_key,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AzureUpdateResponse,
                    parse_obj_as(
                        type_=AzureUpdateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def sync(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> AzureBlobExportStorage:
        """

        Sync tasks to an Azure export/target storage connection. You will need to provide the export storage ID. You can find this using [List export storages](list).

        Sync operations with external containers only go one way. They either create tasks from objects in the container (source/import storage) or push annotations to the output container (export/target storage). Changing something on the Microsoft side doesn’t guarantee consistency in results.

        <Note>Before proceeding, you should review [How sync operations work - Source storage](https://labelstud.io/guide/storage#Source-storage) to ensure that your data remains secure and private.</Note>

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AzureBlobExportStorage


        Examples
        --------
        from label_studio_sdk import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.export_storage.azure.sync(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/storages/export/azure/{jsonable_encoder(id)}/sync",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AzureBlobExportStorage,
                    parse_obj_as(
                        type_=AzureBlobExportStorage,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncAzureClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, *, project: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AzureBlobExportStorage]:
        """

        You can connect your Microsoft Azure Blob storage container to Label Studio as a source storage or target storage. Use this API request to get a list of all Azure export (target) storage connections for a specific project.

        The project ID can be found in the URL when viewing the project in Label Studio, or you can retrieve all project IDs using [List all projects](../projects/list).

        For more information about working with external storage, see [Sync data from external storage](https://labelstud.io/guide/storage).

        Parameters
        ----------
        project : typing.Optional[int]
            Project ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AzureBlobExportStorage]


        Examples
        --------
        import asyncio

        from label_studio_sdk import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.export_storage.azure.list()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/storages/export/azure",
            method="GET",
            params={
                "project": project,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[AzureBlobExportStorage],
                    parse_obj_as(
                        type_=typing.List[AzureBlobExportStorage],  # type: ignore
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
        can_delete_objects: typing.Optional[bool] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        project: typing.Optional[int] = OMIT,
        container: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        account_name: typing.Optional[str] = OMIT,
        account_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AzureCreateResponse:
        """

        Create a new target storage connection to Microsoft Azure Blob storage.

        For information about the required fields and prerequisites, see [Microsoft Azure Blob storage](https://labelstud.io/guide/storage#Microsoft-Azure-Blob-storage) in the Label Studio documentation.

        <Tip>After you add the storage, you should validate the connection before attempting to sync your data. Your data will not be exported until you [sync your connection](sync).</Tip>

        Parameters
        ----------
        can_delete_objects : typing.Optional[bool]
            Deletion from storage enabled

        title : typing.Optional[str]
            Storage title

        description : typing.Optional[str]
            Storage description

        project : typing.Optional[int]
            Project ID

        container : typing.Optional[str]
            Azure blob container

        prefix : typing.Optional[str]
            Azure blob prefix name

        account_name : typing.Optional[str]
            Azure Blob account name

        account_key : typing.Optional[str]
            Azure Blob account key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AzureCreateResponse


        Examples
        --------
        import asyncio

        from label_studio_sdk import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.export_storage.azure.create()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/storages/export/azure",
            method="POST",
            json={
                "can_delete_objects": can_delete_objects,
                "title": title,
                "description": description,
                "project": project,
                "container": container,
                "prefix": prefix,
                "account_name": account_name,
                "account_key": account_key,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AzureCreateResponse,
                    parse_obj_as(
                        type_=AzureCreateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def validate(
        self,
        *,
        id: typing.Optional[int] = OMIT,
        can_delete_objects: typing.Optional[bool] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        project: typing.Optional[int] = OMIT,
        container: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        account_name: typing.Optional[str] = OMIT,
        account_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """

        Validate a specific Azure export storage connection. This is useful to ensure that the storage configuration settings are correct and operational before attempting to export data.

        Parameters
        ----------
        id : typing.Optional[int]
            Storage ID. If set, storage with specified ID will be updated

        can_delete_objects : typing.Optional[bool]
            Deletion from storage enabled

        title : typing.Optional[str]
            Storage title

        description : typing.Optional[str]
            Storage description

        project : typing.Optional[int]
            Project ID

        container : typing.Optional[str]
            Azure blob container

        prefix : typing.Optional[str]
            Azure blob prefix name

        account_name : typing.Optional[str]
            Azure Blob account name

        account_key : typing.Optional[str]
            Azure Blob account key

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
            await client.export_storage.azure.validate()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/storages/export/azure/validate",
            method="POST",
            json={
                "id": id,
                "can_delete_objects": can_delete_objects,
                "title": title,
                "description": description,
                "project": project,
                "container": container,
                "prefix": prefix,
                "account_name": account_name,
                "account_key": account_key,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> AzureBlobExportStorage:
        """

        Get a specific Azure export storage connection. You will need to provide the export storage ID. You can find this using [List export storages](list).

        For more information about working with external storage, see [Sync data from external storage](https://labelstud.io/guide/storage).

        Parameters
        ----------
        id : int
            A unique integer value identifying this azure blob export storage.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AzureBlobExportStorage


        Examples
        --------
        import asyncio

        from label_studio_sdk import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.export_storage.azure.get(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/storages/export/azure/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AzureBlobExportStorage,
                    parse_obj_as(
                        type_=AzureBlobExportStorage,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """

        Delete a specific Azure export storage connection. You will need to provide the export storage ID. You can find this using [List export storages](list).

        Deleting an export/target storage connection does not affect tasks with synced data in Label Studio. If you want to remove the tasks that were synced from the external storage, you will need to delete them manually from within the Label Studio UI or use the [Delete tasks](../../tasks/delete-all-tasks) API.

        Parameters
        ----------
        id : int
            A unique integer value identifying this azure blob export storage.

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
            await client.export_storage.azure.delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/storages/export/azure/{jsonable_encoder(id)}",
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
        *,
        can_delete_objects: typing.Optional[bool] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        project: typing.Optional[int] = OMIT,
        container: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        account_name: typing.Optional[str] = OMIT,
        account_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AzureUpdateResponse:
        """

        Update a specific Azure export storage connection. You will need to provide the export storage ID. You can find this using [List export storages](list).

        For more information about working with external storage, see [Sync data from external storage](https://labelstud.io/guide/storage).

        Parameters
        ----------
        id : int
            A unique integer value identifying this azure blob export storage.

        can_delete_objects : typing.Optional[bool]
            Deletion from storage enabled

        title : typing.Optional[str]
            Storage title

        description : typing.Optional[str]
            Storage description

        project : typing.Optional[int]
            Project ID

        container : typing.Optional[str]
            Azure blob container

        prefix : typing.Optional[str]
            Azure blob prefix name

        account_name : typing.Optional[str]
            Azure Blob account name

        account_key : typing.Optional[str]
            Azure Blob account key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AzureUpdateResponse


        Examples
        --------
        import asyncio

        from label_studio_sdk import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.export_storage.azure.update(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/storages/export/azure/{jsonable_encoder(id)}",
            method="PATCH",
            json={
                "can_delete_objects": can_delete_objects,
                "title": title,
                "description": description,
                "project": project,
                "container": container,
                "prefix": prefix,
                "account_name": account_name,
                "account_key": account_key,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AzureUpdateResponse,
                    parse_obj_as(
                        type_=AzureUpdateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def sync(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> AzureBlobExportStorage:
        """

        Sync tasks to an Azure export/target storage connection. You will need to provide the export storage ID. You can find this using [List export storages](list).

        Sync operations with external containers only go one way. They either create tasks from objects in the container (source/import storage) or push annotations to the output container (export/target storage). Changing something on the Microsoft side doesn’t guarantee consistency in results.

        <Note>Before proceeding, you should review [How sync operations work - Source storage](https://labelstud.io/guide/storage#Source-storage) to ensure that your data remains secure and private.</Note>

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AzureBlobExportStorage


        Examples
        --------
        import asyncio

        from label_studio_sdk import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.export_storage.azure.sync(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/storages/export/azure/{jsonable_encoder(id)}/sync",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AzureBlobExportStorage,
                    parse_obj_as(
                        type_=AzureBlobExportStorage,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
