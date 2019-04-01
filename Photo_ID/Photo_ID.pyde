add_library('sound')
add_library('pdf')
add_library("sound")
def setup():
    size(648,800)#PDF,"zepa_id.pdf")
    global id_photo
    global glasses
    global beard
    global sf
    sf = SoundFile(this,"drum.mp3")
    id_photo = loadImage("zepa.jpg")
    glasses = loadImage("glasses.png")
    beard = loadImage("beard.png")
    beginRecord(PDF,"zepa_id2.0.pdf")
def keyPressed():
       sf.play()
def draw():
    global id_photo
    global glasses
    global beard
    image(id_photo, 0,0,648,800)
    if keyCode==LEFT:
        beginRecord
        image(glasses, 150,300,350,200)
        endRecord()
    if keyCode==DOWN:
         beginRecord
         image(beard, 125,440,400,550)
         endRecord()
    if keyCode==UP:
        beginRecord
        image(id_photo, 0,0,648,800)
        endRecord()  
    if keyCode==RIGHT:
        beginRecord
        image(glasses, 150,300,350,200)
        image(beard, 125,440,400,550)
        endRecord()  
    if mousePressed:
         endRecord()
         exit()      
