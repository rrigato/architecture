##################################################
#Any commands in comments need to be run from the root of github.com/rrigato/architecture
#locally before 
##################################################

#homebrew to path
eval "$(/opt/homebrew/bin/brew shellenv)"

#cp -r shell_config ~
source ~/shell_config/setup_alias.sh

#cp dev_config/mac/.bash_profile ~/.bash_profile

#nvm 
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion