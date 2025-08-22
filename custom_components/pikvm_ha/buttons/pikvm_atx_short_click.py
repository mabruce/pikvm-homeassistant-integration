
import functools
import requests
import logging

from ..button import PiKVMBaseButton

_LOGGER = logging.getLogger(__name__)


class PiKVMClickPowerButton(PiKVMBaseButton):

    def __init__(self, coordinator, unique_id_base, device_name) -> None:
        """Initialize the sensor."""
        name = f"{device_name} Click ATX Power Button"
        super().__init__(
            coordinator,
            unique_id_base,
            "ATX_click_power",
            name,
            icon="mdi:check-circle",
        )
    
    async def async_press(self) -> None:
        """Handle the button press"""
        try:
            response = await self.coordinator.hass.async_add_executor_job(
                functools.partial(
                    self.coordinator.session.post,
                    f"{self.coordinator.url}/api/atx/click?button=power",
                    auth=self.coordinator.auth,
                    timeout=10,
                )
            )
        except requests.exceptions.RequestException as err:
            _LOGGER.error("Failed to click power button")
