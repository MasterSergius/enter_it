#!/bin/bash

# Requirements: curl, jq, wget

#set -e
#set -x

download_package() {
    local package_name="$1"
    local pypi_url="https://pypi.org/pypi/${package_name}/json"

    echo "Fetching metadata for ${package_name} from PyPI..."

    json_response=$(curl -s -f "$pypi_url")

    if [ -z "$json_response" ]; then
        echo "Error: Package '${package_name}' not found on PyPI or network error."
        return 1
    fi

    latest_version=$(echo "$json_response" | jq -r '.info.version')

    if [ -z "$latest_version" ] || [ "$latest_version" == "null" ]; then
        echo "Error: Could not determine the latest version for '${package_name}'."
        return 1
    fi

    echo "Latest version of ${package_name}: ${latest_version}"

    latest_release=$(echo "$json_response" | jq -r ".releases[\"$latest_version\"][]")

    found_tgz=0
    while read release_data; do
        filename=$(echo "$release_data" | jq -r '.filename')
        url=$(echo "$release_data" | jq -r '.url')

        if [[ "$filename" == *".tar.gz" ]]; then
            wget -O $(basename $url) "$url"
            found_tgz=1
        fi
    done < <(echo "$latest_release" | jq -c '.')
}



if [ "$#" -eq 0 ]; then
    echo "Usage: $0 <package_name_1> [package_name_2 ...]"
    echo "Example: $0 requests numpy"
    exit 1
fi

for pkg in "$@"; do
    echo "----------------------------------------------------"
    download_package "$pkg" || echo "Skipping ${pkg} due to previous errors."
    echo "----------------------------------------------------"
done

echo "Script finished."
