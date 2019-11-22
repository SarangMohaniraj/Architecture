# Architecture
Create a drawing of a neural network with any shape

## Getting Started

```batch
git clone https://github.com/SarangMohaniraj/Architecture.git
```

or add `architecture.py` to your project

## Usage

Add the following code to your file:

```python
from architecture import Architecture

a = Architecture().draw()
```

You can modify the following arguments to the architecture of the network:

| argument | description | example |
|---|---|---|
|`shape` | neurons per layer (includes input and output) | `shape=[4,5,5,2]`|
|`figsize` | width,height of figure | `figsize=(10,5)`|
|`xkcd` | comical drawing style | `xkcd=True`|
