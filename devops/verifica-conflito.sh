#!/bin/bash 

diretorio=$1

if [ $# -ne 1 ]; then
	echo "Uso: $0 diretorio"
	exit 1
fi

if [ ! -f "$diretorio" ]; then 
	echo "O arquivo $diretorio nao existe"
	exit 1
fi

for arquivo in "$diretorio"/*; do 
	if [ -f "$arquivo" ]; then
		if grep -q -E '<<<<<<<|=======|>>>>>>>' "$arquivo"; then
        		echo "O arquivo $arquivo contem marcacoes de conflito de merge"
		else
        		echo "O arquivo $arquivo nao contem marcacoes de conflito de merge"
		fi
	fi
done
