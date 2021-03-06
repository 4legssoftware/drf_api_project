import nose.tools as nt

from drf_api.monitoring.models import Health


class TestHealth:

    def setup(self):
        self.health = Health()

    def test_unstable_by_default(self):
        nt.assert_equal(self.health.get_status(), "unstable")

    def test_up_and_running(self):
        self.health.started()
        nt.assert_equal(self.health.get_status(), "healthy")

    # @skip("if you want ignore a test temporarily")
    def test_degraded(self):
        self.health.started()
        self.health.service_error()
        nt.assert_equal(self.health.get_status(), "degraded")
