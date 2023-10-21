# (C) 2019-2020 lifegpc
# This file is part of bili.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from getopt import getopt, GetoptError
from re import search
from biliTime import checktime
from file import filterd
from lang import lan, getlan, getdict
from JSONParser import loadset
import sys
from urllib.parse import parse_qs, urlsplit, unquote_plus


onewline = '\n'
nnewline = '\n    '


def ph():
    h = f'''{la['O1']}
    start.py -h/-?/--help   {la['O2']}
    start.py [-i <input>] [-d <method>] [-p <number>] [-m <boolean>/--ym/--nm] [--ac <boolean>/--yac/--nac] [--dm <boolean>/--ydm/--ndm] [--ad <boolean>/--yad/--nad] [-r <boolean>/--yr/--nr] [-y/-n] [--yf/--nf] [--mc avc/hev] [--ar/--nar] [--ax <number>] [--as <number>] [--ak <number>] [--ab/--nab] [--fa none/prealloc/trunc/falloc] [--sv <boolean>/--ysv/--nsv] [--ma <boolean>/--yma/--nma] [--ms <speed>] [--da <boolean>/--yda/--nda] [--httpproxy <URI>] [--httpsproxy <URI>] [--jt <number>|a|b] [--jts <date>] [-F] [-v <id>] [-a <id>] [-o <dir>] [--af/--naf] [--afp <number>] [-s] [--slt/--nslt] [--te/--nte] [--bd/--nbd] [--cad/--ncad] [--lrh/--nlrh] [--ahttpproxy <PROXY>] [--ahttpsproxy <PROXY>] [--lan <LANGUAGECODE>] [--bp/--nbp] [--in/--nin] [--mt/--nmt] [--vi <URL_index>] [--uc/--nuc] [--ass/--nass] [--dmp/--ndmp] [--vf <format>] [--lmd <time>] [--ynal/--nnal] [--log/--nlog] [--yauf/--nauf] [--ydwa/--ndwa] [--yol/--nol] [--ltid] [--ycc/--ncc] [--nfo/--nnfo] [-V <format id>[<coding format>]] [--anopro] [--mxd <number>] [--imn/--nimn] [--nlt <second>] [--nsp <speed>] [--fnl <length>] [--lp/--nlp]
    start.py show c/w   {la['O3']}
    -i <input>   {la['O4']}
    -d <method>   {la['O5']}
    {la['O6']}
    -p <number>    {la['O7']}
    -m <boolean>    {la['O8']}
    --ym    {la['AL'].replace('<value>','-m true')}
    --nm    {la['AL'].replace('<value>','-m false')}
    --ac <boolean>  {la['O9']}
    --yac   {la['AL'].replace('<value>','--ac true')}
    --nac   {la['AL'].replace('<value>','--ac false')}
    --dm <boolean>  {la['O10']}
    --ydm   {la['AL'].replace('<value>','--dm true')}
    --ndm   {la['AL'].replace('<value>','--dm false')}
    --ad <boolean>  {la['O11']}
    --yad   {la['AL'].replace('<value>','--ad true')}
    --nad   {la['AL'].replace('<value>','--ad false')}
    -r <boolean>    {la['O12']}
    --yr    {la['AL'].replace('<value>','-r true')}
    --nr    {la['AL'].replace('<value>','-r false')}
    -y  {la['O13']}
    -n  {la['O14']}
    --yf    {la['O15']}
    --nf    {la['O16']}
    --mc avc/hev    {la['O17']}
    --ar    {la['O18']}
    --nar   {la['O19']}
    --ax <number>   {la['O20'].replace('<value>','1-16')}
    --as <number>   {la['O21'].replace('<value>','1-*')}
    --ak <number>   {la['O22'].replace('<value1>','M').replace('<value2>','1-1024')}
    --ab    {la['O23']}
    --nab   {la['O24']}
    --fa none/prealloc/trunc/falloc {la['O25']}
    --sv <boolean>  {la['O26']}
    --ysv   {la['AL'].replace('<value>','--sv true')}
    --nsv   {la['AL'].replace('<value>','--sv false')}
    --ma <boolean>  {la['O27']}
    --yma   {la['AL'].replace('<value>','--ma true')}
    --nma   {la['AL'].replace('<value>','--ma false')}
    --ms <speed>    {la['O28']}
    --da <boolean>  {la['O29']}
    --yda   {la['AL'].replace('<value>','--da true')}
    --nda   {la['AL'].replace('<value>','--da false')}
    --httpproxy <URI>   {la['O30']}{la['O31']}
    --httpsproxy <URI>  {la['O32']}{la['O31']}
    --jt <number>|a|b   {la['O33'].replace('<value>','1-365')}
    --jts <date>    {la['O34']}
    -F      {la['O35']}
    -v <id>     {la['O36']}
    -a <id>     {la['O37']}
    -o <dir>    {la['O38']}
    --af    {la['O39']}
    --naf   {la['O40']}
    --afp <number>  {la['O41']}
    -s      {la['O42']}
    --slt   {la['O43']}
    --nslt  {la['O44']}
    --te    {la['O45']}
    --nte   {la['O46']}
    --bd    {la['O47']}
    --nbd   {la['O48']}
    --cad   {la['O49']}
    --ncad  {la['O50']}
    --lrh   {la['O51']}
    --nlrh  {la['O52']}
    --ahttpproxy <PROXY>    {la['O53']}
    --ahttpsproxy <PROXY>   {la['O54']}
    --lan <LANGUAGECODE>    {la['O55']}
    --bp    {la['O60']}
    --nbp   {la['O61']}
    --in    {la['O62']}
    --nin   {la['O63']}
    --mt    {la['O64']}
    --nmt   {la['O65']}
    --vi <URL_index>    {la['O66']}
    --uc    {la['O67']}
    --nuc   {la['O68']}
    --ass   {la['O69']}
    --nass  {la['O70']}
    --dmp   {la['O71']}
    --ndmp  {la['O72']}
    --vf <format>   {la['O77'].replace('<value>', 'mkv, mp4')}
    --lmd <time>    {la['O78'].replace('<value>', '0-*').replace('<value2>', 'ms')}
    --ynal  {la['O79']}
    --nnal  {la['O80']}
    --log   {la['O81']}
    --nlog  {la['O82']}
    --yauf  {la['O83']}
    --nauf  {la['O84']}
    --ydwa  {la['O85']}
    --ndwa  {la['O86']}
    --yol   {la['O87']}
    --nol   {la['O88']}
    --ltid  {la['O89']}
    -c      {la['O90']}
    -b [bili scheme URI]    {la['O91']}
    --ncc   {la['O92']}
    --ycc   {la['O93']}
    --nfo   {la['O94']}
    --nnfo  {la['O95']}
    -V <format id>[<coding format>] {la['O96']}
    {la['O97'].replace(onewline, nnewline)}
    {la['O101'].replace(onewline, nnewline)}
    {la['O98'].replace('<codecs>', 'avc, hev')}
    {la['O99']}
    --anopro    {la['O100']}
    --mxd <number>  {la['O102']}
    --imn   {la['O103']}
    --nimn  {la['O104']}
    --nlt <second>  {la['O105']}
    --nsp <speed>   {la['O107'].replace(onewline, nnewline)}
    --fnl <length>  {la['O108']}
    --lp    {la['O109']}
    --nlp   {la['O110']}
    {la['O56']}
    {la['O57']}
    {la['O58']}
    {la['O59']}'''
    print(h)


def gopt(args, d: bool = False):
    re = getopt(args, 'h?i:d:p:m:r:ynFv:a:o:scb:V:', ['help', 'ac=', 'dm=', 'ad=', 'yf', 'nf', 'mc=', 'ar', 'nar', 'ax=', 'as=', 'ak=', 'ab', 'nab', 'fa=', 'sv=', 'ma=', 'ms=', 'da=', 'httpproxy=', 'httpsproxy=', 'jt=', 'jts=', 'af', 'naf', 'afp=', 'slt', 'nslt', 'te', 'nte', 'bd', 'nbd', 'cad', 'ncad', 'lrh', 'nlrh', 'ym', 'nm', 'yac', 'nac', 'ydm', 'ndm', 'yad', 'nad', 'yr', 'nr', 'ysv', 'nsv', 'yma', 'nma', 'yda', 'nda', 'ahttpproxy=', 'ahttpsproxy=', 'lan=', 'bp', 'nbp', 'in', 'nin', 'mt', 'nmt', 'vi=', 'uc', 'nuc', 'ass', 'nass', 'dmp', 'ndmp', 'vf=', 'lmd=', 'ynal', 'nnal', 'log', 'nlog', 'yauf', 'nauf', 'ydwa', 'ndwa', 'yol', 'nol', 'ltid', 'ncc', 'ycc', 'nfo', 'nnfo', 'anopro', 'mxd=', 'imn', 'nimn', 'nlt=', 'nsp=', 'fnl=', 'lp', 'nlp'])
    if d:
        print(re)
    rr = re[0]
    r = {}
    h = False
    for i in rr:
        if i[0] == '-h' or i[0] == '-?' or i[0] == '--help':
            h = True
        if i[0] == '-i' and 'i' not in r:
            r['i'] = i[1]
        if i[0] == '-d' and 'd' not in r and i[1].isnumeric() and int(i[1]) > 0 and int(i[1]) < 9:
            r['d'] = int(i[1])
        if i[0] == '-p' and 'p' not in r:
            r['p'] = i[1]
        if i[0] == '-m' and 'm' not in r:
            if i[1].lower() == 'true':
                r['m'] = True
            elif i[1].lower() == 'false':
                r['m'] = False
        if i[0] == '--ym' and 'm' not in r:
            r['m'] = True
        if i[0] == '--nm' and 'm' not in r:
            r['m'] = False
        if i[0] == '--ac' and 'ac' not in r:
            if i[1].lower() == 'true':
                r['ac'] = True
            elif i[1].lower() == 'false':
                r['ac'] = False
        if i[0] == '--yac' and 'ac' not in r:
            r['ac'] = True
        if i[0] == '--nac' and 'ac' not in r:
            r['ac'] = False
        if i[0] == '--dm' and 'dm' not in r:
            if i[1].lower() == 'true':
                r['dm'] = True
            elif i[1].lower() == 'false':
                r['dm'] = False
        if i[0] == '--ydm' and 'dm' not in r:
            r['dm'] = True
        if i[0] == '--ndm' and 'dm' not in r:
            r['dm'] = False
        if i[0] == '--ad' and 'ad' not in r:
            if i[1].lower() == 'true':
                r['ad'] = True
            elif i[1].lower() == 'false':
                r['ad'] = False
        if i[0] == '--yad' and 'ad' not in r:
            r['ad'] = True
        if i[0] == '--nad' and 'ad' not in r:
            r['ad'] = False
        if i[0] == '-r' and 'r' not in r:
            if i[1].lower() == 'true':
                r['r'] = True
            elif i[1].lower() == 'false':
                r['r'] = False
        if i[0] == '--yr' and 'r' not in r:
            r['r'] = True
        if i[0] == '--nr' and 'r' not in r:
            r['r'] = False
        if i[0] == '-y' and 'y' not in r:
            r['y'] = True
        if i[0] == '-n' and 'y' not in r:
            r['y'] = False
        if i[0] == '--yf' and 'yf' not in r:
            r['yf'] = True
        if i[0] == '--nf' and 'yf' not in r:
            r['yf'] = False
        if i[0] == '--mc' and 'mc' not in r:
            if i[1].lower() == 'avc':
                r['mc'] = True
            elif i[1].lower() == 'hev':
                r['mc'] = False
        if i[0] == '--ar' and 'ar' not in r:
            r['ar'] = True
        if i[0] == '--nar' and 'ar' not in r:
            r['ar'] = False
        if i[0] == '--ax' and 'ax' not in r:
            if i[1].isnumeric():
                i2 = int(i[1])
                if i2 < 17 and i2 > 0:
                    r['ax'] = i2
        if i[0] == '--as' and 'as' not in r:
            if i[1].isnumeric():
                i2 = int(i[1])
                if i2 > 0:
                    r['as'] = i2
        if i[0] == '--ak' and 'ak' not in r:
            if i[1].isnumeric():
                i2 = int(i[1])
                if i2 > 0 and i2 < 1025:
                    r['ak'] = i2
        if i[0] == '--ab' and 'ab' not in r:
            r['ab'] = True
        if i[0] == '--nab' and 'ab' not in r:
            r['ab'] = False
        if i[0] == '--fa' and 'fa' not in r:
            if i[1].lower() == 'none' or i[1].lower() == 'prealloc' or i[1].lower() == 'trunc' or i[1].lower() == 'falloc':
                r['fa'] = i[1].lower()
        if i[0] == '--sv' and 'sv' not in r:
            if i[1].lower() == 'true':
                r['sv'] = True
            elif i[1].lower() == 'false':
                r['sv'] = False
        if i[0] == '--ysv' and 'sv' not in r:
            r['sv'] = True
        if i[0] == '--nsv' and 'sv' not in r:
            r['sv'] = False
        if i[0] == '--ma' and 'ma' not in r:
            if i[1].lower() == 'true':
                r['ma'] = True
            elif i[1].lower() == 'false':
                r['ma'] = False
        if i[0] == '--yma' and 'ma' not in r:
            r['ma'] = True
        if i[0] == '--nma' and 'ma' not in r:
            r['ma'] = False
        if i[0] == '--ms' and 'ms' not in r:
            t = search("^[0-9]+[MK]?$", i[1])
            if t is not None:
                r['ms'] = i[1]
        if i[0] == '--da' and 'da' not in r:
            if i[1].lower() == 'true':
                r['da'] = True
            elif i[1].lower() == 'false':
                r['da'] = False
        if i[0] == '--yda' and 'da' not in r:
            r['da'] = True
        if i[0] == '--nda' and 'da' not in r:
            r['da'] = False
        if i[0] == '--httpproxy' and 'httpproxy' not in r:
            r['httpproxy'] = i[1]
        if i[0] == '--httpsproxy' and 'httpsproxy' not in r:
            r['httpsproxy'] = i[1]
        if i[0] == "--jt" and 'jt' not in r:
            if i[1].lower() == 'a' or i[1].lower() == 'b' or i[1].isnumeric():
                r['jt'] = i[1].lower()
        if i[0] == '--jts' and 'jts' not in r:
            if checktime(i[1]):
                r['jts'] = i[1]
        if i[0] == '-F' and 'F' not in r:
            r['F'] = True
        if i[0] == '-v' and 'v' not in r:
            if i[1].isnumeric():
                if int(i[1]) > 0:
                    r['v'] = i[1]
        if i[0] == '-a' and 'a' not in r:
            if i[1].isnumeric():
                if int(i[1]) > 0:
                    r['a'] = i[1]
        if i[0] == '-o' and 'o' not in r:
            r['o'] = filterd(i[1])
        if i[0] == '--af' and 'af' not in r:
            r['af'] = False
        if i[0] == '--naf' and 'af' not in r:
            r['af'] = True
        if i[0] == '--afp' and 'afp' not in r:
            r['afp'] = i[1]
        if i[0] == '-s' and 's' not in r:
            r['s'] = True
        if i[0] == '--slt' and 'slt' not in r:
            r['slt'] = True
        if i[0] == '--nslt' and 'slt' not in r:
            r['slt'] = False
        if i[0] == '--te' and 'te' not in r:
            r['te'] = True
        if i[0] == '--nte' and 'te' not in r:
            r['te'] = False
        if i[0] == '--bd' and 'bd' not in r:
            r['bd'] = True
        if i[0] == '--nbd' and 'bd' not in r:
            r['bd'] = False
        if i[0] == '--cad' and 'cad' not in r:
            r['cad'] = True
        if i[0] == '--ncad' and 'cad' not in r:
            r['cad'] = False
        if i[0] == '--lrh' and 'lrh' not in r:
            r['lrh'] = True
        if i[0] == '--nlrh' and 'lrh' not in r:
            r['lrh'] = False
        if i[0] == '--ahttpproxy' and 'ahttpproxy' not in r:
            r['ahttpproxy'] = i[1]
        if i[0] == '--ahttpsproxy' and 'ahttpsproxy' not in r:
            r['ahttpsproxy'] = i[1]
        if i[0] == '--lan' and 'lan' not in r and (i[1] == 'null' or i[1] in lan):
            r['lan'] = i[1]
        if i[0] == '--bp' and 'bp' not in r:
            r['bp'] = True
        if i[0] == '--nbp' and 'bp' not in r:
            r['bp'] = False
        if i[0] == '--in' and 'in' not in r:
            r['in'] = True
        if i[0] == '--nin' and 'in' not in r:
            r['in'] = False
        if i[0] == '--mt' and 'mt' not in r:
            r['mt'] = True
        if i[0] == '--nmt' and 'mt' not in r:
            r['mt'] = False
        if i[0] == '--vi' and 'vi' not in r:
            if i[1].isnumeric():
                r['vi'] = int(i[1])
        if i[0] == '--uc' and 'uc' not in r:
            r['uc'] = True
        if i[0] == '--nuc' and 'uc' not in r:
            r['uc'] = False
        if i[0] == '--ass' and 'ass' not in r:
            r['ass'] = True
        if i[0] == '--nass' and 'ass' not in r:
            r['ass'] = False
        if i[0] == '--dmp' and 'dmp' not in r:
            r['dmp'] = True
        if i[0] == '--ndmp' and 'dmp' not in r:
            r['dmp'] = False
        if i[0] == '--vf' and 'vf' not in r and i[1] in ['mkv', 'mp4']:
            r['vf'] = i[1]
        if i[0] == '--lmd' and 'lmd' not in r and i[1].isnumeric():
            if int(i[1]) >= 0:
                r['lmd'] = int(i[1])
        if i[0] == '--ynal' and 'nal' not in r:
            r['nal'] = True
        if i[0] == '--nnal' and 'nal' not in r:
            r['nal'] = False
        if i[0] == '--log' and 'log' not in r:
            r['log'] = True
        if i[0] == '--nlog' and 'log' not in r:
            r['log'] = False
        if i[0] == '--yauf' and 'auf' not in r:
            r['auf'] = True
        if i[0] == '--nauf' and 'auf' not in r:
            r['auf'] = False
        if i[0] == '--ydwa' and 'dwa' not in r:
            r['dwa'] = True
        if i[0] == '--ndwa' and 'dwa' not in r:
            r['dwa'] = False
        if i[0] == '--yol' and 'ol' not in r:
            r['ol'] = True
        if i[0] == '--nol' and 'ol' not in r:
            r['ol'] = False
        if i[0] == '--ltid':
            r['ltid'] = True
        if i[0] == '--ycc' and 'cc' not in r:
            r['cc'] = True
        if i[0] == '--ncc' and 'cc' not in r:
            r['cc'] = False
        if i[0] == '--nfo' and 'nfo' not in r:
            r['nfo'] = True
        if i[0] == '--nnfo' and 'nfo' not in r:
            r['nfo'] = False
        if i[0] == '-V' and 'V' not in r:
            rs = search(r'^([0-9]+)(avc|hev)?$', i[1])
            if rs is not None:
                vid = int(rs.groups()[0])
                if vid in [16, 32, 64, 74, 80, 112, 116, 120, 125]:
                    r['V'] = {'id': vid, 'codec': rs.groups()[1]}
                elif vid in range(1, 12):
                    r['V'] = {'id': vid, 'codec': rs.groups()[1]}
        if i[0] == '--anopro' and 'anopro' not in r:
            r['anopro'] = True
        if i[0] == '--mxd' and 'mxd' not in r:
            if i[1].isnumeric():
                if int(i[1]) >= 0:
                    r['mxd'] = int(i[1])
        if i[0] == '--imn' and 'imn' not in r:
            r['imn'] = True
        if i[0] == '--nimn' and 'imn' not in r:
            r['imn'] = False
        if i[0] == '--nlt' and search(r'^\+?\d+(\.\d+)?$', i[1]) and 'nlt' not in r:
            r['nlt'] = float(i[1])
        if i[0] == '--nsp' and search(r'^\+?\d+(\.\d+)?$', i[1]) and 'nsp' not in r:
            t = float(i[1])
            t = min(max(round(t * 4), 1), 8) / 4
            if t in [1, 2]:
                t = round(t)
            r['nsp'] = t
        if i[0] == '--fnl' and i[1].isnumeric() and 'fnl' not in r:
            r['fnl'] = int(i[1])
        if i[0] == '--lp' and 'lp' not in r:
            r['lp'] = True
        if i[0] == '--nlp' and 'lp' not in r:
            r['lp'] = False
        if i[0] == '-b':
            ree = urlsplit(i[1])
            if ree.scheme == "bili":
                pat = f"{ree.netloc}{ree.path}"
                if ree.path == "/" and i[1].find("://") > -1:
                    pat = ree.netloc
                argv = ['-i', unquote_plus(pat)]
                getp = parse_qs(ree.query, True)
                for key in getp.keys():
                    if key == 'b':
                        continue
                    val = getp[key]
                    if len(key) == 1:
                        key = f"-{key}"
                    elif len(key) > 1:
                        key = f"--{key}"
                    else:
                        continue
                    if len(val) == 1 and val[0] == "":
                        argv.append(key)
                    else:
                        for v in val:
                            argv.append(key)
                            argv.append(v)
                if d:
                    print(argv)
                try:
                    return gopt(argv)
                except GetoptError:
                    t = i[1][5:]
                    if t.startswith('//'):
                        t = t[2:]
                    argv = ['-i', t]
                    if d:
                        print(argv)
                    return gopt(argv)
    if h:
        global la
        la = getdict('command', getlan(se, r))
        ph()
        sys.exit(0)
    for i in re[1]:
        if i.lower() == "show":
            r['SHOW'] = True
    return r


la = None
se = loadset()
if se == -1 or se == -2:
    se = {}
la = getdict('command', getlan(se, {}))
if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) == 1:
        print('该文件仅供测试命令行输入使用，请运行start.py')
    else:
        print(gopt(sys.argv[1:], True))
