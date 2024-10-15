from unittest import TestCase
from fastapi.testclient import TestClient
from coze_api.app.application import create_application


class TestBaseEventHandler(TestCase):
    def test_startup_handler(self):
        app = create_application()
        with self.assertLogs('coze_api', level='INFO') as cm:

            with TestClient(app):
                pass
            self.assertEqual(cm.output,
                             ['INFO:coze_api:Starting up ...',
                              'INFO:coze_api:Shutting down ...'])
