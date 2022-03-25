#install home-brew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

#add brew to path
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/ryan/.zprofile

eval "$(/opt/homebrew/bin/brew shellenv)"
