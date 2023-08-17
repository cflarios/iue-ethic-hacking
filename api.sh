#!/bin/bash

rand-str()
{
    # Return random alpha-numeric string of given LENGTH
    #
    # Usage: VALUE=$(rand-str $LENGTH)
    #    or: VALUE=$(rand-str)

    local DEFAULT_LENGTH=64
    local LENGTH=${1:-$DEFAULT_LENGTH}

    LC_CTYPE=C  tr -dc A-Za-z0-9 </dev/urandom | head -c $LENGTH
    # -dc: delete complementary set == delete all except given set
}


clear
cat << "EOF"
  _   _            _                _____ _   _           
 | | | | __ _  ___| | _____  ___   | ____| |_(_) ___ ___  
 | |_| |/ _` |/ __| |/ / _ \/ _ \  |  _| | __| |/ __/ _ \ 
 |  _  | (_| | (__|   <  __/ (_) | | |___| |_| | (_| (_) |
 |_| |_|\__,_|\___|_|\_\___|\___/  |_____|\__|_|\___\___/ 
                                                           
EOF

tput setaf 128;
printf "$msg"
tput setaf 7;

printf "\n\n\nBienvenido, este script ejecutará los 4 proyectos de las API. \n\n"
printf "Verás entre paréntesis y en $(tput setaf 128)(este color)$(tput setaf 7) la opción por defecto que se selecciona presionando enter.\n"
printf "De lo contrario podrás ingresar manualmente la opción solicitada.\n"
printf "No te preocupes al final del cuestionario, verás un resumen antes de confirmar.\n\n\n"

read -p "Presiona [enter] para continuar..."                                                                                                                                                                                                                

# Función para ejecutar un contenedor
run_node_basic_container() {
    echo "Ejecutando el contenedor $1..."
    CONTAINER_ID=$(sudo docker run -d -p 3000:3000 $1)
    sleep 5
    echo "Publicando datos..."
    curl -X POST -H "Content-Type: application/json" -d '{"task": "Hacer compras"}' http://localhost:3000/data
    sleep 1
    echo "Obteniendo datos..."
    curl http://localhost:3000/data
    sleep 1
    echo "Eliminando datos..."
    curl -X DELETE http://localhost:3000/data/0
    echo "Deteniendo el contenedor $1..."
    sudo docker stop $CONTAINER_ID
    sudo docker rm $CONTAINER_ID
}

run_python_basic_container() {
    echo "Ejecutando el contenedor $1..."
    CONTAINER_ID=$(sudo docker run --name python_basic -d -p 5000:5000 $1)
    sleep 1
    sudo docker logs $CONTAINER_ID
    sleep 3
    printf "\n\nPublicando datos...\n\n"
    curl -X POST -H "Content-Type: application/json" -d '{"task": "Hacer compras"}' http://localhost:5000/data
    sleep 3
    printf "\n\nObteniendo datos...\n\n"
    curl http://localhost:5000/data
    sleep 3
    printf "\n\nEliminando datos...\n\n"
    curl -X DELETE http://localhost:5000/data/0
    sleep 3
    printf "\n\nDeteniendo el contenedor $1...\n\n"
    sudo docker stop $CONTAINER_ID
    sudo docker rm $CONTAINER_ID
}

## ______________________________
#SSL?
printf "\n\n🔐 ¿Quieres que la API use certificados SSL? \n"
printf "   Si tu respuesta es 'SÍ', selecciona 'Con SSL'. \n"
printf "   Si tu respuesta es 'No', selecciona 'Sin SSL'. \n\n"

PS3='   SSL?: '
options=("Con SSL" "Sin SSL")
select opt in "${options[@]}"
do
    case $REPLY in
        "1")
            echo "         SSL? ► ${character} ✅"
            break
            ;;
        "2")
            echo "         SSL? ► ${character} ✅"
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done

SSL=$REPLY

#Nodejs or Python?
printf "\n\n¿Cuál quieres? ¿Node.js o Python? \n"
printf "   Si tu respuesta es 'Node.js', selecciona 'Con Node.js'. \n"
printf "   Si tu respuesta es 'Python', selecciona 'Con Python'. \n\n"

PS3='   Node.js o Python?: '
fr_options=("Con Node.js" "Con Python")

if [[ $SSL -eq 1 ]]
    then
        select opt in "${fr_options[@]}"
        do
            case $REPLY in
                "1")
                    echo "         Node.js? ► ${character} ✅"
                    break
                    ;;
                "2")
                    echo "         Python? ► ${character} ✅"
                    break
                    ;;
                *) echo "invalid option $REPLY";;
            esac
        done
    else
        echo "Opción inválida. Por favor, seleccione una opción válida."
fi

if [[ $SSL -eq 2 ]]
    then
        select opt in "${fr_options[@]}"
        do
            case $REPLY in
                "1")
                    echo "         Node.js? ► ${character} ✅" && run_node_basic_container node_basic_api:1.0
                    break
                    ;;
                "2")
                    echo "         Python? ► ${character} ✅" && run_python_basic_container python_basic_api:1.0
                    break
                    ;;
                *) echo "invalid option $REPLY";;
            esac
        done
    else
        echo "Opción inválida. Por favor, seleccione una opción válida."
fi
