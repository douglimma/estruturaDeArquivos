#include <stdio.h>

typedef struct _Endereco Endereco;

struct _Endereco{
	char log[72];
	char bairro[72];
	char cidade[72];
	char uf[72];
	char sigla[2];
	char cep[8];
	char lixo[2];
};

void buscandoCep (long fim, FILE *f, char* cep){
	
	int qntd;
	int i = 0;
	long inicio = 0;
	long meio;
	Endereco e;
	while (inicio <= fim){
		i++;
		meio = (inicio + fim)/2;
		fseek(f, meio*sizeof(Endereco), SEEK_SET);
		qntd = fread(&e, sizeof(Endereco), 1, f);
		if(strncmp(cep, e.cep, 8) == 0){ 
			printf("%.72s\n%.72s\n%.72s\n%.72s\n%.2s\n%.8s\n",e.log,e.bairro,e.cidade,e.uf,e.sigla,e.cep);
			break;
		}else{
			if (strncmp(cep,e.cep,8) < 0){
				fim = meio - 1;
			}else{
				inicio = meio + 1;
			}
		}
	}
	printf("Quantidade de vezes passadas: %d", i);

}
	
int main(int argc, char**argv)
{
	FILE *f;
	Endereco e;
	long pos, ult;

	
	if(argc != 2)
	{
		fprintf(stderr, "USO: %s [CEP]", argv[0]);
		return 1;
	}
	
	f = fopen("cep_ordenado.dat","r");
	fseek(f,0,SEEK_END);
	pos = ftell(f);
	rewind(f);

	ult = (pos/sizeof(Endereco)) - 1;

	buscaCep(ult, f, argv[1]);

	fclose(f);

	return 0;

}