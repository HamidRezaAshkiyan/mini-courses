from dataclasses import dataclass, field


# --- Builder Pattern ---

@dataclass(frozen=True)
class HttpRequest:
    method: str
    url: str
    headers: dict[str, str] = field(default_factory=dict)
    timeout_seconds: int = 30


class HttpRequestBuilder:
    def __init__(self, url: str) -> None:
        self._url = url
        self._method = "GET"
        self._headers: dict[str, str] = {}
        self._timeout = 30

    def method(self, method: str) -> "HttpRequestBuilder":
        self._method = method.upper()
        return self

    def header(self, key: str, value: str) -> "HttpRequestBuilder":
        self._headers[key] = value
        return self

    def timeout(self, seconds: int) -> "HttpRequestBuilder":
        if seconds <= 0:
            raise ValueError("timeout must be positive")
        self._timeout = seconds
        return self

    def build(self) -> HttpRequest:
        return HttpRequest(
            method=self._method,
            url=self._url,
            headers=dict(self._headers),
            timeout_seconds=self._timeout,
        )


# --- Singleton Pattern ---

class AppConfig:
    _instance: "AppConfig | None" = None

    def __new__(cls) -> "AppConfig":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.env = "development"
        return cls._instance


if __name__ == "__main__":
    req = (
        HttpRequestBuilder("https://api.example.com/orders")
        .method("POST")
        .header("Authorization", "Bearer token-123")
        .timeout(10)
        .build()
    )
    print("Built request:", req)

    cfg1 = AppConfig()
    cfg2 = AppConfig()
    cfg1.env = "production"
    print(f"Same instance? {cfg1 is cfg2}, cfg2.env = {cfg2.env}")
