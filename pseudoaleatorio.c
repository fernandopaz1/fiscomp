#include <stdio.h>
#include <math.h>

#define A 16807
#define M 2147483647
#define Q 127773
#define R 2836
#define S 260572
#define T 10000
#define B 10

float random(int *p);
void hist(float *f,float *h);


int main()
{
  int i,semilla=S;
  int *p=&semilla;
  float s=0.0,data[T],beams[B];
  float *f=&data[0],*h=&beams[0];

  for(i=0;i<T;i++) 
    {
      s=random(p);
      *(f+i)=s;
    }

  hist(f,h);
  for(i=0;i<B;i++) printf("%f\n",*(h+i));

  return 1;

}


float random(int *semilla)
{

/* 
     Devuelve un numero aleatorio entre 0.0 y 1.0
     a partir de una semilla dada. Se usa el metodo
     de Park y Miller
*/

int k;
float x;

k=(*semilla)/Q;
*semilla=A*(*semilla-k*Q)-R*k;
if (*semilla<0) *semilla+=M;

x=(*semilla)*(1.0/M);

return x;
} 

void hist(float *f,float *h)
{

  /* Esta funcion genera un histograma a partir de 
     'max' cantidad de datos. El histograma tiene 
     'beams' barras.
  */

  int i,k;
  float s=0.0;

  for (i=0;i<B;i++) *(h+i)=s;

  for(i=0;i<T;i++)
    {
      k=(int)((*f)*B);
      *(h+k)=(*(h+k))+(1.0/T);
      f++;
    }
}

