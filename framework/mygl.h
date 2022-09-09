#ifndef _MYGL_H_
#define _MYGL_H_

#include "definitions.h"

//-----------------------------------------------------------------------------
void MyGlDraw(void);

//*****************************************************************************
int FindPixel(int pos_x, int pos_y){
    return pos_x*4 + pos_y*IMAGE_WIDTH*4;
}

void PutPixel(int pos_x, int pos_y, int _R, int _G, int _B, int _A){
    int MemPos = FindPixel(pos_x, pos_y);
    FBptr[MemPos] = _R;
    FBptr[MemPos + 1] = _G;
    FBptr[MemPos + 2] = _B;
    FBptr[MemPos + 3] = _A;
}
//*****************************************************************************


#endif // _MYGL_H_
