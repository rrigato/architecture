#install home-brew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

#add brew to bash_profile
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/ryan/.bash_profile

eval "$(/opt/homebrew/bin/brew shellenv)"
