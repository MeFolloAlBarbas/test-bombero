from PIL import Image
H=[
"...K.......K",
"..KYK.....KY",
"..KYOK...KYO",
"..KOOK..KKKK",
"...KORKKNNNN",
"...KRKNNNNNG",
"...KRKNNNNGG",
"..KKKKKKKKKK",
"..KRRRRRRRRR",
".KRRRRRRRRRR",
".KROOKKKOOOO",
".KROKKWKOOOO",
".KROKKKKOOOO",
"KRROKKKKOOOO",
"KROPPOKWWWWW",
"KRROOKWWWWWW",
".KRROKWSWWWW",
"..KRRKWSWWSW",
".KRROKWSWWSW",
"KRRYKWWSWWSW",
"KOKYKWSWWSWW",
"KOKYKSWWSWWW",
".KRYKSWWSWWW",
".KRYYKSWWSWW",
".KRRYKSWWSWW",
"..KRRKSWSWWW",
"..KRRKSWSWWW",
"..KOOKKSWSWW",
"..KKKK.KSWSW",
".......KSWSW",
"........KSWW",
"........KSWW",
".......KSWWS",
"........KWSW",
".........KSW",
".........KWW",
"..........KW",
"..........KK",
]
G=[r+r[::-1] for r in H]
C={'K':(45,22,22),'N':(35,55,110),'G':(245,195,45),'R':(222,52,34),'O':(250,135,35),'Y':(255,212,70),'W':(255,248,225),'P':(255,120,140),'S':(200,200,210)}
im=Image.new('RGBA',(42,42),(0,0,0,0))
for y,r in enumerate(G):
  for x,c in enumerate(r):
    if c in C: im.putpixel((x+9,y+1),C[c]+(255,))
for s,n in [(512,'icon-512'),(192,'icon-192'),(180,'apple-touch-icon'),(48,'favicon')]:
  im.resize((s,s),Image.NEAREST).save(f'img/{n}.png')
bg=Image.new('RGBA',(42,42),(255,255,255,255));bg.alpha_composite(im);bg.resize((420,420),Image.NEAREST).save('/tmp/preview.png')
