printf "\nRunning aptitude autoremove. This requires privilege.\n"
sudo apt autoremove -y
printf "\nRunning aptitude clean. This requires privilege.\n"
sudo apt clean -y
printf "\nDeleting thumbnails cache.\n"
rm -rf ~/.cache/thumbnails/*
printf "\nDeleting Chrome and Mozilla caches.\n"
rm -rf ~/.cache/google-chrome/*
rm -rf ~/.cache/mozilla/*

