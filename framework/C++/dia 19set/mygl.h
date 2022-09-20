#ifndef _MYGL_H_
#define _MYGL_H_

#define _R 255
#define _G 255
#define _B 255
#define _A 255

#include "definitions.h"
#include <math.h>
using namespace std;

//-----------------------------------------------------------------------------
void MyGlDraw(void);

//*****************************************************************************
int find_pixel(int pos_x, int pos_y){
    return pos_x*4 + pos_y*IMAGE_WIDTH*4;
}

void put_pixel(int pos_x, int pos_y){
    int MemPos = find_pixel(pos_x, pos_y);
    FBptr[MemPos] = _R;
    FBptr[MemPos + 1] = _G;
    FBptr[MemPos + 2] = _B;
    FBptr[MemPos + 3] = _A;
}
 
// function for line generation
void bresenham1(int x1, int y1, int x2, int y2)
{
    int deltaY = y2 - y1;
    int deltaX = x2 - x1;

    if(x1 > x2 || y1 > y2){
        bresenham1(x2, y2, x1, y1);
        return;
    }
    if(deltaX == 0 && y1 <= y2){
        for (int i = y1; i <= y2; i++){
            put_pixel(x1, i);
        }
    }
    else if(deltaX == 0 && y1 > y2){
        for (int i = y2; i <= y1; i++){
            put_pixel(x1, i);
        }
    }
    else if(deltaY == 0){
        for (int i = x1; i <= x2; i++){
            put_pixel(i, y1);
        }
    }
    else{
        float coeficienteAngular = deltaY/deltaX;
        float coeficienteLinear = y1 - coeficienteAngular*float(x1);

        for (int i = x1; i <= x2; i++){
            int j = round(coeficienteAngular*float(i) + coeficienteLinear);
            put_pixel(i, j);
        }
    }
}

void triangle(int *ponto1, int *ponto2, int *ponto3){
    //cada ponto tera um x,y e se ligara ao outro

    bresenham1(ponto1[0], ponto1[1], ponto2[0], ponto2[1]);
    bresenham1(ponto2[0], ponto2[1], ponto3[0], ponto3[1]);
    bresenham1(ponto3[0], ponto3[1], ponto1[0], ponto1[1]);
}
//*****************************************************************************


#endif // _MYGL_H_
