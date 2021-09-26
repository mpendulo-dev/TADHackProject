//#pragma once
#ifdef __STUDENT__
#define __STUDENT__
#include<iostream>

using namespace std;

class Shape{

protected:
      int height, width;
public:
    void setHeight(int);
    void setWidth(int);
};

class Rectangle: public Shape
{
    public:
        int getArea();
};
#endif