"""Support for PiKVM ATX enabled sensor."""

from homeassistant.const import EntityCategory

from ..sensor import PiKVMBaseSensor


class PiKVMATXEnabledSensor(PiKVMBaseSensor):
    """Representation of a PiKVM ATX enabled sensor."""

    def __init__(self, coordinator, unique_id_base, device_name) -> None:
        """Initialize the sensor."""
        name = f"{device_name} ATX Enabled"
        super().__init__(
            coordinator,
            unique_id_base,
            "ATX_enabled",
            name,
            icon="mdi:check-circle",
        )
        self._attr_entity_category = EntityCategory.DIAGNOSTIC

    @property
    def state(self) -> bool:
        """Return the state of the sensor."""
        return self.coordinator.data["atx"]["enabled"]
