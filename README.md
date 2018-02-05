Intro
=====
Luigi in dockerized version to be used during PyTN 2018 tutorial.

Prerequisites
=============

Install Docker: https://docs.docker.com/install/

Install docker-compose: https://docs.docker.com/compose/install/

Please ensure port 8082 is not used on your system before following the instructions.

Instructions:
=============

1. Clone the repo.

2. Run:

```
docker-compose up
```
You can optionally add `-d` flag if you prefer it to run in the background.

3.Verify you can access Luigi UI at: http://localhost:8082

Alternative Installation:
=========================

In case of WiFi issues at the venue or just slow installation.

We will have several USB drives in the class.

1. Copy the .tar files from USB drive.

2. For each file run:

```
docker load --input <file-name>
```

3. Navigate back to the repo directory. Follow steps 2 and 3 from above.

Tutorial:
=========

The dags directory is where you will put the DAGS you will create. It is mapped into
/usr/local/luigi/dags in the containers.

Test input is located at /usr/local/luigi/datafiles. Methods are provided in the test modules to
get file locations.

If you are not familiar with docker, you can use the trigger_dag.sh script to run your dags. Do this
in the same way you'd run the python command.

Consult the solutions directory or DAG examples if you need to.
