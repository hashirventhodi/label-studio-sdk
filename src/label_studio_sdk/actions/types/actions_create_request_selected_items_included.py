# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ...core.serialization import FieldMetadata
import pydantic
import typing
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class ActionsCreateRequestSelectedItemsIncluded(UniversalBaseModel):
    all_: typing_extensions.Annotated[bool, FieldMetadata(alias="all")] = pydantic.Field()
    """
    No tasks are selected
    """

    included: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    List of included task IDs
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
