#####################################
# exports all variables declared in 
# shell script allowing sourcing of .env files
#####################################
set -o allexport

source .env

set +o allexport