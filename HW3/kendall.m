clear; clc; close all

#A = importdata('C:\Users\Micros\Dropbox\FALL14\CS495\hw\HW3\1.txt');
#B = importdata('C:\Users\Micros\Dropbox\FALL14\CS495\hw\HW3\2.txt');

A = importdata('1.txt');
B = importdata('2.txt');

[RHO,PVAL] = corr(B,A,'type','Kendall')
