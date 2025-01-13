# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from .actions_create_request_filters_conjunction import ActionsCreateRequestFiltersConjunction
import pydantic
import typing
from .actions_create_request_filters_items_item import ActionsCreateRequestFiltersItemsItem
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class ActionsCreateRequestFilters(UniversalBaseModel):
    """
    Filters to apply on tasks. You can use [the helper class `Filters` from this page](https://labelstud.io/sdk/data_manager.html) to create Data Manager Filters.<br>Example: `{"conjunction": "or", "items": [{"filter": "filter:tasks:completed_at", "operator": "greater", "type": "Datetime", "value": "2021-01-01T00:00:00.000Z"}]}`
    """

    conjunction: ActionsCreateRequestFiltersConjunction = pydantic.Field()
    """
    Logical conjunction for the filters. This conjunction (either "or" or "and") will be applied to all items in the filters list. It is not possible to combine "or" and "and" within one list of filters. All filters will be either combined with "or" or with "and", but not a mix of both.
    """

    items: typing.List[ActionsCreateRequestFiltersItemsItem] = pydantic.Field()
    """
    List of filter items
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
