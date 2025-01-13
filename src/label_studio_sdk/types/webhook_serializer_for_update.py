# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .webhook_serializer_for_update_actions_item import WebhookSerializerForUpdateActionsItem
import datetime as dt
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class WebhookSerializerForUpdate(UniversalBaseModel):
    id: typing.Optional[int] = None
    organization: typing.Optional[int] = None
    project: typing.Optional[int] = None
    url: str = pydantic.Field()
    """
    URL of webhook
    """

    send_payload: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If value is False send only action
    """

    send_for_all_actions: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If value is False - used only for actions from WebhookAction
    """

    headers: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Key Value Json of headers
    """

    is_active: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If value is False the webhook is disabled
    """

    actions: typing.Optional[typing.List[WebhookSerializerForUpdateActionsItem]] = None
    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Creation time
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Last update time
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
