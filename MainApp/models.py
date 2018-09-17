from django.db import models


class Schedule(models.Model):
    vtu_id = models.IntegerField()
    tts_id = models.IntegerField()
    sub_id = models.IntegerField()
    room_id = models.IntegerField()
    seat_id = models.IntegerField()
    date = models.DateField()
    session = models.CharField(max_length=2, choices=[('AN', 'AN'), ('FN', 'FN')])

    def str(self):
        return 'Seat: %d, Room: %d, Sub: %d, Session: %d, Date: %s'.format(self.seat_id, self.room_id, self.sub_id,
                                                                           self.session, str(self.date))
