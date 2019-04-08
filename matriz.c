#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>



int rand(void);
float aleatorio(void);
float powf(float x, float y);
int poblar(int *red, float p, int dim);
int imprimir(int *red, int dim);
int clasificar(int *red,int dim); 
int etiqueta_falsa(int *red, int dim, int *historial, int s1, int s2, int i);
int percola(int *red, int dim, int *etiqueta_percolante);
int masa(int *red, int dim,int *etiqueta_percolante, int *mass);
int dist_clusters(int *red, int dim, int *etiqueta_cluster, int *size_cluster);
int problema1a(FILE *fp, float presicion, int iteraciones);



int main(int argc,char *argv[]){
	int dim;
	float p;

	double total_time;
	clock_t start, end;
	start = clock();

	FILE *fp= fopen("pc", "w");
	sscanf(argv[1], "%d", & dim);
	sscanf(argv[2], "%f", & p);
	srand(time(NULL)); 


	problema1a(fp, pow(10,-5) , 270);            //problema1a  27k iteraciones



	end = clock();
	//time count stops 
	total_time = ((double) (end - start)) / CLOCKS_PER_SEC;
	//calulate total time
	printf("\nEl tiempo requerido es:  %f \n", total_time);
		

	fclose(fp);	
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


// FILE *fp;     para pasarlo como argumento a un afuncion hay que  pasarlos  como file *fp
// fp= fopen("nomblre", "w")   w de escritura

// fprintf(fp, "%f \n", pc);   pc es la variable que quiero guardar


// fclose(fp);

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

int percola(int *red, int dim,int *etiqueta_percolante){
	int perc, j, i,s;
	s=1;
	perc=0;
	for(i=0;i<dim;i++){                                                      //Este for se fija si percola abajo_arriba
		if(*(red+i)>s){
			s=*(red+i);
			for(j=0;j<dim;j++){
				if(*(red+dim*(dim-1)+j)==s){
					perc=1;
					*etiqueta_percolante=s;
				}
			}
		}
	}
return perc;
}



int masa(int *red, int dim,int *etiqueta_percolante, int *mass){
	int i,cuentomasa;
	cuentomasa=0;
	for(i=0;i<dim*dim;i++){
		if(*(red+i)==*etiqueta_percolante){
			cuentomasa++;		
		}
	}
*mass=cuentomasa;
return 0;	
}




int dist_clusters(int *red, int dim, int *etiqueta_cluster, int *size_cluster){
	int i, cuento_clusters, *auxiliar;
	auxiliar=(int*)malloc(dim*dim*sizeof(int));
	cuento_clusters=1;
	for(i=0;i<dim*dim; i++){
		*(auxiliar+i)=i;
	}
	
	for(i=0;i<dim*dim; i++){
		if(*(red+i)!=0){
			if(*(auxiliar+*(red+i))>0){
				*(auxiliar+*(red+i))=-cuento_clusters;
				*(red+i)=cuento_clusters;
				*(etiqueta_cluster+*(red+i))=cuento_clusters;
				*(size_cluster+*(red+i))=1;
				cuento_clusters++;
				
			}
			else{
				*(red+i)=-*(auxiliar+*(red+i));	
				*(size_cluster+*(red+i))=*(size_cluster+*(red+i))+1;
			}
		}
	}
free(auxiliar);
return cuento_clusters-1;
}


int problema1a(FILE *fp, float presicion, int iteraciones){
	int i, j, k, percola_flag, *red, dim, *etiqueta_percolante, *mass, *etiqueta_cluster, *size_cluster;
	float cota, p;
	cota=-log2(presicion);
	p=0.5;
	etiqueta_percolante=(int*)malloc(sizeof(int));
	mass=(int*)malloc(sizeof(int));
	for(k=0;k<5;k++){
		dim=pow(2,k+2);
		red=(int*)malloc(dim*dim*sizeof(int));
		size_cluster=(int*)malloc((dim*dim)*sizeof(int));
		etiqueta_cluster=(int*)malloc((dim*dim)*sizeof(int));
		for(j=0;j<iteraciones;j++){
			i=0;
			while(i<cota){
				poblar(red, p,  dim);
				clasificar(red, dim);
				percola_flag=percola(red, dim, etiqueta_percolante);
				masa(red, dim, etiqueta_percolante, mass);
				dist_clusters(red, dim, etiqueta_cluster, size_cluster);
/*				imprimir(red, dim);
				printf("Indice i:  ");
				printf("%d \n",i);
				printf("Indice j:  ");
				printf("%d \n",j);
				printf("Indice k:  ");
				printf("%d \n",k);
				if(percola_flag){
					printf("\n");
					printf("Percola con etiqueta:  ");
					printf("%d",*etiqueta_percolante);
					printf(" y masa :  ");
					printf("%d",*mass);
					printf("\n");	}
				else{printf("\n");
					printf("No Percola");
					printf("\n");}                 */
				if(percola_flag==1){
					p=p-pow(2.0,-i*1.0);
				}
				else{
					p=p+pow(2.0,-i*1.0);
				}
				i++;
			}
		
			fprintf(fp, "%d %f %f %d \n",dim, p, pow(p,2), *mass);  //En la primer fila imprime L y despues p, p**2 y masa
			 
		}
		free(red);
		free(etiqueta_cluster);
		free(size_cluster);
	}

free(mass);
free(etiqueta_percolante);
return 0;
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

