"""Platform for button integration."""

import logging

from homeassistant.components.button import ButtonEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .entity import PiKVMEntity
from .utils import get_unique_id_base

_LOGGER = logging.getLogger(__name__)


class PiKVMBaseButton(PiKVMEntity, ButtonEntity):
    """Base class for a PiKVM button."""
    def __init__(
            self,
            coordinator,
            unique_id_base,
            button_type,
            name,
            icon=None,
        ) -> None:
            """Initialize the sensor."""
            super().__init__(coordinator, unique_id_base)
            self._attr_unique_id = f"{unique_id_base}_{button_type}"
            self._attr_name = name
            self._attr_icon = icon
            self._unique_id_base = unique_id_base


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up PiKVM buttons from a config entry."""
    _LOGGER.debug("Setting up PiKVM buttons from config entry")
    coordinator = hass.data[DOMAIN][config_entry.entry_id]
    unique_id_base = get_unique_id_base(config_entry, coordinator)
    device_name = coordinator.data["meta"]["server"]["host"]

    # Use "pikvm" if the device name is "localhost.localdomain"
    if device_name == "localhost.localdomain":
        device_name = DOMAIN
    else:
        device_name = device_name.replace(".", "_")

    lazy_import_buttons()
    button_classes = lazy_import_buttons()

    buttons = [
         button_classes["power_click"](coordinator, unique_id_base, device_name),
    ]

    async_add_entities(buttons, True)
    _LOGGER.debug("%s PiKVM buttons added to Home Assistant", device_name)


# pylint: disable=import-outside-toplevel
def lazy_import_buttons():
     """Lazy load the button classes."""
     from .buttons.pikvm_atx_short_click import PiKVMClickPowerButton

     return {
          "power_click": PiKVMClickPowerButton
     }