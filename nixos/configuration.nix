{
  config,
  lib,
  pkgs,
  ...
}:

{
  imports = [
    ./hardware-configuration.nix
    ./modules/fonts.nix
    ./modules/nvidia.nix
    ./modules/fish.nix
  ];

  boot.loader = {
    efi.canTouchEfiVariables = true;
    grub = {
      enable = true;
      efiSupport = true;
      device = "nodev";
      useOSProber = true;
    };
  };

  services = {
    flatpak.enable = true;

    xserver.xkb = {
      layout = "us";
      variant = "";
    };

    libinput.enable = true;
    blueman.enable = true;
    power-profiles-daemon.enable = true;

    desktopManager.cosmic.enable = true;
    displayManager.cosmic-greeter.enable = true;

    pipewire = {
      enable = true;
      pulse.enable = true;
      alsa.enable = true;
      jack.enable = true;
      alsa.support32Bit = true;
    };

  };

  networking = {
    hostName = "nixos";
    networkmanager.enable = true;
  };

  time.timeZone = "Asia/Kolkata";

  nix.settings.experimental-features = [
    "nix-command"
    "flakes"
  ];

  i18n = {
    defaultLocale = "en_US.UTF-8";
    extraLocaleSettings = {
      LC_ADDRESS = "en_IN";
      LC_IDENTIFICATION = "en_IN";
      LC_MEASUREMENT = "en_IN";
      LC_MONETARY = "en_IN";
      LC_NAME = "en_IN";
      LC_NUMERIC = "en_IN";
      LC_PAPER = "en_IN";
      LC_TELEPHONE = "en_IN";
      LC_TIME = "en_IN";
    };
  };

  security.polkit.enable = true;

  xdg.portal = {
    enable = true;
    extraPortals = [
      pkgs.xdg-desktop-portal-gtk
      pkgs.xdg-desktop-portal-wlr
      pkgs.xdg-desktop-portal-cosmic
    ];
    config.common.default = "*";
  };

  users.users.kush = {
    isNormalUser = true;
    description = "Shivansh Kush";
    extraGroups = [
      "wheel"
      "networkmanager"
    ];
    home = "/home/kush";
    shell = pkgs.fish;
  };

  environment.systemPackages = with pkgs; [

    xdg-user-dirs-gtk
    xdg-user-dirs
    neovim
    discord
    spotify
    viewnior
    mpv
    libnotify
    wl-clipboard
    wl-clip-persist
    qbittorrent
    alacritty
    kitty
    brave
    obsidian
    logseq

    # nvidia
    nvidia-vaapi-driver
    libva
    libva-utils
    vulkan-tools
    vulkan-validation-layers
    vulkan-headers
    vulkan-loader
    vulkan-extension-layer
    mesa-demos
    egl-wayland
    nvtopPackages.full

    # tools and utilities
    eza
    vim
    wget
    git
    xfce.tumbler
    ifuse
    xarchiver
    gocryptfs
    unzip
    ntfs3g
    lshw
    jq
    gcc
    curl
    fzf
    ripgrep
    wget
    fd
    bat
    pkg-config
    gnupg
    gnumake
    pkg-config
    autoconf
    automake
    libtool
    tldr
    rsync
    cmake
    sassc

    # neovim lsp
    # lua
    luajitPackages.luacheck
    luajitPackages.luarocks-nix
    stylua
    lua-language-server

    # python
    python315

    #nix
    nixd
    statix
    nixfmt

    # dev
    mysql-workbench
  ];

  services.mysql = {
    enable = true;
    package = pkgs.mariadb;
  };

  system.stateVersion = "25.11";
}
