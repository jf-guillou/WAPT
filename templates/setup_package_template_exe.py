# -*- coding: utf-8 -*-
from __future__ import print_function
from setuphelpers import *

uninstallkey = []

def install():
    print('installing %(packagename)s')
    install_exe_if_needed("%(installer)s",'%(silentflags)s',key='%(uninstallkey)s',min_version='%(version)s')
