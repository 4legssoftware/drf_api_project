from django.db import models


class Health(models.Model):
    status = 'unstable'

    def started(self):
        self.status = 'healthy'

    def get_status(self):
        return self.status

    def service_error(self):
        self.status = 'degraded'
