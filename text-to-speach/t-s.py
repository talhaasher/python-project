from  gtts import gTTS
import os
from deep_translator import (GoogleTranslator,
                             ChatGptTranslator,
                             MicrosoftTranslator,
                             PonsTranslator,
                             LingueeTranslator,
                             MyMemoryTranslator,
                             YandexTranslator,
                             PapagoTranslator,
                             DeeplTranslator,
                             QcriTranslator,
                             single_detection,
                             batch_detection)


languages_info = """
Enter a number (e.g., 1 for Afrikaans, 62 for Maori):
1. Afrikaans                   35. Hebrew                     69. Pashto
2. Albanian                    36. Hindi                      70. Persian
3. Amharic                     37. Hmong                      71. Polish
4. Arabic                      38. Hungarian                  72. Portuguese
5. Armenian                    39. Icelandic                  73. Punjabi
6. Azerbaijani                 40. Igbo                       74. Romanian
7. Basque                      41. Indonesian                 75. Russian
8. Belarusian                  42. Irish                      76. Samoan
9. Bengali                     43. Italian                    77. Scots Gaelic
10. Bosnian                    44. Japanese                   78. Serbian
11. Bulgarian                   45. Javanese                   79. Sesotho
12. Catalan                    46. Kannada                    80. Shona
13. Cebuano                    47. Kazakh                     81. Sindhi
14. Chinese (Simplified)       48. Khmer                      82. Sinhala (Sinhalese)
15. Chinese (Traditional)      49. Korean                     83. Slovak
16. Corsican                   50. Kurdish                    84. Slovenian
17. Croatian                   51. Kyrgyz                     85. Somali
18. Czech                      52. Lao                        86. Spanish
19. Danish                     53. Latin                      87. Sundanese
20. Dutch                      54. Latvian                    88. Swahili
21. English                    55. Lithuanian                 89. Swedish
22. Esperanto                  56. Luxembourgish              90. Tagalog (Filipino)
23. Estonian                   57. Macedonian                 91. Tajik
24. Finnish                    58. Malagasy                   92. Tamil
25. French                     59. Malay                      93. Telugu
26. Frisian                    60. Malayalam                  94. Thai
27. Galician                   61. Maltese                    95. Turkish
28. Georgian                   62. Maori                      96. Ukrainian
29. German                     63. Marathi                    97. Urdu
30. Greek                      64. Mongolian                  98. Uzbek
31. Gujarati                   65. Myanmar (Burmese)          99. Vietnamese
32. Haitian Creole             66. Nepali                    100. Welsh
33. Hausa                      67. Norwegian                 101. Xhosa
34. Hawaiian                   68. Nyanja (Chichewa)         102. Yiddish
                               102. Yiddish                   103. Yoruba
                               104. Zulu
"""

language_dict_1 = {
    1: 'Afrikaans', 2: 'Albanian', 3: 'Amharic', 4: 'Arabic', 5: 'Armenian',
    6: 'Azerbaijani', 7: 'Basque', 8: 'Belarusian', 9: 'Bengali', 10: 'Bosnian',
    11: 'Bulgarian', 12: 'Catalan', 13: 'Cebuano', 14: 'Chinese (Simplified)',
    15: 'Chinese (Traditional)', 16: 'Corsican', 17: 'Croatian', 18: 'Czech',
    19: 'Danish', 20: 'Dutch', 21: 'English', 22: 'Esperanto', 23: 'Estonian',
    24: 'Finnish', 25: 'French', 26: 'Frisian', 27: 'Galician', 28: 'Georgian',
    29: 'German', 30: 'Greek', 31: 'Gujarati', 32: 'Haitian Creole', 33: 'Hausa',
    34: 'Hawaiian', 35: 'Hebrew', 36: 'Hindi', 37: 'Hmong', 38: 'Hungarian',
    39: 'Icelandic', 40: 'Igbo', 41: 'Indonesian', 42: 'Irish', 43: 'Italian',
    44: 'Japanese', 45: 'Javanese', 46: 'Kannada', 47: 'Kazakh', 48: 'Khmer',
    49: 'Korean', 50: 'Kurdish', 51: 'Kyrgyz', 52: 'Lao', 53: 'Latin', 54: 'Latvian',
    55: 'Lithuanian', 56: 'Luxembourgish', 57: 'Macedonian', 58: 'Malagasy',
    59: 'Malay', 60: 'Malayalam', 61: 'Maltese', 62: 'Maori', 63: 'Marathi',
    64: 'Mongolian', 65: 'Myanmar (Burmese)', 66: 'Nepali', 67: 'Norwegian',
    68: 'Nyanja (Chichewa)', 69: 'Pashto', 70: 'Persian', 71: 'Polish',
    72: 'Portuguese', 73: 'Punjabi', 74: 'Romanian', 75: 'Russian', 76: 'Samoan',
    77: 'Scots Gaelic', 78: 'Serbian', 79: 'Sesotho', 80: 'Shona', 81: 'Sindhi',
    82: 'Sinhala (Sinhalese)', 83: 'Slovak', 84: 'Slovenian', 85: 'Somali',
    86: 'Spanish', 87: 'Sundanese', 88: 'Swahili', 89: 'Swedish', 90: 'Tagalog (Filipino)',
    91: 'Tajik', 92: 'Tamil', 93: 'Telugu', 94: 'Thai', 95: 'Turkish',
    96: 'Ukrainian', 97: 'Urdu', 98: 'Uzbek', 99: 'Vietnamese', 100: 'Welsh',
    101: 'Xhosa', 102: 'Yiddish', 103: 'Yoruba', 104: 'Zulu'
}

language_dict_2 = {
    'Afrikaans': 'af', 'Albanian': 'sq', 'Amharic': 'am', 'Arabic': 'ar', 'Armenian': 'hy',
    'Azerbaijani': 'az', 'Basque': 'eu', 'Belarusian': 'be', 'Bengali': 'bn', 'Bosnian': 'bs',
    'Bulgarian': 'bg', 'Catalan': 'ca', 'Cebuano': 'ceb', 'Chinese (Simplified)': 'zh-cn',
    'Chinese (Traditional)': 'zh-tw', 'Corsican': 'co', 'Croatian': 'hr', 'Czech': 'cs',
    'Danish': 'da', 'Dutch': 'nl', 'English': 'en', 'Esperanto': 'eo', 'Estonian': 'et',
    'Finnish': 'fi', 'French': 'fr', 'Frisian': 'fy', 'Galician': 'gl', 'Georgian': 'ka',
    'German': 'de', 'Greek': 'el', 'Gujarati': 'gu', 'Haitian Creole': 'ht', 'Hausa': 'ha',
    'Hawaiian': 'haw', 'Hebrew': 'he', 'Hindi': 'hi', 'Hmong': 'hmn', 'Hungarian': 'hu',
    'Icelandic': 'is', 'Igbo': 'ig', 'Indonesian': 'id', 'Irish': 'ga', 'Italian': 'it',
    'Japanese': 'ja', 'Javanese': 'jv', 'Kannada': 'kn', 'Kazakh': 'kk', 'Khmer': 'km',
    'Korean': 'ko', 'Kurdish': 'ku', 'Kyrgyz': 'ky', 'Lao': 'lo', 'Latin': 'la', 'Latvian': 'lv',
    'Lithuanian': 'lt', 'Luxembourgish': 'lb', 'Macedonian': 'mk', 'Malagasy': 'mg', 'Malay': 'ms',
    'Malayalam': 'ml', 'Maltese': 'mt', 'Maori': 'mi', 'Marathi': 'mr', 'Mongolian': 'mn',
    'Myanmar (Burmese)': 'my', 'Nepali': 'ne', 'Norwegian': 'no', 'Nyanja (Chichewa)': 'ny',
    'Pashto': 'ps', 'Persian': 'fa', 'Polish': 'pl', 'Portuguese': 'pt', 'Punjabi': 'pa',
    'Romanian': 'ro', 'Russian': 'ru', 'Samoan': 'sm', 'Scots Gaelic': 'gd', 'Serbian': 'sr',
    'Sesotho': 'st', 'Shona': 'sn', 'Sindhi': 'sd', 'Sinhala (Sinhalese)': 'si', 'Slovak': 'sk',
    'Slovenian': 'sl', 'Somali': 'so', 'Spanish': 'es', 'Sundanese': 'su', 'Swahili': 'sw',
    'Swedish': 'sv', 'Tagalog (Filipino)': 'tl', 'Tajik': 'tg', 'Tamil': 'ta', 'Telugu': 'te',
    'Thai': 'th', 'Turkish': 'tr', 'Ukrainian': 'uk', 'Urdu': 'ur', 'Uzbek': 'uz',
    'Vietnamese': 'vi', 'Welsh': 'cy', 'Xhosa': 'xh', 'Yiddish': 'yi', 'Yoruba': 'yo', 'Zulu': 'zu'
}
def translate():

    print(languages_info)
    user_input =int( input(":"))

    if user_input in language_dict_1:
        lang_name = language_dict_1[user_input]
        lang_code = language_dict_2.get(lang_name)
        print(f"You Selected {lang_name}")
        audio_convet(lang_name,lang_code)
        
def audio_convet(lang_name,lang_code):

    text_ts=str(input("Input text:"))
    name_of_audio=input("Audio File Name:")    
    translated = GoogleTranslator(source='auto', target=lang_code).translate(text_ts)
    Original_text=text_ts
    translated_text=translated
    print("orginal:"+Original_text+"\n translated:"+translated_text)

    audio=gTTS(text=translated,lang=lang_code,slow=False)
    name_of_audio=name_of_audio+".mp3"
    audio.save(name_of_audio)
    os.system(name_of_audio)


translate()