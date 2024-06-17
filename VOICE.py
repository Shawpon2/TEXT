import os 
import requests
from gtts import gTTS
import os
from concurrent.futures import ThreadPoolExecutor as bff 
import sys
WHITE = '\033[1;97m'
RED = '\033[1;91m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
import os
import json
import re
import time
import _thread
import base64
import requests
from datetime import datetime
from rich.markdown import Markdown as mark
from rich.panel import Panel
from rich import print as Luciver_Xploit_Emang_Ganteng
from rich import print as rprint
from rich import print as Hujatanmu_Adalah_Kebodohanmu
from rich.progress import track
from rich.text import Text as tekz
from rich.console import Console
from rich.text import Text
from rich.columns import Columns
from rich.panel import Panel as nel
from rich.panel import Panel as panel
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as par
from rich.console import Group as gp
from bs4 import BeautifulSoup as parser
from rich.columns import Columns as col
from rich.console import Console as sol
from bs4 import BeautifulSoup as beautifulsoup
from rich.markdown import Markdown as mark
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as LuciverXD 
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
RED = '\033[1;91m'
###----------[ ANSII COLOR STYLE ]---------- ###
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
N = '\x1b[0m'	# WARNA MATI
PT = '\x1b[1;97m' # PUTIH TEBAL
MT = '\x1b[1;91m' # MERAH TEBAL
HT = '\x1b[1;92m' # HIJAU TEBAL
KT = '\x1b[1;93m' # KUNING TEBAL
BT = '\x1b[1;94m' # BIRU TEBAL
UT = '\x1b[1;95m' # UNGU TEBAL
OT = '\x1b[1;96m' # BIRU MUDA TEBAL
O = '\x1b[1;96m' # BIRU MUDA,,
x = '\x1b[0m'    # Def
send=0 
def Kiss(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
def lod(message):
    
    for i in track(range(100), description=f"[red][bold] {message}"):
        time.sleep(0.03)
user=str(input(f"\n\n{H}USERNAME {RED}=>{H} "))
pas=str(input(f"{H}PASSWORD {RED}=>{H} "))
rp= 'SHAWPON'
tx = 'SP-BD'
if 'SHAWPON'==user and 'SP-BD'==pas:
        Kiss(f"\n\n\t\t      LOGIN SUCCESSFUL  ")
   
#############
Y = '\033[1;33m'
RED = '\033[1;91m'
R = '\033[1;31m'
B = '\033[2;34m'
G = '\033[2;32m'
x = '\x1b[0m'
#############
#> COLOR RICH
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
ggg = '/sdcard'
os.system('xdg-open https://www.github.com/shawpon2')
def Logo_Bangsat():
	Luciver_Xploit_Emang_Ganteng(panel(f"""[bold red]
╦  ╦╔═╗╦╔═╗╔═╗  ╔╗ ╔═╗╔╦╗
╚╗╔╝║ ║║║  ║╣───╠╩╗║ ║ ║ 
 ╚╝ ╚═╝╩╚═╝╚═╝  ╚═╝╚═╝ ╩ 
[bold cyan]TEXT TO VOICE CONVERTER MADE BY SP-BD [bold yellow]   """,width=50,padding=(0,4),title=f"[bold yellow]亗 [bold green]BANGlADESHI TEAM [bold yellow]亗",style=f"bold green"))
Logo_Bangsat()
mytext=input(f'\n\n{H}ENTER YOUR TEXT :')
lod('Extract Voice...')
language='bn'
myobj=gTTS(text=mytext,
           lang=language,slow=False)
File = input(f'{H}YOUR FILE SAVED IN {RED}: ')
myobj.save(f'{File}')
os.system(f'mv {File} {ggg}')
Kiss(f'{H}VOICE SAVED SUCCESS')
Kiss(f'{H}VOICE SAVED IN /sdcard/{File}')
Fuck = input(f'{H}[Y] FOR BACK MENU')
if Fuck in ["y","Y","1"]:
	os.system('python VOICE.py')