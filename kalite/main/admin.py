from django.contrib import admin
from models import *

class VideoLogAdmin(admin.ModelAdmin):
    list_display = ("youtube_id", "user", "points", "total_seconds_watched", "complete",)
    list_filter = ("youtube_id", "user", "complete",)
admin.site.register(VideoLog, VideoLogAdmin)


class ExerciseLogAdmin(admin.ModelAdmin):
    list_display = ("exercise_id", "user", "streak_progress", "complete",)
    list_filter = ("exercise_id", "user", "complete",)
admin.site.register(ExerciseLog, ExerciseLogAdmin)

class UserLogAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserLog, UserLogAdmin)
    
class VideoFileAdmin(admin.ModelAdmin):
    list_display = ("youtube_id", "flagged_for_download", "download_in_progress", "cancel_download", "percent_complete",)
    list_filter = ("flagged_for_download", "download_in_progress", "flagged_for_subtitle_download", "subtitle_download_in_progress",)
admin.site.register(VideoFile, VideoFileAdmin)

class LanguagePackAdmin(admin.ModelAdmin):
	list_display = ("lang_id", "lang_name")
	list_filter = ("lang_id", "lang_name")
admin.site.register(LanguagePack, LanguagePackAdmin)

class PlaylistAdmin(admin.ModelAdmin):
    list_display = ("title","description","forked_from","creator")
    list_filter = ("creator",)
admin.site.register(Playlist, PlaylistAdmin)

class PlaylistEntityAdmin(admin.ModelAdmin):
    list_display = ("entity_source","entity_kind","entity_id","playlist","teacher_note","sort_order")
    list_filter = ("playlist", "entity_kind",)
admin.site.register(PlaylistEntity, PlaylistEntityAdmin)
