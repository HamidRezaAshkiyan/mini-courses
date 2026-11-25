from abc import ABC, abstractmethod


# --- Target Interface ---

class WeatherClient(ABC):
    @abstractmethod
    def get_celsius(self, city: str) -> float:
        pass


# --- Incompatible Legacy Service ---

class LegacyFahrenheitApi:
    def fetch_temp_f(self, location: str) -> float:
        data = {"Tehran": 77.0, "London": 59.0}
        return data.get(location, 68.0)


# --- Adapter ---

class FahrenheitToCelsiusAdapter(WeatherClient):
    def __init__(self, legacy_api: LegacyFahrenheitApi) -> None:
        self._legacy_api = legacy_api

    def get_celsius(self, city: str) -> float:
        temp_f = self._legacy_api.fetch_temp_f(city)
        return round((temp_f - 32.0) * 5.0 / 9.0, 1)


# --- Decorators (implement the SAME WeatherClient interface) ---

class CachingWeatherDecorator(WeatherClient):
    def __init__(self, inner: WeatherClient) -> None:
        self._inner = inner
        self._cache: dict[str, float] = {}

    def get_celsius(self, city: str) -> float:
        if city not in self._cache:
            print(f"[CACHE MISS] fetching {city}...")
            self._cache[city] = self._inner.get_celsius(city)
        else:
            print(f"[CACHE HIT]  returning cached {city}")
        return self._cache[city]


if __name__ == "__main__":
    # Compose Adapter + Decorator seamlessly
    client: WeatherClient = CachingWeatherDecorator(
        FahrenheitToCelsiusAdapter(LegacyFahrenheitApi())
    )
    print("Tehran:", client.get_celsius("Tehran"), "°C")
    print("Tehran:", client.get_celsius("Tehran"), "°C")
    print("London:", client.get_celsius("London"), "°C")
