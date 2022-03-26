brew install git

git config --global user.email <email>

git config --global user.name <user_name>


# check ssh keys
ls -al ~/.ssh

#creating a new ssh key
ssh-keygen -t ed25519 -C "<email_address>"

#copy public key to clipboard
pbcopy < ~/.ssh/id_ed25519.pub
# go to remote to to paste your public key