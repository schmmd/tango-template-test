# tango-beaker-template

This is a template for research projects using Tango and Beaker.

## What's in here

In this repository you'll find several files that you can use as starting point to kick off your project:

- **[`tango.yml`](./tango.yml)**

  This is a Tango settings file. This tells Tango where to save results (the [`workspace`](https://ai2-tango.readthedocs.io/en/latest/api/settings.html#tango.settings.TangoGlobalSettings.workspace) field) and how to run steps (the [`executor`](https://ai2-tango.readthedocs.io/en/latest/api/settings.html#tango.settings.TangoGlobalSettings.executor) field).
  This one in particular tells Tango to use the [Beaker workspace](https://ai2-tango.readthedocs.io/en/latest/api/integrations/beaker.html#tango.integrations.beaker.BeakerWorkspace), which utilizes Beaker datasets to cache step results, and the [Beaker executor](https://ai2-tango.readthedocs.io/en/latest/api/integrations/beaker.html#tango.integrations.beaker.BeakerExecutor), which runs steps as Beaker jobs on the clusters of your choosing.

- **[`steps.py`](./steps.py)**

  This is just an example of Python module where you can define your Tango [Step](https://ai2-tango.readthedocs.io/en/latest/api/components/step.html#tango.step.Step) classes.
  You could call this whatever you want, just make sure to update the `include_package` field in your `tango.yml`.
  This one just contains a single example step, called "hello", which prints out a greeting and whether Torch finds any CUDA-enabled GPU devices.

- **[`config.jsonnet`](./config.jsonnet)**

  This is an experiment configuration file. It defines the experiment - made up of steps - that Tango will run.

- **[`requirements.txt`](./requirements.txt)**

  This file specifies your Python dependencies. You could also use a conda `environment.yml` file if you want, but at least one of these is required to be able to use the Beaker executor (Tango uses this to recreate your Python environment on Beaker).

## Getting started

1. Hit the ["Use this template"](https://github.com/allenai/tango-beaker-template/generate) button to initialize your own repository with all of the files from this repo as a starting point.
2. Change the `beaker_workspace` field in the [`tango.yml`](./tango.yml) file to the name of your own workspace on Beaker (Tango will create it if it doesn't already exist).
3. If you haven't already [installed and configured the Beaker CLI](https://beaker-docs.apps.allenai.org/start/install.html), do that now. Otherwise you can just the environment variable `BEAKER_TOKEN` to your Beaker user token.
4. Create a [GitHub personal access token](https://github.com/settings/tokens/new) with at least the "repo" scope and set it to the environment variable `GITHUB_TOKEN`. Tango will use this token to clone your project when it runs on Beaker.
5. Create a new Python environment and install your project's dependencies with:

    ```bash
    pip install -r requirements.txt
    ```

6. Run your first Tango experiment on Beaker! Just run:

    ```bash
    tango run config.jsonnet
    ```
