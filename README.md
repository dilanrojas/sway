# Sway

![screenshot-2023-12-17-11:24:18](https://github.com/dilanrojas/sway/assets/99371498/01c86071-e24d-4001-9446-6c349c567f32)


# Contenidos
- [Programas y configuraciones](#programas-y-configuraciones)
- [Keybindings](#keybindings)

# Programas y configuraciones

Dependencias:

```bash
sudo pacman -S sddm xorg-xwayland pulseaudio pavucontrol alsa-utils sway swayidle swaybg waybar alacritty xdg-user-dirs lxappearance thunar thunar-archive-plugin pamixer playerctl glib2 gvfs-mtp ntfs-3g rofi mako git grim slurp polkit-gnome papirus-icon-theme fish starship lsd bat ttf-jetbrains-mono-nerd ttf-dejavu ttf-liberation noto-fonts
```

Habilitar servicio de SDDM:

```bash
sudo systemctl enable sddm
```

Instalar AUR Helper:

```bash
git clone https://aur.archlinux.org/yay-git.git
cd yay-git
makepkg -si --noconfirm
```

Temas:

```bash
yay -S sddm-theme-astronaut catppuccin-gtk-theme-mocha
```

```bash
sudo pacman -S npm python-virtualenv
git clone https://github.com/NvChad/NvChad ~/.config/nvim --depth 1 && nvim
```

Directorios necesarios:

```bash
xdg-user-dirs-update
mkdir ~/Imágenes/"Capturas de pantalla"
```

Fish como shell:

```bash
sudo usermod --shell /usr/bin/fish $USER
sudo usermod --shell /usr/bin/fish root
```

Dotfiles:

```bash
git clone https://github.com/dilanrojas/sway.git
cp -r sway/.config/ ~/
cp -r sway/.local/ ~/
sudo cp -r sway/sddm/ /usr/share/
sudo chmod +x sway/rofi-power-menu && sudo cp sway/rofi-power-menu /usr/bin/
```

Wallpapers:

```bash
sudo git clone https://github.com/dilanrojas/wallpapers.git
sudo mv wallpapers/ /usr/share/
```

# Keybindings

```bash
------------ Programas ------------
Win + Enter = Terminal
Win + B = Navegador Web
Win + M = Menú Rofi
Win + E = Explorador de archivos
Win + R = Activa luz nocturna [Redshift]
Win + Shift + R = Desactiva luz nocturna
Win + Shift + S = Tomar captura recortada

------------ Sistema ------------
Win + Shift + Q = Menú de apagado
Win + Control + R = Recargar configuración

------------ Configuración de ventanas ------------

--- Cambiar entre ventanas ---
Win + H = Ventana de la izquierda
Win + L = Ventana de la derecha
Win + J = Ventana de abajo
Win + K = Ventana de arriba

--- Mover ventanas ---
Win + Shift + H = Hacia la izquierda
Win + Shift + L = Hacia la derecha
Win + Shift + J = Hacia arriba
Win + Shift + K = Hacia abajo

--- Aumentar tamaño de ventanas ---
Win + Control + H = Aumentar hacia la izquierda
Win + Control + L = Aumentar hacia la derecha
Win + Control + J = Aumentar hacia abajo
Win + Control + K = Aumentar hacia arriba
```
