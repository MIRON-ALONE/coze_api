import pytest
from pydantic.error_wrappers import ValidationError
from coze_api.app.configs.base import Settings
from coze_api.app.configs import get_settings


@pytest.mark.parametrize("mode, settings_cls",
                         [("DEV", Settings),
                          ("TEST", Settings),
                          ("PROD", Settings),
                          (None, Settings),
                          ("None", Settings)])
def test_get_settings(monkeypatch, mode, settings_cls):
    get_settings.cache_clear()
    if mode:
        monkeypatch.setenv("MODE", mode)
    settings = get_settings()
    # assert the settings is an instance of the corresponding settings class
    assert isinstance(settings, settings_cls)
    if mode:
        monkeypatch.delenv("MODE")


@pytest.mark.parametrize("cors_origins, expected_result",
                         [(["https://example.com", "https://example.de"],
                           ["https://example.com", "https://example.de"]),
                          ("https://example.com, https://example.de",
                           ["https://example.com", "https://example.de"]),
                          ("['https://example.com', 'https://example.de']",
                           ["https://example.com", "https://example.de"])
                          ])
def test_assemble_cors_origins_success(cors_origins, expected_result):
    s = Settings(CORS_ORIGINS=cors_origins,
                 CORS_ORIGIN_REGEX='https:\\/\\/.*\\.example\\.?')
    assert s.CORS_ORIGINS == expected_result


def test_assemble_cors_origins_fail():
    with pytest.raises(ValueError) as e:
        Settings(CORS_ORIGINS=None)
    assert type(e.value) == ValidationError
    assert len(e.value.errors()) == 1
    assert e.value.errors()[0] == dict(loc=('CORS_ORIGINS',),
                                       msg='None',
                                       type='value_error')

