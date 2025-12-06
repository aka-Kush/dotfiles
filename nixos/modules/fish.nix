{
  config,
  lib,
  pkgs,
  ...
}:
{
  programs.fish = {
    enable = true;
    interactiveShellInit = ''
      set fish_greeting # Disable greeting
    '';
    shellAliases = {
      ls = "eza -l";
      lsa = "eza -al";
      buildnow = "sudo nixos-rebuild switch --flake /home/kush/nixos-dotfiles#nixos";
      buildboot = "sudo nixos-rebuild boot --flake /home/kush/nixos-dotfiles#nixos";
      nc = "nvim ~/nixos-dotfiles";
      cleannow = "sudo nix-env --delete-generations +2 --profile /nix/var/nix/profiles/system && sudo nix-collect-garbage -d";
    };
  };

  programs.zoxide = {
    enable = true;
    enableFishIntegration = true;
  };
}
