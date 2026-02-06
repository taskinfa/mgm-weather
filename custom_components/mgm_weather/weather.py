"""MGM Hava Durumu platformu."""
from __future__ import annotations

import logging
from datetime import timedelta
import aiohttp
import async_timeout

from homeassistant.components.weather import (
    WeatherEntity,
    WeatherEntityFeature,
    Forecast,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    UnitOfPressure,
    UnitOfSpeed,
    UnitOfTemperature,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
    UpdateFailed,
)

from .const import DOMAIN, API_URL, SCAN_INTERVAL_SECONDS, CONF_CITY

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Config entry kullanarak hava durumu entity'sini ekle."""
    city = entry.data[CONF_CITY]
    
    # Veri güncelleyiciyi (Coordinator) başlat
    coordinator = MGMDataUpdateCoordinator(hass, city)
    await coordinator.async_config_entry_first_refresh()

    async_add_entities([MGMWeatherEntity(coordinator, city)])


class MGMDataUpdateCoordinator(DataUpdateCoordinator):
    """MGM verilerini periyodik olarak çeken sınıf."""

    def __init__(self, hass: HomeAssistant, city: str) -> None:
        """Coordinator'ı başlat."""
        super().__init__(
            hass,
            _LOGGER,
            name=f"MGM Weather {city}",
            update_interval=timedelta(seconds=SCAN_INTERVAL_SECONDS),
        )
        self.city = city
        self.api_url = API_URL.format(city)

    async def _async_update_data(self):
        """API'dan veriyi çek."""
        try:
            async with async_timeout.timeout(10):
                async with aiohttp.ClientSession() as session:
                    async with session.get(self.api_url) as response:
                        if response.status != 200:
                            raise UpdateFailed(f"API Hatası: {response.status}")
                        data = await response.json()
                        
                        # API'den hata mesajı dönerse
                        if "error" in data:
                             raise UpdateFailed(f"API Mesajı: {data['error']}")
                             
                        return data
        except Exception as err:
            raise UpdateFailed(f"MGM verisi alınamadı: {err}")


class MGMWeatherEntity(CoordinatorEntity, WeatherEntity):
    """MGM Hava Durumu Entity'si."""

    _attr_has_entity_name = True
    _attr_native_temperature_unit = UnitOfTemperature.CELSIUS
    _attr_native_pressure_unit = UnitOfPressure.HPA
    _attr_native_wind_speed_unit = UnitOfSpeed.KILOMETERS_PER_HOUR
    _attr_supported_features = WeatherEntityFeature.FORECAST_DAILY

    def __init__(self, coordinator: MGMDataUpdateCoordinator, city: str) -> None:
        """Entity'yi başlat."""
        super().__init__(coordinator)
        self._city = city
        self._attr_unique_id = f"mgm_{city.lower()}"
        self._attr_name = None  # Cihaz adını kullanması için None bırakıyoruz

    @property
    def condition(self) -> str | None:
        """Anlık hava durumu durumu (sunny, cloudy vb.)."""
        return self.coordinator.data.get("condition")

    @property
    def native_temperature(self) -> float | None:
        """Sıcaklık."""
        return self.coordinator.data.get("temperature")

    @property
    def native_pressure(self) -> float | None:
        """Basınç."""
        return self.coordinator.data.get("pressure")

    @property
    def humidity(self) -> float | None:
        """Nem."""
        return self.coordinator.data.get("humidity")

    @property
    def native_wind_speed(self) -> float | None:
        """Rüzgar hızı."""
        return self.coordinator.data.get("wind_speed")

    @property
    def forecast(self) -> list[Forecast] | None:
        """Eski tip tahmin (Geri uyumluluk için, opsiyonel)."""
        return self._get_forecast()

    async def async_forecast_daily(self) -> list[Forecast] | None:
        """Günlük tahmin verisi (Modern HA için)."""
        return self._get_forecast()

    def _get_forecast(self) -> list[Forecast] | None:
        """API verisini HA formatına çevir."""
        forecast_data = []
        api_forecast = self.coordinator.data.get("forecast", [])
        
        for item in api_forecast:
            forecast_data.append({
                "datetime": item["datetime"],
                "native_temperature": item["temperature"],
                "native_templow": item["templow"],
                "condition": item["condition"],
                "humidity": item["humidity"],
            })
        return forecast_data