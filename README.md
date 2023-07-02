# Attendance Tracker for MS Teams 

## Introduction
Welcome to my first project! I threw myself off the deep-end by trying to build something relatively useful as my first real step into the programming world. In 2021, during online classes, I realised that teachers often spent a significant amount of class time in manually marking attendance in google sheets. Not only was this process highly ineffecient, students who faced internet troubles during that specific period of class wouldn't be marked present. While MS Teams did generate an attendance report, it was pretty much unusable since all it contained were timestamps of joins and leaves (see demoAttendance.csv for reference).
Hence, I figured that it'd be pretty nifty if I could build a script that'd process those timestamps, generate a report based off the teacher's preferences, and update that onto Google Sheets.

Also, it turns out that MS Teams attendance reports were updated in 2022 to also reflect the total time that each participant spends in the meeting, but because I learnt of this update halfway into building this, we're gonna pretend that that's not a thing :) 

## Description
This Python project manages class attendance by reading a CSV file of attendance data and updating a Google Sheet with students' attendance status. It calculates the duration each student was present in class and compares it with a user-provided threshold to determine if the student should be marked present or absent. 

## Setup and Requirements
* Python 3.x
* A Google account with access to Google Sheets API (credentials in a .env file, refer to .env.sample)
* Required Python packages: csv, os, dotenv, gspread, oauth2client. All are easily installable via pip

## Usage
To use this project,
* Clone this repo
* Activate Google Sheets API from Google Cloud Console and download Service Account Credentials
* Update a .env file with Google Sheets API Credentials (refer to  .env.sample)
* Create a google sheets with the name 'Demo Attendance'. Share this file to the Email mentioned in the API Credentials 
* Run main.py



