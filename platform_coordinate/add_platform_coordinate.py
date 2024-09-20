import xarray as xr
import os
import sys

def extract_platform_name(filename):
    """
    Extract the platform name from the filename.
    Simplified extraction based on fixed positions.
    """
    parts = filename.split('_')
    if len(parts) >= 3:
        return parts[2]  # Assumes the platform name is always the second part
    return 'unknown_platform'

def add_platform_variable(file_path):
    """
    Add a platform variable dependent on the 'sounding' dimension to the NetCDF file.
    """
    # Load the dataset
    ds = xr.open_dataset(file_path)
    
    # Extract the platform name from the filename
    platform_name = extract_platform_name(os.path.basename(file_path))
    
    # Create an array with the platform name repeated for each sounding
    platform_data = [platform_name] * ds.dims['sounding']
    
    # Add the platform variable to the dataset
    ds['platform'] = (('sounding',), platform_data)
    ds['platform'].attrs['long_name'] = 'Launching platform'
    
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
            add_platform_variable(file_path)

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
