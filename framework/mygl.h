#ifndef _MYGL_H_
#define _MYGL_H_

#define _R 255
#define _G 255
#define _B 255
#define _A 255

#include "definitions.h"

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

void bresenham1(int x1, int y1, int x2, int y2){        
        int slope;
        int dx, dy, incE, incNE, d, x, y;
        // Onde inverte a linha x1 > x2       
        if (x1 > x2){
            bresenham1(x2, y2, x1, y1);
             return;
        }        
        dx = x2 - x1;
        dy = y2 - y1;
    
        if (dy < 0){            
            slope = -1;
            dy = -dy;
        }
        else{            
           slope = 1;
        }
        // Constante de Bresenham
        incE = 2 * dy;
        incNE = 2 * dy - 2 * dx;
        d = 2 * dy - dx;
        y = y1;       
        for (x = x1; x <= x2; x++){
            put_pixel(x, y);
            if (d <= 0){
              d += incE;
            }
            else{
              d += incNE;
              y += slope;
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
