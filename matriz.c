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
int clasificar(int *red,int dim); /*
int caso2(int *red,int dim,int frag, int i);
int caso3(int *red,int dim, int *historial, int s1, int s2, int i);
int etiqueta_falsa(int *red, int dim, int *historial, int s1 int s2, int i);
*/


int main(int argc,char *argv[]){
	int dim, *red;
	float p;
	sscanf(argv[1], "%d", & dim);
	sscanf(argv[2], "%f", & p); 
	red=(int*)malloc(dim*dim*sizeof(int));
	srand(time(NULL));
	poblar(red , p , dim);
	clasificar(red, dim);
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

int caso2(int *red,int dim,int frag, int i){



return 0;
}
*/



/* 

int caso3(int *red,int dim, int *historial, int s1, int s2, int i){



return 0;
}
*/


/* 

int caso4(int *red,int dim, int *historial, int s1, int s2, int i){



return 0;
}
*/



int clasificar(int *red,int dim){
	int i, s1, *historial,frag;
	frag=2;
	historial=(int*)malloc(dim*dim*sizeof(int));
	for(i=0;i<dim*dim;i++){
		*(historial+i)=i;
	}	
	
	s1=(*red);
	
	if(s1){
		*red=frag;
		frag++;
		}
	
	
	for(i=1;i<dim;i++){                                //Caso 2 para la primer fila
		if(*(red+i)){
			if(s1){
				*(red+i)=*(red+i-1);				
			}
			else{
				*(red+i)=frag;
				frag++;
			}
		
		}
	s1=(*(red+i));

	}
free(historial);
return 0;
}
/*

	}
	for(i=dim;i<dim*dim;i++){
		if(i % dim !=0){
			if(*(red+i)==1 && *(red+i-1)==0 && *(red+i-dim)==0){
										If correspondiente al caso 2
							
			}
			if(*(red+i)==1 && ((*(red+i-1)==0 && *(red+i-dim)==1)) || (*(red+i-1)==1 && *(red+i-dim)==0))){   
				s1=*(red+i-1);			                                If correspondiente al caso 3 
				
			}

			if(*(red+i)==1 && *(red+i-1)!=0 && *(red+i-dim)!=0){
										If correspondiente al caso 4
							
			}
		}	
	}
return 0;
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

