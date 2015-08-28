#! /usr/bin/python
from armoryengine.ALL import *
from extras.breakDownWallet import *

#print wlt.getNextUnusedAddress().getAddrStr()
#give function parameters
createNewWallet(wlt, rootEntry, newWalletFilePath, withEncrypt, kdfParam=None)