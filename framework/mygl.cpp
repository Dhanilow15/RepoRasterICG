#include "definitions.h"

//-----------------------------------------------------------------------------
void MyGlDraw(void)
{
    //*************************************************************************
    int ponto1[2], ponto2[2], ponto3[2];
    ponto1[0] = 100;
    ponto1[1] = 100;
    ponto2[0] = 200;
    ponto2[1] = 100;
    ponto3[0] = 150;
    ponto3[1] = 150;
    triangle(ponto1, ponto2, ponto3);
    
    ponto1[0] = 200;
    ponto1[1] = 200;
    ponto2[0] = 300;
    ponto2[1] = 200;
    ponto3[0] = 250;
    ponto3[1] = 250;
    triangle(ponto1, ponto2, ponto3);
    
    //************************************************************************* 

}