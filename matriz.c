#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>

/*#define red[400]
#define dim 20
#define p 0.5*/

int rand(void);
float aleatorio(void);
int poblar(int *red, float p, int dim);
int imprimir(int *red, int dim);
/*int clasificar(int *red,int dim);
int etiqueta_falsa(int *red, int *historial, int s1 int s2, int i);
*/


int main(int argc,char *argv[]){
	int dim=20;
	int red[dim*dim];
	float p=0.5;
/*	sscanf(argv[1], "%d", & dim);
	sscanf(argv[2], "%f", & p); 
	red=(int*)malloc(dim*dim*sizeof(int)); */
	srand(time(NULL));
	poblar(red , p , dim);
	imprimir(red, dim);
	free(red);	
	return 0;
}





float aleatorio(void){
	float a;
	a=((float)rand())/((float)RAND_MAX);
	return a;
}


int poblar(int *red, float p, int dim){
	int i;
	for(i=0;i<dim*dim;i++){
		*(red+i)=0;
		if(aleatorio()<p){
			*(red+i)=1;		
		}	
	}
return 0;
}


/*
int clasificar(int *red,int dim){
	int i, s1, s2, *hitorial,frag;
	frag=1;

	for(i=0;i<dim*dim/2;i++){
		*(historial+i)=i;
	}

	for(i=0;i<dim;i++){
		if(*(red+i)==1 && *(red+i+dim)==0 && *(red+i+1)==0){
			*(ref+1)=*(historial+frag);
			frag++;
		}
		if(*(red+i)==1 &&)		
	}
}
*/


int imprimir(int *red, int dim){
	int i,j;
	for(i=0;i<dim;i++){
		for(j=0;j<dim;j++){
			printf("%d ",*(red+dim*i+j));	
		}	
	printf("\n");
	}
return 0;
}

