from unittest import skip

from drf_api.monitoring.models import Health
import nose.tools as nt


class TestHealth(object):

    def setup(self):
        self.health = Health()

    def test_unstable_by_default(self):
        nt.assert_equal(self.health.get_status(), "unstable")

    def test_up_and_running(self):
        self.health.started()
        nt.assert_equal(self.health.get_status(), "healthy")

    # @skip("WIP")
    def test_degraded(self):
        self.health.started()
        self.health.service_error()
        nt.assert_equal(self.health.get_status(), "degraded")
