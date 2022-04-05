
Pipe Setup
==========

Pipe Settings Location
----------------------

The Default *CUT&RUN-Flow* settings used by the system are located in
*CUT&RUN-Flow's* installation directory. This is by default located
in the user's ``$HOME`` directory as such:

.. code-block:: bash
   
      # Pipe Defaults Configuration:
      $NXF_HOME/assets/RenneLab/CnR-flow/nextflow.config  # Pipe Executor, Dependency, Resource, etc. Configuration
      #Default: $HOME/.nextflow/assets/RenneLab/CnR-flow/nextflow.config

It is recommended that dependency configuration and other pipe-level
settings be configured here. An example of this file is provided 
in :ref:`Pipe nextflow.config`.

.. note:: If any settings are provided in both the 
   above :ref:`Pipe nextflow.config` file and the 
   :ref:`Task nextflow.config` file located in the task directory, 
   the task-directory settings will take precedence. For more
   information on Nextflow configuration precedence, see
   :manpage:`config`.

Dependencies
------------

The following external dependencies are utilized by *CUT&RUN-Flow*:

.. note:: Versions utilized in containers may differ slightly 
          from those listed based on availabilty.  


.. csv-table:: Dependencies
   :header-rows: 1
   :file: ../../build_info/dependencies.tsv
   :delim: tab
   :class: longtable
   :name: dependencies_table

Dependency Config
-----------------



Conda/Bioconda 
++++++++++++++

| *CUT&RUN-Flow* comes preconfigured to use the Conda_ package manager, 
  along with tools from the Bioconda_  package 
  suite for automated dependency handling. 
  [Bioconda_Citation]_  
| Nextflow_ automatically 
  acquires, stores, and activates each conda environment as it is
  required in the pipeline. For more information on Nextflow's,
  usage of conda, see :manpage:`conda`. 

    .. include:: ../../build_info/config_zz_auto_conda_config.txt
       :literal:

Singularity Containers 
++++++++++++++++++++++

| In addition to a default setup with Conda, *CUT&RUN-Flow* also 
  comes preconfigured to use Docker_ containers 
  from the BioContainers_ project using Singularity_. [BioContainers_Citation]_
| Nextflow_ automatically 
  pulls and runs singularity containers as required during the pipeline.
  This feature is enabled with :obj:`-profile singularity`.

    .. include:: ../../build_info/config_zz_auto_singularity_config.txt
       :literal:

Docker Containers 
+++++++++++++++++

| In addition to a default setup with Conda, *CUT&RUN-Flow* also 
  comes preconfigured to use Docker_ containers.
| Nextflow_ automatically 
  pulls and runs singularity containers as required during the pipeline.
  This feature is enabled with :obj:`-profile docker`.

    .. include:: ../../build_info/config_zz_auto_docker_config.txt
       :literal:

Modules 
++++++++++++++

| *CUT&RUN-FLow* comes with an alternative "easy" configuration option
  utilizing `Environment Modules`_. Each conda
  dependency paramater has an equivalent "module" paramater. Each module
  will then be loaded at runtime for the appropriate steps of the pipeline.
  For more information on Nextflow's use of Environment Modules, 
  see :manpage:`process` ("modules section").
 
    .. include:: ../../build_info/config_zz_auto_module_config.txt
       :literal:

Executable System Calls
++++++++++++++++++++++++

| To accommodate custom module or local setups, each required
  dependency system call can be customized:
 
    .. include:: ../../build_info/config_zz_auto_call_config.txt
       :literal:
