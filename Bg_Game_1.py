#import library
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
w,h= 500,500

def game_lvl1():
    #papan
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(225, 251, 231)
    glVertex2f(0, 0)
    glVertex2f(0, 700)
    glVertex2f(500, 700)
    glVertex2f(500, 0)
    glEnd()

    #kayu atas papan
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(150, 75, 0)
    glVertex2f(20, 680)
    glVertex2f(480, 680)
    glVertex2f(460, 660)
    glVertex2f(40, 660)
    glEnd()

    #kayu samping kiri papan
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(150, 75, 0)
    glVertex2f(20, 680)
    glVertex2f(20, 200)
    glVertex2f(40, 220)
    glVertex2f(40, 660)
    glEnd()

    #kayu bawah papan
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(150, 75, 0)
    glVertex2f(20, 200)
    glVertex2f(40, 220)
    glVertex2f(460, 220)
    glVertex2f(480, 200)
    glEnd()

    #kayu samping kanan papan 
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(150, 75, 0)
    glVertex2f(480, 200)
    glVertex2f(480, 680)
    glVertex2f(460, 660)
    glVertex2f(460, 220)
    glEnd()

    #papan tulis
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(225, 225, 225)
    glVertex2f(40, 660)
    glVertex2f(460, 660)
    glVertex2f(460, 220)
    glVertex2f(40, 220)
    glEnd()

    #kayu pembatas dengan lantai
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(150, 75, 0)
    glVertex2f(0, 160)
    glVertex2f(0, 180)
    glVertex2f(500, 180)
    glVertex2f(500, 160)
    glEnd()

    #lantai
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(210, 105, 305)
    glVertex2f(0, 0)
    glVertex2f(0, 160)
    glVertex2f(500, 160)
    glVertex2f(500, 0)
    glEnd()

    #kotak pilihan bawah kiri
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(225, 225, 225)
    glVertex2f(20, 20)
    glVertex2f(20, 60)
    glVertex2f(180, 60)
    glVertex2f(180, 20)
    glEnd()

    #kotak pilihan atas kiri
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(225, 225, 225)
    glVertex2f(20, 100)
    glVertex2f(20, 140)
    glVertex2f(180, 140)
    glVertex2f(180, 100)
    glEnd()

    #kotak pilihan atas kanan
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(225, 225, 225)
    glVertex2f(480, 140)
    glVertex2f(300, 140)
    glVertex2f(300, 100)
    glVertex2f(480, 100)
    glEnd()

    #kotak pilihan bawah kanan
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(225, 225, 225)
    glVertex2f(480, 60)
    glVertex2f(300, 60)
    glVertex2f(300, 20)
    glVertex2f(480, 20)
    glEnd()

    #segitiga soal
    glColor3ub(129, 38, 235)
    glBegin(GL_POLYGON)
    glVertex2f(125,500)
    glVertex2f(100,450)
    glVertex2f(150,450)
    glEnd()

    glPushMatrix()
    glTranslated(-50, 0, 0)
    glColor3ub(129, 38, 235)
    glBegin(GL_POLYGON)
    glVertex2f(125,500)
    glVertex2f(100,450)
    glVertex2f(150,450)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslated(0, -100, 0)
    glColor3ub(129, 38, 235)
    glBegin(GL_POLYGON)
    glVertex2f(125,500)
    glVertex2f(100,450)
    glVertex2f(150,450)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslated(-50, -100, 0)
    glColor3ub(129, 38, 235)
    glBegin(GL_POLYGON)
    glVertex2f(125,500)
    glVertex2f(100,450)
    glVertex2f(150,450)
    glEnd()
    glPopMatrix()
    glPushMatrix()
    glTranslated(200, 0, 0)
    glColor3ub(247, 237, 37)
    glBegin(GL_POLYGON)
    glVertex2f(125,500)
    glVertex2f(100,450)
    glVertex2f(150,450)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslated(250, 0, 0)
    glColor3ub(247, 237, 37)
    glBegin(GL_POLYGON)
    glVertex2f(125,500)
    glVertex2f(100,450)
    glVertex2f(150,450)
    glEnd()
    glPopMatrix()


    #kurang   
    glPushMatrix()
    glTranslated(-25, -50, 0)
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(0, 0, 0)
    glVertex2f(200, 500)
    glVertex2f(280, 500)
    glVertex2f(280, 480)
    glVertex2f(200, 480)
    glEnd()
    glPopMatrix()


    #sama degan    
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(0, 0, 0)
    glVertex2f(420, 500)
    glVertex2f(420, 480)
    glVertex2f(450, 480)
    glVertex2f(450, 500)
    glEnd()    
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(0, 0, 0)
    glVertex2f(420, 460)
    glVertex2f(420, 440)
    glVertex2f(450, 440)
    glVertex2f(450, 460)
    glEnd()

def game_lvl2():
    #papan
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(225, 251, 231)
    glVertex2f(0, 0)
    glVertex2f(0, 700)
    glVertex2f(500, 700)
    glVertex2f(500, 0)
    glEnd()

    #kayu atas papan
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(150, 75, 0)
    glVertex2f(20, 680)
    glVertex2f(480, 680)
    glVertex2f(460, 660)
    glVertex2f(40, 660)
    glEnd()

    #kayu samping kiri papan
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(150, 75, 0)
    glVertex2f(20, 680)
    glVertex2f(20, 200)
    glVertex2f(40, 220)
    glVertex2f(40, 660)
    glEnd()

    #kayu bawah papan
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(150, 75, 0)
    glVertex2f(20, 200)
    glVertex2f(40, 220)
    glVertex2f(460, 220)
    glVertex2f(480, 200)
    glEnd()

    #kayu samping kanan papan 
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(150, 75, 0)
    glVertex2f(480, 200)
    glVertex2f(480, 680)
    glVertex2f(460, 660)
    glVertex2f(460, 220)
    glEnd()

    #papan tulis
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(225, 225, 225)
    glVertex2f(40, 660)
    glVertex2f(460, 660)
    glVertex2f(460, 220)
    glVertex2f(40, 220)
    glEnd()

    #kayu pembatas dengan lantai
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(150, 75, 0)
    glVertex2f(0, 160)
    glVertex2f(0, 180)
    glVertex2f(500, 180)
    glVertex2f(500, 160)
    glEnd()

    #lantai
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(210, 105, 305)
    glVertex2f(0, 0)
    glVertex2f(0, 160)
    glVertex2f(500, 160)
    glVertex2f(500, 0)
    glEnd()

    #kotak pilihan bawah kiri
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(225, 225, 225)
    glVertex2f(20, 20)
    glVertex2f(20, 60)
    glVertex2f(180, 60)
    glVertex2f(180, 20)
    glEnd()

    #kotak pilihan atas kiri
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(225, 225, 225)
    glVertex2f(20, 100)
    glVertex2f(20, 140)
    glVertex2f(180, 140)
    glVertex2f(180, 100)
    glEnd()

    #kotak pilihan atas kanan
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(225, 225, 225)
    glVertex2f(480, 140)
    glVertex2f(300, 140)
    glVertex2f(300, 100)
    glVertex2f(480, 100)
    glEnd()

    #kotak pilihan bawah kanan
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(225, 225, 225)
    glVertex2f(480, 60)
    glVertex2f(300, 60)
    glVertex2f(300, 20)
    glVertex2f(480, 20)
    glEnd()

    #object kotak
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(255, 41, 226)
    glVertex2f(50, 500)
    glVertex2f(100, 500)
    glVertex2f(100, 450)
    glVertex2f(50, 450)
    glEnd()

    glPushMatrix()
    glTranslated(75,0,0)
    glColor3ub(255, 41, 226)
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glVertex2f(50, 500)
    glVertex2f(100, 500)
    glVertex2f(100, 450)
    glVertex2f(50, 450)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslated(75,-75,0)
    glColor3ub(255, 41, 226)
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glVertex2f(50, 500)
    glVertex2f(100, 500)
    glVertex2f(100, 450)
    glVertex2f(50, 450)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslated(0,-75,0)
    glColor3ub(255, 41, 226)
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glVertex2f(50, 500)
    glVertex2f(100, 500)
    glVertex2f(100, 450)
    glVertex2f(50, 450)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslated(225,-50,0)
    glColor3ub(38, 251, 255)
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glVertex2f(50, 500)
    glVertex2f(100, 500)
    glVertex2f(100, 450)
    glVertex2f(50, 450)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslated(300,-50,0)
    glColor3ub(38, 251, 255)
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glVertex2f(50, 500)
    glVertex2f(100, 500)
    glVertex2f(100, 450)
    glVertex2f(50, 450)
    glEnd()
    glPopMatrix()

    # x
    glPushMatrix()
    glTranslated(-75,-20,0)
    glColor3ub(0,0,0)
    glBegin(GL_QUADS)
    glVertex2f(280,480)
    glVertex2f(270,470)
    glVertex2f(320,420)
    glVertex2f(330,430)

    glVertex2f(330,470)
    glVertex2f(320,480)
    glVertex2f(270,430)
    glVertex2f(280,420)
    glEnd()
    glPopMatrix()
    

    #sama degan    
    glPushMatrix()
    glTranslated(0,-50,0)
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(0, 0, 0)
    glVertex2f(420, 500)
    glVertex2f(420, 480)
    glVertex2f(450, 480)
    glVertex2f(450, 500)
    glEnd()    
    glPopMatrix()

    glPushMatrix()
    glTranslated(0,-50,0)
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(0, 0, 0)
    glVertex2f(420, 460)
    glVertex2f(420, 440)
    glVertex2f(450, 440)
    glVertex2f(450, 460)
    glEnd()  
    glPopMatrix()

def game_lvl3():
    #papan
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(225, 251, 231)
    glVertex2f(0, 0)
    glVertex2f(0, 700)
    glVertex2f(500, 700)
    glVertex2f(500, 0)
    glEnd()

    #kayu atas papan
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(150, 75, 0)
    glVertex2f(20, 680)
    glVertex2f(480, 680)
    glVertex2f(460, 660)
    glVertex2f(40, 660)
    glEnd()

    #kayu samping kiri papan
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(150, 75, 0)
    glVertex2f(20, 680)
    glVertex2f(20, 200)
    glVertex2f(40, 220)
    glVertex2f(40, 660)
    glEnd()

    #kayu bawah papan
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(150, 75, 0)
    glVertex2f(20, 200)
    glVertex2f(40, 220)
    glVertex2f(460, 220)
    glVertex2f(480, 200)
    glEnd()

    #kayu samping kanan papan 
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(150, 75, 0)
    glVertex2f(480, 200)
    glVertex2f(480, 680)
    glVertex2f(460, 660)
    glVertex2f(460, 220)
    glEnd()

    #papan tulis
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(225, 225, 225)
    glVertex2f(40, 660)
    glVertex2f(460, 660)
    glVertex2f(460, 220)
    glVertex2f(40, 220)
    glEnd()

    #kayu pembatas dengan lantai
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(150, 75, 0)
    glVertex2f(0, 160)
    glVertex2f(0, 180)
    glVertex2f(500, 180)
    glVertex2f(500, 160)
    glEnd()

    #lantai
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(210, 105, 305)
    glVertex2f(0, 0)
    glVertex2f(0, 160)
    glVertex2f(500, 160)
    glVertex2f(500, 0)
    glEnd()

    #kotak pilihan bawah kiri
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(225, 225, 225)
    glVertex2f(20, 20)
    glVertex2f(20, 60)
    glVertex2f(180, 60)
    glVertex2f(180, 20)
    glEnd()

    #kotak pilihan atas kiri
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(225, 225, 225)
    glVertex2f(20, 100)
    glVertex2f(20, 140)
    glVertex2f(180, 140)
    glVertex2f(180, 100)
    glEnd()

    #kotak pilihan atas kanan
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(225, 225, 225)
    glVertex2f(480, 140)
    glVertex2f(300, 140)
    glVertex2f(300, 100)
    glVertex2f(480, 100)
    glEnd()

    #kotak pilihan bawah kanan
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(225, 225, 225)
    glVertex2f(480, 60)
    glVertex2f(300, 60)
    glVertex2f(300, 20)
    glVertex2f(480, 20)
    glEnd()

    #object kotak
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(255, 41, 226)
    glVertex2f(50, 550)
    glVertex2f(100, 550)
    glVertex2f(100, 500)
    glVertex2f(50, 500)
    glEnd()

    glPushMatrix()
    glTranslated(75,0,0)
    glColor3ub(255, 41, 226)
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glVertex2f(50, 550)
    glVertex2f(100, 550)
    glVertex2f(100, 500)
    glVertex2f(50, 500)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslated(75,-75,0)
    glColor3ub(255, 41, 226)
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glVertex2f(50, 550)
    glVertex2f(100, 550)
    glVertex2f(100, 500)
    glVertex2f(50, 500)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslated(0,-75,0)
    glColor3ub(255, 41, 226)
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glVertex2f(50, 550)
    glVertex2f(100, 550)
    glVertex2f(100, 500)
    glVertex2f(50, 500)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslated(75,-150,0)
    glColor3ub(255, 41, 226)
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glVertex2f(50, 550)
    glVertex2f(100, 550)
    glVertex2f(100, 500)
    glVertex2f(50, 500)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslated(0,-150,0)
    glColor3ub(255, 41, 226)
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glVertex2f(50, 550)
    glVertex2f(100, 550)
    glVertex2f(100, 500)
    glVertex2f(50, 500)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslated(225,-50,0)
    glColor3ub(38, 251, 255)
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glVertex2f(50, 550)
    glVertex2f(100, 550)
    glVertex2f(100, 500)
    glVertex2f(50, 500)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslated(300,-50,0)
    glColor3ub(38, 251, 255)
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glVertex2f(50, 550)
    glVertex2f(100, 550)
    glVertex2f(100, 500)
    glVertex2f(50, 500)
    glEnd()
    glPopMatrix()

    # -
    glPushMatrix()
    glTranslated(30,0,0)
    glBegin(GL_QUADS)
    glColor3ub(0,0,0)
    glVertex2f(170,440)
    glVertex2f(170,460)
    glVertex2f(230,460)
    glVertex2f(230,440)
    glEnd()
    glPopMatrix()

    # :
    glPushMatrix()
    glTranslated(30,0,0)
    glBegin(GL_QUADS)
    glColor3ub(0,0,0)
    glVertex2f(190,470)
    glVertex2f(190,490)
    glVertex2f(210,490)
    glVertex2f(210,470)
    glEnd()
    glPopMatrix()

    # :
    glPushMatrix()
    glTranslated(30,-60,0)
    glBegin(GL_QUADS)
    glColor3ub(0,0,0)
    glVertex2f(190,470)
    glVertex2f(190,490)
    glVertex2f(210,490)
    glVertex2f(210,470)
    glEnd()
    glPopMatrix()

    #sama degan    
    glPushMatrix()
    glTranslated(0,-50,0)
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(0, 0, 0)
    glVertex2f(420, 500)
    glVertex2f(420, 480)
    glVertex2f(450, 480)
    glVertex2f(450, 500)
    glEnd()    
    glPopMatrix()

    glPushMatrix()
    glTranslated(0,-50,0)
    glBegin(GL_QUADS) #utk membuat objek gambar/ titik koordinatnya ada 4
    glColor3ub(0, 0, 0)
    glVertex2f(420, 460)
    glVertex2f(420, 440)
    glVertex2f(450, 440)
    glVertex2f(450, 460)
    glEnd()  
    glPopMatrix()
    
#fungsi iterasi
def iterate():
    glViewport(0, 0, 500, 700)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Peletakan titik koordinat (0, 0) di pojok kiri bawah
    glOrtho(0.0, 500, 0.0, 700, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClearColor(1.07, 1.0, 0.1, 1.37)#mengganti warna background 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #utk membersihkan layar
    glLoadIdentity()
    iterate()
    game_lvl1()
    game_lvl2()
    game_lvl3()
    glutSwapBuffers() #utk membersihkan layar, double buffering

glutInit() #inisialisasi glut
glutInitDisplayMode(GLUT_RGBA) #utk mengatur display supaya berwarna
glutInitWindowSize(500, 700) #utk mengatur ukuran window
glutInitWindowPosition(0, 0) #utk mengatur letak window
#utk transparansi (tapi belum bisa)
#glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
#glEnable(GL_BLEND)
wind = glutCreateWindow("Bg Game 1") #utk memberi nama pada window
glutDisplayFunc(showScreen) #utk fungsi callback
glutIdleFunc(showScreen) #utk fungsi callback
glutMainLoop() #fungsi yang akan memulai keseluruhan program
