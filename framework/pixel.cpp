#include <pixel.h>
#include <definitions.h>
#include <main.h>

int Pixel::FindPixel(void){
    return this->_pos.x*4 + this->_pos.y*IMAGE_WIDTH*4;
}

void Pixel::PutPixel(void){
    int MemPos = this->FindPixel();
    FBptr[MemPos] = this->_R;
    FBptr[MemPos + 1] = this->_G;
    FBptr[MemPos + 2] = this->_B;
    FBptr[MemPos + 3] = this->_A;
}