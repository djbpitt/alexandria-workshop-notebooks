## Notebooks + support code for Alexandria workshop

### to install:
`python3 setup.py install`

### to create docker image:
`docker build -t huygensing/alexandria-workshop-notebooks .`

### to run the docker image:
`docker run -d -p${local_port}:8888 -v ${local_workdir}:/data/work huygensing/alexandria-workshop-notebooks`