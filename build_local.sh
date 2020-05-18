#!/usr/bin/env bash

# this script will only run if the build dir is available and there are at-least one previous build present
branch='master'
tag_version=`git describe --tags`

# import the studio env paths in terminal
source ~/star/systems/pipe-env.sh
build_path_dir=${STUDIO_BUILD_DIR}/tools/${branch}/

# get the latest build number to be built for
output_build_no=$(python ./get_build_no.py ${build_path_dir} 2>&1 >/dev/null)
echo ${output}

# construct the build dir
build_path=${STUDIO_BUILD_DIR}/tools/${branch}/${tag_version}-${output_build_no}

# sync to file to its latest
#git checkout origin ${branch}
script_dir=`dirname $0 | xargs realpath`
rsync -avz --exclude '.*' ${script_dir}/ ${build_path}
echo ${build_path}
echo ${script_dir}







