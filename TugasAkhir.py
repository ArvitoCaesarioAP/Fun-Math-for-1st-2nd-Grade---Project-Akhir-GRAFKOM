from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import OpenGL.GLUT as gl

# Atur kecepatan gerak objek
gerakKr = 20
gerakKn = 20
gerak_box = 10
gerak_box2 = 20
# glTranslated 
geser_awanKr = 0
geser_awanKn = 0
geser_capit = 0
geser_box = 0
geser_box2 = 0
geser_box3 = 0
geser_box4 = 0
geser_box5 = 0
geser_box6 = 0
# Colision
batas_awan = 360
batas_box = 450
batas_box2 = 450
batas_box3 = 450
batasKn_merah = 300
batasKn_biru = 300
batasKn_pink = 300
batasKr_merah = 200
batasKr_biru = 200
batasKr_pink = 200
# iterasi
scene = 0
jumlah_box = 0
# bool gerak objek
gerak_awan = False

# Background awal
def bg():
    # langit 
    glBegin(GL_QUADS)
    glColor3ub(166, 233, 255)
    glVertex2f(0,190)
    glVertex2f(500,190)
    glColor3ub(43, 202, 255)
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
    glColor3ub(34, 173, 21)
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

def pagar():
    # plang
    glColor3ub(105, 54, 7)
    glBegin(GL_QUADS)
    glVertex2f(-20,20)
    glVertex2f(-20,40)
    glVertex2f(160,40)
    glVertex2f(160,20)
    glEnd()

    # pagar kiri
    glColor3ub(105, 54, 7)
    glBegin(GL_QUADS)
    glVertex2f(0,0)
    glColor3ub(148, 78, 13)
    glVertex2f(20,0)
    glColor3ub(105, 54, 7)
    glVertex2f(20,60)
    glVertex2f(0,60)
    glEnd()
 
    glColor3ub(34, 173, 21)
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(10,50)
    glEnd()

    glColor3ub(105, 54, 7)
    glBegin(GL_TRIANGLES)
    glVertex2f(20,60)
    glVertex2f(10,80)
    glVertex2f(0,60)
    glEnd()

    # pagar kiri 2
    glTranslated(40,0,0)
    glColor3ub(105, 54, 7)
    glBegin(GL_QUADS)
    glVertex2f(0,0)
    glColor3ub(148, 78, 13)
    glVertex2f(20,0)
    glColor3ub(105, 54, 7)
    glVertex2f(20,60)
    glVertex2f(0,60)
    glEnd()

    glColor3ub(34, 173, 21)
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(10,50)
    glEnd()

    glColor3ub(105, 54, 7)
    glBegin(GL_TRIANGLES)
    glVertex2f(20,60)
    glVertex2f(10,80)
    glVertex2f(0,60)
    glEnd()

    # pagar kiri 3
    glTranslated(40,0,0)
    glColor3ub(105, 54, 7)
    glBegin(GL_QUADS)
    glVertex2f(0,0)
    glColor3ub(148, 78, 13)
    glVertex2f(20,0)
    glColor3ub(105, 54, 7)
    glVertex2f(20,60)
    glVertex2f(0,60)
    glEnd()

    glColor3ub(34, 173, 21)
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(10,50)
    glEnd()

    glColor3ub(105, 54, 7)
    glBegin(GL_TRIANGLES)
    glVertex2f(20,60)
    glVertex2f(10,80)
    glVertex2f(0,60)
    glEnd()

    # pagar kiri 4
    glTranslated(40,0,0)
    glColor3ub(105, 54, 7)
    glBegin(GL_QUADS)
    glVertex2f(0,0)
    glColor3ub(148, 78, 13)
    glVertex2f(20,0)
    glColor3ub(105, 54, 7)
    glVertex2f(20,60)
    glVertex2f(0,60)
    glEnd()

    glColor3ub(34, 173, 21)
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(10,50)
    glEnd()

    glColor3ub(105, 54, 7)
    glBegin(GL_TRIANGLES)
    glVertex2f(20,60)
    glVertex2f(10,80)
    glVertex2f(0,60)
    glEnd()

def awan_kiri():
    # awan 3
    glPushMatrix()
    glTranslated(-50,0,0)
    glTranslated(geser_awanKr,0,0)
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(50,510)
    glVertex2f(61,508)
    glVertex2f(72,500)
    glVertex2f(77.5,492)
    glVertex2f(80,480)
    glVertex2f(78.5,470)
    glVertex2f(72.5,460)
    glVertex2f(60.5,452)
    glVertex2f(50,450)
    glVertex2f(39.5,452)
    glVertex2f(28,460)
    glVertex2f(21.5,470)
    glVertex2f(20,480)
    glVertex2f(22.5,492)
    glVertex2f(27.5,500)
    glVertex2f(39,508)
    glVertex2f(50,510)
    glEnd()
    glPopMatrix()

    # awan 3
    glPushMatrix()
    glTranslated(-50,0,0)
    glTranslated(geser_awanKr,0,0)
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(90,510)
    glVertex2f(101,508)
    glVertex2f(112,500)
    glVertex2f(117.5,492)
    glVertex2f(120,480)
    glVertex2f(118.5,470)
    glVertex2f(112.5,460)
    glVertex2f(100.5,452)
    glVertex2f(90,450)
    glVertex2f(79.5,452)
    glVertex2f(68,460)
    glVertex2f(61.5,470)
    glVertex2f(60,480)
    glVertex2f(62.5,492)
    glVertex2f(67.5,500)
    glVertex2f(79,508)
    glVertex2f(90,510)
    glEnd()
    glPopMatrix()

    # awan 3
    glPushMatrix()
    glTranslated(-50,0,0)
    glTranslated(geser_awanKr,0,0)
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(130,510)
    glVertex2f(141,508)
    glVertex2f(152,500)
    glVertex2f(157.5,492)
    glVertex2f(160,480)
    glVertex2f(158.5,470)
    glVertex2f(152.5,460)
    glVertex2f(140.5,452)
    glVertex2f(130,450)
    glVertex2f(119.5,452)
    glVertex2f(108,460)
    glVertex2f(101.5,470)
    glVertex2f(100,480)
    glVertex2f(102.5,492)
    glVertex2f(107.5,500)
    glVertex2f(119,508)
    glVertex2f(130,510)
    glEnd()
    glPopMatrix()

    # awan 4
    glPushMatrix()
    glTranslated(-50,0,0)
    glTranslated(geser_awanKr,90,0)
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(50,610)
    glVertex2f(61,608)
    glVertex2f(72,600)
    glVertex2f(77.5,592)
    glVertex2f(80,580)
    glVertex2f(78.5,570)
    glVertex2f(72.5,560)
    glVertex2f(60.5,552)
    glVertex2f(50,550)
    glVertex2f(39.5,552)
    glVertex2f(28,560)
    glVertex2f(21.5,570)
    glVertex2f(20,580)
    glVertex2f(22.5,592)
    glVertex2f(27.5,600)
    glVertex2f(39,608)
    glVertex2f(50,610)
    glEnd()
    glPopMatrix()

    # awan 4
    glPushMatrix()
    glTranslated(-50,0,0)
    glTranslated(geser_awanKr,90,0)
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(90,610)
    glVertex2f(101,608)
    glVertex2f(112,600)
    glVertex2f(117.5,592)
    glVertex2f(120,580)
    glVertex2f(118.5,570)
    glVertex2f(112.5,560)
    glVertex2f(100.5,552)
    glVertex2f(90,550)
    glVertex2f(79.5,552)
    glVertex2f(68,560)
    glVertex2f(61.5,570)
    glVertex2f(60,580)
    glVertex2f(62.5,592)
    glVertex2f(67.5,600)
    glVertex2f(79,608)
    glVertex2f(90,610)
    glEnd()
    glPopMatrix()

    # awan 4
    glPushMatrix()
    glTranslated(-50,0,0)
    glTranslated(geser_awanKr,90,0)
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(130,610)
    glVertex2f(141,608)
    glVertex2f(152,600)
    glVertex2f(157.5,592)
    glVertex2f(160,580)
    glVertex2f(158.5,570)
    glVertex2f(152.5,560)
    glVertex2f(140.5,552)
    glVertex2f(130,550)
    glVertex2f(119.5,552)
    glVertex2f(108,560)
    glVertex2f(101.5,570)
    glVertex2f(100,580)
    glVertex2f(102.5,592)
    glVertex2f(107.5,600)
    glVertex2f(119,608)
    glVertex2f(130,610)
    glEnd()
    glPopMatrix()

def awan_kanan():
    # awan 1
    glPushMatrix()
    glTranslated(350,0,0)
    glTranslated(geser_awanKn,-100,0)
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(50,510)
    glVertex2f(61,508)
    glVertex2f(72,500)
    glVertex2f(77.5,492)
    glVertex2f(80,480)
    glVertex2f(78.5,470)
    glVertex2f(72.5,460)
    glVertex2f(60.5,452)
    glVertex2f(50,450)
    glVertex2f(39.5,452)
    glVertex2f(28,460)
    glVertex2f(21.5,470)
    glVertex2f(20,480)
    glVertex2f(22.5,492)
    glVertex2f(27.5,500)
    glVertex2f(39,508)
    glVertex2f(50,510)
    glEnd()
    glPopMatrix()

    # awan 1
    glPushMatrix()
    glTranslated(350,0,0)
    glTranslated(geser_awanKn,-100,0)
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(90,510)
    glVertex2f(101,508)
    glVertex2f(112,500)
    glVertex2f(117.5,492)
    glVertex2f(120,480)
    glVertex2f(118.5,470)
    glVertex2f(112.5,460)
    glVertex2f(100.5,452)
    glVertex2f(90,450)
    glVertex2f(79.5,452)
    glVertex2f(68,460)
    glVertex2f(61.5,470)
    glVertex2f(60,480)
    glVertex2f(62.5,492)
    glVertex2f(67.5,500)
    glVertex2f(79,508)
    glVertex2f(90,510)
    glEnd()
    glPopMatrix()

    # awan 1
    glPushMatrix()
    glTranslated(350,0,0)
    glTranslated(geser_awanKn,-100,0)
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(130,510)
    glVertex2f(141,508)
    glVertex2f(152,500)
    glVertex2f(157.5,492)
    glVertex2f(160,480)
    glVertex2f(158.5,470)
    glVertex2f(152.5,460)
    glVertex2f(140.5,452)
    glVertex2f(130,450)
    glVertex2f(119.5,452)
    glVertex2f(108,460)
    glVertex2f(101.5,470)
    glVertex2f(100,480)
    glVertex2f(102.5,492)
    glVertex2f(107.5,500)
    glVertex2f(119,508)
    glVertex2f(130,510)
    glEnd()
    glPopMatrix()

    # awan 2
    glPushMatrix()
    glTranslated(350,0,0)
    glTranslated(geser_awanKn,0,0)
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(50,610)
    glVertex2f(61,608)
    glVertex2f(72,600)
    glVertex2f(77.5,592)
    glVertex2f(80,580)
    glVertex2f(78.5,570)
    glVertex2f(72.5,560)
    glVertex2f(60.5,552)
    glVertex2f(50,550)
    glVertex2f(39.5,552)
    glVertex2f(28,560)
    glVertex2f(21.5,570)
    glVertex2f(20,580)
    glVertex2f(22.5,592)
    glVertex2f(27.5,600)
    glVertex2f(39,608)
    glVertex2f(50,610)
    glEnd()
    glPopMatrix()

    # awan 2
    glPushMatrix()
    glTranslated(350,0,0)
    glTranslated(geser_awanKn,0,0)
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(90,610)
    glVertex2f(101,608)
    glVertex2f(112,600)
    glVertex2f(117.5,592)
    glVertex2f(120,580)
    glVertex2f(118.5,570)
    glVertex2f(112.5,560)
    glVertex2f(100.5,552)
    glVertex2f(90,550)
    glVertex2f(79.5,552)
    glVertex2f(68,560)
    glVertex2f(61.5,570)
    glVertex2f(60,580)
    glVertex2f(62.5,592)
    glVertex2f(67.5,600)
    glVertex2f(79,608)
    glVertex2f(90,610)
    glEnd()
    glPopMatrix()

    # awan 2
    glPushMatrix()
    glTranslated(350,0,0)
    glTranslated(geser_awanKn,0,0)
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(130,610)
    glVertex2f(141,608)
    glVertex2f(152,600)
    glVertex2f(157.5,592)
    glVertex2f(160,580)
    glVertex2f(158.5,570)
    glVertex2f(152.5,560)
    glVertex2f(140.5,552)
    glVertex2f(130,550)
    glVertex2f(119.5,552)
    glVertex2f(108,560)
    glVertex2f(101.5,570)
    glVertex2f(100,580)
    glVertex2f(102.5,592)
    glVertex2f(107.5,600)
    glVertex2f(119,608)
    glVertex2f(130,610)
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

def play():
    # kotak
    glBegin(GL_POLYGON)
    glColor3ub(255, 66, 66)
    glVertex2f(195,335)
    glVertex2f(197,345)
    glVertex2f(200,350)
    glVertex2f(205,352)
    glVertex2f(215,355)
    glVertex2f(285,355)
    glVertex2f(295,352)
    glVertex2f(300,350)
    glVertex2f(302,345)
    glVertex2f(305,335)
    glVertex2f(305,265)
    glVertex2f(302,255)
    glVertex2f(300,250)
    glVertex2f(295,248)
    glVertex2f(285,245)
    glVertex2f(215,245)
    glVertex2f(205,248)
    glVertex2f(200,250)
    glVertex2f(198,255)
    glVertex2f(195,265)
    glEnd()

    # segitiga
    glColor3ub(255, 244, 31)
    glBegin(GL_POLYGON)
    glVertex2f(220,340)
    glVertex2f(290,300)
    glVertex2f(220,260)
    glEnd()

def judul_game():
    # F
    glBegin(GL_QUADS)
    glColor3ub(8, 0, 255)
    glVertex2f(140,630)
    glVertex2f(140,540)
    glVertex2f(160,540)
    glVertex2f(160,630)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(160,570)
    glVertex2f(200,570)
    glVertex2f(195,595)
    glVertex2f(160,592)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(160,615)
    glVertex2f(195,610)
    glVertex2f(198,630)
    glVertex2f(160,630)
    glEnd()

    # U
    glBegin(GL_POLYGON)
    glColor3ub(245, 241, 0)
    glVertex2f(215,595)
    glVertex2f(220,555)
    glVertex2f(235,540)
    glVertex2f(235,563)
    glVertex2f(230,600)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(235,563)
    glVertex2f(235,540)
    glVertex2f(258,540)
    glVertex2f(258,560)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(256,602)
    glVertex2f(258,560)
    glVertex2f(258,541)
    glVertex2f(269,550)
    glVertex2f(273,600)
    glEnd()

    # n
    glBegin(GL_POLYGON)
    glColor3ub(247, 23, 255)
    glVertex2f(287,600)
    glVertex2f(283,543)
    glVertex2f(300,540)
    glVertex2f(302,573)
    glVertex2f(307,580)
    glVertex2f(312,583)
    glVertex2f(312,598)
    glVertex2f(300,595)
    glVertex2f(300,600)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(312,598)
    glVertex2f(320,600)
    glVertex2f(332,597)
    glVertex2f(328,578)
    glVertex2f(320,583)
    glVertex2f(312,583)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(332,597)
    glVertex2f(342,583)
    glVertex2f(340,540)
    glVertex2f(330,542)
    glVertex2f(332,573)
    glVertex2f(328,578)
    glEnd()

    # m
    glBegin(GL_POLYGON)
    glColor3ub(237, 0, 0)
    glVertex2f(255,513)
    glVertex2f(266,515)
    glVertex2f(267,512)
    glVertex2f(272,515)
    glVertex2f(277,515)
    glVertex2f(277,510)
    glVertex2f(271,508)
    glVertex2f(265,506)
    glVertex2f(265,480)
    glVertex2f(255,480)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(237, 0, 0)
    glVertex2f(277,515)
    glVertex2f(284,512)
    glVertex2f(287,505)
    glVertex2f(291,513)
    glVertex2f(297,514)
    glVertex2f(296,507)
    glVertex2f(291,504)
    glVertex2f(290,496)
    glVertex2f(290,480)
    glVertex2f(283,481)
    glVertex2f(283,499)
    glVertex2f(282,506)
    glVertex2f(277,510)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(237, 0, 0)
    glVertex2f(297,514)
    glVertex2f(304,514)
    glVertex2f(310,508)
    glVertex2f(310,504)
    glVertex2f(310,480)
    glVertex2f(304,480)
    glVertex2f(304,506)
    glVertex2f(296,507)
    glEnd()

    # a
    glBegin(GL_POLYGON)
    glColor3ub(237, 0, 0)
    glVertex2f(320,512)
    glVertex2f(328,512)
    glVertex2f(334,506)
    glVertex2f(334,500)
    glVertex2f(328,500)
    glVertex2f(328,504)
    glVertex2f(326,506)
    glVertex2f(320,506)
    glVertex2f(316,504)
    glVertex2f(314,508)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3ub(237, 0, 0)
    glVertex2f(320,500)
    glVertex2f(316,496)
    glVertex2f(316,484)
    glVertex2f(320,480)
    glVertex2f(328,480)
    glVertex2f(329,482)
    glVertex2f(330,480)
    glVertex2f(334,480)
    glVertex2f(334,500)
    glVertex2f(328,500)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(43, 202, 255)
    glVertex2f(320,494)
    glVertex2f(320,490)
    glVertex2f(320,486)
    glVertex2f(322,484)
    glVertex2f(328,484)
    glVertex2f(330,486)
    glVertex2f(330,496)
    glVertex2f(324,496)
    glEnd()

    # t
    glBegin(GL_POLYGON)
    glColor3ub(237, 0, 0)
    glVertex2f(350,506)
    glVertex2f(358,506)
    glVertex2f(358,512)
    glVertex2f(350,512)
    glVertex2f(350,520)
    glVertex2f(344,520)
    glVertex2f(344,512)
    glVertex2f(336,512)
    glVertex2f(336,506)
    glVertex2f(344,506)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(237, 0, 0)
    glVertex2f(344,506)
    glVertex2f(344,484)
    glVertex2f(350,486)
    glVertex2f(350,506)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(237, 0, 0)
    glVertex2f(344,484)
    glVertex2f(348,480)
    glVertex2f(356,480)
    glVertex2f(360,484)
    glVertex2f(362,488)
    glVertex2f(358,488)
    glVertex2f(356,484)
    glVertex2f(352,484)
    glVertex2f(350,486)
    glEnd()
    
    # h
    glBegin(GL_POLYGON)
    glColor3ub(237, 0, 0)
    glVertex2f(370,504)
    glVertex2f(370,520)
    glVertex2f(365,520)
    glVertex2f(365,480)
    glVertex2f(370,480)
    glVertex2f(370,496)
    glVertex2f(372,500)
    glVertex2f(374,502)
    glVertex2f(374,508)
    glVertex2f(372,506)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(384,506)
    glVertex2f(380,508)
    glVertex2f(374,508)
    glVertex2f(374,502)
    glVertex2f(380,502)
    glVertex2f(382,500)
    glVertex2f(384,496)
    glVertex2f(384,480)
    glVertex2f(389,480)
    glVertex2f(389,496)
    glVertex2f(388,500)
    glVertex2f(386,504)
    glEnd()

# Background game 1
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

# Background game capit
def lapangan():
    # bg
    glColor3ub(69, 138, 247)
    glBegin(GL_QUADS)
    glVertex2f(0,0)
    glVertex2f(500,0)
    glVertex2f(500,700)
    glVertex2f(0, 700)
    glEnd()

    # score
    glColor3ub(48, 48, 45)
    glBegin(GL_QUADS)
    glVertex2f(0,660)
    glVertex2f(100,660)
    glVertex2f(100,630)
    glVertex2f(0,630)
    glEnd()

    glColor3ub(48, 48, 45)
    glBegin(GL_QUADS)
    glVertex2f(0,620)
    glVertex2f(80,620)
    glVertex2f(80,590)
    glVertex2f(0,590)
    glEnd()

    # lantai
    glColor3ub(242, 197, 131)
    glBegin(GL_QUADS)
    glVertex2f(0,0)
    glVertex2f(0,150)
    glVertex2f(500,150)
    glVertex2f(500,0)
    glEnd()

    # garis tepi merah
    glColor3ub(171, 14, 37)
    glLineWidth(15)
    glBegin(GL_LINE_LOOP)
    glVertex2f(50,150)
    glVertex2f(60,110)
    glVertex2f(70,100)
    glVertex2f(100,80)
    glVertex2f(130,70)
    glVertex2f(160,60)
    glVertex2f(190,50)
    glVertex2f(220,45)
    glVertex2f(280,45)
    glVertex2f(310,50)
    glVertex2f(340,60)
    glVertex2f(370,70)
    glVertex2f(400,80)
    glVertex2f(430,100)
    glVertex2f(440,110)
    glVertex2f(450,150)
    glEnd()

    # kayu
    glColor3ub(150, 80, 5)
    glBegin(GL_QUADS)
    glVertex2f(0,350)
    glVertex2f(0,150)
    glVertex2f(500,150)
    glVertex2f(500,350)
    glEnd()

    # papan
    glColor3ub(201, 125, 42)
    glBegin(GL_QUADS)
    glVertex2f(5,345)
    glVertex2f(35,345)
    glVertex2f(35,155)
    glVertex2f(5,155)
    glEnd()

    # papan 2
    glColor3ub(201, 125, 42)
    glBegin(GL_QUADS)
    glVertex2f(5,345)
    glVertex2f(35,345)
    glVertex2f(35,155)
    glVertex2f(5,155)
    glEnd()

    # papan 3
    glColor3ub(201, 125, 42)
    glBegin(GL_QUADS)
    glVertex2f(45,345)
    glVertex2f(75,345)
    glVertex2f(75,155)
    glVertex2f(45,155)
    glEnd()

    # papan 4
    glColor3ub(201, 125, 42)
    glBegin(GL_QUADS)
    glVertex2f(85,345)
    glVertex2f(115,345)
    glVertex2f(115,155)
    glVertex2f(85,155)
    glEnd()

    # papan 5
    glColor3ub(201, 125, 42)
    glBegin(GL_QUADS)
    glVertex2f(125,345)
    glVertex2f(155,345)
    glVertex2f(155,155)
    glVertex2f(125,155)
    glEnd()

    # papan 6
    glColor3ub(201, 125, 42)
    glBegin(GL_QUADS)
    glVertex2f(165,345)
    glVertex2f(195,345)
    glVertex2f(195,155)
    glVertex2f(165,155)
    glEnd()

    # papan 7
    glColor3ub(201, 125, 42)
    glBegin(GL_QUADS)
    glVertex2f(205,345)
    glVertex2f(235,345)
    glVertex2f(235,155)
    glVertex2f(205,155)
    glEnd()

    # papan 8
    glColor3ub(201, 125, 42)
    glBegin(GL_QUADS)
    glVertex2f(245,345)
    glVertex2f(275,345)
    glVertex2f(275,155)
    glVertex2f(245,155)
    glEnd()

    # papan 9
    glColor3ub(201, 125, 42)
    glBegin(GL_QUADS)
    glVertex2f(285,345)
    glVertex2f(315,345)
    glVertex2f(315,155)
    glVertex2f(285,155)
    glEnd()

    # papan 10
    glColor3ub(201, 125, 42)
    glBegin(GL_QUADS)
    glVertex2f(325,345)
    glVertex2f(355,345)
    glVertex2f(355,155)
    glVertex2f(325,155)
    glEnd()

    # papan 11
    glColor3ub(201, 125, 42)
    glBegin(GL_QUADS)
    glVertex2f(365,345)
    glVertex2f(395,345)
    glVertex2f(395,155)
    glVertex2f(365,155)
    glEnd()

    # papan 12
    glColor3ub(201, 125, 42)
    glBegin(GL_QUADS)
    glVertex2f(405,345)
    glVertex2f(435,345)
    glVertex2f(435,155)
    glVertex2f(405,155)
    glEnd()

    # papan 13
    glColor3ub(201, 125, 42)
    glBegin(GL_QUADS)
    glVertex2f(445,345)
    glVertex2f(475,345)
    glVertex2f(475,155)
    glVertex2f(445,155)
    glEnd()

    # papan 14
    glColor3ub(201, 125, 42)
    glBegin(GL_QUADS)
    glVertex2f(485,345)
    glVertex2f(500,345)
    glVertex2f(500,155)
    glVertex2f(485,155)
    glEnd()

    # kotak basket
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(50,150)
    glVertex2f(60,110)
    glVertex2f(70,100)
    glVertex2f(100,80)
    glVertex2f(130,70)
    glVertex2f(160,60)
    glVertex2f(190,50)
    glVertex2f(220,45)
    glVertex2f(280,45)
    glVertex2f(310,50)
    glVertex2f(340,60)
    glVertex2f(370,70)
    glVertex2f(400,80)
    glVertex2f(430,100)
    glVertex2f(440,110)
    glVertex2f(450,150)
    glEnd()

def box():
    glPushMatrix()
    glTranslated(geser_box2,geser_box,0)
    glColor3ub(171, 14, 37)
    glBegin(GL_QUADS)
    glVertex2f(200,550)
    glVertex2f(200,450)
    glVertex2f(300,450)
    glVertex2f(300,550)
    glEnd()
    glPopMatrix()

    # garis silang
    glPushMatrix()
    glTranslated(geser_box2,geser_box,0)
    glColor3ub(0,0,0)
    glBegin(GL_QUADS)
    glVertex2f(200,550)
    glVertex2f(200,540)
    glVertex2f(290,450)
    glVertex2f(300,450)
    glVertex2f(300,460)
    glVertex2f(210,550)
    glEnd()
    glPopMatrix()

    # garis silang 2
    glPushMatrix()
    glTranslated(geser_box2,geser_box,0)
    glColor3ub(0,0,0)
    glBegin(GL_QUADS)
    glVertex2f(300,550)
    glVertex2f(300,540)
    glVertex2f(210,450)
    glVertex2f(200,450)
    glVertex2f(200,460)
    glVertex2f(290,550)
    glEnd()
    glPopMatrix()

def box2():
    glPushMatrix()
    glTranslated(geser_box3,geser_box5,0)
    glColor3ub(16, 31, 232)
    glBegin(GL_QUADS)
    glVertex2f(200,550)
    glVertex2f(200,450)
    glVertex2f(300,450)
    glVertex2f(300,550)
    glEnd()
    glPopMatrix()

    # garis silang
    glPushMatrix()
    glTranslated(geser_box3,geser_box5,0)
    glColor3ub(0,0,0)
    glBegin(GL_QUADS)
    glVertex2f(200,550)
    glVertex2f(200,540)
    glVertex2f(290,450)
    glVertex2f(300,450)
    glVertex2f(300,460)
    glVertex2f(210,550)
    glEnd()
    glPopMatrix()

    # garis silang 2
    glPushMatrix()
    glTranslated(geser_box3,geser_box5,0)
    glColor3ub(0,0,0)
    glBegin(GL_QUADS)
    glVertex2f(300,550)
    glVertex2f(300,540)
    glVertex2f(210,450)
    glVertex2f(200,450)
    glVertex2f(200,460)
    glVertex2f(290,550)
    glEnd()
    glPopMatrix()

def box3():
    glPushMatrix()
    glTranslated(geser_box4,geser_box6,0)
    glColor3ub(231, 15, 242)
    glBegin(GL_QUADS)
    glVertex2f(200,550)
    glVertex2f(200,450)
    glVertex2f(300,450)
    glVertex2f(300,550)
    glEnd()
    glPopMatrix()

    # garis silang
    glPushMatrix()
    glTranslated(geser_box4,geser_box6,0)
    glColor3ub(0,0,0)
    glBegin(GL_QUADS)
    glVertex2f(200,550)
    glVertex2f(200,540)
    glVertex2f(290,450)
    glVertex2f(300,450)
    glVertex2f(300,460)
    glVertex2f(210,550)
    glEnd()
    glPopMatrix()

    # garis silang 2
    glPushMatrix()
    glTranslated(geser_box4,geser_box6,0)
    glColor3ub(0,0,0)
    glBegin(GL_QUADS)
    glVertex2f(300,550)
    glVertex2f(300,540)
    glVertex2f(210,450)
    glVertex2f(200,450)
    glVertex2f(200,460)
    glVertex2f(290,550)
    glEnd()
    glPopMatrix()

def capit():
    global geser_capit
    # atas
    glPushMatrix()
    glTranslated(geser_capit,0,0)
    glColor3ub(252, 207, 3)
    glBegin(GL_QUADS)
    glVertex2f(230,700)
    glVertex2f(230,650)
    glVertex2f(270,650)
    glVertex2f(270,700)
    glEnd()
    glPopMatrix()

    # kiri
    glPushMatrix()
    glTranslated(geser_capit,0,0)
    glColor3ub(252, 207, 3)
    glBegin(GL_POLYGON)
    glVertex2f(230,650)
    glVertex2f(180,600)
    glVertex2f(200,550)
    glVertex2f(220,560)
    glVertex2f(200,600)
    glVertex2f(250,620)
    glVertex2f(250,650)
    glEnd()
    glPopMatrix()

    # kanan
    glPushMatrix()
    glTranslated(geser_capit,0,0)
    glColor3ub(252, 207, 3)
    glBegin(GL_POLYGON)
    glVertex2f(270,650)
    glVertex2f(320,600)
    glVertex2f(300,550)
    glVertex2f(280,560)
    glVertex2f(300,600)
    glVertex2f(250,620)
    glVertex2f(250,650)
    glEnd()
    glPopMatrix()

# Background pilihan level game berhitung
def bg_lvl():
    # bg
    glColor3ub(255, 219, 140)
    glBegin(GL_QUADS)
    glVertex2f(0,0)
    glVertex2f(500,0)
    glVertex2f(500,700)
    glVertex2f(0, 700)
    glEnd()

    # tulisan lvl
    # L
    glColor3ub(240, 36, 36)
    glBegin(GL_QUADS)
    glVertex2f(130,660)
    glVertex2f(110,660)
    glVertex2f(110,620)
    glVertex2f(130,620)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(110,600)
    glVertex2f(150,600)
    glVertex2f(150,620)
    glVertex2f(110,620)
    glEnd()

    # E
    glBegin(GL_QUADS)
    glVertex2f(160,660)
    glVertex2f(160,600)
    glVertex2f(180,600)
    glVertex2f(180,660)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(180,660)
    glVertex2f(180,650)
    glVertex2f(200,650)
    glVertex2f(200,660)
    glEnd()

    glPushMatrix()
    glTranslated(0,-25,0)
    glBegin(GL_QUADS)
    glVertex2f(180,660)
    glVertex2f(180,650)
    glVertex2f(200,650)
    glVertex2f(200,660)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslated(0,-50,0)
    glBegin(GL_QUADS)
    glVertex2f(180,660)
    glVertex2f(180,650)
    glVertex2f(200,650)
    glVertex2f(200,660)
    glEnd()
    glPopMatrix()

    # V
    glBegin(GL_POLYGON)
    glVertex2f(230,660)
    glVertex2f(210,660)
    glVertex2f(240,600)
    glVertex2f(250,600)
    glVertex2f(250,620)
    glVertex2f(245,620)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(270,660)
    glVertex2f(290,660)
    glVertex2f(260,600)
    glVertex2f(250,600)
    glVertex2f(250,620)
    glVertex2f(255,620)
    glEnd()

    # E
    glPushMatrix()
    glTranslated(140,0,0)
    glBegin(GL_QUADS)
    glVertex2f(160,660)
    glVertex2f(160,600)
    glVertex2f(180,600)
    glVertex2f(180,660)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslated(140,0,0)
    glBegin(GL_QUADS)
    glVertex2f(180,660)
    glVertex2f(180,650)
    glVertex2f(200,650)
    glVertex2f(200,660)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslated(140,-25,0)
    glBegin(GL_QUADS)
    glVertex2f(180,660)
    glVertex2f(180,650)
    glVertex2f(200,650)
    glVertex2f(200,660)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslated(140,-50,0)
    glBegin(GL_QUADS)
    glVertex2f(180,660)
    glVertex2f(180,650)
    glVertex2f(200,650)
    glVertex2f(200,660)
    glEnd()
    glPopMatrix()

    # L
    glPushMatrix()
    glTranslated(250,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(130,660)
    glVertex2f(110,660)
    glVertex2f(110,620)
    glVertex2f(130,620)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslated(250,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(110,600)
    glVertex2f(150,600)
    glVertex2f(150,620)
    glVertex2f(110,620)
    glEnd()
    glPopMatrix()

def kotak_lvl() :
    # lvl 1
    glPushMatrix()
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(60,500)
    glVertex2f(20,460)
    glVertex2f(20,340)
    glVertex2f(60,300)
    glVertex2f(200,300)
    glVertex2f(240,340)
    glVertex2f(240,460)
    glVertex2f(200,500)
    glEnd()
    glPopMatrix()

    # lvl 2
    glPushMatrix()
    glTranslated(240,0,0)
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(60,500)
    glVertex2f(20,460)
    glVertex2f(20,340)
    glVertex2f(60,300)
    glVertex2f(200,300)
    glVertex2f(240,340)
    glVertex2f(240,460)
    glVertex2f(200,500)
    glEnd()
    glPopMatrix()

    # lvl 3
    glPushMatrix()
    glTranslated(0,-250,0)
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(60,500)
    glVertex2f(20,460)
    glVertex2f(20,340)
    glVertex2f(60,300)
    glVertex2f(200,300)
    glVertex2f(240,340)
    glVertex2f(240,460)
    glVertex2f(200,500)
    glEnd()
    glPopMatrix()

    # comingsoon
    glPushMatrix()
    glTranslated(240,-250,0)
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(60,500)
    glVertex2f(20,460)
    glVertex2f(20,340)
    glVertex2f(60,300)
    glVertex2f(200,300)
    glVertex2f(240,340)
    glVertex2f(240,460)
    glVertex2f(200,500)
    glEnd()
    glPopMatrix()

# Background pilih game berhitung dan game capit
def pilih_game():
    # langit 
    glBegin(GL_QUADS)
    glColor3ub(166, 233, 255)
    glVertex2f(0,190)
    glVertex2f(500,190)
    glColor3ub(43, 202, 255)
    glVertex2f(500,700)
    glVertex2f(0, 700)
    glEnd()

    # awan 1
    glPushMatrix()
    glTranslated(350,0,0)
    glTranslated(geser_awanKn,-100,0)
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(50,510)
    glVertex2f(61,508)
    glVertex2f(72,500)
    glVertex2f(77.5,492)
    glVertex2f(80,480)
    glVertex2f(78.5,470)
    glVertex2f(72.5,460)
    glVertex2f(60.5,452)
    glVertex2f(50,450)
    glVertex2f(39.5,452)
    glVertex2f(28,460)
    glVertex2f(21.5,470)
    glVertex2f(20,480)
    glVertex2f(22.5,492)
    glVertex2f(27.5,500)
    glVertex2f(39,508)
    glVertex2f(50,510)
    glEnd()
    glPopMatrix()

    # awan 1
    glPushMatrix()
    glTranslated(350,0,0)
    glTranslated(geser_awanKn,-100,0)
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(90,510)
    glVertex2f(101,508)
    glVertex2f(112,500)
    glVertex2f(117.5,492)
    glVertex2f(120,480)
    glVertex2f(118.5,470)
    glVertex2f(112.5,460)
    glVertex2f(100.5,452)
    glVertex2f(90,450)
    glVertex2f(79.5,452)
    glVertex2f(68,460)
    glVertex2f(61.5,470)
    glVertex2f(60,480)
    glVertex2f(62.5,492)
    glVertex2f(67.5,500)
    glVertex2f(79,508)
    glVertex2f(90,510)
    glEnd()
    glPopMatrix()

    # awan 1
    glPushMatrix()
    glTranslated(350,0,0)
    glTranslated(geser_awanKn,-100,0)
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(130,510)
    glVertex2f(141,508)
    glVertex2f(152,500)
    glVertex2f(157.5,492)
    glVertex2f(160,480)
    glVertex2f(158.5,470)
    glVertex2f(152.5,460)
    glVertex2f(140.5,452)
    glVertex2f(130,450)
    glVertex2f(119.5,452)
    glVertex2f(108,460)
    glVertex2f(101.5,470)
    glVertex2f(100,480)
    glVertex2f(102.5,492)
    glVertex2f(107.5,500)
    glVertex2f(119,508)
    glVertex2f(130,510)
    glEnd()
    glPopMatrix()

    # awan 2
    glPushMatrix()
    glTranslated(350,0,0)
    glTranslated(geser_awanKn,0,0)
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(50,610)
    glVertex2f(61,608)
    glVertex2f(72,600)
    glVertex2f(77.5,592)
    glVertex2f(80,580)
    glVertex2f(78.5,570)
    glVertex2f(72.5,560)
    glVertex2f(60.5,552)
    glVertex2f(50,550)
    glVertex2f(39.5,552)
    glVertex2f(28,560)
    glVertex2f(21.5,570)
    glVertex2f(20,580)
    glVertex2f(22.5,592)
    glVertex2f(27.5,600)
    glVertex2f(39,608)
    glVertex2f(50,610)
    glEnd()
    glPopMatrix()

    # awan 2
    glPushMatrix()
    glTranslated(350,0,0)
    glTranslated(geser_awanKn,0,0)
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(90,610)
    glVertex2f(101,608)
    glVertex2f(112,600)
    glVertex2f(117.5,592)
    glVertex2f(120,580)
    glVertex2f(118.5,570)
    glVertex2f(112.5,560)
    glVertex2f(100.5,552)
    glVertex2f(90,550)
    glVertex2f(79.5,552)
    glVertex2f(68,560)
    glVertex2f(61.5,570)
    glVertex2f(60,580)
    glVertex2f(62.5,592)
    glVertex2f(67.5,600)
    glVertex2f(79,608)
    glVertex2f(90,610)
    glEnd()
    glPopMatrix()

    # awan 2
    glPushMatrix()
    glTranslated(350,0,0)
    glTranslated(geser_awanKn,0,0)
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(130,610)
    glVertex2f(141,608)
    glVertex2f(152,600)
    glVertex2f(157.5,592)
    glVertex2f(160,580)
    glVertex2f(158.5,570)
    glVertex2f(152.5,560)
    glVertex2f(140.5,552)
    glVertex2f(130,550)
    glVertex2f(119.5,552)
    glVertex2f(108,560)
    glVertex2f(101.5,570)
    glVertex2f(100,580)
    glVertex2f(102.5,592)
    glVertex2f(107.5,600)
    glVertex2f(119,608)
    glVertex2f(130,610)
    glEnd()
    glPopMatrix()

    # awan 3
    glPushMatrix()
    glTranslated(-50,0,0)
    glTranslated(geser_awanKr,0,0)
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(50,510)
    glVertex2f(61,508)
    glVertex2f(72,500)
    glVertex2f(77.5,492)
    glVertex2f(80,480)
    glVertex2f(78.5,470)
    glVertex2f(72.5,460)
    glVertex2f(60.5,452)
    glVertex2f(50,450)
    glVertex2f(39.5,452)
    glVertex2f(28,460)
    glVertex2f(21.5,470)
    glVertex2f(20,480)
    glVertex2f(22.5,492)
    glVertex2f(27.5,500)
    glVertex2f(39,508)
    glVertex2f(50,510)
    glEnd()
    glPopMatrix()

    # awan 3
    glPushMatrix()
    glTranslated(-50,0,0)
    glTranslated(geser_awanKr,0,0)
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(90,510)
    glVertex2f(101,508)
    glVertex2f(112,500)
    glVertex2f(117.5,492)
    glVertex2f(120,480)
    glVertex2f(118.5,470)
    glVertex2f(112.5,460)
    glVertex2f(100.5,452)
    glVertex2f(90,450)
    glVertex2f(79.5,452)
    glVertex2f(68,460)
    glVertex2f(61.5,470)
    glVertex2f(60,480)
    glVertex2f(62.5,492)
    glVertex2f(67.5,500)
    glVertex2f(79,508)
    glVertex2f(90,510)
    glEnd()
    glPopMatrix()

    # awan 3
    glPushMatrix()
    glTranslated(-50,0,0)
    glTranslated(geser_awanKr,0,0)
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(130,510)
    glVertex2f(141,508)
    glVertex2f(152,500)
    glVertex2f(157.5,492)
    glVertex2f(160,480)
    glVertex2f(158.5,470)
    glVertex2f(152.5,460)
    glVertex2f(140.5,452)
    glVertex2f(130,450)
    glVertex2f(119.5,452)
    glVertex2f(108,460)
    glVertex2f(101.5,470)
    glVertex2f(100,480)
    glVertex2f(102.5,492)
    glVertex2f(107.5,500)
    glVertex2f(119,508)
    glVertex2f(130,510)
    glEnd()
    glPopMatrix()

    # awan 4
    glPushMatrix()
    glTranslated(-50,0,0)
    glTranslated(geser_awanKr,-180,0)
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(50,510)
    glVertex2f(61,508)
    glVertex2f(72,500)
    glVertex2f(77.5,492)
    glVertex2f(80,480)
    glVertex2f(78.5,470)
    glVertex2f(72.5,460)
    glVertex2f(60.5,452)
    glVertex2f(50,450)
    glVertex2f(39.5,452)
    glVertex2f(28,460)
    glVertex2f(21.5,470)
    glVertex2f(20,480)
    glVertex2f(22.5,492)
    glVertex2f(27.5,500)
    glVertex2f(39,508)
    glVertex2f(50,510)
    glEnd()
    glPopMatrix()

    # awan 4
    glPushMatrix()
    glTranslated(-50,0,0)
    glTranslated(geser_awanKr,-180,0)
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(90,510)
    glVertex2f(101,508)
    glVertex2f(112,500)
    glVertex2f(117.5,492)
    glVertex2f(120,480)
    glVertex2f(118.5,470)
    glVertex2f(112.5,460)
    glVertex2f(100.5,452)
    glVertex2f(90,450)
    glVertex2f(79.5,452)
    glVertex2f(68,460)
    glVertex2f(61.5,470)
    glVertex2f(60,480)
    glVertex2f(62.5,492)
    glVertex2f(67.5,500)
    glVertex2f(79,508)
    glVertex2f(90,510)
    glEnd()
    glPopMatrix()

    # awan 4
    glPushMatrix()
    glTranslated(-50,0,0)
    glTranslated(geser_awanKr,-180,0)
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(130,510)
    glVertex2f(141,508)
    glVertex2f(152,500)
    glVertex2f(157.5,492)
    glVertex2f(160,480)
    glVertex2f(158.5,470)
    glVertex2f(152.5,460)
    glVertex2f(140.5,452)
    glVertex2f(130,450)
    glVertex2f(119.5,452)
    glVertex2f(108,460)
    glVertex2f(101.5,470)
    glVertex2f(100,480)
    glVertex2f(102.5,492)
    glVertex2f(107.5,500)
    glVertex2f(119,508)
    glVertex2f(130,510)
    glEnd()
    glPopMatrix()

    # awan 5
    glPushMatrix()
    glTranslated(-50,0,0)
    glTranslated(geser_awanKr,90,0)
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(50,610)
    glVertex2f(61,608)
    glVertex2f(72,600)
    glVertex2f(77.5,592)
    glVertex2f(80,580)
    glVertex2f(78.5,570)
    glVertex2f(72.5,560)
    glVertex2f(60.5,552)
    glVertex2f(50,550)
    glVertex2f(39.5,552)
    glVertex2f(28,560)
    glVertex2f(21.5,570)
    glVertex2f(20,580)
    glVertex2f(22.5,592)
    glVertex2f(27.5,600)
    glVertex2f(39,608)
    glVertex2f(50,610)
    glEnd()
    glPopMatrix()

    # awan 5
    glPushMatrix()
    glTranslated(-50,0,0)
    glTranslated(geser_awanKr,90,0)
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(90,610)
    glVertex2f(101,608)
    glVertex2f(112,600)
    glVertex2f(117.5,592)
    glVertex2f(120,580)
    glVertex2f(118.5,570)
    glVertex2f(112.5,560)
    glVertex2f(100.5,552)
    glVertex2f(90,550)
    glVertex2f(79.5,552)
    glVertex2f(68,560)
    glVertex2f(61.5,570)
    glVertex2f(60,580)
    glVertex2f(62.5,592)
    glVertex2f(67.5,600)
    glVertex2f(79,608)
    glVertex2f(90,610)
    glEnd()
    glPopMatrix()

    # awan 5
    glPushMatrix()
    glTranslated(-50,0,0)
    glTranslated(geser_awanKr,90,0)
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(130,610)
    glVertex2f(141,608)
    glVertex2f(152,600)
    glVertex2f(157.5,592)
    glVertex2f(160,580)
    glVertex2f(158.5,570)
    glVertex2f(152.5,560)
    glVertex2f(140.5,552)
    glVertex2f(130,550)
    glVertex2f(119.5,552)
    glVertex2f(108,560)
    glVertex2f(101.5,570)
    glVertex2f(100,580)
    glVertex2f(102.5,592)
    glVertex2f(107.5,600)
    glVertex2f(119,608)
    glVertex2f(130,610)
    glEnd()
    glPopMatrix()

    # rumput
    glColor3ub(10, 117, 0)
    glBegin(GL_POLYGON)
    glVertex2f(0,190)
    glVertex2f(120,200)
    glVertex2f(380,200)
    glVertex2f(500,190)
    glColor3ub(34, 173, 21)
    glVertex2f(500,0)
    glVertex2f(0,0)
    glEnd()

    # kotak game 1
    glColor3ub(255, 245, 179)
    glBegin(GL_POLYGON)
    glVertex2f(180,600)
    glVertex2f(140,560)
    glVertex2f(140,440)
    glVertex2f(180,400)
    glVertex2f(320,400)
    glVertex2f(360,440)
    glVertex2f(360,560)
    glVertex2f(320,600)
    glEnd()

    # +
    glColor3ub(29, 199, 14)
    glBegin(GL_QUADS)
    glVertex2f(180,580)
    glVertex2f(180,520)
    glVertex2f(200,520)
    glVertex2f(200,580)

    glColor3ub(29, 199, 14)
    glVertex2f(160,560)
    glVertex2f(160,540)
    glVertex2f(220,540)
    glVertex2f(220,560)

    # -
    glColor3ub(164, 14, 201)
    glVertex2f(270,560)
    glVertex2f(270,540)
    glVertex2f(330,540)
    glVertex2f(330,560)

    # -
    glColor3ub(201, 14, 14)
    glVertex2f(170,440)
    glVertex2f(170,460)
    glVertex2f(230,460)
    glVertex2f(230,440)

    # :
    glColor3ub(201, 14, 14)
    glVertex2f(190,470)
    glVertex2f(190,490)
    glVertex2f(210,490)
    glVertex2f(210,470)

    # x
    glColor3ub(255, 240, 36)
    glVertex2f(280,480)
    glVertex2f(270,470)
    glVertex2f(320,420)
    glVertex2f(330,430)

    glVertex2f(330,470)
    glVertex2f(320,480)
    glVertex2f(270,430)
    glVertex2f(280,420)
    glEnd()

    # :
    glPushMatrix()
    glTranslated(0,-60,0)
    glBegin(GL_QUADS)
    glColor3ub(201, 14, 14)
    glVertex2f(190,470)
    glVertex2f(190,490)
    glVertex2f(210,490)
    glVertex2f(210,470)
    glEnd()
    glPopMatrix()

    # kotak game 2
    glPushMatrix()
    glTranslated(0,-250,0)
    glColor3ub(255, 245, 179)
    glBegin(GL_POLYGON)
    glVertex2f(180,600)
    glVertex2f(140,560)
    glVertex2f(140,440)
    glVertex2f(180,400)
    glVertex2f(320,400)
    glVertex2f(360,440)
    glVertex2f(360,560)
    glVertex2f(320,600)
    glEnd()
    glPopMatrix()

    # capit
    # atas
    glPushMatrix()
    glTranslated(0,-350,0)
    glColor3ub(252, 207, 3)
    glBegin(GL_QUADS)
    glVertex2f(230,700)
    glVertex2f(230,650)
    glVertex2f(270,650)
    glVertex2f(270,700)
    glEnd()
    glPopMatrix()

    # kiri
    glPushMatrix()
    glTranslated(0,-350,0)
    glColor3ub(252, 207, 3)
    glBegin(GL_POLYGON)
    glVertex2f(230,650)
    glVertex2f(180,600)
    glVertex2f(200,550)
    glVertex2f(220,560)
    glVertex2f(200,600)
    glVertex2f(250,620)
    glVertex2f(250,650)
    glEnd()
    glPopMatrix()

    # kanan
    glPushMatrix()
    glTranslated(0,-350,0)
    glColor3ub(252, 207, 3)
    glBegin(GL_POLYGON)
    glVertex2f(270,650)
    glVertex2f(320,600)
    glVertex2f(300,550)
    glVertex2f(280,560)
    glVertex2f(300,600)
    glVertex2f(250,620)
    glVertex2f(250,650)
    glEnd()
    glPopMatrix()

# Background feedback 
def feedback():
    # bg
    glColor3ub(255, 219, 140)
    glBegin(GL_QUADS)
    glVertex2f(0,0)
    glVertex2f(500,0)
    glVertex2f(500,700)
    glVertex2f(0, 700)
    glEnd()

    # tombol kanan
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(310,130)
    glVertex2f(300,110)
    glVertex2f(300,70)
    glVertex2f(310,50)
    glVertex2f(450,50)
    glVertex2f(460,70)
    glVertex2f(460,110)
    glVertex2f(450,130)
    glEnd()

    # tombol kiri
    glPushMatrix()
    glTranslated(-260,0,0)
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(310,130)
    glVertex2f(300,110)
    glVertex2f(300,70)
    glVertex2f(310,50)
    glVertex2f(450,50)
    glVertex2f(460,70)
    glVertex2f(460,110)
    glVertex2f(450,130)
    glEnd()
    glPopMatrix()

def feedback2():
    # bg
    glColor3ub(255, 219, 140)
    glBegin(GL_QUADS)
    glVertex2f(0,0)
    glVertex2f(500,0)
    glVertex2f(500,700)
    glVertex2f(0, 700)
    glEnd()

    # tombol kanan
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(310,130)
    glVertex2f(300,110)
    glVertex2f(300,70)
    glVertex2f(310,50)
    glVertex2f(450,50)
    glVertex2f(460,70)
    glVertex2f(460,110)
    glVertex2f(450,130)
    glEnd()

    # tombol kiri
    glPushMatrix()
    glTranslated(-260,0,0)
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(310,130)
    glVertex2f(300,110)
    glVertex2f(300,70)
    glVertex2f(310,50)
    glVertex2f(450,50)
    glVertex2f(460,70)
    glVertex2f(460,110)
    glVertex2f(450,130)
    glEnd()
    glPopMatrix()

# input keyboard game capit
def keyboard (key,x,y) :
    # memanggil variabel global
    global geser_box2, geser_capit, jumlah_box,geser_box3,geser_box4,batasKn_merah,batasKn_biru,batasKn_pink,batasKr_merah
    global batasKr_biru,batasKr_pink
    # key untuk menggerakkan objek ke kanan
    if key == GLUT_KEY_RIGHT :
        # Kami menggunakan iterasi jumlah box untuk menggerakkan box merah, biru, dan pink. Selain itu kami juga menambahkan 
        # batas kanan dan kiri dari masing-masing box ketika key ditekan
        if jumlah_box == 0 :
            geser_box2 += 20
            geser_box3 += 20
            geser_box4 += 20
            batasKn_merah += 20
            batasKn_biru += 20
            batasKn_pink += 20
            batasKr_merah += 20
            batasKr_biru += 20
            batasKr_pink += 20
            geser_capit += 20
            print("Ke kanan ", "(", geser_box2, ",", 0, ")")
            print("Batas kanan","(", batasKn_merah, ",", 0, ")")
        # Ketika jumlah box berjumlah 1 maka yang dapat digerakkan hanya box biru, dan pink. Selain itu kami juga menambahkan 
        # batas kanan dan kiri dari masing-masing box ketika key ditekan
        elif jumlah_box == 1 :
            geser_box3 += 20
            geser_box4 += 20
            batasKn_biru += 20
            batasKn_pink += 20
            batasKr_biru += 20
            batasKr_pink += 20
            geser_capit += 20
            print("Ke kanan ", "(", geser_box3, ",", 0, ")")
            print("Batas kanan","(", batasKn_biru, ",", 0, ")")
        # Ketika jumlah box berjumlah 2 maka yang dapat digerakkan hanya box pink. Selain itu kami juga menambahkan 
        # batas kanan dan kiri dari box ketika key ditekan
        elif jumlah_box == 2 :
            geser_box4 += 20
            batasKn_pink += 20
            batasKr_pink += 20
            geser_capit += 20
            print("Ke kanan ", "(", geser_box4, ",", 0, ")")
            print("Batas kanan","(", batasKn_pink, ",", 0, ")")
        # Ketika semua box telah dijatuhkan yang bisa digerakkan hanya mesin capit itu sendiri
        else :
            geser_capit += 20
            print("Ke kanan ", "(", geser_box4, ",", 0, ")")
    # key untuk menggerakkan objek ke kiri
    if key == GLUT_KEY_LEFT :
        # Kami menggunakan iterasi jumlah box untuk menggerakkan box merah, biru, dan pink. Selain itu kami juga menambahkan 
        # batas kanan dan kiri dari masing-masing box ketika key ditekan
        if jumlah_box == 0 :
            geser_box2 -= 20
            geser_box3 -= 20
            geser_box4 -= 20
            batasKn_merah -= 20
            batasKn_biru -= 20
            batasKn_pink -= 20
            batasKr_merah -= 20
            batasKr_biru -= 20
            batasKr_pink -= 20
            geser_capit -= 20
            print("Ke kiri ", "(", geser_box2, ",", 0, ")")
            print("Batas kiri","(", batasKr_merah, ",", 0, ")")
        # Ketika jumlah box berjumlah 1 maka yang dapat digerakkan hanya box biru, dan pink. Selain itu kami juga menambahkan 
        # batas kanan dan kiri dari masing-masing box ketika key ditekan
        elif jumlah_box == 1 :
            geser_box3 -= 20
            geser_box4 -= 20
            batasKn_biru -= 20
            batasKn_pink -= 20
            batasKr_biru -= 20
            batasKr_pink -= 20
            geser_capit -= 20
            print("Ke kiri ", "(", geser_box3, ",", 0, ")")
            print("Batas kiri","(", batasKr_biru, ",", 0, ")")
        # Ketika jumlah box berjumlah 2 maka yang dapat digerakkan hanya box pink. Selain itu kami juga menambahkan 
        # batas kanan dan kiri dari box ketika key ditekan
        elif jumlah_box == 2 :
            geser_box4 -= 20
            batasKn_pink -= 20
            batasKr_pink -= 20
            geser_capit -= 20
            print("Ke kiri ", "(", geser_box4, ",", 0, ")")
            print("Batas kiri","(", batasKr_pink, ",", 0, ")")
        # Ketika semua box telah dijatuhkan yang bisa digerakkan hanya mesin capit itu sendiri
        else :
            geser_capit -= 20
            print("Ke kiri ", "(", geser_box4, ",", 0, ")")

# input mouse game
def mouse_awal(button, state, x, y):
    global scene, jumlah_box,geser_box, geser_box5,geser_box6
    # tombol play
    if scene == 0 :
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN :
            if (x >= 195 and x <= 305) and (y >= 345 and y <= 455) :
                scene = 1
            print("Klik Kiri ditekan ", "(", x, ",", y, ")")
    # tombol pilihan game berhitung dan game capit
    elif scene == 1 :
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN :
            if (x >= 140 and x <= 360) and (y >= 100 and y <= 300) :
                scene = 5
            elif (x >= 140 and x <= 360) and (y >= 350 and y <= 550) :
                scene = 3
            print("Klik Kiri ditekan ", "(", x, ",", y, ")")
    # tombol game 1 lvl 1
    elif scene == 2 :
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN :
            if (x >= 20 and x <= 180) and (y >= 560 and y <= 600) :
                print("Jawaban kamu salah")
            elif (x >= 20 and x <= 180) and (y >= 640 and y <= 680) :
                print("Jawaban kamu salah")
            elif (x >= 300 and x <= 480) and (y >= 560 and y <= 600) :
                scene = 4
            elif (x >= 300 and x <= 480) and (y >= 640 and y <= 680) :
                print("Jawaban kamu salah")
            print("Klik Kiri ditekan ", "(", x, ",", y, ")")
    # tombol game capit
    elif scene == 3 :
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN :
            if jumlah_box == 0 :
                timer_box(0)
            elif jumlah_box == 1 :
                timer_box2(0)
            elif jumlah_box == 2 :
                timer_box3(0)
            elif jumlah_box == 3 :
                geser_box = 0
                geser_box5 = 0
                geser_box6 = 0
                jumlah_box = 0
                scene = 4
            print("Klik Kiri ditekan ", "(", x, ",", y, ")")
    # tombol feedback game 1&2 WIN
    elif scene == 4 :
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN :
            if (x >= 310 and x <= 460) and (y >= 570 and y <= 650) :
                scene = 0
            elif (x >= 40 and x <= 200) and (y >= 570 and y <= 650) :
                scene = 1
            print("Klik Kiri ditekan ", "(", x, ",", y, ")")
    # tombol pilihan level
    elif scene == 5 :
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN :
            if (x >= 20 and x <= 240) and (y >= 200 and y <= 400) :
                scene = 2
            elif (x >= 260 and x <= 475) and (y >= 200 and y <= 400) :
                scene = 6
            if (x >= 20 and x <= 240) and (y >= 450 and y <= 650) :
                scene = 7
            print("Klik Kiri ditekan ", "(", x, ",", y, ")")
    # tombol game 1 lvl 2
    elif scene == 6 :
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN :
            if (x >= 20 and x <= 180) and (y >= 560 and y <= 600) :
                print("Jawaban kamu salah")
            elif (x >= 20 and x <= 180) and (y >= 640 and y <= 680) :
                scene = 4
            elif (x >= 300 and x <= 480) and (y >= 560 and y <= 600) :
                print("Jawaban kamu salah")
            elif (x >= 300 and x <= 480) and (y >= 640 and y <= 680) :
                print("Jawaban kamu salah")
            print("Klik Kiri ditekan ", "(", x, ",", y, ")")
    # tombol game 1 lvl 3
    elif scene == 7 :
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN :
            if (x >= 20 and x <= 180) and (y >= 560 and y <= 600) :
                print("Jawaban kamu salah")
            elif (x >= 20 and x <= 180) and (y >= 640 and y <= 680) :
                print("Jawaban kamu salah")
            elif (x >= 300 and x <= 480) and (y >= 560 and y <= 600) :
                print("Jawaban kamu salah")
            elif (x >= 300 and x <= 480) and (y >= 640 and y <= 680) :
                scene = 4
            print("Klik Kiri ditekan ", "(", x, ",", y, ")")
    # tombol feedback game 2 LOSE
    elif scene == 8 :
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN :
            if (x >= 310 and x <= 460) and (y >= 570 and y <= 650) :
                # jumlah_box = 0
                scene = 0
            elif (x >= 40 and x <= 200) and (y >= 570 and y <= 650) :
                # jumlah_box = 0
                scene = 1
            print("Klik Kiri ditekan ", "(", x, ",", y, ")")

# timer box game 2 dan awan
# timer box merah
def timer_box(value):
    global gerak_box,geser_box,batas_box,jumlah_box
    glutTimerFunc(50, timer_box,0)
    # jika batas box lebih dari sama dengan 0 maka nilai geser box dan batas box akan dikurangi sebesar nilai dari gerak box
    # kemudian nilai tersebut akan dikonversi dalam fungsi box dan variabel batas box
    if batas_box>=0 :
        geser_box -= gerak_box
        batas_box -= gerak_box
    # jika batas box kurang dari sama dengan 0 maka box akan berhenti dan jumlah box memiliki nilai 1
    if batas_box <=0 :
        jumlah_box = 1

# timer box biru
def timer_box2(value):
    global gerak_box,batas_box2,jumlah_box,geser_box5,batasKn_merah,batasKn_biru,batasKr_merah,batasKr_biru,scene
    glutTimerFunc(50, timer_box2,0)
    gerak_box = 10
    # jika jumlah box sama dengan 1 dan batas box lebih dari sama dengan 100 maka nilai geser box dan batas box akan dikurangi sebesar nilai dari gerak box
    # kemudian nilai tersebut akan dikonversi dalam fungsi box dan variabel batas box
    if jumlah_box == 1 and batas_box2 >=100:
        geser_box5 -= gerak_box
        batas_box2 -= gerak_box
    # jika batas box2 kurang dari sama dengan dan lebih dari sama dengan koordinat tersebut maka box akan berhenti jika memenuhi syarat dibawah
    if 95>=batas_box2<=100 :
        # jika batas kanan pada box biru lebih dari batas kiri box merah dan batas kiri box biru kurang dari batas kanan box merah
        # maka box akan berhenti dan jumlah box box memiliki nilai 2
        if batasKn_biru > batasKr_merah and batasKr_biru < batasKn_merah:
            jumlah_box = 2
        # jika tidak maka akan muncul feedback LOSE
        else :
            scene = 8
            
# timer box pink 
def timer_box3(value):
    global gerak_box,batas_box3,jumlah_box,geser_box6,batasKn_pink,batasKn_biru,batasKr_pink,batasKr_biru,scene
    glutTimerFunc(50, timer_box3,0)
    gerak_box = 10
    # jika jumlah box sama dengan 2 dan batas box lebih dari sama dengan 200 maka nilai geser box dan batas box akan dikurangi sebesar nilai dari gerak box
    # kemudian nilai tersebut akan dikonversi dalam fungsi box dan variabel batas box
    if jumlah_box == 2 and batas_box3 >= 200 :
        geser_box6 -= gerak_box
        batas_box3 -= gerak_box
    # jika batas box2 kurang dari sama dengan dan lebih dari sama dengan koordinat tersebut maka box akan berhenti jika memenuhi syarat dibawah
    if 195>=batas_box3<=200:
        # jika batas kanan pada box pink lebih dari batas kiri box biru dan batas kiri box pink kurang dari batas kanan box biru
        # maka box akan berhenti dan jumlah box box memiliki nilai 3
        if batasKn_pink > batasKr_biru and batasKr_pink < batasKn_biru:
            jumlah_box = 3
        # jika tidak maka akan muncul feedback LOSE
        else :
            scene = 8

# timer awan sisi kanan
def timer_awan_kanan(value):
    global gerakKn,geser_awanKn,batas_awan,gerak_awan
    glutTimerFunc(200, timer_awan_kanan,0)
    if gerak_awan == True:
        geser_awanKn += gerakKn
    else :
        batas_awan -= gerakKn
        geser_awanKn -= gerakKn

    if batas_awan == 600 or batas_awan == -200 :
        gerakKn = -gerakKn

# timer awan sisi kiri
def timer_awan_kiri(value):
    global gerakKr,geser_awanKr,batas_awan,gerak_awan
    glutTimerFunc(200, timer_awan_kiri,0)
    if gerak_awan == False:
        geser_awanKr += gerakKr
    else :
        batas_awan -= gerakKr
        geser_awanKr -= gerakKr

    if batas_awan == 600 or batas_awan == -200 :
        gerakKr = -gerakKr

# fungsi tulisan pada game 2 dan pilihan level game berhitung
def drawBitmapText(string,x,y,z) :
    global text
    if text == True :
        glRasterPos3f(x,y,z)
        for karakter in string :
            glColor3ub(0, 76, 207)
            glutBitmapCharacter(gl.GLUT_BITMAP_TIMES_ROMAN_24,ord(karakter))
    elif text == False :
        glRasterPos3f(x,y,z)
        for karakter in string :
            glColor3ub(255,255,255)
            glutBitmapCharacter(gl.GLUT_BITMAP_TIMES_ROMAN_24,ord(karakter))

# fungsi tulisan pada feedback
def drawBitmapText2(string,x,y,z):
    glRasterPos3f(x,y,z)
    for karakter in string :
        glColor3ub(0,0,0)
        glutBitmapCharacter(gl.GLUT_BITMAP_TIMES_ROMAN_24,ord(karakter))

# tulisan feedback
def text_fb():
    global scene
    # tulisan feedback pada game 1&2 WIN
    if scene == 4 :
        drawBitmapText2(" ", 300,100,0)
        drawBitmapText2("AWAL", 345,80,0)
        drawBitmapText2("MENU", 85,80,0)
        drawBitmapText2("CONGRATULATION!", 130,350,0)
        drawBitmapText2("YOU WIN!", 190,300,0)
    # tulisan feedback pada game 2 LOSE
    elif scene == 8 :
        drawBitmapText2(" ", 300,100,0)
        drawBitmapText2("AWAL", 345,80,0)
        drawBitmapText2("MENU", 85,80,0)
        drawBitmapText2("DON'T GIVE UP!", 163,350,0)
        drawBitmapText2("YOU CAN DO IT!", 160,300,0)
    # Tulisan pada game 1 lvl 1
    elif scene == 2 :
        drawBitmapText2(" ", 300,100,0)
        drawBitmapText2("SOAL LVL 1", 50,620,0)
        drawBitmapText2("4", 100,112,0)
        drawBitmapText2("2", 390,112,0)
        drawBitmapText2("8", 100,32,0)
        drawBitmapText2("6", 390,32,0)
    # tulisan pada game 2 lvl 2
    elif scene == 6 :
        drawBitmapText2(" ", 300,100,0)
        drawBitmapText2("SOAL LVL 2", 50,620,0)
        drawBitmapText2("4", 100,112,0)
        drawBitmapText2("2", 390,112,0)
        drawBitmapText2("8", 100,32,0)
        drawBitmapText2("6", 390,32,0)
    # tulisan pada game 3 lvl 3
    elif scene == 7 :
        drawBitmapText2(" ", 300,100,0)
        drawBitmapText2("SOAL LVL 3", 50,620,0)
        drawBitmapText2("4", 100,112,0)
        drawBitmapText2("12", 390,112,0)
        drawBitmapText2("8", 100,32,0)
        drawBitmapText2("3", 390,32,0)

# tulisan game 2 dan pilihan level game berhitung
def text_score():
    global text, jumlah_box,batas_box,batas_box2,batas_box3
    # tulisan skor pada game mesin capit
    if text == False :
        drawBitmapText(" " ,10,638,0)
        drawBitmapText("SCORE" ,10,638,0)
        if jumlah_box == 0 :
            drawBitmapText("0" ,10,597,0)
        elif jumlah_box == 1 :
            drawBitmapText("1" ,10,597,0)
        elif jumlah_box == 2 :
            drawBitmapText("2" ,10,597,0)
        elif jumlah_box == 3 :
            drawBitmapText("3" ,10,597,0)
    # tulisan pada pilihan level game 1
    elif text == True :
        drawBitmapText(" ",120,100,0)
        drawBitmapText("1" ,125,400,0)
        drawBitmapText("2",365,400,0)
        drawBitmapText("3",125,140,0)
        drawBitmapText("COMINGSOON",290,140,0)

# fungsi iterasi
def iterate():
    glViewport(0, 0, 500, 700)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Peletakan titik koordinat (0, 0) di pojok kiri bawah
    glOrtho(0.0, 500, 0.0, 700, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

# fungsi showscreen 
def pilihan():
    global scene, jumlah_box, text
    # fungsi untuk membersihkan layar
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # untuk mereset semua posisi grafik/bentuk
    glLoadIdentity()
    # fungsi looping
    iterate()
    # jika scene bernilai 0 maka akan kembali pada tampilan awal game
    if scene == 0 :
        # memanggil fungsi 
        bg()
        awan_kiri()
        awan_kanan()
        judul_game()
        sekolah()
        jarum_jam()
        play()
        glPushMatrix()
        pagar()
        glPopMatrix()
        glPushMatrix()
        glTranslated(360,0,0)
        pagar()
        glPopMatrix()
    # jika scene bernilai 1 maka akan masuk pada pilihan game pada Fun Math
    elif scene == 1 :
        # memanggil fungsi
        pilih_game()
    # jika scene bernilai 2 maka akan masuk pada permainan operasi matematika lvl 1
    elif scene == 2 :
        # memanggil fungsi
        game_lvl1()
        text_fb()
    # jika scene bernilai 3 maka akan masuk pada tampilan game mesin capit
    elif scene == 3 :
        # memanggil fungsi 
        text = False
        lapangan()
        text_score()
        capit()
        box3()
        box2()
        box()
    # jika scene bernilai 4 maka akan masuk pada feedback WIN
    elif scene == 4 :
        # memanggil fungsi 
        feedback()
        text_fb()
    # jika scene bernilai 5 maka akan masuk pada tampilan pilihan level pada game operasi matematika
    elif scene == 5 :
        # memanggil fungsi
        text = True 
        bg_lvl()
        kotak_lvl()
        text_score()
    # jika scene bernilai 6 maka akan masuk pada permainan operasi matematika lvl 2
    elif scene == 6 :
        # memanggil fungsi
        game_lvl2()
        text_fb()
    # jika scene bernilai 7 maka akan masuk pada permainan operasi matematika lvl 3
    elif scene == 7 :
        # memanggil fungsi
        game_lvl3()
        text_fb()
    # jika scene bernilai 8 maka akan masuk pada feedback LOSE
    elif scene == 8 :
        # memanggil fungsi
        feedback2()
        text_fb()
    # untuk membersihkan layar 
    glutSwapBuffers()

# fungsi windows
def display_game():
    global scene
    # inisialisasi glut 
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB) 
    # untuk mengatur ukuran layar/window (lebar(x), tinggi(y)) diagram cartesius
    glutInitWindowSize(500, 700)
    # untuk mengatur posisi layar/window (lebar(x), tinggi(y)) diagram cartesius
    glutInitWindowPosition(0, 0)
    # untuk memberi nama pada layar/window
    glutCreateWindow("FUN MATH")
    glutDisplayFunc(pilihan)
    timer_awan_kanan(0)
    timer_awan_kiri(0)
    # untuk memerintah openGL untuk selalu membuka dan menampilkan objek
    glutIdleFunc(pilihan)
    glutMouseFunc(mouse_awal)
    glutSpecialFunc(keyboard)
    # untuk memulai segalanya, untuk melooping objek terus menerus 
    glutMainLoop()

display_game()
