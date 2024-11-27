class VoiceNote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="voice_notes")
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to="voice_notes/")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"VoiceNote by {self.user.username} in {self.room.name}"

class Call(models.Model):
    CALL_TYPE_CHOICES = [
        ('audio', 'Audio'),
        ('video', 'Video'),
    ]
    caller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="initiated_calls")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_calls")
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    call_type = models.CharField(max_length=10, choices=CALL_TYPE_CHOICES)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.call_type.capitalize()} call between {self.caller.username} and {self.receiver.username}"
