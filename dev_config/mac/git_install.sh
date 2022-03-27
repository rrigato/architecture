brew install git

git config --global user.email <email>

git config --global user.name <user_name>

# keep git from printing ignored files
git config --global advice.addIgnoredFile false

#default branch name for backwards compatibility
git config --global init.defaultBranch master

#####################################
#remote ssh setup
#
#####################################

# check ssh keys
ls -al ~/.ssh

#creating a new ssh key
ssh-keygen -t ed25519 -C "<email_address>"

#copy public key to clipboard
pbcopy < ~/.ssh/id_ed25519.pub
# go to remote to to paste your public key