from PIL import Image
G=[
"........KKKK........",
"......KKNNNNKK......",
".....KNNNGGNNNK.....",
"..K.KNNNGGGGNNNK.K..",
".KRKKNNNNGGNNNNKKRK.",
".KRRKKKKKKKKKKKKRRK.",
"..KRRRRRRRRRRRRRRK..",
"..KRRWWKRRRRWWKRRK..",
"..KRRWKKRRRRWKKRRK..",
"..KRROOOOOOOOOORRK..",
".KRROOOKOOOOKOOORRK.",
".KRROOOOKKKKOOOORRK.",
".KRROOYYYYYYYYOORRK.",
"KRROOYYYYYYYYYYOORRK",
"KRROYYYYWWWWYYYYORRK",
"KRROYYYWWWWWWYYYORRK",
".KRROYYYWWWWYYYORRK.",
"..KRROOYYYYYYOORRK..",
"...KKRROOOOOORRKK...",
".....KKKKKKKKKK.....",
]
C={'K':(40,20,20),'N':(30,45,90),'G':(240,190,40),'R':(215,45,30),'O':(250,130,30),'Y':(255,210,60),'W':(255,250,230)}
assert all(len(r)==20 for r in G)
im=Image.new('RGBA',(24,24),(0,0,0,0))
for y,r in enumerate(G):
  for x,c in enumerate(r):
    if c in C: im.putpixel((x+2,y+2),C[c]+(255,))
for s,n in [(512,'icon-512'),(192,'icon-192'),(180,'apple-touch-icon'),(48,'favicon')]:
  im.resize((s,s),Image.NEAREST).save(f'img/{n}.png')
bg=Image.new('RGBA',(24,24),(255,255,255,255));bg.alpha_composite(im);bg.resize((240,240),Image.NEAREST).save('/tmp/preview.png')
