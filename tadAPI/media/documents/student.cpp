#include "student.h"

#include <iostream>
using namespace std;

void Shape::setHeight(int h)
{
    height=h;
}
void Shape::setWidth(int w)
{
    width=w;
}

int Rectangle::getArea() {return width*height;}