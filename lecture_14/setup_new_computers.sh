sudo xbps-install -Sy tree neovim curl jq wget
exit_status=$?
if [[ $exit_status == "0" ]]; then
    echo "install completed"
else
    echo "install failed"
fi
