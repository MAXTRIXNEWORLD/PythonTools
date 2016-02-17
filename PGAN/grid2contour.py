# ---------------------------------------------------------------------------
# grid2contour.py
# Created on: 2016-01-29
# Author: James Fee
# Description: Convert Grids to contours
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Check out any necessary licenses
arcpy.CheckOutExtension("spatial")

# Overwrite pre-existing files
arcpy.env.overwriteOutput = True


# Local variables:
# Add as many inputs as needed to batch process
input1 = "Z:\\Projects\Matrix\\PGAN\\data\\SUA_FEB_2016_V2.grd"
output1 = "Z:\\Projects\\Matrix\\PGAN\\data\\PGAN.gdb\\Groundwater_Contours\\Contour_SUA_FEB_2016"

# Process: Contour w/ 2ft contour
# Add as many inputs as needed to batch process, make it match the local variables above.
arcpy.gp.Contour_sa(input1, output1, "2", "0", "1")
