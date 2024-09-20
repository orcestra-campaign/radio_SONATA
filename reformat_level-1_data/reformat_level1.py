import xarray as xr
import os
import sys

def run_reformat(file_path):
    """
    WHAT DOES THIS DO ?
    """
    # Load the dataset
    ds = xr.open_dataset(file_path)
    
    launch_time_value = str(ds["launch_time"].values)
    ds = (ds.reset_coords('p', drop=False)
          .drop_vars('dz')
          .isel(sounding=0)
          .rename({'sounding': 'sonde_id'})
          .reset_coords('sonde_id', drop=False)
          .rename({'flight_time': 'time'})
          .swap_dims({'level': 'time'})
          .drop_vars({"launch_time", "level"})
          .set_coords('alt')
        )
    ds.attrs["launch_time"] = launch_time_value
    ds = ds[list(['u', 'v', 'ta', 'p', 'rh', 'sonde_id'])]
    
    # If the file exists, delete it
    if os.path.exists(file_path):
        os.remove(file_path)
    
    # Save the dataset to the same file (will overwrite if it exists)
    print(file_path)
    ds.to_netcdf(file_path, mode='w')


def process_files(directory):
    """
    Process all NetCDF files in the given directory.
    """
    for file_name in os.listdir(directory):
        if file_name.endswith('.nc'):
            print(file_name)
            file_path = os.path.join(directory, file_name)
            run_reformat(file_path)

def main():
    """
    Main function to execute the script.
    """
    if len(sys.argv) != 2:
        sys.exit(1)

    directory = sys.argv[1]
    
    if not os.path.isdir(directory):
        print(f"Error: The directory {directory} does not exist.")
        sys.exit(1)
    
    # Process all files in the directory
    process_files(directory)

if __name__ == "__main__":
    main()