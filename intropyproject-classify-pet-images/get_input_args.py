#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: Hoang Tran
# DATE CREATED: 9/21/2024                                  
# REVISED DATE: 9/23/2024
# PURPOSE: Create a function that retrieves the following 3 command line inputs 
#          from the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
# Imports python modules
import argparse

# TODO 1: Define get_input_args function below please be certain to replace None
#       in the return statement with parser.parse_args() parsed argument 
#       collection that you created with this function
# 
def get_input_args():
  """
  Retrieves and parses the 3 command line arguments provided by the user when
  they run the program from a terminal window. This function uses Python's 
  argparse module to created and defined these 3 command line arguments. If 
  the user fails to provide some or all of the 3 arguments, then the default 
  values are used for the missing arguments. 
  Command Line Arguments:
    1. Image Folder as --dir with default value 'pet_images'
    2. CNN Model Architecture as --arch with default value 'vgg'
    3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
  This function returns these arguments as an ArgumentParser object.
  Parameters:
    None - simply using argparse module to create & store command line arguments
  Returns:
    parse_args() -data structure that stores the command line arguments object  
  """
  # Replace None with parser.parse_args() parsed argument collection that 
  # you created with this function   
  parser = argparse.ArgumentParser(prog="Get Input Args", 
                                   description="retrieves the image folder, CNN model qrchitecture and text file with dog names")
  parser.add_argument('--dir', help="Image Folder", nargs='?', default="pet_images/")
  parser.add_argument('--arch', help="CNN Model Architecture must be resnet, vgg or alexnet", nargs='?', default="vgg")
  parser.add_argument('--dogfile', help="Text File with Dog Names", nargs='?', default="dognames.txt")
  return parser.parse_args()

def main():
  args = get_input_args()
  print("Argument 1:", args.dir)
  print("Argument 2:", args.arch)
  print("Argument 3:", args.dogfile)
  
if __name__ == "__main__":
    main()