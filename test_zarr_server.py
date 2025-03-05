import xarray as xr
import xpublish
import numpy as np
import pandas as pd
import os

print(os.listdir())
data = xr.open_zarr(
    "simple_zarr_dataset.zarr",
    consolidated=True,
)
rest = xpublish.SingleDatasetRest(data)
# Start the server and keep it running
if __name__ == "__main__":
    print("Serving simple dataset...")
    rest.serve(port=8000)
