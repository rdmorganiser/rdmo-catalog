#!/bin/bash

scriptdir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
basedir=$(echo "${scriptdir}" | grep -Po ".*(?=\/)")
arr=($(find "${basedir}/shared" -regex ".*\.xml$" | sort))

tmpfile="/tmp/rdmocatalogtable.tmp"
readme_tpl="${basedir}/readme.tpl"
readme_out="${basedir}/readme.md"

rm -f "${tmpfile}"

function ec(){
    echo -e "${1}" >> "${readme_out}"
}

c=0
echo "Generate shared catalog table "
for f in "${arr[@]}"; do
    if [[ $(grep -Pc "<catalog\sdc:uri=.*>" "${f}") != 0 ]]; then
        c=$((c+1))
        title=$(
            cat "${f}" \
            | tr '\n' ' ' \
            | grep -Po "<catalog\s.*<\/catalog>" \
            | grep -Po "(?<=title lang=\"en\">).*?(?=</title)"
        )
        file=$(echo "${f}" | grep -Po "(?<=${basedir}\/).*")
        echo "Process file ${file}"
        echo "|${title}|${file}|" >> "${tmpfile}"
    fi
done

cat "${readme_tpl}" > "${readme_out}"
ec "\n\n## Shared catalogs"
ec "\n|Name|File|"
ec "|---|---|"
cat "${tmpfile}" | sort >> "${readme_out}"
ec "\n${c} catalogs shared"

echo "Done"
