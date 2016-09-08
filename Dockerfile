FROM jupyter/datascience-notebook
# user is set to jovyan

USER root
run apt-get update && apt-get install -y graphviz

ENV vol=/data
RUN mkdir -p ${vol}/examples/data
COPY *.ipynb ${vol}/examples/
COPY data/* ${vol}/examples/data/
RUN mkdir -p ${vol}/work
RUN chown -R jovyan ${vol}

ENV wd=/tmp
ADD . ${wd}
WORKDIR ${wd}
USER jovyan
RUN pip install --user pydot
RUN python setup.py install --user

WORKDIR ${vol}

ENTRYPOINT jupyter notebook
VOLUME ${vol}/work
