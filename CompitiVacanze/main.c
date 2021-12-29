#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define DIM 3
//commento prova
int chiediDim(int max) {
    int dim;

    do {
        printf("inserisci la dimensione: ");
        scanf("%d",&dim);
    } while((dim<0)||(dim>max));
    return dim;
}
//commento prova
void caricaMat(int mat[][DIM],int nr,int nc) {

    for(int r=0; r<nr; r++) {

        for(int c=0; c<nc; c++) {

            printf("inserisci l'elemento: ");
            scanf("%d",&mat[r][c]);
        }
    }
}

/*
int sommaDiagPrinc(int mat[][DIM],int dim) {
    int somma=0;
    for(int r=0; r<dim; r++) {
        somma+= mat[r][r];
    }
    return somma;
}
*/
int sommaDiagSec(int mat[][DIM],int dim) {
    int somma=0;
    for(int r=0; r<dim; r++) {
        somma+= mat[r][dim-r];
    }
    return somma;
}
int main() {
    int mat[DIM][DIM];
    int dim=chiediDim(DIM);
    caricaMat(mat,dim,dim);
    int sommaPric = sommaDiagPrinc(mat,dim);
    int sommaSec = sommaDiagSec(mat,dim);

    if(sommaPric==sommaSec)
        printf("le somme coincidono");
    else
        printf("le somme non coincidono");
    return 0;
}
