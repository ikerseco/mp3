import os
from sys import argv




class grupoa(object):
 def __init__(self, titleg):
  self.titleg = titleg
 
 def grupoa_sortu(self):
  os.mkdir(self.titleg)
  
class kanta(grupoa):
 def __init__(self, titlek):
  self.titlek = titlek 
 def izena_ezarri(self):
  carpetak = os.listdir("./music")
  luzehera = len(carpetak)
  print("grupoak:")
  for x in range(luzehera):
   print(x,".",carpetak[x])
  taldea = input("musikaren taldea zenbakia:")
  izena = input("izena jarri:")
  taldeaz = int(taldea)
  os.rename(self.titlek,"./music/"+carpetak[taldeaz]+"/"+izena+".mp3")

class grupoak_erakutsi(object):
 def __init__(self, balorea):
  self.balorea  = balorea
  self.url = ""
  
 def t_ikustatu(self):
  if self.balorea == "null":
   karpetak = os.listdir(".\\music")
   luzehera = len(karpetak)
   print("taldeak:")
   for x in range(luzehera):
    print(x,".",karpetak[x])
   taldea = input("taldea:")
   taldeaz = int(taldea)
   self.url += ".\\music\\" + karpetak[taldeaz]
   
class musica_exekutatu(grupoak_erakutsi):
 def __init__(self,url):
  super(musica_exekutatu, self).__init__(url)
 
 def k_ikustatu(self):
  kantak = os.listdir(self.url)
  luzehera = len(kantak)
  print("musika:")
  for x in range(luzehera):
   print(x,".",kantak[x])
  kanta = input("kanta aukeratu:")
  kantaz = int(kanta)
  self.url += "\\" + kantak[kantaz] 
  
 def exekutatu(self):
  os.startfile(self.url)
  
  
  
 
  

#-g 
script, cmd, info = argv
 
 
if cmd == "-g": 
 grupoak = grupoa("music/" + info)
 grupoak.grupoa_sortu()
 
if cmd == "-mp3":
 kantak = kanta(info)
 kantak.izena_ezarri()
 
if cmd == "-start":
 while True:
  mp3 = musica_exekutatu(info)
  url = mp3.t_ikustatu() 
  mp3.k_ikustatu()
  print(mp3.exekutatu())