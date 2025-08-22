
import functools
import requests
import logging

from ..button import PiKVMBaseButton

_LOGGER = logging.getLogger(__name__)


class PiKVMLongPressPowerButton(PiKVMBaseButton):

    def __init__(self, coordinator, unique_id_base, device_name) -> None:
        """Initialize the sensor."""
        name = f"{device_name} Long Press Power Button"
        super().__init__(
            coordinator,
            unique_id_base,
            "ATX_long_press_power",
            name,
            icon="mdi:check-circle",
        )
    
    async def async_press(self) -> None:
        """Handle the button press"""
        try:
            response = await self.coordinator.hass.async_add_executor_job(
                functools.partial(
                    self.coordinator.session.post,
                    f"{self.coordinator.url}/api/atx/click?button=power_long",
                    auth=self.coordinator.auth,
                    timeout=10,
                )
            )
        except requests.exceptions.RequestException as err:
            _LOGGER.error("Failed to long press power button")
