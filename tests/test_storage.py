"""Storage details."""

from __future__ import annotations

import inspect

from homeassistant.core import HomeAssistant
from homeassistant.helpers.storage import Store

from custom_components.neonplan3d.storage import FloorplanData


async def test_large_stores_are_serialised_off_the_event_loop(hass: HomeAssistant) -> None:
    """Images and restore points can be megabytes: their JSON must not be built in the event loop."""
    data = FloorplanData(hass)
    if "serialize_in_event_loop" not in inspect.signature(Store.__init__).parameters:
        return  # before HA 2025.12 every store serialised in the executor
    assert data._image_store._serialize_in_event_loop is False
    assert data._history_store._serialize_in_event_loop is False
