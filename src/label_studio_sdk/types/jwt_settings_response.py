# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class JwtSettingsResponse(UniversalBaseModel):
    api_tokens_enabled: bool = pydantic.Field()
    """
    Whether JWT API tokens are enabled
    """

    legacy_api_tokens_enabled: bool = pydantic.Field()
    """
    Whether legacy API tokens are enabled
    """

    api_token_ttl_days: int = pydantic.Field()
    """
    Number of days before API tokens expire
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
