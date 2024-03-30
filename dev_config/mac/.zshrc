#cp -r shell_config ~
#cp dev_config/mac/.zshrc ~
source ~/shell_config/bash_functions.sh
source ~/shell_config/setup_alias.sh


#nvm to path
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion