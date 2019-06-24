import xbmc
import xbmcgui

to_play = "http://distribution.bbb3d.renderfarming.net/video/mp4/bbb_sunflower_1080p_60fps_normal.mp4"


class MyPlayer(xbmc.Player):
    def __init__(self, *args, **kwargs):
        self.url = kwargs.get("url")
        xbmc.log(
            "The Player has been initialized with the URL: %s" % (self.url),
            xbmc.LOGERROR,
        )

    def onPlayBackStarted(self):
        xbmc.log("Playback started!", xbmc.LOGERROR)

    def onPlayBackEnded(self):
        xbmc.log("Playback ended!", xbmc.LOGERROR)

    def onPlayBackStopped(self):
        self.onPlayBackEnded()

    def onPlayBackError(self):
        self.onPlayBackEnded()


if __name__ == "__main__":
    xbmc.log("Addon started!", xbmc.LOGERROR)
    MyPlayer(url=to_play).play(to_play, xbmcgui.ListItem(label="Big Buck Bunny"))
