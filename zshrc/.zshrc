# starship theme
eval "$(starship init zsh)"

# alias
alias ls="lsd -l"
alias lsa="lsd -al"
alias gs="git status"
alias gaa="git add ."
ga() { git add "$1"}
gc() {git commit -m "$1"}
alias gp="git push"

# plugins
source /home/kush/.config/zsh/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /home/kush/.config/zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
source /home/kush/.config/zsh/zsh-autocomplete/zsh-autocomplete.plugin.zsh
