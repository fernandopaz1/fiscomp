#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>

int rand(void);
float aleatorio(void);
int poblar(int *red, float p, int dim);
int imprimir(int *red, int dim);
/*int clasificar(int *red,int dim);*/


int main(int argc,char *argv[]){
	int dim, *red;
	float p;
	sscanf(argv[1], "%d", & dim);
	sscanf(argv[2], "%f", & p);
	red=(int*)malloc(dim*dim*sizeof(int));
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
		if(aleatorio()<p){
			*(red+i)=1;		
		}	
	}
return 0;
}


/*
int clasificar(int *red,int dim);

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

