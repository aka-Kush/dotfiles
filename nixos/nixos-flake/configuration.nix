{ config, pkgs, ... }:

{
	imports =
		[ 
		./hardware-configuration.nix
		];

	boot.loader.systemd-boot.enable = true;
	boot.loader.efi.canTouchEfiVariables = true;

	boot.kernelPackages = pkgs.linuxPackages;

	services.flatpak.enable = true;

	networking.hostName = "nixos"; 
	networking.networkmanager.enable = true;

	nix.settings.experimental-features = ["nix-command" "flakes"];

	time.timeZone = "Asia/Kolkata";
	i18n.defaultLocale = "en_US.UTF-8";
	i18n.extraLocaleSettings = {
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

	services.xserver.xkb = {
		layout = "us";
		variant = "";
	};

	users.users.kush = {
		isNormalUser = true;
		description = "Shivansh Kush";
		extraGroups = [ "networkmanager" "wheel" ];
		home = "/home/kush";
		shell = pkgs.fish;
	};

	nixpkgs.config.allowUnfree = true;

	environment.systemPackages = with pkgs; [
            vim 
			librewolf
			neovim
			discord
			spotify
			kitty
			viewnior
			mpv
			protonvpn-gui
			imagemagick
			cliphist
			libnotify
			qbittorrent

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


        zoxide
        eza
			git
			ffmpegthumbnailer
			libheif
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


			nodejs_24
			python313
        luajitPackages.luarocks-nix
			go
			];

	fonts.packages = with pkgs; [
		nerd-fonts.jetbrains-mono
			nerd-fonts.fira-code
			nerd-fonts.meslo-lg
	];

	services.pulseaudio.enable = false;
	services.pipewire = {
		enable = true;
		alsa.enable = true;
		alsa.support32Bit = true;
		pulse.enable = true;
		jack.enable = true;
	};

	services.blueman.enable = true;
	hardware.bluetooth.enable = true;
	services.power-profiles-daemon.enable = true;

	programs.fish.enable = true;

	hardware.graphics = {
		enable = true;
		enable32Bit = true;
	};

	services.xserver.videoDrivers = [ "nvidia" ];
	hardware.nvidia = {
		modesetting.enable = true;
		open = false;
		nvidiaSettings = true;
		package = config.boot.kernelPackages.nvidiaPackages.production.overrideAttrs {
			version = "580.105.08";
			src = pkgs.fetchurl {
				url = "https://us.download.nvidia.com/XFree86/Linux-x86_64/580.105.08/NVIDIA-Linux-x86_64-580.105.08.run";
				sha256 = "2cboGIZy8+t03QTPpp3VhHn6HQFiyMKMjRdiV2MpNHU=";
			};    
		};
		prime = {

			sync.enable = true;
			nvidiaBusId = "PCI:1:0:0";
			amdgpuBusId = "PCI:6:0:0";
		};
	};

	services.desktopManager.cosmic.enable = true;
	services.displayManager.cosmic-greeter.enable = true;

	fileSystems."/home/kush/DATA" = {
		device = "/dev/disk/by-uuid/1B002967488B4738";
		fsType = "ntfs";
		options = [
			"uid=1000"
				"gid=100"
				"dmask=022"
				"fmask=133"
				"windows_names"
		];
	};

	system.stateVersion = "25.05"; 

}
