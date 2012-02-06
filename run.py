import sys
import os

from ciphers import CaesarCipher
from crackers import CaesarCracker


sys.path.insert(0, os.path.split(os.path.abspath(__file__))[0])

encrypted = """WUHDWV IRU JHDU KHDGV
EB DOLFH UDZVWKRUQ
SXEOLVKHG: VHSWHPEHU 19, 2010

QHZ BRUN - RQH FDU VXUYLYHG D VSHFWDFXODU FUDVK LQ ZKLFK LWV GULYHU GLHG, RQOB WR EH GHVWURBHG EB ILUH ZKHQ WKH JDVROLQH WDQN FDS ZDV DFFLGHQWDOOB OHIW RII. DQRWKHU HQMRBHG D EULHI EXUVW RI JORUB ZKHQ LW IHUULHG K.J. ZHOOV DURXQG PDQKDWWDQ EHIRUH LW FUDVKHG WRR. LW ZDV OHIW WR URW LQ DULCRQD XQWLO EHLQJ UHVFXHG, DQG UHVWRUHG EB ORFDO HQJLQHHULQJ VWXGHQWV. D WKLUG FDU ZDV GULYHQ DURXQG WKH XQLWHG VWDWHV WR SURPRWH WKH DOOLHG FDXVH GXULQJ ZRUOG ZDU LL, WKHQ VROG IRU VFUDS EB D NDQVDV MXQNBDUG.

WKRVH DFFLGHQW-SURQH YHKLFOHV ZHUH WKH WKUHH GBPDALRQ FDUV, ZKLFK ZHUH GHVLJQHG DQG PDQXIDFWXUHG LQ EULGJHSRUW, FRQQHFWLFXW, LQ WKH 1930V EB U. EXFNPLQVWHU IXOOHU, RU "EXFNB" DV KH SUHIHUUHG WR EH FDOOHG.

ELOOLQJ KLPVHOI DV "D PDYHULFN WKLQNHU, D JHQWOH UHYROXWLRQLVW, D ORYHDEOH JHQLXV, DQ DQWL-DFDGHPLFLDQ, GRFWRU RI VFLHQFH, GRFWRU RI DUWV, GRFWRU RI GHVLJQ," DPRQJ PDQB RWKHU UROHV, KH DLPHG WR EXLOG WKH PRVW IXHO-HIILFLHQW FDU RQ WKH URDG. DV BRX ZRXOG HASHFW RI D ORYHDEOH JHQLXV, PDQB RI IXOOHU'V FODLPV IRU KLV GHVLJQV ZHUH ZLOGOB HADJJHUDWHG, EXW KH VXFFHHGHG LQ DFKLHYLQJ KLV REMHFWLYH ZLWK WKLV RQH.

WKUHH-TXDUWHUV RI D FHQWXUB DIWHU WKH ODVW RI WKH RULJLQDO PRGHOV, FDU #3, UROOHG RII WKH SURGXFWLRQ OLQH, D QHZ GBPDALRQ FDU KDV EHHQ FUHDWHG, FDU #4. EDVHG RQ WKH GUDZLQJV RI FDU #3 DQG SDLQVWDNLQJ DQDOBVLV RI FDU #2, LW ZDV EXLOW LQ WKH HQJOLVK FRXQWUBVLGH LQ WKH HDVW VXVVHA ZRUNVKRSV RI FURVWKZDLWH & JDUGLQHU, ZKLFK VSHFLDOLCHV LQ UHVWRULQJ 1930V UDFLQJ FDUV. WKH QHZ FDU ZDV FRPPLVVLRQHG EB QRUPDQ IRVWHU, WKH EULWLVK DUFKLWHFW RI VXFK PRGHUQ ODQGPDUNV DV EHLMLQJ DLUSRUW, WKH QHZ UHLFKVWDJ LQ EHUOLQ DQG WKH "JKHUNLQ" LQ ORQGRQ. D SDVVLRQDWH FDU FROOHFWRU, KH XQGHUWRRN WKH SURMHFW DV D ODERU RI ORYH DQG DQ KRPDJH WR IXOOHU, ZKR KH PHW LQ 1971 DQG FROODERUDWHG ZLWK XQWLO IXOOHU'V GHDWK LQ 1983.

999"""

plain = """TREATS FOR GEAR HEADS
BY ALICE RAWSTHORN
PUBLISHED: SEPTEMBER 19, 2010

NEW YORK - ONE CAR SURVIVED A SPECTACULAR CRASH IN WHICH ITS DRIVER DIED, ONLY TO BE DESTROYED BY FIRE WHEN THE GASOLINE TANK CAP WAS ACCIDENTALLY LEFT OFF. ANOTHER ENJOYED A BRIEF BURST OF GLORY WHEN IT FERRIED H.G. WELLS AROUND MANHATTAN BEFORE IT CRASHED TOO. IT WAS LEFT TO ROT IN ARIZONA UNTIL BEING RESCUED, AND RESTORED BY LOCAL ENGINEERING STUDENTS. A THIRD CAR WAS DRIVEN AROUND THE UNITED STATES TO PROMOTE THE ALLIED CAUSE DURING WORLD WAR II, THEN SOLD FOR SCRAP BY A KANSAS JUNKYARD.

THOSE ACCIDENT-PRONE VEHICLES WERE THE THREE DYMAXION CARS, WHICH WERE DESIGNED AND MANUFACTURED IN BRIDGEPORT, CONNECTICUT, IN THE 1930S BY R. BUCKMINSTER FULLER, OR "BUCKY" AS HE PREFERRED TO BE CALLED.

BILLING HIMSELF AS "A MAVERICK THINKER, A GENTLE REVOLUTIONIST, A LOVEABLE GENIUS, AN ANTI-ACADEMICIAN, DOCTOR OF SCIENCE, DOCTOR OF ARTS, DOCTOR OF DESIGN," AMONG MANY OTHER ROLES, HE AIMED TO BUILD THE MOST FUEL-EFFICIENT CAR ON THE ROAD. AS YOU WOULD EXPECT OF A LOVEABLE GENIUS, MANY OF FULLER'S CLAIMS FOR HIS DESIGNS WERE WILDLY EXAGGERATED, BUT HE SUCCEEDED IN ACHIEVING HIS OBJECTIVE WITH THIS ONE.

THREE-QUARTERS OF A CENTURY AFTER THE LAST OF THE ORIGINAL MODELS, CAR #3, ROLLED OFF THE PRODUCTION LINE, A NEW DYMAXION CAR HAS BEEN CREATED, CAR #4. BASED ON THE DRAWINGS OF CAR #3 AND PAINSTAKING ANALYSIS OF CAR #2, IT WAS BUILT IN THE ENGLISH COUNTRYSIDE IN THE EAST SUSSEX WORKSHOPS OF CROSTHWAITE & GARDINER, WHICH SPECIALIZES IN RESTORING 1930S RACING CARS. THE NEW CAR WAS COMMISSIONED BY NORMAN FOSTER, THE BRITISH ARCHITECT OF SUCH MODERN LANDMARKS AS BEIJING AIRPORT, THE NEW REICHSTAG IN BERLIN AND THE "GHERKIN" IN LONDON. A PASSIONATE CAR COLLECTOR, HE UNDERTOOK THE PROJECT AS A LABOR OF LOVE AND AN HOMAGE TO FULLER, WHO HE MET IN 1971 AND COLLABORATED WITH UNTIL FULLER'S DEATH IN 1983.

999"""


plain = """De Griekse regering gaat nog dit jaar 15.000 ambtenaren ontslaan. Het ontslag was een van de eisen van de EU, de ECB en het IMF, voor het toekennen van een steunpakket van 130 miljard euro.

De Griekse regering is nog steeds in onderhandeling over dat pakket. Tot nu toe was het niet mogelijk om ambtenaren te ontslaan, omdat de Griekse wet dat niet toelaat. Griekenland heeft nu nog zo'n 750.000 ambtenaren. Eind 2015 moeten dat er 150.000 minder zijn.

Vakbonden hebben voor dinsdag een 24-uurs-staking aangekondigd uit protest
tegen de bezuinigingsmaatregelen van de Griekse regering."""
encrypted = CaesarCipher(shift=5).encrypt(plain)

cracker = CaesarCracker(encrypted)
result = cracker.run()
assert(result == plain.upper())

msg = 'Decryption succeeded. Shift appears to be %d' % cracker.cipher.shift
print '=' * len(msg)
print msg
print '=' * len(msg)
print result
