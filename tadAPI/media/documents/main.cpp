#include<iostream>
//#include "student.h"


using namespace std;
class Body{
    protected:
    int x,y;
};
class Shape: public Body{

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
void Shape::setHeight(int h)
{
    height=h;
}
void Shape::setWidth(int w)
{
    width=w;
}

int Rectangle::getArea() {return width*height;}
int main()
{
   Rectangle Rec;
   int area;
   Rec.setHeight(3);
   Rec.setWidth(3);
   area= Rec.getArea();

    cout<<"Area of Rectangle is  "<<area<<endl;
   return 0;
}