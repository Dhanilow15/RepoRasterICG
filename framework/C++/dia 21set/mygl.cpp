#include "definitions.h"
#include "mygl.h"

//-----------------------------------------------------------------------------
void MyGlDraw(void)
{
    //*************************************************************************
    int ponto1[2], ponto2[2], ponto3[2], ponto4[2];
    ponto1[0] = 125;
    ponto1[1] = 225;
    ponto2[0] = 225;
    ponto2[1] = 225;
    ponto3[0] = 175;
    ponto3[1] = 150;
    ponto4[0] = 125;
    ponto4[1] = 225;
    //House polygons
    draw_triangle(ponto1, ponto2, ponto3);
    //draw_line(225, 225, 175, 150);
    //draw_rectangle(ponto4, 100, 100);
    //************************************************************************* 

}