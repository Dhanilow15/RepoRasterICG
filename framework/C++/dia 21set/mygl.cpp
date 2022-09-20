#include "definitions.h"
#include "mygl.h"

//-----------------------------------------------------------------------------
void MyGlDraw(void)
{
    //*************************************************************************
    int ponto1[2], ponto2[2], ponto3[2], ponto4[2], ponto5[2], ponto6[2];
    
    ponto1[0] = 125;
    ponto1[1] = 225;
    
    ponto2[0] = 225;
    ponto2[1] = 225;

    ponto3[0] = 175;
    ponto3[1] = 175;

    ponto4[0] = 125;
    ponto4[1] = 225;

    ponto5[0] = ponto4[0] + int(COMPRIMENTO/3);
    ponto5[1] = ponto4[1] + int(ALTURA);

    ponto6[0] = 260;
    ponto6[1] = 250;
    //225 350
    //250 325
    //275 300
    //***************************House polygons*******************************//
    //telhado frente
    draw_triangle(ponto1, ponto2, ponto3);
    //parede frente
    draw_rectangle(ponto4, COMPRIMENTO, ALTURA);
    //porta
    draw_rectangle(ponto5, int(COMPRIMENTO/3), -int(ALTURA/2));
    //telhado lateral
    draw_line(ponto3[0], ponto3[1], ponto3[0]+125, ponto3[1]);
    draw_line(ponto2[0], ponto2[1], ponto2[0]+125, ponto2[1]);
    draw_line(ponto3[0]+125, ponto3[1], ponto2[0]+125, ponto2[1]);
    //parede lateral
    draw_rectangle(ponto2, 125, ALTURA);
    //janela
    draw_rectangle(ponto6, 60, int(ALTURA/3));
    draw_line(ponto6[0]+30, ponto6[1], ponto6[0]+30, ponto6[1]+int(ALTURA/3));
    draw_line(ponto6[0], ponto6[1]+int(ALTURA/6), ponto6[0]+60, ponto6[1]+int(ALTURA/6));
    //************************************************************************* 

}