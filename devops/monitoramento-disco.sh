#!/bin/bash

ponto_montagem="/System/Volumes/Update/mnt1"
nome_log=$(date +%F-%H:%M)
diretorio="/Users/isadoradantas/Projetos/alura/devops"

uso_disco=$(df -h | grep $ponto_montagem | awk '{print $5}')

echo "Uso de disco em $uso_disco" > "$diretorio/$nome_log.log"


# Adicionar no crontab 
## crontab -e 
## */2 * * * * /Users/isadoradantas/Projetos/alura/devops/monitoramento-disco.sh /Users/isadoradantas/Projetos/alura/devops
