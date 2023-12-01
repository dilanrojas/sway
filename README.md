# Sway
![screenshot-2023-11-28-10:01:33](https://github.com/dilanrojas/sway/assets/99371498/76ce3e11-1aed-44b1-8fb5-605b51cab35a)

# Instalación

sudo pacman -S sway swaybg swayidle eog mpv materia-gtk-theme papirus-icon-theme grim slurp mako rofi thunar thunar-archive-plugin file-roller pulseaudio pavucontrol alsa-utils waybar alacritty sway xorg-xwayland ttf-jetbrains-mono-nerd starship fish polkit-gnome

yay -S qogir-cursor-theme-git sddm-theme-astronaut

cp -r sway/.config/* ~/.config/

chmod +x ~/.config/scripts/*
sudo usermod --shell /usr/bin/fish $USER
sudo usermod --shell /usr/bin/fish root

sudo cp sway/rofi-power-menu /usr/bin/
sudo chmod +x /usr/bin/rofi-power-menu

# Fuentes

Jetbrains Nerd Font

Font Awesome
