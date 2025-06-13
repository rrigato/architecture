#Make sure to run scripts/full_zsh_setup.sh
source ~/shell_config/bash_functions.sh
source ~/shell_config/setup_alias.sh
source ~/shell_config/load_zsh_secrets.sh

#nvm to path
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completionexport


#pyenv and pyenv-virtualenv to path
PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

# terminal markup starship
eval "$(starship init zsh)"