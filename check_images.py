#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#
# TODO 0: Add your information below for Programmer & Date Created.
# PROGRAMMER:   Pranjali Singh
# DATE CREATED:     09 Nov 2023
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task.
#          Note that the true identity of the pet (or object) in the image is
#          indicated by the filename of the image. Therefore, your program must
#          first extract the pet image label from the filename before
#          classifying the images using the pretrained CNN model. With this
#          program we will be comparing the performance of 3 different CNN model
#          architectures to determine which provides the 'best' classification.
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Imports python modules
from time import time, sleep

# Imports print functions that check the lab
from print_functions_for_lab_checks import *

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Main program function defined below
def main():
    # Start measuring program runtime
    start_time = time()

    # Get command line arguments from the user
    in_arg = get_input_args()

    # Check the validity of command line arguments
    check_command_line_arguments(in_arg)


    # Get pet labels from the directory
    results = get_pet_labels(in_arg.dir)

    # Check the creation of pet image labels
    check_creating_pet_image_labels(results)


    # Classify pet images using the specified architecture
    classify_images(in_arg.dir, results, in_arg.arch)

    # Check the classification of pet images
    check_classifying_images(results)


    # Adjust the results to determine if they are dogs or not
    adjust_results4_isadog(results, in_arg.dogfile)

    # Check the adjustment of results
    check_classifying_labels_as_dogs(results)


    # Calculate the results statistics
    results_stats = calculates_results_stats(results)

    # Check the calculation of results statistics
    check_calculating_results(results, results_stats)

    # Print the results
    print_results(results, results_stats, in_arg.arch, True, True)



    # Measure total program runtime and print it
    end_time = time()
    tot_time = end_time - start_time #calculate difference between end time and start time
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time/3600)))+":"+str(int((tot_time%3600)/60))+":"
          +str(int((tot_time%3600)%60)) )


# Call to main function to run the program
if __name__ == "__main__":
    main()
