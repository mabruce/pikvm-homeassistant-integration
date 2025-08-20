"""Support for PiKVM ATX enabled sensor."""

from homeassistant.const import EntityCategory

from ..sensor import PiKVMBaseSensor


class PiKVMATXPowerLEDSensor(PiKVMBaseSensor):
    """Representation of a PiKVM ATX power LED sensor."""

    def __init__(self, coordinator, unique_id_base, device_name) -> None:
        """Initialize the sensor."""
        name = f"{device_name} ATX Power LED Enabled"
        super().__init__(
            coordinator,
            unique_id_base,
            "ATX_power_led_enabled",
            name,
            icon="mdi:power",
        )

    @property
    def state(self) -> bool:
        """Return the state of the sensor."""
        return self.coordinator.data["atx"]["leds"]["power"]
