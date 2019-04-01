def setup():
    krotkaKolorow=((214,0,0),(0,214,0),(0,0,214),(75,200,240))
    size(400, 400)
    frameRate(30)
    rectMode(CENTER)
    global x
    global y
    x = 0
    y = 200
    stroke(*krotkaKolorow[1])
    strokeWeight(1) 
    fill(*krotkaKolorow[0])
def draw():
    krotkaKolorow=((214,0,0),(0,214,0),(0,0,214),(75,200,240))
    global x
    global y
    background(89,147,139);
    if x >= 0 and x<= width/2:
        rect(x,y,50,50)
        x+= 2
        y+= 2.25
    if x >= 100 and x<= width/2:
        rect(x,y,50,50)
        fill(*krotkaKolorow[1])
        x+= 2
        y+= 2.25
    if x>= width/2 and x <= 300:
        fill(*krotkaKolorow[2])
        rect(x,y,50,50)
        x+= 2
        y-= 2.25
    
    if x>= 300 and x <= width:
        fill(*krotkaKolorow[3])
        rect(x,y,50,50)
        x+= 2
        y-= 2.25
        
        #exit()?
    
        