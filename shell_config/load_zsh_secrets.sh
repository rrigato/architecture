export anki_openai_key=$(
    security find-generic-password  -s anki_openai_key -w 2>/dev/null
)
[[ -z "$anki_openai_key" ]] && \
echo "\n load_zsh_secrets.sh - Warning anki_openai_key environment variable not set"