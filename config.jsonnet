// This is an experiment configuration file. This example defines a simple
// experiment consisting of a single step called "hello_torch".
// This step comes from the HelloTorchStep defined in steps.py
{
  steps: {
    hello_torch: {
      type: "torch_hello", // tells Tango to use the step class registered as "torch_hello"
      step_resources: { gpu_count: 1 }, // tells Tango what compute resources the step needs
      // Inputs to the step should also be defined here:
      name: "Sitka", // this is the name of Michael's cat - if you have your own cat, change that here
    },
  }
}
