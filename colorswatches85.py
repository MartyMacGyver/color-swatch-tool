#!/usr/bin/python

#   Copyright (c) 2015 Martin F. Falatic
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""
Based on http://www.tcl.tk/man/tcl8.5/TkCmd/colors.htm

"""

from __future__ import print_function

from collections import OrderedDict


COLORS_ODICT = OrderedDict([
    ('000000', ['black',   'gray0', 'grey0']),
    ('030303', ['gray1',   'grey1']),
    ('050505', ['gray2',   'grey2']),
    ('080808', ['gray3',   'grey3']),
    ('0A0A0A', ['gray4',   'grey4']),
    ('0D0D0D', ['gray5',   'grey5']),
    ('0F0F0F', ['gray6',   'grey6']),
    ('121212', ['gray7',   'grey7']),
    ('141414', ['gray8',   'grey8']),
    ('171717', ['gray9',   'grey9']),
    ('1A1A1A', ['gray10',  'grey10']),
    ('1C1C1C', ['gray11',  'grey11']),
    ('1F1F1F', ['gray12',  'grey12']),
    ('212121', ['gray13',  'grey13']),
    ('242424', ['gray14',  'grey14']),
    ('262626', ['gray15',  'grey15']),
    ('292929', ['gray16',  'grey16']),
    ('2B2B2B', ['gray17',  'grey17']),
    ('2E2E2E', ['gray18',  'grey18']),
    ('303030', ['gray19',  'grey19']),
    ('333333', ['gray20',  'grey20']),
    ('363636', ['gray21',  'grey21']),
    ('383838', ['gray22',  'grey22']),
    ('3B3B3B', ['gray23',  'grey23']),
    ('3D3D3D', ['gray24',  'grey24']),
    ('404040', ['gray25',  'grey25']),
    ('424242', ['gray26',  'grey26']),
    ('454545', ['gray27',  'grey27']),
    ('474747', ['gray28',  'grey28']),
    ('4A4A4A', ['gray29',  'grey29']),
    ('4D4D4D', ['gray30',  'grey30']),
    ('4F4F4F', ['gray31',  'grey31']),
    ('525252', ['gray32',  'grey32']),
    ('545454', ['gray33',  'grey33']),
    ('575757', ['gray34',  'grey34']),
    ('595959', ['gray35',  'grey35']),
    ('5C5C5C', ['gray36',  'grey36']),
    ('5E5E5E', ['gray37',  'grey37']),
    ('616161', ['gray38',  'grey38']),
    ('636363', ['gray39',  'grey39']),
    ('666666', ['gray40',  'grey40']),
    ('696969', ['gray41',  'grey41', 'dim gray', 'dim grey', 'DimGray', 'DimGrey']),
    ('6B6B6B', ['gray42',  'grey42']),
    ('6E6E6E', ['gray43',  'grey43']),
    ('707070', ['gray44',  'grey44']),
    ('737373', ['gray45',  'grey45']),
    ('757575', ['gray46',  'grey46']),
    ('787878', ['gray47',  'grey47']),
    ('7A7A7A', ['gray48',  'grey48']),
    ('7D7D7D', ['gray49',  'grey49']),
    ('7F7F7F', ['gray50',  'grey50']),
    ('828282', ['gray51',  'grey51']),
    ('858585', ['gray52',  'grey52']),
    ('878787', ['gray53',  'grey53']),
    ('8A8A8A', ['gray54',  'grey54']),
    ('8C8C8C', ['gray55',  'grey55']),
    ('8F8F8F', ['gray56',  'grey56']),
    ('919191', ['gray57',  'grey57']),
    ('949494', ['gray58',  'grey58']),
    ('969696', ['gray59',  'grey59']),
    ('999999', ['gray60',  'grey60']),
    ('9C9C9C', ['gray61',  'grey61']),
    ('9E9E9E', ['gray62',  'grey62']),
    ('A1A1A1', ['gray63',  'grey63']),
    ('A3A3A3', ['gray64',  'grey64']),
    ('A6A6A6', ['gray65',  'grey65']),
    ('A8A8A8', ['gray66',  'grey66']),
    ('A9A9A9', ['dark gray', 'dark grey', 'DarkGray', 'DarkGrey']),
    ('ABABAB', ['gray67',  'grey67']),
    ('ADADAD', ['gray68',  'grey68']),
    ('B0B0B0', ['gray69',  'grey69']),
    ('B3B3B3', ['gray70',  'grey70']),
    ('B5B5B5', ['gray71',  'grey71']),
    ('B8B8B8', ['gray72',  'grey72']),
    ('BABABA', ['gray73',  'grey73']),
    ('BDBDBD', ['gray74',  'grey74']),
    ('BEBEBE', ['gray',    'grey']),
    ('BFBFBF', ['gray75',  'grey75']),
    ('C2C2C2', ['gray76',  'grey76']),
    ('C4C4C4', ['gray77',  'grey77']),
    ('C7C7C7', ['gray78',  'grey78']),
    ('C9C9C9', ['gray79',  'grey79']),
    ('CCCCCC', ['gray80',  'grey80']),
    ('CFCFCF', ['gray81',  'grey81']),
    ('D1D1D1', ['gray82',  'grey82']),
    ('D3D3D3', ['light gray', 'light grey', 'LightGray', 'LightGrey']),
    ('D4D4D4', ['gray83',  'grey83']),
    ('D6D6D6', ['gray84',  'grey84']),
    ('D9D9D9', ['gray85',  'grey85']),
    ('DBDBDB', ['gray86',  'grey86']),
    ('DCDCDC', ['gainsboro']),
    ('DEDEDE', ['gray87',  'grey87']),
    ('E0E0E0', ['gray88',  'grey88']),
    ('E3E3E3', ['gray89',  'grey89']),
    ('E5E5E5', ['gray90',  'grey90']),
    ('E8E8E8', ['gray91',  'grey91']),
    ('EBEBEB', ['gray92',  'grey92']),
    ('EDEDED', ['gray93',  'grey93']),
    ('F0F0F0', ['gray94',  'grey94']),
    ('F2F2F2', ['gray95',  'grey95']),
    ('F5F5F5', ['gray96',  'grey96', 'white smoke', 'WhiteSmoke']),
    ('F7F7F7', ['gray97',  'grey97']),
    ('FAFAFA', ['gray98',  'grey98']),
    ('FCFCFC', ['gray99',  'grey99']),
    ('FFFFFF', ['gray100', 'grey100', 'white']),

    ('F8F8FF', ['ghost white', 'GhostWhite']),

    ('FFFAFA', ['snow', 'snow1']),
    ('EEE9E9', ['snow2']),
    ('CDC9C9', ['snow3']),
    ('8B8989', ['snow4']),

    ('FFF5EE', ['seashell', 'seashell1']),
    ('EEE5DE', ['seashell2']),
    ('CDC5BF', ['seashell3']),
    ('8B8682', ['seashell4']),

    ('FFFFF0', ['ivory', 'ivory1']),
    ('EEEEE0', ['ivory2']),
    ('CDCDC1', ['ivory3']),
    ('8B8B83', ['ivory4']),

    ('FFFAF0', ['floral white', 'FloralWhite']),

    ('FDF5E6', ['old lace', 'OldLace']),

    ('FAF0E6', ['linen']),

    ('FFEFDB', ['AntiqueWhite1']),
    ('FAEBD7', ['antique white', 'AntiqueWhite']),
    ('EEDFCC', ['AntiqueWhite2']),
    ('CDC0B0', ['AntiqueWhite3']),
    ('8B8378', ['AntiqueWhite4']),

    ('F5F5DC', ['beige']),

    ('FFF8DC', ['cornsilk', 'cornsilk1']),
    ('EEE8CD', ['cornsilk2']),
    ('CDC8B1', ['cornsilk3']),
    ('8B8878', ['cornsilk4']),

    ('FFEFD5', ['papaya whip', 'PapayaWhip']),

    ('FFEBCD', ['blanched almond', 'BlanchedAlmond']),

    ('FFE4B5', ['moccasin']),

    ('FFE4C4', ['bisque', 'bisque1']),
    ('EED5B7', ['bisque2']),
    ('CDB79E', ['bisque3']),
    ('8B7D6B', ['bisque4']),

    ('FFE7BA', ['wheat1']),
    ('F5DEB3', ['wheat']),
    ('EED8AE', ['wheat2']),
    ('CDBA96', ['wheat3']),
    ('8B7E66', ['wheat4']),

    ('FFD39B', ['burlywood1']),
    ('EEC591', ['burlywood2']),
    ('DEB887', ['burlywood']),
    ('CDAA7D', ['burlywood3']),
    ('8B7355', ['burlywood4']),

    ('FFDEAD', ['navajo white', 'NavajoWhite', 'NavajoWhite1']),
    ('EECFA1', ['NavajoWhite2']),
    ('CDB38B', ['NavajoWhite3']),
    ('8B795E', ['NavajoWhite4']),

    ('FFDAB9', ['peach puff', 'PeachPuff', 'PeachPuff1']),
    ('EECBAD', ['PeachPuff2']),
    ('CDAF95', ['PeachPuff3']),
    ('8B7765', ['PeachPuff4']),

    ('FFF0F5', ['lavender blush', 'LavenderBlush', 'LavenderBlush1']),
    ('EEE0E5', ['LavenderBlush2']),
    ('CDC1C5', ['LavenderBlush3']),
    ('8B8386', ['LavenderBlush4']),

    ('F0F8FF', ['alice blue', 'AliceBlue']),

    ('F0FFFF', ['azure', 'azure1']),
    ('E0EEEE', ['azure2']),
    ('C1CDCD', ['azure3']),
    ('838B8B', ['azure4']),

    ('7FFFD4', ['aquamarine', 'aquamarine1']),
    ('76EEC6', ['aquamarine2']),
    ('66CDAA', ['aquamarine3', 'medium aquamarine', 'MediumAquamarine']),
    ('458B74', ['aquamarine4']),

    ('BBFFFF', ['PaleTurquoise1']),
    ('AFEEEE', ['pale turquoise', 'PaleTurquoise']),
    ('AEEEEE', ['PaleTurquoise2']),
    ('96CDCD', ['PaleTurquoise3']),
    ('668B8B', ['PaleTurquoise4']),

    ('48D1CC', ['medium turquoise', 'MediumTurquoise']),

    ('00CED1', ['dark turquoise', 'DarkTurquoise']),

    ('40E0D0', ['turquoise']),
    ('00F5FF', ['turquoise1']),
    ('00E5EE', ['turquoise2']),
    ('00C5CD', ['turquoise3']),
    ('00868B', ['turquoise4']),

    ('00FFFF', ['cyan', 'cyan1']),
    ('00EEEE', ['cyan2']),
    ('00CDCD', ['cyan3']),
    ('008B8B', ['cyan4', 'dark cyan', 'DarkCyan']),

    ('E0FFFF', ['light cyan', 'LightCyan', 'LightCyan1']),
    ('D1EEEE', ['LightCyan2']),
    ('B4CDCD', ['LightCyan3']),
    ('7A8B8B', ['LightCyan4']),

    ('BFEFFF', ['LightBlue1']),
    ('B2DFEE', ['LightBlue2']),
    ('ADD8E6', ['light blue', 'LightBlue']),
    ('9AC0CD', ['LightBlue3']),
    ('68838B', ['LightBlue4']),

    ('B0E0E6', ['powder blue', 'PowderBlue']),

    ('B0E2FF', ['LightSkyBlue1']),
    ('A4D3EE', ['LightSkyBlue2']),
    ('8DB6CD', ['LightSkyBlue3']),
    ('87CEFA', ['light sky blue', 'LightSkyBlue']),
    ('607B8B', ['LightSkyBlue4']),

    ('CAE1FF', ['LightSteelBlue1']),
    ('BCD2EE', ['LightSteelBlue2']),
    ('B0C4DE', ['light steel blue', 'LightSteelBlue']),
    ('A2B5CD', ['LightSteelBlue3']),
    ('6E7B8B', ['LightSteelBlue4']),

    ('98F5FF', ['CadetBlue1']),
    ('8EE5EE', ['CadetBlue2']),
    ('7AC5CD', ['CadetBlue3']),
    ('5F9EA0', ['cadet blue', 'CadetBlue']),
    ('53868B', ['CadetBlue4']),

    ('87CEFF', ['SkyBlue1']),
    ('87CEEB', ['sky blue', 'SkyBlue']),
    ('7EC0EE', ['SkyBlue2']),
    ('6CA6CD', ['SkyBlue3']),
    ('4A708B', ['SkyBlue4']),

    ('00BFFF', ['deep sky blue', 'DeepSkyBlue', 'DeepSkyBlue1']),
    ('00B2EE', ['DeepSkyBlue2']),
    ('009ACD', ['DeepSkyBlue3']),
    ('00688B', ['DeepSkyBlue4']),

    ('1E90FF', ['dodger blue', 'DodgerBlue', 'DodgerBlue1']),
    ('1C86EE', ['DodgerBlue2']),
    ('1874CD', ['DodgerBlue3']),
    ('104E8B', ['DodgerBlue4']),

    ('6495ED', ['cornflower blue', 'CornflowerBlue']),

    ('63B8FF', ['SteelBlue1']),
    ('5CACEE', ['SteelBlue2']),
    ('4F94CD', ['SteelBlue3']),
    ('4682B4', ['steel blue', 'SteelBlue']),
    ('36648B', ['SteelBlue4']),

    ('4876FF', ['RoyalBlue1']),
    ('436EEE', ['RoyalBlue2']),
    ('4169E1', ['royal blue', 'RoyalBlue']),
    ('3A5FCD', ['RoyalBlue3']),
    ('27408B', ['RoyalBlue4']),

    ('8470FF', ['light slate blue', 'LightSlateBlue']),

    ('7B68EE', ['medium slate blue', 'MediumSlateBlue']),

    ('6A5ACD', ['slate blue', 'SlateBlue']),
    ('836FFF', ['SlateBlue1']),
    ('7A67EE', ['SlateBlue2']),
    ('6959CD', ['SlateBlue3']),
    ('473C8B', ['SlateBlue4']),

    ('483D8B', ['dark slate blue', 'DarkSlateBlue']),

    ('0000FF', ['blue', 'blue1']),
    ('0000EE', ['blue2']),
    ('0000CD', ['blue3', 'medium blue', 'MediumBlue']),
    ('00008B', ['blue4', 'dark blue', 'DarkBlue']),
    ('000080', ['navy', 'navy blue', 'NavyBlue']),
    ('191970', ['midnight blue', 'MidnightBlue']),

    ('778899', ['light slate gray', 'light slate grey', 'LightSlateGray', 'LightSlateGrey']),

    ('C6E2FF', ['SlateGray1']),
    ('B9D3EE', ['SlateGray2']),
    ('9FB6CD', ['SlateGray3']),
    ('708090', ['slate gray', 'slate grey', 'SlateGray', 'SlateGrey']),
    ('6C7B8B', ['SlateGray4']),

    ('97FFFF', ['DarkSlateGray1']),
    ('8DEEEE', ['DarkSlateGray2']),
    ('79CDCD', ['DarkSlateGray3']),
    ('528B8B', ['DarkSlateGray4']),
    ('2F4F4F', ['dark slate gray', 'dark slate grey', 'DarkSlateGray', 'DarkSlateGrey']),

    ('F5FFFA', ['mint cream', 'MintCream']),

    ('F0FFF0', ['honeydew', 'honeydew1']),
    ('E0EEE0', ['honeydew2']),
    ('C1CDC1', ['honeydew3']),
    ('838B83', ['honeydew4']),

    ('9AFF9A', ['PaleGreen1']),
    ('98FB98', ['pale green', 'PaleGreen']),
    ('90EE90', ['light green', 'LightGreen', 'PaleGreen2']),
    ('7CCD7C', ['PaleGreen3']),
    ('548B54', ['PaleGreen4']),

    ('00FF7F', ['spring green', 'SpringGreen', 'SpringGreen1']),
    ('00EE76', ['SpringGreen2']),
    ('00CD66', ['SpringGreen3']),
    ('008B45', ['SpringGreen4']),

    ('20B2AA', ['light sea green', 'LightSeaGreen']),

    ('00FA9A', ['medium spring green', 'MediumSpringGreen']),

    ('54FF9F', ['SeaGreen1']),
    ('4EEE94', ['SeaGreen2']),
    ('43CD80', ['SeaGreen3']),
    ('2E8B57', ['sea green', 'SeaGreen', 'SeaGreen4']),

    ('3CB371', ['medium sea green', 'MediumSeaGreen']),

    ('C1FFC1', ['DarkSeaGreen1']),
    ('B4EEB4', ['DarkSeaGreen2']),
    ('9BCD9B', ['DarkSeaGreen3']),
    ('8FBC8F', ['dark sea green', 'DarkSeaGreen']),
    ('698B69', ['DarkSeaGreen4']),

    ('C0FF3E', ['OliveDrab1']),
    ('B3EE3A', ['OliveDrab2']),
    ('9ACD32', ['OliveDrab3', 'yellow green', 'YellowGreen']),
    ('6B8E23', ['olive drab', 'OliveDrab']),
    ('698B22', ['OliveDrab4']),

    ('CAFF70', ['DarkOliveGreen1']),
    ('BCEE68', ['DarkOliveGreen2']),
    ('A2CD5A', ['DarkOliveGreen3']),
    ('6E8B3D', ['DarkOliveGreen4']),
    ('556B2F', ['dark olive green', 'DarkOliveGreen']),

    ('ADFF2F', ['green yellow', 'GreenYellow']),

    ('7CFC00', ['lawn green', 'LawnGreen']),

    ('7FFF00', ['chartreuse', 'chartreuse1']),
    ('76EE00', ['chartreuse2']),
    ('66CD00', ['chartreuse3']),
    ('458B00', ['chartreuse4']),

    ('00FF00', ['green', 'green1']),
    ('00EE00', ['green2']),
    ('00CD00', ['green3']),
    ('008B00', ['green4']),

    ('32CD32', ['lime green', 'LimeGreen']),

    ('228B22', ['forest green', 'ForestGreen']),

    ('006400', ['dark green', 'DarkGreen']),

    ('E6E6FA', ['lavender']),

    ('FFE1FF', ['thistle1']),
    ('EED2EE', ['thistle2']),
    ('D8BFD8', ['thistle']),
    ('CDB5CD', ['thistle3']),
    ('8B7B8B', ['thistle4']),

    ('FFBBFF', ['plum1']),
    ('EEAEEE', ['plum2']),
    ('DDA0DD', ['plum']),
    ('CD96CD', ['plum3']),
    ('8B668B', ['plum4']),

    ('EE82EE', ['violet']),

    ('FF83FA', ['orchid1']),
    ('EE7AE9', ['orchid2']),
    ('DA70D6', ['orchid']),
    ('CD69C9', ['orchid3']),
    ('8B4789', ['orchid4']),

    ('E066FF', ['MediumOrchid1']),
    ('D15FEE', ['MediumOrchid2']),
    ('BA55D3', ['medium orchid', 'MediumOrchid']),
    ('B452CD', ['MediumOrchid3']),
    ('7A378B', ['MediumOrchid4']),

    ('BF3EFF', ['DarkOrchid1']),
    ('B23AEE', ['DarkOrchid2']),
    ('9932CC', ['dark orchid', 'DarkOrchid']),
    ('9A32CD', ['DarkOrchid3']),
    ('68228B', ['DarkOrchid4']),

    ('A020F0', ['purple']),
    ('9B30FF', ['purple1']),
    ('912CEE', ['purple2']),
    ('7D26CD', ['purple3']),
    ('551A8B', ['purple4']),

    ('AB82FF', ['MediumPurple1']),
    ('9F79EE', ['MediumPurple2']),
    ('9370DB', ['medium purple', 'MediumPurple']),
    ('8968CD', ['MediumPurple3']),
    ('5D478B', ['MediumPurple4']),

    ('8A2BE2', ['blue violet', 'BlueViolet']),

    ('9400D3', ['dark violet', 'DarkViolet']),

    ('FFE4E1', ['misty rose', 'MistyRose', 'MistyRose1']),
    ('EED5D2', ['MistyRose2']),
    ('CDB7B5', ['MistyRose3']),
    ('8B7D7B', ['MistyRose4']),

    ('FFC1C1', ['RosyBrown1']),
    ('EEB4B4', ['RosyBrown2']),
    ('CD9B9B', ['RosyBrown3']),
    ('BC8F8F', ['rosy brown', 'RosyBrown']),
    ('8B6969', ['RosyBrown4']),

    ('FFB6C1', ['light pink', 'LightPink']),
    ('FFAEB9', ['LightPink1']),
    ('EEA2AD', ['LightPink2']),
    ('CD8C95', ['LightPink3']),
    ('8B5F65', ['LightPink4']),

    ('FFC0CB', ['pink']),
    ('FFB5C5', ['pink1']),
    ('EEA9B8', ['pink2']),
    ('CD919E', ['pink3']),
    ('8B636C', ['pink4']),

    ('FF82AB', ['PaleVioletRed1']),
    ('EE799F', ['PaleVioletRed2']),
    ('DB7093', ['pale violet red', 'PaleVioletRed']),
    ('CD687F', ['PaleVioletRed3']),
    ('8B475D', ['PaleVioletRed4']),

    ('FF3E96', ['VioletRed1']),
    ('EE3A8C', ['VioletRed2']),
    ('D02090', ['violet red', 'VioletRed']),
    ('CD3278', ['VioletRed3']),
    ('8B2252', ['VioletRed4']),

    ('C71585', ['medium violet red', 'MediumVioletRed']),

    ('FF00FF', ['magenta', 'magenta1']),
    ('EE00EE', ['magenta2']),
    ('CD00CD', ['magenta3']),
    ('8B008B', ['dark magenta', 'DarkMagenta', 'magenta4']),

    ('FF1493', ['deep pink', 'DeepPink', 'DeepPink1']),
    ('EE1289', ['DeepPink2']),
    ('CD1076', ['DeepPink3']),
    ('8B0A50', ['DeepPink4']),

    ('FF34B3', ['maroon1']),
    ('EE30A7', ['maroon2']),
    ('CD2990', ['maroon3']),
    ('B03060', ['maroon']),
    ('8B1C62', ['maroon4']),

    ('FF6EB4', ['HotPink1']),
    ('EE6AA7', ['HotPink2']),
    ('FF69B4', ['hot pink', 'HotPink']),
    ('CD6090', ['HotPink3']),
    ('8B3A62', ['HotPink4']),

    ('FF6A6A', ['IndianRed1']),
    ('EE6363', ['IndianRed2']),
    ('CD5C5C', ['indian red', 'IndianRed']),
    ('CD5555', ['IndianRed3']),
    ('8B3A3A', ['IndianRed4']),

    ('F08080', ['light coral', 'LightCoral']),
    ('FF7F50', ['coral']),
    ('FF7256', ['coral1']),
    ('EE6A50', ['coral2']),
    ('CD5B45', ['coral3']),
    ('8B3E2F', ['coral4']),

    ('FFA07A', ['light salmon', 'LightSalmon', 'LightSalmon1']),
    ('EE9572', ['LightSalmon2']),
    ('CD8162', ['LightSalmon3']),
    ('8B5742', ['LightSalmon4']),

    ('FF8C69', ['salmon1']),
    ('FA8072', ['salmon']),
    ('EE8262', ['salmon2']),
    ('CD7054', ['salmon3']),
    ('8B4C39', ['salmon4']),

    ('E9967A', ['dark salmon', 'DarkSalmon']),

    ('FF8247', ['sienna1']),
    ('EE7942', ['sienna2']),
    ('CD6839', ['sienna3']),
    ('A0522D', ['sienna']),
    ('8B4726', ['sienna4']),

    ('FF6347', ['tomato', 'tomato1']),
    ('EE5C42', ['tomato2']),
    ('CD4F39', ['tomato3']),
    ('8B3626', ['tomato4']),

    ('FFA500', ['orange', 'orange1']),
    ('EE9A00', ['orange2']),
    ('CD8500', ['orange3']),
    ('8B5A00', ['orange4']),

    ('FF8C00', ['dark orange', 'DarkOrange']),
    ('FF7F00', ['DarkOrange1']),
    ('EE7600', ['DarkOrange2']),
    ('CD6600', ['DarkOrange3']),
    ('8B4500', ['DarkOrange4']),

    ('FF4500', ['orange red', 'OrangeRed', 'OrangeRed1']),
    ('EE4000', ['OrangeRed2']),
    ('CD3700', ['OrangeRed3']),
    ('8B2500', ['OrangeRed4']),

    ('FF0000', ['red', 'red1']),
    ('EE0000', ['red2']),
    ('CD0000', ['red3']),
    ('8B0000', ['dark red', 'DarkRed', 'red4']),

    ('FF3030', ['firebrick1']),
    ('EE2C2C', ['firebrick2']),
    ('CD2626', ['firebrick3']),
    ('B22222', ['firebrick']),
    ('8B1A1A', ['firebrick4']),

    ('FF4040', ['brown1']),
    ('EE3B3B', ['brown2']),
    ('CD3333', ['brown3']),
    ('A52A2A', ['brown']),
    ('8B2323', ['brown4']),

    ('FF7F24', ['chocolate1']),
    ('EE7621', ['chocolate2']),
    ('D2691E', ['chocolate']),
    ('CD661D', ['chocolate3']),
    ('8B4513', ['chocolate4', 'saddle brown', 'SaddleBrown']),

    ('D2B48C', ['tan']),
    ('FFA54F', ['tan1']),
    ('EE9A49', ['tan2']),
    ('CD853F', ['peru', 'tan3']),
    ('8B5A2B', ['tan4']),

    ('F4A460', ['sandy brown', 'SandyBrown']),

    ('FFFFE0', ['light yellow', 'LightYellow', 'LightYellow1']),
    ('FAFAD2', ['light goldenrod yellow', 'LightGoldenrodYellow']),
    ('EEEED1', ['LightYellow2']),
    ('CDCDB4', ['LightYellow3']),
    ('8B8B7A', ['LightYellow4']),

    ('FFFACD', ['lemon chiffon', 'LemonChiffon', 'LemonChiffon1']),
    ('EEE9BF', ['LemonChiffon2']),
    ('CDC9A5', ['LemonChiffon3']),
    ('8B8970', ['LemonChiffon4']),

    ('EEE8AA', ['pale goldenrod', 'PaleGoldenrod']),

    ('FFEC8B', ['LightGoldenrod1']),
    ('EEDD82', ['light goldenrod', 'LightGoldenrod']),
    ('EEDC82', ['LightGoldenrod2']),
    ('CDBE70', ['LightGoldenrod3']),
    ('8B814C', ['LightGoldenrod4']),

    ('FFF68F', ['khaki1']),
    ('F0E68C', ['khaki']),
    ('EEE685', ['khaki2']),
    ('CDC673', ['khaki3']),
    ('BDB76B', ['dark khaki', 'DarkKhaki']),
    ('8B864E', ['khaki4']),

    ('FFD700', ['gold', 'gold1']),
    ('EEC900', ['gold2']),
    ('CDAD00', ['gold3']),
    ('8B7500', ['gold4']),

    ('FFB90F', ['DarkGoldenrod1']),
    ('EEAD0E', ['DarkGoldenrod2']),
    ('CD950C', ['DarkGoldenrod3']),
    ('B8860B', ['dark goldenrod', 'DarkGoldenrod']),
    ('8B6508', ['DarkGoldenrod4']),

    ('FFC125', ['goldenrod1']),
    ('EEB422', ['goldenrod2']),
    ('DAA520', ['goldenrod']),
    ('CD9B1D', ['goldenrod3']),
    ('8B6914', ['goldenrod4']),

    ('FFFF00', ['yellow', 'yellow1']),
    ('EEEE00', ['yellow2']),
    ('CDCD00', ['yellow3']),
    ('8B8B00', ['yellow4']),
])
