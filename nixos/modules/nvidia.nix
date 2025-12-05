{
  config,
  lib,
  pkgs,
  ...
}:
{
  hardware.graphics = {
    enable = true;
    enable32Bit = true;
  };

  nixpkgs.config.allowUnfree = true;
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
}
