#ifndef _MYGL_H_
#define _MYGL_H_

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
void draw_line(int x1, int y1, int x2, int y2)
{
    // desenha a linha encontrando a equacao da reta entre elas
    int deltaY = y2 - y1;
    int deltaX = x2 - x1;

    if(x1 > x2){
        draw_line(x2, y2, x1, y1);
        return;
    }

    // reta vertical
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
    // reta horizontal
    else if(deltaY == 0){
        for (int i = x1; i <= x2; i++){
            put_pixel(i, y1);
        }
    }
    // encontrando a equacao
    else{
        float coeficienteAngular = float(deltaY)/float(deltaX);
        float coeficienteLinear = y1 - coeficienteAngular*float(x1);
        //printf("[%.2f e %.2f]", coeficienteAngular, coeficienteLinear);
        for (int i = x1; i <= x2; i++){
            int j = coeficienteAngular*i + coeficienteLinear;
            //printf("%d e %d", i, j);
            put_pixel(i, j);
        }
    }
}

void draw_triangle(int *ponto1, int *ponto2, int *ponto3){
    //cada ponto tera um x,y e se ligara ao outro

    draw_line(ponto1[0], ponto1[1], ponto2[0], ponto2[1]);
    draw_line(ponto2[0], ponto2[1], ponto3[0], ponto3[1]);
    draw_line(ponto3[0], ponto3[1], ponto1[0], ponto1[1]);

}
//*****************************************************************************

void draw_rectangle(int *origem, int comprimento, int altura){

    draw_line(origem[0], origem[1], origem[0]+comprimento, origem[1]);
    draw_line(origem[0]+comprimento, origem[1], origem[0]+comprimento, origem[1]+altura);
    draw_line(origem[0]+comprimento, origem[1]+altura, origem[0], origem[1]+altura);
    draw_line(origem[0], origem[1]+altura, origem[0], origem[1]);
}

void change_background(unsigned char key, int x, int y){
    // background change if spacebar is pressed
    if (key == ' ')
    {
        puts("po");
        printf("%f", bcgR);
        bcgR = 1.0;
        bcgB = 0.7;
    }
}
#endif // _MYGL_H_
