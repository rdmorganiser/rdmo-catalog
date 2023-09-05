#!/bin/bash
scriptdir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
basedir=$(echo "${scriptdir}" | grep -Po ".*(?=\/)")
mapfile -t arr < <(find "${basedir}/shared" -regex ".*\.xml$" | sort)

placeholder="___NEW_TABLE___"
readme_file="${basedir}/README.md"
temp_readme="/tmp/readme.tmp"
temp_table="/tmp/new_table.tmp"

truncate -s 0 "${temp_readme}"
truncate -s 0 "${temp_table}"

# functions
ett() {
    echo -e "${1}" >>"${temp_table}"
}

make_table() {
    echo "Generate shared catalog table"
    ett "\n\n## Shared catalogs"
    ett "\n|Title|File|"
    ett "|---|---|"
    for f in "${arr[@]}"; do
        if [[ $(grep -Pc "<catalog\sdc:uri=.*>" "${f}") != 0 ]]; then
            counter=$((counter + 1))
            title=$(
                tr '\n' ' ' <"${f}" |
                    grep -Po "<catalog\s.*<\/catalog>" |
                    grep -Po "(?<=title lang=\"en\">).*?(?=</title)"
            )
            file=$(echo "${f}" | grep -Po "(?<=${basedir}\/).*")
            echo "  Process ${file}"
            ett "|${title}|${file}|"
        fi
    done
    ett "\n${counter} catalogs shared\n"
}

remove_old_table() {
    echo "Remove old table"
    sed -ze "s/## Shared catalogs[^<]*catalogs shared/${placeholder}/g" \
        "${readme_file}" >"${temp_readme}"
}

insert_new_table() {
    echo "Insert new table"
    sed -i "/${placeholder}/r ${temp_table}" "${temp_readme}"
}

clean_up() {
    echo "Clean up README.md"
    sed -i "s/${placeholder}//g" "${temp_readme}"
    cat -s "${temp_readme}" >"${readme_file}"
}

# main
make_table
remove_old_table
insert_new_table
clean_up
