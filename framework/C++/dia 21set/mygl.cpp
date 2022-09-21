#include "definitions.h"
#include "mygl.h"

//-----------------------------------------------------------------------------
void MyGlDraw(void)
{
    //**
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
    
    glutKeyboardFunc(change_background);
    //***************************House polygons*******************************//
    house();
}