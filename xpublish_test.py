import xarray as xr
import xpublish
from xpublish import SingleDatasetRest
import os
import argparse
from dotenv import load_dotenv


def start_server(output_zarr_store, host="0.0.0.0", port=8000):
    # Expand the tilde to the full path
    output_zarr_store = os.path.expanduser(output_zarr_store)

    # Load the dataset from the Zarr store as an xarray dataset
    data = xr.open_zarr(output_zarr_store)

    # Create the REST API for the dataset
    rest = SingleDatasetRest(data)
    print("serving")

    print("Serving dataset...")
    rest.serve(host=host, port=port)


if __name__ == "__main__":
    # Load environment variables from the .env file
    load_dotenv()

    # Get the directory paths from the environment variables
    output_zarr_store = os.getenv("OUTPUT_ZARR_STORE")

    parser = argparse.ArgumentParser(
        description="Start the xpublish server with a specified Zarr store."
    )
    parser.add_argument(
        "--zarr_store",
        type=str,
        default=output_zarr_store,
        help="Path to the Zarr store",
    )
    args = parser.parse_args()

    start_server(args.zarr_store)
