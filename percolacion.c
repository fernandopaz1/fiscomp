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
//int dist_clusters(int *red, int dim, int *etiqueta_cluster, int *size_cluster);
int nss(int *red, int *ns,int dim);
int problema1a(float presicion, int iteraciones);
int problema1b(float paso , int iteraciones);
int problema2(float paso , int iteraciones);
int problema3(int l_min, int l_max , int iteraciones,int nro_ptos);
int problema4(float paso , int iteraciones,int dim);


int main(int argc,char *argv[]){
	int iteraciones;


	double total_time;
	clock_t start, end;
	start = clock();

	
	sscanf(argv[1], "%d", & iteraciones);
	srand(time(NULL)); 


//	problema1a(15 , iteraciones);            //problema1a  27k iteraciones
//	problema1b(0.05 , iteraciones);
	problema3(4, 200, iteraciones,100);
	problema2(0.01 , iteraciones);
//	problema4(0.00001 , iteraciones,128);

	end = clock();
	//time count stops 
	if(iteraciones<=300){
		total_time = ((double) ((end - start)) / CLOCKS_PER_SEC)/60;
		printf("\nEl tiempo (minutos) requerido es:  %f \n", total_time);
		total_time=total_time*100/60;
		printf("\nEl tiempo (horas) requerido es:  %f \n", total_time);	
		}
	else{
		total_time = ((double) (((end - start)) / CLOCKS_PER_SEC)/60)/60;	
		printf("\nEl tiempo (horas) requerido es:  %f \n", total_time);	
		
	}
	//calulate total time
	//printf("\nEl tiempo (minutos) requerido es:  %f \n", total_time);
		

	
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
	int j, i,s;
	s=1;
	*etiqueta_percolante=0;
	for(i=0;i<dim;i++){                                                      //Este for se fija si percola abajo_arriba
		if(*(red+i)>s){
			s=*(red+i);
			for(j=0;j<=dim;j++){
				if(*(red+dim*(dim-1)+j)==s){
					*etiqueta_percolante=s;
					return 1;
				}
			}
		}
	}
return 0;
}



int masa(int *red, int dim,int *etiqueta_percolante, int *mass){
	int i,cuentomasa;
	cuentomasa=1;
	if(*etiqueta_percolante!=0){
		for(i=0;i<dim*dim;i++){
			if(*(red+i)==*etiqueta_percolante){
				cuentomasa++;		
			}
		}		
	}
	else{
		cuentomasa=0;
	}
*mass=cuentomasa;
return 0;	
}





int nss(int *red, int *ns,int dim)
{

int i,j;
int *vec;

vec = (int *)malloc(dim*dim*sizeof(int));

for (i=0; i<dim*dim; i++) *(vec+i)=0;  //inicio vec en 0

for (i=0; i<dim*dim; i++)
    {
      j=(*(red+i));				//Guarda en j la etiqueta del fragmento
      (*(vec+j))++;  				//Cada vez que se encuentra con con la etiqueta j acumula en vect el tamaño del cluster
    }

for(i=0; i<dim*dim; i++)
    {
         j=(*(vec+i));			//recorre el vector y  asigna a j el tamaño del cluster
         (*(ns+j))++;			//
    }

*(ns+0)=0;

free(vec);

return 0;

}


int problema1a(float presicion, int iteraciones){
	int i, j, k, percola_flag, *red, dim, *etiqueta_percolante,*dimension;
	float p, dp;
	FILE *fp= fopen("pc", "w");
	etiqueta_percolante=(int*)malloc(sizeof(int));
	dimension=(int*)malloc(20*sizeof(int));
	
	
        
	for(k=0;k<10;k++){
		*(dimension+k)=4+k*(128-4)/10;
	}

	for(k=0;k<10;k++){
		*(dimension+k+10)=128+k*(512-128)/10;                      // division entera
	}
	
	for(k=0;k<20;k++){                                            //k va de 0 a 4   L va de 4 a 64 
		dim=*(dimension+k);
		red=(int*)malloc(dim*dim*sizeof(int));
		p=0.5;
		for(j=0;j<iteraciones;j++){
		//	*etiqueta_percolante=0;
			srand(time(NULL)); 
			i=0;
			dp=0.5*p;
			while(i<presicion){
				poblar(red, p,  dim);
				clasificar(red, dim);
				percola_flag=percola(red, dim, etiqueta_percolante);       
				if(percola_flag==1){
					p=p-dp;
				}
				else{
					p=p+dp;
				}
				i++;
				dp=0.5*dp;
			}
		
			fprintf(fp, "%d %f %f \n",dim, p, pow(p,2));  //En la primer fila imprime L y despues p, p**2 y masa
			 
		}
		free(red);
		
	}

free(etiqueta_percolante);
free(dimension);
fclose(fp);
return 0;
}



int problema1b(float paso , int iteraciones){
	int i,k, *red, dim, *etiqueta_percolante,*dimension;
	float p,acumulador;
	FILE *fpb= fopen("datos_1b", "w");
	dim=64;
	
	etiqueta_percolante=(int*)malloc(sizeof(int));
	dimension=(int*)malloc(5*sizeof(int));

        for(k=0;k<5;k++){
		*(dimension+k)=dim+k*(128-dim)/5;
	}
	p=0;
	
	while(p<1.0){
		fprintf(fpb, "%f",p);
		for(k=0;k<5;k++){
			dim=*(dimension+k);
			acumulador=0;
			red=(int*)malloc(dim*dim*sizeof(int));
			for(i=0;i<iteraciones;i++){
				//*etiqueta_percolante=0;
				poblar(red, p,  dim);
				clasificar(red, dim);
				acumulador=acumulador+percola(red, dim, etiqueta_percolante);
			}
			acumulador=acumulador/iteraciones;
			fprintf(fpb, " %f", acumulador);
			free(red);
		}
		fprintf(fpb, "\n");
		if(p>0.5 && p<0.65){p=p+0.01*paso;}
		else{p=p+paso;}
	}
	
fclose(fpb);	
free(dimension);
free(etiqueta_percolante);
return 0;
}


int problema2(float paso , int iteraciones){
	int i,k, *red, dim, *etiqueta_percolante,*dimension,*mass;
	float p, masa_prom;
	long long int masa_acum;
	FILE *fm= fopen("masa", "w");
	etiqueta_percolante=(int*)malloc(sizeof(int));
	dimension=(int*)malloc(10*sizeof(int));
	mass=(int*)malloc(sizeof(int));

        for(k=0;k<10;k++){
		*(dimension+k)=64+k*(128-64)/10;
	}

	for(k=0;k<10;k++){
		p=0;
		dim=*(dimension+k);
		red=(int*)malloc((dim*dim)*sizeof(int));
		while(p<1.0){
			i=0;	
			masa_acum=0;
			*mass=0;
			for(i=0;i<iteraciones;i++){
			//	*etiqueta_percolante=0;
				poblar(red, p,  dim);
				clasificar(red, dim);
				if(percola(red, dim, etiqueta_percolante)){
					masa(red, dim, etiqueta_percolante, mass);
					masa_acum=masa_acum+*mass;
				}
			}
			masa_prom= (1.0*masa_acum)/(1.0*iteraciones);
			fprintf(fm, "%d %f %f \n", dim, p, masa_prom);
			if(p>=0.55 && p<0.65){p=p+0.1*paso;}
			else{p=p+paso;}
			
		}
		free(red);
	}
free(dimension);
free(etiqueta_percolante);
free(mass);
fclose(fm);
return 0;
}


int problema3(int l_min, int l_max , int iteraciones,int nro_ptos){
	int i,j,k, *red, dim, *etiqueta_percolante,*mass,delta;
	float pc,p, masa_prom;
	long long int masa_acum;
	FILE *fm2= fopen("dim_fractal", "w");
	etiqueta_percolante=(int*)malloc(sizeof(int));
	mass=(int*)malloc(sizeof(int));
	
	pc=0.59256;
	delta=0.035;
	p=pc+delta;
	
	fprintf(fm2, "%d", 0);	
	i=0;
	while(i<5){
		p=pc+0.007;
		fprintf(fm2, " %f", p);
		i++;	
	}
        fprintf(fm2, "\n");
	
	for(k=0;k<nro_ptos;k++){
		dim=l_min+k*(l_max-l_min)/nro_ptos;
		red=(int*)malloc((dim*dim)*sizeof(int));
		j=0;
		fprintf(fm2, "%d", dim);
		while(j<5){                                         // Este while recorre las disitntas probabilidades
			i=0;
			*mass=0;
			masa_acum=0;
			while(i<iteraciones){
				poblar(red, p,  dim);
				clasificar(red, dim);
				if(percola(red, dim, etiqueta_percolante)){
					masa(red, dim, etiqueta_percolante, mass);
					masa_acum=masa_acum+*mass;
				}
				i++;
			}
			masa_prom= (1.0*masa_acum)/(1.0*iteraciones);
			fprintf(fm2, " %f", masa_prom);
			p=pc+0.007;
			j++;
		}
		fprintf(fm2, "\n");	
		free(red);	
	}
free(etiqueta_percolante);
free(mass);
fclose(fm2);
return 0;
}




int problema4(float paso , int iteraciones,int dim){
	int i,j, *red, *etiqueta_percolante,*etiqueta_cluster, *size_cluster, *ns;
	float p;	
	FILE *fs= fopen("distribucion_fragmentos", "w");
	
		
	
	red=(int*)malloc(dim*dim*sizeof(int));
	etiqueta_percolante=(int*)malloc(sizeof(int));
	size_cluster=(int*)malloc((dim*dim)*sizeof(int));
	etiqueta_cluster=(int*)malloc((dim*dim)*sizeof(int));
	ns  = (int *)malloc(dim*dim*sizeof(int));

	
	p=0.58;
	
	while(p<0.6){
		for(i=0;i<dim*dim;i++){*(ns+i)=0;}
		for(i=0;i<iteraciones;i++){
			*etiqueta_percolante=0;
			poblar(red, p,  dim);
			clasificar(red, dim);
			percola(red, dim, etiqueta_percolante);
			nss(red,ns,dim);
			
			
		}
		fprintf(fs, "%f",p);
		for(j=1;j<=dim*dim;j++){
			fprintf(fs, " %f",(1.0*(*(ns+j)))/(1.0*iteraciones));
		}
		fprintf(fs, "\n");
		
		p=p+paso;
	}
free(red);
free(etiqueta_cluster);
free(size_cluster);
free(etiqueta_percolante);
free(ns);
fclose(fs);
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

