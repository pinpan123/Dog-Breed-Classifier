#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#
# PROGRAMMER:   Pranjali Singh
# DATE CREATED:     09 Nov 2023
# PURPOSE: Create the function get_pet_labels that creates the pet labels from
#          the image's filename. This function inputs:
#           - The Image Folder as image_dir within get_pet_labels function and
#             as in_arg.dir for the function call within the main function.
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main.
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create
#       with this function
#
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames
    of the image files. These pet image labels are used to check the accuracy
    of the labels that are returned by the classifier function, since the
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function

    # Create an empty dictionary to store results
    results_dict = {}

    # List all files in the image directory
    filenames = listdir(image_dir)

    # Extract pet labels from filenames and add to the results dictionary
    for filename in filenames:
        # Skip hidden files (dot files)
        if filename.startswith('.'):
            # Print a message indicating that the hidden file is skipped
            #print(f"Skipped hidden file: {filename}")
            continue

        # Convert the filename to lowercase and split by underscores
        name_parts = filename.lower().split('_')

        # Initialize an empty string for the pet label
        pet_label = " ".join([word.strip() for word in name_parts if word.isalpha()])

        # Store the pet label in the results dictionary
        results_dict[filename] = [pet_label]

    return results_dict
