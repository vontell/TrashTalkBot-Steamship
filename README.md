# TrashTalk Bot using GPT-4 from Regression Games

This repository contains the trash talking bot for use in the Regression Games Capture the Flag game mode.
You can find the full tutorial here: https://medium.com/@RGAaron/writing-a-trash-talking-bot-on-regression-games-using-steamship-7633e231ccf1

## Quick Start

Deploy and use this package in under a minute!

First, make sure you have the Steamship CLI installed:

```bash
npm install -g steamship && ship login
```

Next, provide a handle for this project in `steamship.json`. Package handles must be globally unique. We recommend `YOURNAME-demo`.

```json
{
  "handle": "yourname-demo",
}
```

Then, deploy your package!

```bash
ship deploy
```

Wait about 30 seconds after deployment finishes for the package to become available.

### Invoke your Package from the CLI

Then, create an instance.

```bash
ship package:instance:create --default_name="Beautiful"
```

That keyword argument above is part of the required configuration.
You can see where it's defined in both the [steamship.json](steamship.json) file and in the [src/api.py](src/api.py) file.

The response will let you know what your **Instance Handle** is.

Finally, invoke a method!

```bash
ship package:instance:invoke --instance="INSTANCE_HANDLE" --method="greet"    
```

Full documentation for developers is available at [https://docs.steamship.com/packages/developing](https://docs.steamship.com/packages/developing).