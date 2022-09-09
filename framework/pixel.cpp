#include <pixel.h>
#include <definitions.h>
#include <main.h>

int Pixel::FindPixel(void){
    return this->_pos.x*4 + this->_pos.y*IMAGE_WIDTH*4;
}

void Pixel::PutPixel(int _R, _G, _B, _A){
    int MemPos = this->FindPixel();
    FBptr[MemPos] = _R;
    FBptr[MemPos + 1] = _G;
    FBptr[MemPos + 2] = _B;
    FBptr[MemPos + 3] = _A;
}