// weiner attack used against RSA
// Wiener's theorem
// continued fractions of e/n

// to get n and e from public key
// from Crypto.PublicKey import RSA
// python file .py
// i = 0
// while(i<10):
//		f = open('key-'+str(i)+'.pem','r')
//		r = RSA.importKey(f.read())
//  	print 'Key #' + str(i)
//  	print r.n
//  	print r.e
//  	print ""
//  	i = i + 1

#include <stdio.h>
#include <stdlib.h>
#include <string.h>



int main(int argc, char *argv[])
{

	FILE *eFile = NULL;
	FILE *nFile = NULL;
	int *eBuffer=NULL; 
	int *nBuffer=NULL;
	
	
	int temp;
	int e=0;
	int index,key,count,row,col,ecount;
	int i=0,j=0,k;
	
	int eCap = 10000;
	int nCap = 10000;
	int size = 0;

	eBuffer=malloc(sizeof(int)*eCap);
	nBuffer=malloc(sizeof(int)*nCap);
	

	// encryption key file will store a single positive integer,
	if ((eFile = fopen(argv[1], "r")) == NULL)
	{
		fprintf(stderr, "Could not open %s in main()!\n", argv[1]);
		exit(0);
	}
	
	// N 
	if ((nFile = fopen(argv[2], "r")) == NULL)
	{
		fprintf(stderr, "Could not open %s in main()!\n", argv[2]);
		exit(0);
	}


return 0; 
}