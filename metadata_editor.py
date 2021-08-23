import mutagen.id3
import mutagen.mp3


class MetadataEditor:
    def __init__(self, path):
        self.song_path = path
        try:
            self.tags = mutagen.id3.ID3(self.song_path)
            self.audio = mutagen.mp3.MP3(path)
            try:
                self.audio.add_tags()
            except:
                pass

        except mutagen.id3.ID3NoHeaderError:
            self.tags = mutagen.id3.ID3()

    def tag(self, tag_data):
        for tag, value in tag_data.items():
            string = 'mutagen.id3.%s(encoding=3, text=u"%s")' % (tag, value)
            print(string)
            if tag != 'APIC':
                self.tags[tag] = eval(string)

            else:
                self.tags[tag] = mutagen.id3.APIC(
                    encoding=3,
                    mime=u'image/png',
                    type=3,
                    desc=u'Cover',
                    data=value[1]
                )

                self.audio.tags.add(
                    mutagen.id3.APIC(
                        mime=u'image/png',
                        type=3,
                        desc=u'Cover',
                        data=value[1]
                    )
                )

        self.audio.save()
        # self.tags.save(self.song_path)
