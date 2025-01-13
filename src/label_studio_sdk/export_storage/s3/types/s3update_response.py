# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import typing_extensions
from ....core.serialization import FieldMetadata
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class S3UpdateResponse(UniversalBaseModel):
    can_delete_objects: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Deletion from storage enabled.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    Storage title
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Storage description
    """

    project: typing.Optional[int] = pydantic.Field(default=None)
    """
    Project ID
    """

    bucket: typing.Optional[str] = pydantic.Field(default=None)
    """
    S3 bucket name
    """

    prefix: typing.Optional[str] = pydantic.Field(default=None)
    """
    S3 bucket prefix
    """

    aws_access_key_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    AWS_ACCESS_KEY_ID
    """

    aws_secret_access_key: typing.Optional[str] = pydantic.Field(default=None)
    """
    AWS_SECRET_ACCESS_KEY
    """

    aws_session_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    AWS_SESSION_TOKEN
    """

    aws_sse_kms_key_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    AWS SSE KMS Key ID
    """

    region_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    AWS Region
    """

    s3endpoint: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="s3_endpoint")] = pydantic.Field(
        default=None
    )
    """
    S3 Endpoint
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
