################################################################################
#
# Refer to "LICENSE" for licensing information
#
# Author: John Skubic
# Email:  skubicjj@gmail.com
# Date:   4/6/17
#
# Description: Contains the top level class for SystemVerilog to Verilog 
#              conversion.  Conversion can be viewed as applying a series of
#              filters, one filter per SystemVerilog feature.
#
################################################################################

class SV2VConvert:
  def __init__(self):
    print "SV2VConvert built"
