from django.db import models


class Schedule(models.Model):
    vtu_id = models.CharField(max_length=8)
    tts_id = models.CharField(max_length=8)
    sub_id = models.CharField(max_length=9)
    room_id = models.CharField(max_length=4)
    date = models.DateField()
    session = models.CharField(max_length=2, choices=[('AN', 'AN'), ('FN', 'FN')])

    def str(self):
        return 'Seat: %d, Room: %d, Sub: %d, Session: %d, Date: %s'.format(self.room_id, self.sub_id,
                                                                           self.session, str(self.date))
