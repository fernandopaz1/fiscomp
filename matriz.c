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
int clasificar(int *red,int dim); 
int etiqueta_falsa(int *red, int dim, int *historial, int s1, int s2, int i);

int percola(int *red, int dim);



int main(int argc,char *argv[]){
	int dim, *red,seed_flag,seed, percola_flag;
	float p;
	sscanf(argv[1], "%d", & dim);
	sscanf(argv[2], "%f", & p);
	sscanf(argv[3], "%d", & seed_flag);
	sscanf(argv[4], "%d", & seed);
	if(seed_flag==0){
		srand(time(NULL));
	}
	else{
		srand(seed);
	} 
	red=(int*)malloc(dim*dim*sizeof(int));
	poblar(red , p , dim);
	clasificar(red, dim);
	imprimir(red, dim);
	percola_flag=percola(red, dim);
	if(percola_flag){
		printf("\n");
		printf("Percola");
		printf("\n");
	}
	else{printf("\n");
		printf("No Percola");
		printf("\n");}
	free(red);	
	return percola_flag;
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





int etiqueta_falsa(int *red,int dim, int *historial, int s1, int s2, int i){
	int minimo, maximo;
	while(*(historial+s1)<0){
		s1=-(*(historial+s1));
	}
	while(*(historial+s2)<0){
		s2=-(*(historial+s2));
	}
	if(s1<s2){
		minimo=s1;
		maximo=s2;
	}
	else{
		minimo=s2;
		maximo=s1;
	}
	*(red+i)=minimo;
	*(historial+maximo)=-minimo;
	*(historial+minimo)=minimo;
return 0;
}




int clasificar(int *red,int dim){
	int i, s, s1, s2,*historial,frag;
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


	
	for(i=dim;i<dim*dim;i++){
	s1=(*(red+i-1));							//Etiqueta del casillero anterior
	s2=(*(red+i-dim));							//Etiqueta del casillero de arriba
		if(*(red+i)){
			if(i % dim !=0){
				if(s1==0){
					if(s2==0){
						*(red+i)=frag;
						frag++;	}				//If correspondiente al caso 2
					else{ *(red+i)=s2; }				//corresponde caso 3 s2 distinto de cero
								
				}
				else{
					if(s2==0)
						{*(red+i)=s1;}			   //correspondiente al caso 3 s1 distinto de cero
					else{
						etiqueta_falsa(red,dim,historial,s1,s2,i); 	//Caso 4
					}
				}

											
								
			
			}
			else{								//Analisis en la primer columna de la red percolante
				if(s2==0){
					*(red+i)=frag;
					frag++;						//correspondiente al caso2 en el borde 					
				}
				else {*(red+i)=s2;}					//Caso 3 en el borde
			}
		}
	}
	for(i=0;i<dim*dim;i++){
		s=*(red+i);
		while(*(historial+s)<0){
			s=-(*(historial+s));
		}
		*(red+i)=s;
	}
free(historial);
return 0;
}

int percola(int *red, int dim){
	int perc, j, i, s;
	s=1;
	perc=0;
	for(i=0;i<dim;i++){                                                      //Este for se fija si percola abajo_arriba
		if(*(red+i)>s){
			s=*(red+i);
			for(j=0;j<dim;j++){
				if(*(red+dim*(dim-1)+j)==s){
					perc=1;
				}
			}
		}
	}
/*	s=1;
	for(i=0;i<dim;i++){							//Este for se fija si percola derecha_izq
		if(*(red+dim*i)>s){
			s=*(red+dim*i);
			for(j=0;j<dim;j++){
				if(*(red+dim+dim*j)==s){
					perc=1;
				}
			}
		}
	}*/
return perc;
}

int imprimir(int *red, int dim){
	int i,j;
	for(i=0;i<dim;i++){
		for(j=0;j<dim;j++){
			if(*(red+dim*i+j)<10){printf("%d   ",*(red+dim*i+j));}
			else{printf("%d  ",*(red+dim*i+j));}
		}	
	printf("\n");
	}
return 0;
}

