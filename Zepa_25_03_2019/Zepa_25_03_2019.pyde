def setup():
    size (400, 400)
    textSize(120)
    textAlign(CENTER)
    background(200,214,200)
    c =(250,250,250)
    global c
def draw():
    global c
    if keyPressed == True:
        fill(0)
        if key == 'M' or key == 'm':
           text('M', width/2+120, height/2)
        if mousePressed and keyCode==RIGHT:
            fill(123,144,231)
            text('M', width/2+120, height/2)
    else:     
        if mousePressed:
         fill(255,255,255)
         text('D',width/2-120, height/2)
        if mousePressed and keyCode==LEFT:
         fill(200,110,13)
         text('D',width/2-120, height/2)
    s = createShape();
    s.beginShape();
    s.fill(0, 0, 255, 115);
    s.noStroke();
    s.vertex(width/4, height/3*2);
    s.vertex(width/4-50, height/3*2-50);
    s.vertex(width/2, height/3*2);
    s.vertex(width/+50, height/3*2+50);
    s.vertex(width/4+100, height/3*2);
    s.endShape(CLOSE);
    shape(s,25,25)
        
