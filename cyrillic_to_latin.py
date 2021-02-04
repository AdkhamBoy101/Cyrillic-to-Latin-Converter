#=====================================================#
#----CYRILLIC ALPHABET TO LATIN ALPHABET CONVERTER----#
#=====================================================#

class Converter(object):
    cyrillic = {
        u'\u0410': u'A',
        u'\u0411': u'B',
        u'\u0412': u'V',
        u'\u0413': u'G',
        u'\u0414': u'D',
        u'\u0415': u'Ye',
        u'\u0401': u'Yo',
        u'\u0416': u'J',
        u'\u0417': u'Z',
        u'\u0418': u'I',
        u'\u0419': u'Y',
        u'\u041A': u'K',
        u'\u041B': u'L',
        u'\u041C': u'M',
        u'\u041D': u'N',
        u'\u041E': u'O',
        u'\u041F': u'P',
        u'\u0420': u'R',
        u'\u0421': u'S',
        u'\u0422': u'T',
        u'\u0423': u'U',
        u'\u0424': u'F',
        u'\u0425': u'X',
        u'\u0426': u'Ts',
        u'\u0427': u'Ch',
        u'\u0428': u'Sh',
        u'\u0429': u'Sh',
        u'\u042A': u"'",
        u'\u042B': u'I',
        u'\u042D': u'E',
        u'\u042E': u'Yu',
        u'\u042F': u'Ya',
        u'\u049A': u'Q',
        u'\u04B2': u'H',
        u'\u040E': u"O'",
        u'\u0492': u"G'",
        u'\u0430': u'a',
        u'\u0431': u'b',
        u'\u0432': u'v',
        u'\u0433': u'g',
        u'\u0434': u'd',
        u'\u0435': u'e',
        u'\u0451': u'yo',
        u'\u0436': u'j',
        u'\u0437': u'z',
        u'\u0438': u'i',
        u'\u0439': u'y',
        u'\u043A': u'k',
        u'\u043B': u'l',
        u'\u043C': u'm',
        u'\u043D': u'n',
        u'\u043E': u'o',
        u'\u043F': u'p',
        u'\u0440': u'r',
        u'\u0441': u's',
        u'\u0442': u't',
        u'\u0443': u'u',
        u'\u0444': u'f',
        u'\u0445': u'x',
        u'\u0446': u'ts',
        u'\u0447': u'ch',
        u'\u0448': u'sh',
        u'\u0449': u'sh',
        u'\u044B': u'i',
        u'\u044D': u'e',
        u'\u044E': u'yu',
        u'\u044F': u'ya',
        u'\u049B': u'q',
        u'\u04B3': u'h',
        u'\u045E': u"o'",
        u'\u0493': u"g'",
        u'\u044A': u"'"
    }
    def __init__(self,txt):
        self.txt = txt
        
    def from_cyrillic(self,char):
        if char in self.cyrillic:
            return self.cyrillic[char]
        else:
            return char
    
    def transliterate(self):
        return ''.join([self.from_cyrillic(val) for val in self.txt])


cir = Converter('Ваши действия в режиме инкогнито будут недоступны другим пользователям этого устройства. Однако закладки и скачанные файлы сохранятся')
print(cir.transliterate()) # Vashi deystviya v rejime inkognito budut nedostupni drugim polьzovatelyam etogo ustroystva. Odnako zakladki i skachannie fayli soxranyatsya



