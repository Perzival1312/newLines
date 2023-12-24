# FROM python:2.7
# ADD . /todo
# WORKDIR /todo
# RUN pip install -r requirements.txt
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
EXPOSE 5000
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/


# docker run --hostname=d748f49fe208 --env=SESSION_KEY=b'u/y\xb6\x93\x8e\x11\x0f\xa1\xcc\xe4\xfa\xe6\xd59\xf5
#  --env=IMGUR_ID=940280becf0b80f --env=IMGUR_API_KEY=2baaba7ffb209a72fa1ce9f7d0198303177d8a01
#   --env=MONGODB_URI=localhost:27017 --env=TWITTER_CONSUMER_KEY=BzU4lkTpUQLGlnXOuqSxZBu2l
#    --env=TWITTER_ACCESS_TOKEN_SECRET=F5RwYu1b53KE69x0xLAaYJdnWpOwCgAhT1JvwAAPxUdwY
#     --env=network.host=0.0.0.0 --env=http.host=0.0.0.0 --env=TWITTER_ACCESS_TOKEN=1108124560761581568-BodI4CIDxo1sLOf4mynIDFzvAN2phK
#      --env=TWITTER_CONSUMER_SECRET=MRZwaJDvY8CIl01OaIPSX1bivLpyt4ILjLNVGaTBD5Ss0LLlxu --env=SETTINGS=ProductionConfig
#       --env=transport.host=localhost --env=IMGUR_ACCESS_TOKEN=e55c62401c8ae7f1f60d23a9e932a9f2492ff07d
#        --env=PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin --env=LANG=C.UTF-8
#         --env=GPG_KEY=7169605F62C751356D054A26A821E680E5FA6305 --env=PYTHON_VERSION=3.12.1 --env=PYTHON_PIP_VERSION=23.2.1
#          --env=PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/4cfa4081d27285bda1220a62a5ebf5b4bd749cdb/public/get-pip.py
#           --env=PYTHON_GET_PIP_SHA256=9cc01665956d22b3bf057ae8287b035827bfd895da235bcea200ab3b811790b6 --env=PYTHONUNBUFFERED=1
#            --volume=/home/perzival1312/code/courses/cs12/tweet-gen:/code:rw --network=tweet-gen_default --workdir=/code -p 5000:5000
#             --label='com.docker.compose.config-hash=46e9324badcbac580146b037c735467ae6955bf66e6145ed8d561b1dc0205778'
#              --label='com.docker.compose.container-number=1' --label='com.docker.compose.depends_on=db:service_started:true'
#               --label='com.docker.compose.image=sha256:2d4a454b87a4c6a0e28c2e427eded317cff6069f02ddc55d121741680be994ec'
#                --label='com.docker.compose.oneoff=False' --label='com.docker.compose.project=tweet-gen'
#                 --label='com.docker.compose.project.config_files=/home/perzival1312/code/courses/cs12/tweet-gen/docker-compose.yml'
#                  --label='com.docker.compose.project.working_dir=/home/perzival1312/code/courses/cs12/tweet-gen' --label='com.docker.compose.service=web'
#                   --label='com.docker.compose.version=2.23.0' --label='desktop.docker.io/wsl-distro=Ubuntu' --runtime=runc -d tweet-gen-web

# docker run --hostname=c0588a67b866 --env=IMGUR_API_KEY=2baaba7ffb209a72fa1ce9f7d0198303177d8a01
#  --env=SETTINGS=ProductionConfig --env=IMGUR_ID=940280becf0b80f --env=MONGODB_URI=localhost:27017
#   --env=IMGUR_ACCESS_TOKEN=e55c62401c8ae7f1f60d23a9e932a9f2492ff07d --env=TWITTER_ACCESS_TOKEN_SECRET=F5RwYu1b53KE69x0xLAaYJdnWpOwCgAhT1JvwAAPxUdwY
#    --env=TWITTER_CONSUMER_KEY=BzU4lkTpUQLGlnXOuqSxZBu2l --env=SESSION_KEY=b'u/y\xb6\x93\x8e\x11\x0f\xa1\xcc\xe4\xfa\xe6\xd59\xf5
#     --env=TWITTER_ACCESS_TOKEN=1108124560761581568-BodI4CIDxo1sLOf4mynIDFzvAN2phK --env=transport.host=localhost
#      --env=TWITTER_CONSUMER_SECRET=MRZwaJDvY8CIl01OaIPSX1bivLpyt4ILjLNVGaTBD5Ss0LLlxu --env=PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
#       --env=LANG=C.UTF-8 --env=GPG_KEY=7169605F62C751356D054A26A821E680E5FA6305 --env=PYTHON_VERSION=3.12.1 --env=PYTHON_PIP_VERSION=23.2.1
#        --env=PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/4cfa4081d27285bda1220a62a5ebf5b4bd749cdb/public/get-pip.py
#         --env=PYTHON_GET_PIP_SHA256=9cc01665956d22b3bf057ae8287b035827bfd895da235bcea200ab3b811790b6 --env=PYTHONUNBUFFERED=1
#          --volume=/home/perzival1312/code/courses/cs12/tweet-gen:/code:rw --network=tweet-gen_default --workdir=/code -p 5000:5000
#           --label='com.docker.compose.config-hash=cca34b5eba2a648bf2cdb4b01d5f633e1ca0311050c3dcf8d8bf15c094c175d7' --label='com.docker.compose.container-number=1'
#            --label='com.docker.compose.depends_on=db:service_started:true' --label='com.docker.compose.image=sha256:2d4a454b87a4c6a0e28c2e427eded317cff6069f02ddc55d121741680be994ec'
#             --label='com.docker.compose.oneoff=False' --label='com.docker.compose.project=tweet-gen'
#              --label='com.docker.compose.project.config_files=/home/perzival1312/code/courses/cs12/tweet-gen/docker-compose.yml'
#               --label='com.docker.compose.project.working_dir=/home/perzival1312/code/courses/cs12/tweet-gen'
#                --label='com.docker.compose.replace=d748f49fe20860c0a6726bbd5893845e81252645d1b722d5522ceb05d00acae3'
#                 --label='com.docker.compose.service=web' --label='com.docker.compose.version=2.23.0' --label='desktop.docker.io/wsl-distro=Ubuntu' --runtime=runc -d tweet-gen-web

# docker run --hostname=78875ca3c6c2 --env=TWITTER_CONSUMER_SECRET=MRZwaJDvY8CIl01OaIPSX1bivLpyt4ILjLNVGaTBD5Ss0LLlxu
#  --env=transport.host=localhost --env=SETTINGS=ProductionConfig --env=TWITTER_ACCESS_TOKEN=1108124560761581568-BodI4CIDxo1sLOf4mynIDFzvAN2phK
#   --env=TWITTER_ACCESS_TOKEN_SECRET=F5RwYu1b53KE69x0xLAaYJdnWpOwCgAhT1JvwAAPxUdwY --env=IMGUR_ACCESS_TOKEN=e55c62401c8ae7f1f60d23a9e932a9f2492ff07d
#    --env=TWITTER_CONSUMER_KEY=BzU4lkTpUQLGlnXOuqSxZBu2l --env=network=host --env=MONGODB_URI=localhost:27017
#     --env=SESSION_KEY=b'u/y\xb6\x93\x8e\x11\x0f\xa1\xcc\xe4\xfa\xe6\xd59\xf5 --env=IMGUR_API_KEY=2baaba7ffb209a72fa1ce9f7d0198303177d8a01
#      --env=IMGUR_ID=940280becf0b80f --env=PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin --env=LANG=C.UTF-8
#       --env=GPG_KEY=7169605F62C751356D054A26A821E680E5FA6305 --env=PYTHON_VERSION=3.12.1 --env=PYTHON_PIP_VERSION=23.2.1
#        --env=PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/4cfa4081d27285bda1220a62a5ebf5b4bd749cdb/public/get-pip.py
#         --env=PYTHON_GET_PIP_SHA256=9cc01665956d22b3bf057ae8287b035827bfd895da235bcea200ab3b811790b6 --env=PYTHONUNBUFFERED=1
#          --volume=/home/perzival1312/code/courses/cs12/tweet-gen:/code:rw --network=tweet-gen_default --workdir=/code -p 5000:5000 --label='com.docker.compose.config-hash=e412b14c621a623c8e4d8c3b494bc78885805a49b9d25d62a5f5921cda947bf1' --label='com.docker.compose.container-number=1' --label='com.docker.compose.depends_on=db:service_started:true' --label='com.docker.compose.image=sha256:2d4a454b87a4c6a0e28c2e427eded317cff6069f02ddc55d121741680be994ec' --label='com.docker.compose.oneoff=False' --label='com.docker.compose.project=tweet-gen' --label='com.docker.compose.project.config_files=/home/perzival1312/code/courses/cs12/tweet-gen/docker-compose.yml' --label='com.docker.compose.project.working_dir=/home/perzival1312/code/courses/cs12/tweet-gen' --label='com.docker.compose.replace=c0588a67b8661a5b3428c84d3756b68b7d7d448703a39eaeac339dc82027265b' --label='com.docker.compose.service=web' --label='com.docker.compose.version=2.23.0' --label='desktop.docker.io/wsl-distro=Ubuntu' --runtime=runc -d tweet-gen-web
