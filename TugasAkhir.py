from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
x_time = 0
def bg():
    # langit 
    glColor3ub(43, 202, 255)
    glBegin(GL_QUADS)
    glVertex2f(0,0)
    glVertex2f(500,0)
    glVertex2f(500,700)
    glVertex2f(0, 700)
    glEnd()

    # rumput
    glColor3ub(10, 117, 0)
    glBegin(GL_POLYGON)
    glVertex2f(0,190)
    glVertex2f(120,200)
    glVertex2f(380,200)
    glVertex2f(500,190)
    glVertex2f(500,0)
    glVertex2f(0,0)
    glEnd()

    # pinggir jalan
    glColor3ub(222, 235, 221)
    glBegin(GL_QUADS)
    glVertex2f(353,0)
    glVertex2f(273,200)
    glVertex2f(223.6,200)
    glVertex2f(143.6,0)
    glEnd()

    # jalan
    glColor3ub(97, 105, 96)
    glBegin(GL_QUADS)
    glVertex2f(343.4,0)
    glVertex2f(263.5,200)
    glVertex2f(233.6,200)
    glVertex2f(152.6,0)
    glEnd()

def awan():
    glPushMatrix()
    glTranslated(x_time,0,0)
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(50,410)
    glVertex2f(61,408)
    glVertex2f(72,400)
    glVertex2f(77.5,392)
    glVertex2f(80,380)
    glVertex2f(78.5,370)
    glVertex2f(72.5,360)
    glVertex2f(60.5,352)
    glVertex2f(50,350)
    glVertex2f(39.5,352)
    glVertex2f(28,360)
    glVertex2f(21.5,370)
    glVertex2f(20,380)
    glVertex2f(22.5,392)
    glVertex2f(27.5,400)
    glVertex2f(39,408)
    glVertex2f(50,410)
    glEnd()
    glPopMatrix()

def sekolah():
    # stroke kanan
    glColor3ub(112, 64, 0)
    glBegin(GL_QUADS)
    glVertex2f(300,200)
    glVertex2f(385,200)
    glVertex2f(405,280)
    glVertex2f(310.8,290)
    glEnd()

    # kanan
    glColor3ub(255, 193, 112)
    glBegin(GL_QUADS)
    glVertex2f(300,200)
    glVertex2f(380,200)
    glVertex2f(400,280)
    glVertex2f(310.8,290)
    glEnd()

    # atap kanan 2
    glColor3ub(69, 0, 133)
    glBegin(GL_QUADS)
    glVertex2f(310.8,290)
    glVertex2f(410,280.6)
    glVertex2f(400,330)
    glVertex2f(320,340)
    glEnd()

    # atap kanan
    glColor3ub(69, 0, 133)
    glBegin(GL_QUADS)
    glVertex2f(310.2,300.5)
    glVertex2f(310.8,290)
    glVertex2f(415,270.8)
    glVertex2f(420,280.5)
    glEnd()

    # stroke kiri
    glColor3ub(112, 64, 0)
    glBegin(GL_QUADS)
    glVertex2f(200,200)
    glVertex2f(115,200)
    glVertex2f(95,280)
    glVertex2f(183.2,290)
    glEnd()

    # kiri
    glColor3ub(255, 193, 112)
    glBegin(GL_QUADS)
    glVertex2f(200,200)
    glVertex2f(120,200)
    glVertex2f(100,280)
    glVertex2f(183.2,290)
    glEnd()

    # atap kiri 2
    glColor3ub(69, 0, 133)
    glBegin(GL_QUADS)
    glVertex2f(80.5,280.5)
    glVertex2f(175,290.8)
    glVertex2f(182,340)
    glVertex2f(90,330)
    glEnd()

    # atap kiri 
    glColor3ub(69, 0, 133)
    glBegin(GL_QUADS)
    glVertex2f(80,270.8)
    glVertex2f(183.2,290)
    glVertex2f(180,300.8)
    glVertex2f(75,280.5)
    glEnd()

    # stroke lantai 2
    glColor3ub(112, 64, 0)
    glBegin(GL_POLYGON)
    glVertex2f(175,300.5)
    glVertex2f(325.2,300.5)
    glVertex2f(325.2,390)
    glVertex2f(250,440)
    glVertex2f(175,390)
    glEnd()

    # lantai 2
    glColor3ub(255, 193, 112)
    glBegin(GL_POLYGON)
    glVertex2f(180,300.5)
    glVertex2f(320.2,300.5)
    glVertex2f(320.2,390)
    glVertex2f(250,440)
    glVertex2f(180,390)
    glEnd()

    # stroke depan
    glColor3ub(112, 64, 0)
    glBegin(GL_POLYGON)
    glVertex2f(190,200)
    glVertex2f(310,200)
    glVertex2f(330,300)
    glVertex2f(250,320)
    glVertex2f(170,300)
    glEnd()

    # depan
    glColor3ub(255, 193, 112)
    glBegin(GL_POLYGON)
    glVertex2f(200,200)
    glVertex2f(300,200)
    glVertex2f(320,300)
    glVertex2f(250,320)
    glVertex2f(180,300)
    glEnd()

    # atap tengah kiri
    glColor3ub(118, 23, 207)
    glBegin(GL_QUADS)
    glVertex2f(160.5,290.5)
    glVertex2f(250,310.5)
    glVertex2f(250,320.5)
    glVertex2f(160.2,300)
    glEnd()

    # atap tengah kanan
    glColor3ub(118, 23, 207)
    glBegin(GL_QUADS)
    glVertex2f(250,310.5)
    glVertex2f(330.5,290.5)
    glVertex2f(330.8,300)
    glVertex2f(250,320.5)
    glEnd()

    # atap tengah kiri atas
    glColor3ub(118, 23, 207)
    glBegin(GL_QUADS)
    glVertex2f(160,370.6)
    glVertex2f(150,390)
    glVertex2f(250,460)
    glVertex2f(250,430)
    glEnd()

    # atap tengah kanan atas
    glColor3ub(118, 23, 207)
    glBegin(GL_QUADS)
    glVertex2f(250,460)
    glVertex2f(250,430)
    glVertex2f(340,370.6)
    glVertex2f(350,390)
    glEnd()

    #stroke pintu 
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(249,200)
    glVertex2f(249,241.5)
    glVertex2f(247,240.5)
    glVertex2f(245,240)
    glVertex2f(243,239)
    glVertex2f(241,237)
    glVertex2f(240,234)
    glVertex2f(238,234)
    glVertex2f(236,230)
    glVertex2f(236,200)
    glVertex2f(249,200)
    glVertex2f(249,241.5)
    glVertex2f(251,240.5)
    glVertex2f(253,240)
    glVertex2f(255,239)
    glVertex2f(257,237)
    glVertex2f(258,235)
    glVertex2f(260,233)
    glVertex2f(262,230)
    glVertex2f(262,200)
    glEnd()

    # pintu 
    glColor3ub(69, 46, 10)
    glBegin(GL_POLYGON)
    glVertex2f(249,200)
    glVertex2f(249,240.5)
    glVertex2f(247,239.5)
    glVertex2f(245,239)
    glVertex2f(243,238)
    glVertex2f(241,236)
    glVertex2f(240,234)
    glVertex2f(238,232)
    glVertex2f(237,230)
    glVertex2f(237,200)
    glVertex2f(249,200)
    glVertex2f(249,240.5)
    glVertex2f(251,239.5)
    glVertex2f(253,239)
    glVertex2f(255,238)
    glVertex2f(257,236)
    glVertex2f(258,234)
    glVertex2f(260,232)
    glVertex2f(261,230)
    glVertex2f(261,200)
    glEnd()

    # garis tengah pintu
    glColor3ub(255,255,255)
    glBegin(GL_LINES)
    glVertex2f(249, 240)
    glVertex2f(249, 200)
    glEnd()

    # stroke jendela kanan
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(355,218)
    glVertex2f(355,267)
    glVertex2f(353,266.5)
    glVertex2f(350,266)
    glVertex2f(345,263)
    glVertex2f(340,257)
    glVertex2f(338,250)
    # kiri bawah
    glVertex2f(338,218)
    glVertex2f(355,218)
    glVertex2f(355,267)
    glVertex2f(357,266.5)
    glVertex2f(360,266)
    glVertex2f(365,263)
    glVertex2f(371,257)
    glVertex2f(372,250)
    # kanan bawah
    glVertex2f(372,218)
    glEnd()

    # jendela kanan 
    glColor3ub(69, 46, 10)
    glBegin(GL_POLYGON)
    glVertex2f(355,220)
    glVertex2f(355,265)
    glVertex2f(353,264.5)
    glVertex2f(350,264)
    glVertex2f(345,261)
    glVertex2f(341,255)
    glVertex2f(340,250)
    # kiri bawah
    glVertex2f(340,220)
    glVertex2f(355,220)
    glVertex2f(355,265)
    glVertex2f(357,264.5)
    glVertex2f(360,264)
    glVertex2f(365,261)
    glVertex2f(369,255)
    glVertex2f(370,250)
    # kanan bawah
    glVertex2f(370,220)
    glEnd()

    # garis jendela kanan vertikal
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(353,220)
    glVertex2f(353,264)
    glVertex2f(355,265)
    glVertex2f(357,264)
    glVertex2f(357,220)
    glEnd()

    # garis jendela kanan horizontal
    glColor3ub(255,255,255)
    glBegin(GL_QUADS)
    glVertex2f(340,238)
    glVertex2f(340,240)
    glVertex2f(370,240)
    glVertex2f(370,238)
    glEnd()

    # stroke jendela kiri
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(145,218)
    glVertex2f(145,267)
    glVertex2f(143,266.5)
    glVertex2f(140,266)
    glVertex2f(135,263)
    glVertex2f(130,257)
    glVertex2f(128,250)
    # kiri bawah
    glVertex2f(128,218)
    glVertex2f(145,218)
    glVertex2f(145,267)
    glVertex2f(147,266.5)
    glVertex2f(150,266)
    glVertex2f(155,263)
    glVertex2f(160,257)
    glVertex2f(162,250)
    # kanan bawah
    glVertex2f(162,218)
    glEnd()


    # jendela kiri
    glColor3ub(69, 46, 10)
    glBegin(GL_POLYGON)
    glVertex2f(145,220)
    glVertex2f(145,265)
    glVertex2f(143,264.5)
    glVertex2f(140,264)
    glVertex2f(135,261)
    glVertex2f(131,255)
    glVertex2f(130,250)
    # kiri bawah
    glVertex2f(130,220)
    glVertex2f(145,220)
    glVertex2f(145,265)
    glVertex2f(147,264.5)
    glVertex2f(150,264)
    glVertex2f(155,261)
    glVertex2f(159,255)
    glVertex2f(160,250)
    # kanan bawah
    glVertex2f(160,220)
    glEnd()

    # garis jendela kiri vertikal
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(143,220)
    glVertex2f(143,264)
    glVertex2f(145,265)
    glVertex2f(147,264)
    glVertex2f(147,220)
    glEnd()

    # garis jendela kiri horizontal
    glColor3ub(255,255,255)
    glBegin(GL_QUADS)
    glVertex2f(130,238)
    glVertex2f(130,240)
    glVertex2f(160,240)
    glVertex2f(160,238)
    glEnd()

    #stroke jendela tengah
    glColor3ub(69, 46, 10)
    glBegin(GL_POLYGON)
    glVertex2f(250,250)
    glVertex2f(250,295)
    glVertex2f(248,294.5)
    glVertex2f(245,294)
    glVertex2f(240,291)
    glVertex2f(234,285)
    glVertex2f(233,280)
    # kiri bawah
    glVertex2f(233,250)
    glVertex2f(250,250)
    glVertex2f(250,295)
    glVertex2f(252,294.5)
    glVertex2f(255,294)
    glVertex2f(260,291)
    glVertex2f(264,285)
    glVertex2f(265,280)
    # kanan bawah
    glVertex2f(265,250)
    glEnd()

    # jendela tengah
    glColor3ub(69, 46, 10)
    glBegin(GL_POLYGON)
    glVertex2f(250,250)
    glVertex2f(250,295)
    glVertex2f(248,294.5)
    glVertex2f(245,294)
    glVertex2f(240,291)
    glVertex2f(234,285)
    glVertex2f(233,280)
    # kiri bawah
    glVertex2f(233,250)
    glVertex2f(250,250)
    glVertex2f(250,295)
    glVertex2f(252,294.5)
    glVertex2f(255,294)
    glVertex2f(260,291)
    glVertex2f(264,285)
    glVertex2f(265,280)
    # kanan bawah
    glVertex2f(265,250)
    glEnd()

    # garis jendela tengah vertikal
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(247,250)
    glVertex2f(247,294)
    glVertex2f(249,295)
    glVertex2f(251,294)
    glVertex2f(251,250)
    glEnd()

    # garis jendela tengah horizontal
    glColor3ub(255,255,255)
    glBegin(GL_QUADS)
    glVertex2f(233,268)
    glVertex2f(233,270)
    glVertex2f(265,270)
    glVertex2f(265,268)
    glEnd()

    # stroke jam 
    glColor3ub(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(250,412)
    glVertex2f(261,410)
    glVertex2f(272,402)
    glVertex2f(278.5,394)
    glVertex2f(282,380)
    glVertex2f(279.5,368)
    glVertex2f(272.5,358)
    glVertex2f(260.5,350)
    glVertex2f(250,348)
    glVertex2f(239.5,350)
    glVertex2f(227,358)
    glVertex2f(220.5,368)
    glVertex2f(218,380)
    glVertex2f(221.5,394)
    glVertex2f(227.5,402)
    glVertex2f(239,410)
    glVertex2f(250,412)
    glEnd()

    # jam atas
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(250,410)
    glVertex2f(261,408)
    glVertex2f(272,400)
    glVertex2f(277.5,392)
    glVertex2f(280,380)
    glVertex2f(278.5,370)
    glVertex2f(272.5,360)
    glVertex2f(260.5,352)
    glVertex2f(250,350)
    glVertex2f(239.5,352)
    glVertex2f(228,360)
    glVertex2f(221.5,370)
    glVertex2f(220,380)
    glVertex2f(222.5,392)
    glVertex2f(227.5,400)
    glVertex2f(239,408)
    glVertex2f(250,410)
    glEnd()

def jarum_jam():
    # Jarum besar
    glColor3ub(0,0,0)
    glBegin(GL_LINES)
    glVertex2f(250,380)
    glVertex2f(250,400)
    glEnd()

    # glPushMatrix()
    # glRotated(angle_time,0,0,1)
    # glColor3ub(0,0,0)
    # glBegin(GL_LINES)
    # glVertex2f(250,380)
    # glVertex2f(268,400)
    # glEnd()
    # glPopMatrix()

    # Jarum kecil
    glColor3ub(0,0,0)
    glBegin(GL_LINES)
    glVertex2f(250,380)
    glVertex2f(240,365)
    glEnd()

    # 12
    glColor3ub(0,0,0)
    glBegin(GL_LINES)
    glVertex2f(250,410)
    glVertex2f(250,405)
    glEnd()

    # 3
    glColor3ub(0,0,0)
    glBegin(GL_LINES)
    glVertex2f(280,380)
    glVertex2f(275,380)
    glEnd()

    # 6
    glColor3ub(0,0,0)
    glBegin(GL_LINES)
    glVertex2f(250,350)
    glVertex2f(250,355)
    glEnd()

    # 9
    glColor3ub(0,0,0)
    glBegin(GL_LINES)
    glVertex2f(220,380)
    glVertex2f(225,380)
    glEnd()
    
def timer(value):
    global x_time
    x_time += 3
    glutTimerFunc(200, timer,0)

def iterate():
    glViewport(0, 0, 500, 700)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Peletakan titik koordinat (0, 0) di pojok kiri bawah
    glOrtho(0.0, 500, 0.0, 700, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def display1():
    # fungsi untuk membersihkan layar
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # untuk mereset semua posisi grafik/bentuk
    glLoadIdentity()
    # fungsi looping
    iterate()
    # memanggil fungsi 
    bg()
    awan()
    sekolah()
    jarum_jam()
    # untuk membersihkan layar 
    glutSwapBuffers()

# inisialisasi glut
glutInit() 
# untuk mengatur layar menjadi berwarna (parameter kode warna)
glutInitDisplayMode(GLUT_RGBA)
# untuk mengatur ukuran layar/window (lebar(x), tinggi(y)) diagram cartesius
glutInitWindowSize(500, 700)
# untuk mengatur posisi layar/window (lebar(x), tinggi(y)) diagram cartesius
glutInitWindowPosition(0, 0)
# untuk memberi nama pada layar/window
wind = glutCreateWindow("Display awal")
timer(0)
# timer2(0)
# untuk menampilkan objek pada layar, fungsi callback
glutDisplayFunc(display1)
# untuk memerintah openGL untuk selalu membuka dan menampilkan objek
glutIdleFunc(display1)
# untuk memulai segalanya, untuk melooping objek terus menerus 
glutMainLoop()