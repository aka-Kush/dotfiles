if status is-interactive
alias ls='eza -l'
alias lsa='eza -al'
end
zoxide init --cmd cd fish | source

fish_config theme choose "Rosé Pine Moon"

starship init fish | source
